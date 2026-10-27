"""
Минималистичный TUI для консоли — в духе Claude Code:
тёмная палитра, тонкая рамка, аккуратные акценты, управление стрелками.
Блок центрируется по горизонтали и вертикали, корректно ведёт себя
на любом размере окна. Без внешних зависимостей.
"""
# arena model hunter — model hunter for arena.ai
# Copyright (C) 2026 arena model hunter contributors
# SPDX-License-Identifier: MIT
#
# This program is licensed under the MIT License. See LICENSE for details.


from __future__ import annotations

import os
import shutil
import sys
import time
import unicodedata

from i18n import t

RESET = "\x1b[0m"


def _fg(r: int, g: int, b: int) -> str:
    return f"\x1b[38;2;{r};{g};{b}m"


def _bg(r: int, g: int, b: int) -> str:
    return f"\x1b[48;2;{r};{g};{b}m"


class C:
    """Палитра."""

    accent = _fg(178, 152, 255)
    accent_soft = _fg(126, 108, 190)
    text = _fg(226, 226, 232)
    muted = _fg(118, 118, 132)
    dim = _fg(86, 86, 98)
    border = _fg(70, 70, 84)
    ok = _fg(126, 204, 148)
    warn = _fg(228, 182, 100)
    err = _fg(228, 124, 124)
    sel_bg = _bg(36, 31, 54)
    bold = "\x1b[1m"
    reset = RESET


def enable_ansi() -> None:
    """Включает ANSI-последовательности в консоли Windows и UTF-8 вывод."""
    if os.name == "nt":
        os.system("")
        try:
            import ctypes

            k = ctypes.windll.kernel32
            h = k.GetStdHandle(-11)
            mode = ctypes.c_uint32()
            if k.GetConsoleMode(h, ctypes.byref(mode)):
                k.SetConsoleMode(h, mode.value | 0x0004)
        except Exception:
            pass
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def clear() -> None:
    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.flush()


# --------------------------------------------------------------------------- #
#  Альтернативный экран (как в htop/vim/Claude Code)
#  Меню рисуется во втором буфере терминала, поэтому в скроллбэке
#  не остаётся десятков копий интерфейса, а при выходе возвращается
#  прежнее содержимое консоли.
# --------------------------------------------------------------------------- #

_alternative = False


def enter_alt_screen() -> None:
    global _alternative
    if _alternative:
        return
    if not (sys.stdout and sys.stdout.isatty()):
        return
    sys.stdout.write("\x1b[?1049h\x1b[2J\x1b[H")
    sys.stdout.flush()
    _alternative = True


def exit_alt_screen() -> None:
    global _alternative
    if not _alternative:
        return
    sys.stdout.write("\x1b[?25h\x1b[?1049l")
    sys.stdout.flush()
    _alternative = False


class alt_screen:
    """with ui.alt_screen(): ... — рисуем во втором буфере, потом возвращаемся."""

    def __enter__(self):
        enter_alt_screen()
        return self

    def __exit__(self, *exc):
        exit_alt_screen()
        return False


def hide_cursor() -> None:
    sys.stdout.write("\x1b[?25l")
    sys.stdout.flush()


def show_cursor() -> None:
    sys.stdout.write("\x1b[?25h")
    sys.stdout.flush()


# --------------------------------------------------------------------------- #
#  Геометрия
# --------------------------------------------------------------------------- #

MIN_WIDTH = 52
MAX_WIDTH = 76
SIDE_MARGIN = 4


def term_size() -> tuple[int, int]:
    """Размер видимого окна терминала (обновляется при развороте на весь экран)."""
    if os.name == "nt":
        try:
            import ctypes

            class COORD(ctypes.Structure):
                _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

            class SMALL_RECT(ctypes.Structure):
                _fields_ = [
                    ("Left", ctypes.c_short),
                    ("Top", ctypes.c_short),
                    ("Right", ctypes.c_short),
                    ("Bottom", ctypes.c_short),
                ]

            class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
                _fields_ = [
                    ("dwSize", COORD),
                    ("dwCursorPosition", COORD),
                    ("wAttributes", ctypes.c_ushort),
                    ("srWindow", SMALL_RECT),
                    ("dwMaximumWindowSize", COORD),
                ]

            k = ctypes.windll.kernel32
            handle = k.GetStdHandle(-11)
            info = CONSOLE_SCREEN_BUFFER_INFO()
            if k.GetConsoleScreenBufferInfo(handle, ctypes.byref(info)):
                cols = info.srWindow.Right - info.srWindow.Left + 1
                rows = info.srWindow.Bottom - info.srWindow.Top + 1
                if cols > 10 and rows > 5:
                    return int(cols), int(rows)
        except Exception:
            pass
    size = shutil.get_terminal_size((100, 32))
    return size.columns, size.lines


