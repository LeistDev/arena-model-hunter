#!/usr/bin/env python3
"""
arena model hunter — точка входа.

Запуск:   python main.py
"""

from __future__ import annotations

import sys

import flow
import i18n
import ui
from arena_login import (
    friendly_error,
    is_connected,
    is_parallel,
    is_unlimited,
    login,
    logout,
    save_config,
    session_email,
)
from arena_login import load_config
from i18n import t
from ui import C


def load_config_lang() -> str:
    return load_config().get("lang") or i18n.DEFAULT_LANG

RESET = C.reset

# --------------------------------------------------------------------------- #
#  Пункты меню (набор зависит от состояния аккаунта)
# --------------------------------------------------------------------------- #

START, LOGIN, SETTINGS, EXIT = "start", "login", "settings", "exit"

MAX_CHATS = 100          # лимит по умолчанию
HUGE_CHATS = 100         # выше этого спрашиваем подтверждение и без лимита


def main_items() -> list[tuple[str, str, str]]:
    connected = is_connected()
    items: list[tuple[str, str, str]] = [
        (
            START,
            t("menu.start"),
            f"{C.ok}{t('hint.ready')}{C.reset}"
            if connected
            else f"{C.dim}{t('hint.login_required')}{C.reset}",
        ),
    ]
    if not connected:
        items.append((LOGIN, t("menu.login"), f"{C.accent}{t('hint.mandatory')}{C.reset}"))
    items.append((SETTINGS, t("menu.settings"), f"{C.dim}{t('hint.settings')}{C.reset}"))
    items.append((EXIT, t("menu.exit"), ""))
    return items


def settings_items() -> list[tuple[str, str, str]]:
    parallel = is_parallel()
    items: list[tuple[str, str, str]] = [
        (
            "threads",
            t("settings.threads"),
            f"{C.accent}{t('mode.parallel')}{C.reset}"
            if parallel
            else f"{C.ok}{t('mode.serial')}{C.reset}",
        ),
        (
            "language",
            t("settings.language"),
            f"{C.accent}{i18n.LANGS[i18n.get_language()]}{C.reset}",
        ),
        (
            "unlimited",
            f"{C.text}{t('settings.unlimited')}{C.reset}",
            f"{C.err}⚠ {t('unlimited.on')}{C.reset}"
            if is_unlimited()
            else f"{C.dim}{t('unlimited.off')}{C.reset}",
        ),
    ]
    if is_connected():
        email = session_email() or ""
        items.append(("logout", t("settings.logout"), f"{C.dim}{email}{C.reset}"))
    else:
        items.append(("noop", t("settings.noop"), f"{C.dim}{t('hint.nothing_to_delete')}{C.reset}"))
    items.append(("back", t("settings.back"), ""))
    return items


def body_lines(text: str) -> list[str]:
    """Многострочный текст подтверждения → строки с отступом под рамку."""
    return [f" {C.muted}{line}{RESET}" if line else "" for line in text.split("\n")]


def status_line() -> str:
    mode = (
        f"{C.accent}{t('mode.parallel')}{RESET}"
        if is_parallel()
        else f"{C.dim}{t('mode.serial')}{RESET}"
    )
    lang = f"{C.dim}{i18n.LANGS[i18n.get_language()]}{RESET}"
    if is_unlimited():
        lang += f"  {C.dim}·{RESET}  {C.err}⚠ {t('unlimited.short')}{RESET}"
    if is_connected():
        email = session_email() or ""
        return (
            f"{C.ok}{t('status.connected')}{RESET}  {C.dim}·{RESET}  {C.dim}{email}{RESET}\n"
            f"{C.warn}◷{RESET} {t('status.mode')} {mode}  {C.dim}·{RESET}  {lang}"
        )
    return (
        f"{C.warn}{t('status.disconnected')}{RESET}  {C.dim}·  {t('status.signin_hint')}{RESET}\n"
        f"{C.warn}◷{RESET} {t('status.mode')} {mode}  {C.dim}·{RESET}  {lang}"
    )


# --------------------------------------------------------------------------- #
#  Цикл выбора
# --------------------------------------------------------------------------- #

