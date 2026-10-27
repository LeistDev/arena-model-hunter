"""
Вход в аккаунт arena.ai.

Логика:
  1. Открываем настоящий (headed) Chromium с постоянным профилем —
     так Cloudflare пропускает, а сессия сохраняется между запусками.
  2. Пользователь входит в аккаунт руками: Log In -> почта -> (имя можно
     пропустить) -> письмо со ссылкой -> пароль.
  3. Скрипт сам опрашивает страницу и понимает, что вход выполнен,
     сохраняет сессию и закрывает браузер.
"""

from __future__ import annotations

import asyncio
import json
import os
import time
from pathlib import Path

import ui
import i18n
from i18n import t
from ui import C, render_panel, rule

# Папка профиля. Новая — ~/.arena-model-hunter; если она ещё не создана,
# а старая ~/.arena-helper есть, работаем со старой, чтобы не потерять сессию.
_ENV_HOME = os.environ.get("ARENA_HUNTER_HOME") or os.environ.get("ARENA_HELPER_HOME")
NEW_HOME = Path.home() / ".arena-model-hunter"
OLD_HOME = Path.home() / ".arena-helper"


def _default_home() -> Path:
    if NEW_HOME.exists() or not OLD_HOME.exists():
        return NEW_HOME
    return OLD_HOME


HOME = Path(_ENV_HOME) if _ENV_HOME else _default_home()
PROFILE_DIR = HOME / "profile"
STATE_FILE = HOME / "state.json"      # storage_state (cookies) — пригодится дальше
META_FILE = HOME / "session.json"     # {"email": ..., "logged_in_at": ...}
CONFIG_FILE = HOME / "config.json"    # {"parallel": false, "lang": "en", "unlimited": false}

START_URL = os.environ.get("ARENA_URL", "https://arena.ai/")
LOGIN_TIMEOUT = int(os.environ.get("ARENA_LOGIN_TIMEOUT", "900"))  # 15 минут
POLL_EVERY = 1.5

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
)

# Служебные cookie, которые не означают авторизацию
_COOKIE_IGNORE = (
    "cf_", "__cf", "_ga", "_gid", "_gat", "_dd", "ph_phc", "_vcrr", "_hj",
    "arena_", "provisional_", "user_country", "intercom", "amp_", "_fbp",
    "ajs_", "mp_", "__stripe", "_clck", "_clsk", "ph_",
)


# --------------------------------------------------------------------------- #
#  Настройки (сохраняются между запусками)
# --------------------------------------------------------------------------- #

DEFAULT_CONFIG = {  # однопоточный режим, английский, без лимита выключен
    "parallel": False,
    "lang": "en",
    "unlimited": False,
}


def load_config() -> dict:
    cfg = dict(DEFAULT_CONFIG)
    try:
        data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            cfg.update({k: v for k, v in data.items() if k in DEFAULT_CONFIG})
    except Exception:
        pass
    return cfg


def save_config(**values) -> dict:
    cfg = load_config()
    cfg.update({k: v for k, v in values.items() if k in DEFAULT_CONFIG})
    HOME.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(cfg, ensure_ascii=False, indent=2), encoding="utf-8")
    return cfg


def is_parallel() -> bool:
    return bool(load_config().get("parallel"))


def is_unlimited() -> bool:
    """Максимальное число чатов: False — 1..100, True — без лимита (опасно)."""
    return bool(load_config().get("unlimited"))


# --------------------------------------------------------------------------- #
#  Состояние сессии (без запуска браузера)
# --------------------------------------------------------------------------- #

def load_session() -> dict | None:
    """Возвращает сохранённую сессию, если она есть."""
    try:
        meta = json.loads(META_FILE.read_text(encoding="utf-8"))
    except Exception:
        return None
    if not meta.get("logged_in"):
        return None
    return meta


def session_email() -> str | None:
    meta = load_session()
    return (meta or {}).get("email")


def is_connected() -> bool:
    return load_session() is not None


def logout() -> dict:
    """
    Выход из аккаунта: удаляет браузерный профиль и данные сессии.
    После этого arena.ai снова попросит вход.
    """
    had = is_connected()
    had_profile = PROFILE_DIR.exists()
    reset_session()
    detail = (
        "профиль браузера и cookies удалены"
        if had_profile
        else "профиль браузера отсутствовал"
    )
    return {"ok": True, "was_connected": had, "detail": detail}


def reset_session() -> None:
    """Полный сброс: забыть профиль и сессию."""
    import shutil

    shutil.rmtree(PROFILE_DIR, ignore_errors=True)
    for f in (STATE_FILE, META_FILE):
        try:
            f.unlink()
        except FileNotFoundError:
            pass


# --------------------------------------------------------------------------- #
#  Детект «пользователь уже вошёл»
# --------------------------------------------------------------------------- #

