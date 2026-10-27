"""
Основной рабочий поток: N чатов Arena ↔ N вкладок lm.ikale.io.

Для каждого чата:
  1. открыть отдельную вкладку arena.ai/agent (режим Agent);
  2. открыть парную вкладку lm.ikale.io;
  3. по очереди взять 3 сэмпла, отправить их агенту, ответ вставить в Reply;
  4. нажать Verify, забрать модель и уверенность;
  5. вернуться в чат Arena и переименовать его в «модель уверенность».

Все чаты обрабатываются параллельно: каждая пара вкладок независима.
"""

from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass, field

from arena_login import PROFILE_DIR, UA, is_connected
import i18n
from i18n import t
from ui import C

ARENA_BASE = "https://arena.ai"
AGENT_URL = "https://arena.ai/agent"
IKALE_URL = "https://lm.ikale.io/"

SAMPLES = 3

# --------------------------------------------------------------------------- #
#  JS-снимки состояния страниц
# --------------------------------------------------------------------------- #

_ARENA_STATE_JS = """
() => {
  const body = document.body ? document.body.innerText : '';
  const prosaic = [...document.querySelectorAll('div.prose')].map(e => e.innerText.trim());
  const stop = [...document.querySelectorAll('button')].some(b =>
      /stop|cancel/i.test(b.getAttribute('aria-label') || ''));
  const send = !!document.querySelector("button[aria-label='Send message']");
  const feedback = /Was this task successful|Эта задача была выполнена успешно/i.test(body);
  return {
    url: location.href,
    busy: stop,
    send,
    feedback,
    messages: prosaic,
  };
}
"""

_IKALE_STATE_JS = """
() => {
  const panels = [...document.querySelectorAll("article[id^='sample-panel-']")];
  return {
    panels: panels.map(p => {
      const ta = p.querySelector('textarea');
      const promptNode = p.querySelector('p.text-body') || p.querySelector('p');
      return {
        prompt: promptNode ? promptNode.innerText.trim() : '',
        reply: ta ? ta.value : '',
      };
    }),
  };
}
"""


@dataclass
class ChatResult:
    index: int
    model: str | None = None
    confidence: str | None = None
    renamed_to: str | None = None
    error: str | None = None
    replies: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return self.error is None and bool(self.model)


# --------------------------------------------------------------------------- #
#  Прогресс в консоли
# --------------------------------------------------------------------------- #

_print_lock = asyncio.Lock()


async def log(line: str) -> None:
    async with _print_lock:
        print(line, flush=True)


# --------------------------------------------------------------------------- #
#  Arena: отправка сообщения агенту
# --------------------------------------------------------------------------- #

async def _arena_await_ready(page, timeout: float = 90) -> None:
    await _arena_composer(page, timeout)


async def _arena_composer(page, timeout: float = 90):
    """
    Возвращает поле ввода. После ответа агента его перекрывает карточка
    «Was this task successful?» — она убирается по Esc (или кнопкой Keep working).
    """
    start = time.time()
    while time.time() - start < timeout:
        editor = page.locator("div.ProseMirror").first
        try:
            if await editor.count() and await editor.is_visible():
                return editor
        except Exception:
            pass

        has_feedback = await page.evaluate(
            "() => /Was this task successful|Эта задача была выполнена успешно/i.test(document.body.innerText)"
        )
        if has_feedback:
            await page.keyboard.press("Escape")
            await page.wait_for_timeout(900)
            continue

        await page.wait_for_timeout(700)

    raise TimeoutError(t("flow.err_not_ready"))


async def _focus(page, parallel: bool) -> None:
    """
    В однопоточном режиме вкладку выводим вперёд — так надёжнее.
    В многопоточном НЕ трогаем фокус: иначе вкладки «передерутся» за него.
    """
    if not parallel:
        await page.bring_to_front()
        await page.wait_for_timeout(250)


async def _arena_send(page, text: str, parallel: bool = False) -> None:
    await _focus(page, parallel)
    try:
        await page.keyboard.press("Escape")
        await page.wait_for_timeout(300)
    except Exception:
        pass
    editor = await _arena_composer(page)
    await editor.click(timeout=20_000)
    await page.wait_for_timeout(200)
    await page.keyboard.press("Control+A")
    await page.keyboard.press("Delete")
    await page.keyboard.insert_text(text)
    await page.wait_for_timeout(400)

    send = page.locator("button[aria-label='Send message']").first
    await send.click(timeout=20_000)