def menu_loop(items_fn, cursor_key: str | None = None) -> str:
    """
    Показывает меню и возвращает ключ выбранного пункта.
    Экран перерисовывается при любом изменении размера окна
    (разворот на весь экран, ресайз) — поэтому центрирование всегда актуально.
    """
    keys = ui.KeyReader()
    ui.enter_alt_screen()
    ui.hide_cursor()
    drawn_size: tuple[int, int] | None = None
    try:
        while True:
            items = items_fn()
            keys_available = [k for k, _, _ in items]
            if cursor_key not in keys_available:
                cursor_key = keys_available[0]
            cursor = keys_available.index(cursor_key)

            size = ui.term_size()
            if size != drawn_size:
                ui.clear()
                ui.render_menu(status_line(), items, cursor)
                drawn_size = size

            key = keys.read(timeout=0.15)

            if key is None:
                # пауза: проверяем, не изменился ли размер окна
                if ui.term_size() != drawn_size:
                    pass  # перерисуем на следующей итерации
                continue

            if key == ui.UP:
                cursor_key = keys_available[(cursor - 1) % len(items)]
            elif key == ui.DOWN:
                cursor_key = keys_available[(cursor + 1) % len(items)]
            elif key == ui.ENTER:
                return cursor_key
            elif key == ui.ESC:
                return "back" if items_fn is settings_items else EXIT
            elif key.isdigit() and 1 <= int(key) <= len(items):
                return keys_available[int(key) - 1]

            # после нажатия перерисовываем (подсветка курсора)
            drawn_size = None
    finally:
        ui.show_cursor()
        ui.exit_alt_screen()


def confirm(danger: str, confirm_label: str) -> bool:
    """Экран подтверждения. Возвращает True, если пользователь согласился."""
    keys = ui.KeyReader()
    cursor = 1  # по умолчанию безопасный вариант — «Отмена»
    options = [
        ("yes", confirm_label, f"{C.err}{t('confirm.irreversible')}{RESET}"),
        ("no", t("confirm.cancel"), f"{C.dim}{t('confirm.safe')}{RESET}"),
    ]
    drawn_size: tuple[int, int] | None = None
    ui.enter_alt_screen()
    ui.hide_cursor()
    try:
        while True:
            size = ui.term_size()
            if size != drawn_size:
                ui.clear()
                ui.render_menu(danger, options, cursor)
                drawn_size = size

            key = keys.read(timeout=0.15)
            if key is None:
                continue
            if key in (ui.UP, ui.DOWN):
                cursor = 1 - cursor
                drawn_size = None
            elif key == ui.ENTER:
                return cursor == 0
            elif key in (ui.ESC, "n"):
                return False
            elif key == "y":
                return True
    finally:
        ui.show_cursor()
        ui.exit_alt_screen()


# --------------------------------------------------------------------------- #
#  Действия
# --------------------------------------------------------------------------- #

def do_login() -> None:
    result = login(email_hint=session_email())
    ui.enter_alt_screen()
    ui.clear()
    if result.get("ok"):
        ui.render_panel(
            [
                f"{C.ok}{C.bold}{t('login.panel_ok')}{RESET}",
                "",
                f" {C.muted}{t('login.email')}{RESET} {result.get('email') or '—'}",
                f" {C.muted}{t('login.theme_line')}{RESET} {t('login.theme_dark')}",
                f" {C.muted}{t('login.session')}{RESET} {t('login.session_saved')}",
            ]
        )
    else:
        ui.render_panel(
            [
                f"{C.err}{C.bold}{t('login.panel_fail')}{RESET}",
                "",
                f" {C.muted}{result.get('error') or t('err.unknown')}{RESET}",
            ]
        )
    ui.wait_enter()
    ui.exit_alt_screen()


def do_settings() -> None:
    cursor_key = "threads"
    while True:
        choice = menu_loop(settings_items, cursor_key=cursor_key)
        cursor_key = choice if choice not in ("back", "noop") else "threads"
        if choice in ("back", "noop"):
            return
        if choice == "threads":
            save_config(parallel=not is_parallel())
            continue
        if choice == "unlimited":
            turning_on = not is_unlimited()
            if turning_on:
                body = body_lines(t("confirm.unlimited.body"))
                agreed = confirm(
                    f"{C.warn}{C.bold}{t('confirm.unlimited.title')}{RESET}\n"
                    + "\n".join(body),
                    t("confirm.unlimited.yes"),
                )
                if not agreed:
                    continue
            save_config(unlimited=turning_on)
            continue
        if choice == "language":
            order = list(i18n.LANGS)
            current = i18n.get_language()
            next_lang = order[(order.index(current) + 1) % len(order)]
            save_config(lang=next_lang)
            i18n.set_language(next_lang)
            continue
        if choice == "logout":
            email = session_email() or ""
            agreed = confirm(
                f"{C.text}{t('confirm.logout.title')}{RESET}\n"
                f" {C.muted}{email}{RESET}",
                t("confirm.logout.yes"),
            )
            if not agreed:
                continue
            result = logout()
            ui.enter_alt_screen()
            ui.clear()
            ui.render_panel(
                [
                    f"{C.ok}{C.bold}{t('logout.panel_ok')}{RESET}",
                    "",
                    f" {C.muted}{t('logout.panel_1')}{RESET}",
                    f" {C.muted}{t('logout.panel_2')}{RESET}",
                    "",
                    f" {C.dim}{result.get('detail', '')}{RESET}",
                ]
            )
            ui.wait_enter()
            ui.exit_alt_screen()
            return