_DOM_JS = """
() => {
  const body = document.body ? document.body.innerText || '' : '';
  const controls = [...document.querySelectorAll('button, a, [role=button]')];
  const labels = controls.map(e => (e.innerText || e.getAttribute('aria-label') || '').trim().toLowerCase());
  const hasLoginButton = labels.some(t => t === 'log in' || t === 'login' || t === 'sign in' || t === 'войти');
  const accountHints = controls.some(e => {
    const a = (e.getAttribute('aria-label') || '').toLowerCase();
    const t = (e.innerText || '').toLowerCase();
    return a.includes('account') || a.includes('user menu') || a.includes('profile')
        || t.includes('log out') || t.includes('logout') || t.includes('sign out')
        || t.includes('@') && t.length < 60;
  });
  return {
    url: location.href,
    title: document.title,
    text: body.slice(0, 6000),
    hasLoginButton,
    accountHints,
    emailInputs: document.querySelectorAll('input[type=email]').length,
  };
}
"""


def _is_auth_cookie(name: str) -> bool:
    n = name.lower()
    if any(n.startswith(p) or p in n for p in _COOKIE_IGNORE):
        return False
    return any(k in n for k in ("auth", "session", "token", "jwt", "supabase", "sb-"))


async def _snapshot_cookies(ctx) -> dict[str, str]:
    return {c["name"]: c.get("value", "") for c in await ctx.cookies()}


async def _check_logged_in(page, ctx, baseline: dict[str, str], email: str | None) -> tuple[bool, dict]:
    """Возвращает (вошёл_ли, диагностика)."""
    try:
        info = await page.evaluate(_DOM_JS)
    except Exception:
        return False, {"reason": "page not ready"}

    text = (info.get("text") or "").lower()
    url = info.get("url") or ""
    email_seen = bool(email) and email.lower() in text
    on_auth_path = "/auth/" in url

    cookies = await _snapshot_cookies(ctx)
    new_auth = [
        n for n, v in cookies.items()
        if _is_auth_cookie(n) and n not in baseline and len(v) > 20
    ]

    logged = False
    if email_seen and not on_auth_path:
        logged = True                      # самый надёжный признак — почта в сайдбаре
    elif new_auth and not info.get("hasLoginButton") and not on_auth_path:
        logged = True                      # появилась сессионная cookie, кнопки Log In нет
    elif info.get("accountHints") and not info.get("hasLoginButton") and not on_auth_path:
        logged = True

    return logged, {
        "url": url,
        "email_seen": email_seen,
        "auth_cookies": new_auth,
        "has_login_button": info.get("hasLoginButton"),
    }


async def _try_expand_sidebar(page) -> None:
    """Разворачивает сайдбар, чтобы кнопка Log In была видна."""
    for name in ("Expand sidebar", "Open sidebar"):
        try:
            btn = page.get_by_role("button", name=name)
            if await btn.count():
                await btn.first.click(timeout=3000)
                return
        except Exception:
            continue


async def _maybe_autofill(page, email: str | None, password: str | None) -> None:
    """
    Необязательное автозаполнение формы входа.
    Срабатывает, только если заданы ARENA_EMAIL / ARENA_PASSWORD в окружении.
    """
    if not email:
        return
    try:
        await page.get_by_role("button", name="Log In").first.click(timeout=8000)
        await page.wait_for_timeout(1500)
        await page.locator("input[type=email]").first.fill(email, timeout=8000)
        await page.get_by_role("button", name="Continue with email").first.click(timeout=8000)
        await page.wait_for_timeout(2500)
        if password:
            pwd = page.locator("input[type=password]").first
            if await pwd.count():
                await pwd.fill(password, timeout=8000)
                await page.get_by_role("button", name="Log In").last.click(timeout=8000)
                print(f"  {C.dim}{t('login.autofill_done')}{C.reset}")
                return
        print(f"  {C.dim}{t('login.autofill_email')}{C.reset}")
    except Exception:
        print(f"  {C.dim}{t('login.autofill_unavailable')}{C.reset}")


def _guess_email_from_text(text: str) -> str | None:
    import re

    best = None
    for m in re.finditer(r"[\w.+-]+@[\w-]+\.[\w.]{2,}", text or ""):
        candidate = m.group(0)
        if candidate.lower().endswith(("arena.ai", "example.com")):
            continue
        best = candidate
    return best


# --------------------------------------------------------------------------- #
#  Основной сценарий
# --------------------------------------------------------------------------- #