async def _arena_wait_reply(page, prompt_text: str, timeout: float = 480) -> str:
    """
    Ждёт окончания ответа агента и возвращает текст его сообщения.
    Ориентиры: исчезла кнопка Stop, текст последнего сообщения не меняется,
    появился блок обратной связи.
    """
    start = time.time()
    last_seen = ""
    stable_since = time.time()
    saw_busy = False

    while time.time() - start < timeout:
        await page.wait_for_timeout(1500)
        try:
            state = await page.evaluate(_ARENA_STATE_JS)
        except Exception:
            continue

        if state["busy"]:
            saw_busy = True
            last_seen, stable_since = "", time.time()
            continue

        messages = state["messages"]
        candidate = ""
        for text in reversed(messages):
            if text and text.strip() != prompt_text.strip():
                candidate = text
                break

        if candidate != last_seen:
            last_seen = candidate
            stable_since = time.time()
            continue

        stable_for = time.time() - stable_since
        started_after = time.time() - start

        if candidate and ((state["feedback"] and stable_for > 2) or stable_for > 8 or
                          (saw_busy and stable_for > 4)):
            if started_after > 3:
                return candidate

    raise TimeoutError(t("flow.err_no_reply"))


# --------------------------------------------------------------------------- #
#  Arena: переименование чата
# --------------------------------------------------------------------------- #

async def _arena_ensure_sidebar(page) -> None:
    for name in ("Open sidebar", "Expand sidebar"):
        btn = page.get_by_role("button", name=name)
        try:
            if await btn.count() and await btn.first.is_visible():
                await btn.first.click()
                await page.wait_for_timeout(800)
                return
        except Exception:
            continue


async def _arena_rename(page, new_name: str, parallel: bool = False) -> None:
    await _focus(page, parallel)
    chat_id = page.url.rstrip("/").split("/")[-1].split("?")[0]
    href = f"/agent/{chat_id}"
    await _arena_ensure_sidebar(page)

    li = page.locator(f"li:has(a[href='{href}'])").first
    await li.wait_for(state="visible", timeout=30_000)
    await li.hover()
    await page.wait_for_timeout(600)

    menu_btn = li.locator("button").first
    await menu_btn.click(timeout=15_000)
    await page.wait_for_timeout(800)

    rename_item = page.locator("[role=menuitem]:has-text('Rename')").first
    await rename_item.wait_for(state="visible", timeout=15_000)
    await rename_item.click()
    await page.wait_for_timeout(800)

    dialog = page.locator("[role=dialog]").first
    await dialog.wait_for(state="visible", timeout=15_000)
    field = dialog.locator("input").first
    await field.wait_for(state="visible", timeout=15_000)
    await field.fill(new_name[:100])
    await page.wait_for_timeout(300)
    await dialog.get_by_role("button", name="Rename").first.click()
    await page.wait_for_timeout(1200)


# --------------------------------------------------------------------------- #
#  ikale: сэмплы, ответы, результат
# --------------------------------------------------------------------------- #

async def _ikale_prompts(page) -> list[str]:
    state = await page.evaluate(_IKALE_STATE_JS)
    panels = state.get("panels") or []
    return [p.get("prompt", "") for p in panels]


async def _ikale_fill_reply(page, index: int, text: str, parallel: bool = False) -> None:
    await _focus(page, parallel)
    panel = page.locator(f"article#sample-panel-{index}")
    area = panel.locator("textarea").first
    await area.click(timeout=20_000)
    await area.fill(text)
    await page.wait_for_timeout(500)


_IKALE_RESULT_JS = """
() => {
  const visible = el => {
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  };
  const big = el => parseFloat(getComputedStyle(el).fontSize || '0');

  // проценты уверенности: отдельные крупные узлы вида «21.5%»
  let pct = null, pctSize = 0;
  for (const el of document.querySelectorAll('body *')) {
    const t = (el.innerText || '').trim();
    if (el.children.length === 0 && /^\\d{1,3}(\\.\\d+)?%$/.test(t) && visible(el)) {
      const size = big(el);
      if (size >= pctSize) { pct = t; pctSize = size; }
    }
  }

  // название модели: самый крупный текстовый узел после заголовка Result
  let model = null, modelSize = 0;
  const body = document.body.innerText || '';
  const resultIdx = body.indexOf('Result');
  for (const el of document.querySelectorAll('body *')) {
    if (el.children.length !== 0) continue;
    const t = (el.innerText || '').trim();
    if (!t || t.length > 80 || t === 'Result') continue;
    if (/^\\d/.test(t) || /%$/.test(t)) continue;
    if (!visible(el)) continue;
    const size = big(el);
    if (size < 18) continue;
    const top = el.getBoundingClientRect().top + window.scrollY;
    if (resultIdx >= 0 && top < 0) continue;
    if (size > modelSize) { model = t; modelSize = size; }
  }

  const warn = /Low confidence|Not like a language model reply/i.test(body);
  return {pct, model, warn, hasResult: /Result/.test(body)};
}
"""


async def _ikale_verify(page, timeout: float = 180, parallel: bool = False) -> dict:
    await _focus(page, parallel)
    verify_btn = page.locator("button:has-text('Verify')").first
    await verify_btn.wait_for(state="visible", timeout=30_000)
    label = (await verify_btn.inner_text()).strip()
    if "/" in label:
        done, total = label.split("/")
        if done.strip() != total.strip():
            raise RuntimeError(t("flow.err_partial", label=label))

    await verify_btn.click()
    start = time.time()
    result: dict = {}
    while time.time() - start < timeout:
        await page.wait_for_timeout(2000)
        try:
            state = await page.evaluate(_IKALE_RESULT_JS)
        except Exception:
            continue
        if state.get("hasResult") and (state.get("pct") or state.get("model")):
            result = state
            if state.get("pct") and state.get("model"):
                break
    if not result.get("model"):
        raise RuntimeError(t("flow.err_no_result"))
    return result