def box_width() -> int:
    cols, _ = term_size()
    width = min(MAX_WIDTH, cols - 2 * SIDE_MARGIN)
    return max(MIN_WIDTH, width)


def char_width(ch: str) -> int:
    """Ширина символа в знакоместах: иероглифы и полноширинные — 2."""
    if unicodedata.combining(ch):
        return 0
    return 2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1


def text_width(text: str) -> int:
    return sum(char_width(ch) for ch in text)


def _visible_len(s: str) -> int:
    out, i = 0, 0
    while i < len(s):
        if s[i] == "\x1b":
            while i < len(s) and s[i] != "m":
                i += 1
            i += 1
            continue
        out += char_width(s[i])
        i += 1
    return out


def _pad(text: str, width: int) -> str:
    return text + " " * max(0, width - _visible_len(text))


def _frame(body: list[str], width: int, indent: str) -> list[str]:
    inner = width - 2
    out = [f"{indent}{C.border}╭" + "─" * inner + f"╮{RESET}"]
    for line in body:
        out.append(f"{indent}{C.border}│{RESET}" + _pad(" " + line, inner) + f"{C.border}│{RESET}")
    out.append(f"{indent}{C.border}╰" + "─" * inner + f"╯{RESET}")
    return out


def _indent_for(width: int) -> str:
    cols, _ = term_size()
    return " " * max(0, (cols - (width + 2)) // 2)


# --------------------------------------------------------------------------- #
#  Ключи
# --------------------------------------------------------------------------- #

UP, DOWN, ENTER, ESC = "up", "down", "enter", "esc"


class KeyReader:
    """
    Чтение одиночных нажатий: Windows (msvcrt) и POSIX (termios).
    Поддерживает таймаут, чтобы интерфейс успевал перерисоваться
    при изменении размера окна (разворот на весь экран).
    """

    def __init__(self) -> None:
        self.interactive = sys.stdin is not None and sys.stdin.isatty()

    def read(self, timeout: float | None = None) -> str | None:
        if not self.interactive:
            line = input().strip().lower()
            return {"1": "1", "2": "2", "3": "3", "4": "4", "q": ESC}.get(line, line or ESC)
        if os.name == "nt":
            return self._read_windows(timeout)
        return self._read_posix(timeout)

    @staticmethod
    def _decode(ch: bytes) -> str:
        if ch in (b"\r", b"\n"):
            return ENTER
        if ch in (b"q", b"Q", b"\x03", b"\x04"):
            return ESC
        try:
            return ch.decode("utf-8")
        except UnicodeDecodeError:
            return ""

    def _read_windows(self, timeout: float | None) -> str | None:
        import msvcrt

        def take() -> str:
            ch = msvcrt.getch()
            if ch in (b"\x00", b"\xe0"):
                code = msvcrt.getch()
                return {b"H": UP, b"P": DOWN, b"K": "left", b"M": "right"}.get(code, "")
            if ch == b"\x1b":
                return ESC
            return self._decode(ch)

        if timeout is None:
            return take()

        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            if msvcrt.kbhit():
                return take()
            time.sleep(0.03)
        return None

    def _read_posix(self, timeout: float | None) -> str | None:
        import select
        import termios
        import tty

        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)

            if timeout is not None:
                ready, _, _ = select.select([fd], [], [], timeout)
                if not ready:
                    return None

            def read1() -> bytes:
                # читаем из fd напрямую: текстовый stdin буферизует и ломает select
                return os.read(fd, 1)

            ch = read1()
            if ch == b"\x1b":
                # хвост последовательности стрелок: ESC [ A / B / C / D
                seq = b""
                deadline = time.monotonic() + 0.30
                while len(seq) < 2 and time.monotonic() < deadline:
                    if not select.select([fd], [], [], 0.05)[0]:
                        continue
                    seq += read1()
                return {b"[A": UP, b"[B": DOWN, b"[C": "right", b"[D": "left"}.get(seq, ESC)
            return self._decode(ch)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


# --------------------------------------------------------------------------- #
#  Экраны
# --------------------------------------------------------------------------- #

def logo() -> list[str]:
    return [
        f"{C.accent}{C.bold} ✦  arena model hunter{RESET}",
        f"{C.dim}    {t('app.subtitle')} · v1.0.0{RESET}",
    ]