def do_start() -> None:
    ui.clear()
    if not is_connected():
        ui.render_panel(
            [
                f"{C.warn}{C.bold}{t('start.no_account')}{RESET}",
                "",
                f" {t('start.no_account_hint', item=C.accent + '«' + t('menu.login') + '»' + C.reset)}",
            ]
        )
        ui.wait_enter()
        return

    unlimited = is_unlimited()
    hi = None if unlimited else MAX_CHATS
    with ui.alt_screen():
        count = ui.ask_number(
            t("start.count_title"),
            t("start.count_hint", hi=hi if hi else "∞"),
            1,
            hi,
            note=t("start.unlimited_note") if unlimited else "",
        )
    if count is None:
        return

    if count > HUGE_CHATS:
        body = body_lines(t("confirm.huge.body", count=count))
        agreed = confirm(
            f"{C.warn}{C.bold}{t('confirm.huge.title', count=count)}{RESET}\n"
            + "\n".join(body),
            t("confirm.huge.yes"),
        )
        if not agreed:
            return

    parallel = is_parallel()
    ui.exit_alt_screen()   # логи прогона печатаем в обычном буфере
    ui.clear()
    ui.render_panel(
        [
            f"{C.text}{t('start.running', count=count)}{RESET}",
            "",
            f" {C.muted}{t('start.running_line1')}{RESET}",
            f" {C.muted}{t('start.running_line2')}{RESET}",
            "",
            " " + t(
                "start.running_mode",
                mode=(C.accent + t("mode.parallel") + RESET)
                if parallel
                else (C.ok + t("mode.serial") + RESET),
            ),
        ]
    )

    try:
        results = flow.run(count, parallel=parallel)
    except Exception as exc:  # не установлен браузер, закрыт профиль и т.п.
        with ui.alt_screen():
            ui.render_panel(
                [
                    f"{C.err}{C.bold}{t('login.panel_fail')}{RESET}",
                    "",
                    f" {C.muted}{friendly_error(exc)}{RESET}",
                ]
            )
            ui.wait_enter()
        return
    show_results(results)


def show_results(results: list) -> None:
    ui.clear()
    ok = [r for r in results if r.ok]
    lines: list[str] = [
        f"{C.bold}{t('results.summary', ok=len(ok), total=len(results))}{RESET}",
        "",
    ]
    for r in results:
        if r.ok:
            name = f"{C.accent}{r.model}{RESET} {C.text}{r.confidence}{RESET}".strip()
            lines.append(f" {C.ok}✓{RESET} {t('results.chat', n=r.index + 1)}: {name}")
        else:
            lines.append(
                f" {C.err}✗{RESET} {t('results.chat', n=r.index + 1)}: {C.dim}{r.error}{RESET}"
            )
    if ok:
        lines += ["", f" {C.muted}{t('results.renamed')}{RESET}"]
    with ui.alt_screen():
        ui.render_panel(lines)
        ui.wait_enter()


def main() -> int:
    ui.enable_ansi()
    i18n.set_language(load_config_lang())
    ui.enter_alt_screen()
    cursor_key = START if is_connected() else LOGIN
    try:
        while True:
            choice = menu_loop(main_items, cursor_key=cursor_key)
            cursor_key = choice if choice in (START, LOGIN, SETTINGS) else START
            if choice == EXIT:
                ui.exit_alt_screen()          # возвращаемся в обычный буфер терминала
                print(f"\n  {C.dim}{t('common.bye')}{RESET}\n")
                return 0
            if choice == LOGIN:
                do_login()
                cursor_key = START  # после успешного входа пункт входа исчезает
            elif choice == SETTINGS:
                do_settings()
            elif choice == START:
                do_start()
    except KeyboardInterrupt:
        ui.show_cursor()
        ui.clear()
        ui.exit_alt_screen()
        return 130


if __name__ == "__main__":
    sys.exit(main())