# --------------------------------------------------------------------------- #
#  Один чат целиком
# --------------------------------------------------------------------------- #

async def _run_chat(ctx, index: int, total: int, arena, ikale, parallel: bool = False) -> ChatResult:
    result = ChatResult(index=index)
    tag = f"{C.accent}{t('flow.chat', i=index + 1, n=total)}{C.reset}"

    try:
        await log(f"{tag} {t('flow.preparing')}")
        await _arena_await_ready(arena)
        prompts = await _ikale_prompts(ikale)
        if len(prompts) < SAMPLES:
            raise RuntimeError(t("flow.no_samples"))

        for sample in range(SAMPLES):
            prompt = prompts[sample]
            if not prompt:
                raise RuntimeError(t("flow.empty_prompt", n=sample + 1))

            await log(f"{tag} {t('flow.sending', i=sample + 1, n=SAMPLES)}")
            await _arena_send(arena, prompt, parallel)

            await log(f"{tag} {t('flow.waiting', i=sample + 1, n=SAMPLES)}")
            reply = await _arena_wait_reply(arena, prompt)
            result.replies.append(reply)

            await _ikale_fill_reply(ikale, sample, reply, parallel)
            await log(f"{tag} {t('flow.inserted', i=sample + 1, n=SAMPLES, chars=len(reply))}")

        await log(f"{tag} {t('flow.verifying')}")
        verdict = await _ikale_verify(ikale, parallel=parallel)
        result.model = (verdict.get("model") or "").strip()
        result.confidence = (verdict.get("pct") or "").strip()

        if verdict.get("warn"):
            await log(f"{tag} {C.warn}{t('flow.low_confidence')}{C.reset}")

        new_name = f"{result.model} {result.confidence}".strip()
        await log(f"{tag} {t('flow.renaming', name=new_name)}")
        await _arena_rename(arena, new_name, parallel)
        result.renamed_to = new_name
        await log(f"{tag} {C.ok}{t('flow.done')}{C.reset} — {new_name}")

    except Exception as exc:
        result.error = f"{type(exc).__name__}: {str(exc).splitlines()[0]}"
        await log(f"{tag} {C.err}{t('flow.error')}: {result.error}{C.reset}")

    return result


# --------------------------------------------------------------------------- #
#  Запуск всего потока
# --------------------------------------------------------------------------- #

async def _run(count: int, parallel: bool = False) -> list[ChatResult]:
    from playwright.async_api import async_playwright

    if not is_connected():
        raise RuntimeError(t("flow.err_no_context"))

    PROFILE_DIR.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(
            str(PROFILE_DIR),
            headless=False,
            no_viewport=True,
            user_agent=UA,
            locale="en-US",
            color_scheme="dark",
            ignore_default_args=["--enable-automation"],
            args=["--disable-blink-features=AutomationControlled", "--start-maximized"],
            permissions=["clipboard-read", "clipboard-write"],
        )
        results: list[ChatResult] = []
        try:
            # 1) открываем ровно `count` вкладок Arena в режиме Agent
            arena_pages = []
            for i in range(count):
                page = await ctx.new_page()
                await page.goto(AGENT_URL, wait_until="domcontentloaded", timeout=90_000)
                arena_pages.append(page)
                await log(f"{C.accent}{t('flow.tabs_arena', i=i + 1, n=count)}{C.reset}")

            # 2) открываем столько же вкладок lm.ikale.io
            ikale_pages = []
            for i in range(count):
                page = await ctx.new_page()
                await page.goto(IKALE_URL, wait_until="domcontentloaded", timeout=90_000)
                ikale_pages.append(page)
                await log(f"{C.accent}{t('flow.tabs_ikale', i=i + 1, n=count)}{C.reset}")

            await asyncio.sleep(2)
            mode = t("mode.parallel") if parallel else t("mode.serial")
            await log(f"{C.accent}{t('flow.mode', mode=mode, n=count)}{C.reset}")

            # 3) обработка
            if parallel:
                # все пары вкладок работают одновременно
                results = list(
                    await asyncio.gather(
                        *[
                            _run_chat(ctx, i, count, arena_pages[i], ikale_pages[i], parallel=True)
                            for i in range(count)
                        ]
                    )
                )
            else:
                # пары обрабатываются по очереди
                for i in range(count):
                    results.append(await _run_chat(ctx, i, count, arena_pages[i], ikale_pages[i]))
        finally:
            try:
                await ctx.close()
            except Exception:
                pass
        return results


def run(count: int, parallel: bool = False) -> list[ChatResult]:
    """count чатов; parallel=True — все пары вкладок работают одновременно."""
    from arena_login import load_config

    i18n.set_language(load_config().get("lang"))
    return asyncio.run(_run(count, parallel))