def render_menu(status_line: str, items: list[tuple[str, str, str]], cursor: int) -> None:
    """
    Главный экран: рамка по центру окна.

    items: список (ключ, название, подпись справа)
    """
    width = box_width()
    inner = width - 4

    body: list[str] = [""]
    body.extend(logo())
    body.append("")
    if status_line:
        for line in status_line.split("\n"):
            body.append(f" {line}")
        body.append("")

    for idx, (_key, label, hint) in enumerate(items):
        selected = idx == cursor
        marker = f"{C.accent}▸{RESET}" if selected else " "
        name = f"{C.accent}{C.bold}{label}{RESET}" if selected else f"{C.text}{label}{RESET}"
        gap = inner - 3 - _visible_len(label) - _visible_len(hint)
        row = f"{marker} {name}" + " " * max(2, gap) + hint
        if selected:
            row = C.sel_bg + _pad(" " + row, inner) + RESET
        body.append(row)

    body.append("")
    body.append(f"{C.dim}{t('menu.help')}{RESET}")
    body.append("")

    lines = _frame(body, width, _indent_for(width))
    _, rows = term_size()
    top = max(0, (rows - len(lines)) // 2 - 1)
    sys.stdout.write("\x1b[H" + "\n" * top + "\n".join(lines) + "\n\x1b[J")
    sys.stdout.flush()


def render_panel(lines: list[str], top_margin: int | None = None) -> None:
    """Панель сообщения: по центру по горизонтали, отступ сверху — по центру окна."""
    width = box_width()
    body = [""] + [f" {ln}" for ln in lines] + [""]
    frame = _frame(body, width, _indent_for(width))
    _, rows = term_size()
    if top_margin is None:
        top_margin = max(2, (rows - len(frame)) // 2 - 2)
    sys.stdout.write("\x1b[H" + "\n" * top_margin + "\n".join(frame) + "\n\x1b[J")
    sys.stdout.flush()


def wait_enter(prompt: str | None = None) -> None:
    if not (sys.stdin and sys.stdin.isatty()):
        return
    prompt = prompt or t("common.continue")
    cols, _ = term_size()
    text = f"{C.dim}{prompt}{RESET}"
    pad = max(0, (cols - text_width(prompt)) // 2)
    sys.stdout.write("\n" + " " * pad + text)
    sys.stdout.flush()
    try:
        sys.stdin.readline()
    except (KeyboardInterrupt, EOFError):
        pass


def rule(text: str = "") -> None:
    cols, _ = term_size()
    if text:
        print(f"\n  {C.accent}{text}{RESET}")
    print(f"  {C.dim}" + "─" * max(10, min(cols - 4, MAX_WIDTH)) + f"{RESET}")


def ask_number(
    title: str,
    hint: str,
    lo: int,
    hi: int | None = None,
    note: str = "",
) -> int | None:
    """
    Экран ввода числа по центру. Возвращает число или None при отмене.
    Пустой ввод / Esc — отмена. hi=None — без верхнего предела
    (режим «неограниченное число чатов»), note — красная строка-предупреждение.
    """
    show_cursor()
    while True:
        width = box_width()
        body = ["", f" {C.text}{title}{RESET}"]
        if note:
            for line in note.split("\n"):
                body.append(f" {C.err}{line}{RESET}")
        body.append(f" {C.dim}{hint}{RESET}")
        body.append("")
        frame = _frame(body, width, _indent_for(width))
        _, rows = term_size()
        sys.stdout.write("\x1b[H" + "\n" * max(2, (rows - len(frame)) // 2 - 3) + "\n".join(frame) + "\n\x1b[J")
        sys.stdout.flush()

        cols, _ = term_size()
        pad = " " * max(0, (cols - width) // 2 + 2)
        sys.stdout.write(f"{pad}{C.accent}›{RESET} ")
        sys.stdout.flush()
        try:
            raw = sys.stdin.readline()
        except (KeyboardInterrupt, EOFError):
            return None
        if not raw:
            return None
        value = raw.strip()
        if not value:
            return None
        if value.isdigit() and int(value) >= lo and (hi is None or int(value) <= hi):
            return int(value)

        message = (
            t("start.count_invalid_open", lo=lo)
            if hi is None
            else t("start.count_invalid", lo=lo, hi=hi)
        )
        sys.stdout.write(f"{pad}{C.err}{message}{RESET}\n")
        sys.stdout.flush()
        time.sleep(0.9)