async def _finish(ctx, page, diag: dict, email_hint: str | None) -> dict:
    """Фиксирует сессию, пишет метаданные и закрывает браузер."""
    email = email_hint
    try:
        dom = await page.evaluate(_DOM_JS)
        email = _guess_email_from_text(dom.get("text", "")) or email
    except Exception:
        pass

    try:
        await ctx.storage_state(path=str(STATE_FILE))
    except Exception:
        pass

    META_FILE.write_text(
        json.dumps(
            {
                "logged_in": True,
                "email": email,
                "logged_in_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "url": (diag or {}).get("url"),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"\n  {C.ok}{t('login.ok')}{C.reset}")
    print(f"  {C.muted}{t('login.closing')}{C.reset}")
    try:
        await page.wait_for_timeout(600)
    except Exception:
        pass
    await ctx.close()
    return {"ok": True, "email": email}


async def _login_flow(email_hint: str | None = None) -> dict:
    from playwright.async_api import async_playwright

    HOME.mkdir(parents=True, exist_ok=True)
    PROFILE_DIR.mkdir(parents=True, exist_ok=True)

    ui.clear()
    rule(t("login.title"))
    print(f"  {C.muted}{t('login.profile')}{C.reset} {PROFILE_DIR}")
    print(f"  {C.muted}{t('login.site')}{C.reset}    {START_URL}")
    print(f"  {C.muted}{t('login.theme')}{C.reset}     {t('login.theme_dark')}\n")

    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            str(PROFILE_DIR),
            headless=False,
            no_viewport=True,
            user_agent=UA,
            locale="en-US",
            color_scheme="dark",  # arena.ai берёт тему из prefers-color-scheme
            ignore_default_args=["--enable-automation"],
            args=[
                "--disable-blink-features=AutomationControlled",
                "--start-maximized",
            ],
        )

        page = ctx.pages[0] if ctx.pages else await ctx.new_page()

        try:
            await page.goto(START_URL, wait_until="domcontentloaded", timeout=90_000)
        except Exception as exc:
            await ctx.close()
            return {"ok": False, "error": t("err.open_site", url=START_URL, error=exc)}

        await page.wait_for_timeout(3000)
        baseline = await _snapshot_cookies(ctx)
        await _try_expand_sidebar(page)

        env_email = os.environ.get("ARENA_EMAIL") or email_hint
        already, diag = await _check_logged_in(page, ctx, baseline, env_email)

        if already:
            print(f"  {C.ok}{t('login.already')}{C.reset}")
            print(f"  {C.muted}{t('login.already_skip')}{C.reset}")
            return await _finish(ctx, page, diag, env_email)

        render_panel(
            [
                f"{C.text}{t('login.intro')}{C.reset}",
                "",
                f"  {C.accent}1{C.reset}  {t('login.step1')}",
                f"  {C.accent}2{C.reset}  {t('login.step2')}",
                f"  {C.accent}3{C.reset}  {t('login.step3')}",
                f"     {C.dim}{t('login.step3_new')}{C.reset}",
                f"     {C.dim}{t('login.step3_mail')}{C.reset}",
                "",
                f"{C.muted}{t('login.paste1')}{C.reset}",
                f"{C.muted}{t('login.paste2')}{C.reset}",
                f"{C.muted}{t('login.paste3')}{C.reset}",
            ]
        )

        print(f"\n  {C.dim}{t('login.waiting')}{C.reset}\n")

        await _maybe_autofill(page, os.environ.get("ARENA_EMAIL"), os.environ.get("ARENA_PASSWORD"))

        started = time.time()
        last_report = 0.0
        logged_in = False

        while time.time() - started < LOGIN_TIMEOUT:
            pages = [pg for pg in ctx.pages if not pg.is_closed()]
            if not pages:
                return {"ok": False, "error": t("err.window_closed")}
            page = pages[-1]

            try:
                logged_in, diag = await _check_logged_in(page, ctx, baseline, env_email)
            except Exception:
                # страница в процессе навигации — просто ждём дальше
                logged_in = False

            if logged_in:
                break

            elapsed = time.time() - started
            if elapsed - last_report > 20:
                last_report = elapsed
                path = (diag.get("url") or "").split("//")[-1]
                print(f"  {C.dim}{t('login.poll', sec=int(elapsed), url=path[:70])}{C.reset}")

            await asyncio.sleep(POLL_EVERY)

        if not logged_in:
            await ctx.close()
            return {"ok": False, "error": t("err.login_timeout")}

        return await _finish(ctx, page, diag, env_email)




def friendly_error(exc: BaseException) -> str:
    msg = str(exc)
    if isinstance(exc, ModuleNotFoundError) or "No module named 'playwright'" in msg:
        return t("err.no_playwright")
    if "Executable doesn't exist" in msg or "playwright install" in msg:
        return t("err.no_browser")
    if "Target page, context or browser has been closed" in msg:
        return t("err.browser_closed")
    return f"{type(exc).__name__}: {msg.splitlines()[0]}"


def login(email_hint: str | None = None) -> dict:
    """Синхронная обёртка."""
    i18n.set_language(load_config().get("lang"))
    try:
        return asyncio.run(_login_flow(email_hint))
    except KeyboardInterrupt:
        return {"ok": False, "error": t("err.cancelled")}
    except Exception as exc:
        return {"ok": False, "error": friendly_error(exc)}


if __name__ == "__main__":
    print(json.dumps(login(os.environ.get("ARENA_EMAIL")), ensure_ascii=False))
