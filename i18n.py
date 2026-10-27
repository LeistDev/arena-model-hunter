"""
Локализация интерфейса: English (по умолчанию), Русский, 中文.

Язык хранится в ~/.arena-model-hunter/config.json ("lang") и меняется
в Настройках. Все строки интерфейса берутся через t("ключ").
"""
# arena model hunter — model hunter for arena.ai
# Copyright (C) 2026 arena model hunter contributors
# SPDX-License-Identifier: GPL-3.0
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License, version 3, as published
# by the Free Software Foundation. It is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See LICENSE for details.


from __future__ import annotations

DEFAULT_LANG = "en"

# код -> как язык называется в меню (на самом языке)
LANGS: dict[str, str] = {
    "en": "English",
    "ru": "Русский",
    "zh": "中文",
}

_STRINGS: dict[str, dict[str, str]] = {
    # ------------------------------------------------------------------ меню
    "app.subtitle": {
        "en": "arena.ai automation",
        "ru": "автоматизация arena.ai",
        "zh": "arena.ai 自动化",
    },
    "menu.help": {
        "en": "↑ ↓  select    ↵  open    q  quit",
        "ru": "↑ ↓  выбор    ↵  открыть    q  выход",
        "zh": "↑ ↓  选择    ↵  打开    q  退出",
    },
    "menu.start": {"en": "Start", "ru": "Начать", "zh": "开始"},
    "menu.login": {
        "en": "Sign in to Arena",
        "ru": "Войти в аккаунт Arena",
        "zh": "登录 Arena 账户",
    },
    "menu.settings": {"en": "Settings", "ru": "Настройки", "zh": "设置"},
    "menu.exit": {"en": "Exit", "ru": "Выход", "zh": "退出"},
    "hint.ready": {"en": "ready", "ru": "готово", "zh": "就绪"},
    "hint.login_required": {
        "en": "sign-in required",
        "ru": "требуется вход",
        "zh": "需要登录",
    },
    "hint.mandatory": {"en": "required", "ru": "обязательно", "zh": "必需"},
    "hint.settings": {
        "en": "account & exit",
        "ru": "аккаунт и выход",
        "zh": "账户与退出",
    },
    "hint.reconnect": {
        "en": "reconnect",
        "ru": "переподключить",
        "zh": "重新连接",
    },
    "hint.nothing_to_delete": {
        "en": "nothing to delete",
        "ru": "нечего удалять",
        "zh": "无可删除项",
    },
    # -------------------------------------------------------------- статус
    "status.connected": {
        "en": "● Arena account connected",
        "ru": "● аккаунт Arena подключён",
        "zh": "● Arena 账户已连接",
    },
    "status.disconnected": {
        "en": "○ Arena account not connected",
        "ru": "○ аккаунт не подключён",
        "zh": "○ Arena 账户未连接",
    },
    "status.signin_hint": {
        "en": "sign in first",
        "ru": "сначала войдите в аккаунт",
        "zh": "请先登录",
    },
    "status.mode": {"en": "mode:", "ru": "режим:", "zh": "模式："},
    "mode.serial": {"en": "single-threaded", "ru": "однопоточный", "zh": "单线程"},
    "mode.parallel": {
        "en": "multi-threaded",
        "ru": "многопоточный",
        "zh": "多线程",
    },
    # ------------------------------------------------------------ настройки
    "settings.threads": {"en": "Run mode", "ru": "Режим работы", "zh": "运行模式"},
    "settings.language": {"en": "Language", "ru": "Язык", "zh": "语言"},
    "settings.logout": {
        "en": "Remove active arena.ai account",
        "ru": "Удалить активный аккаунт arena.ai",
        "zh": "移除当前 arena.ai 账户",
    },
    "settings.noop": {
        "en": "No account connected",
        "ru": "Аккаунт не подключён",
        "zh": "账户未连接",
    },
    "settings.unlimited": {
        "en": "Unlimited chats",
        "ru": "Неограниченное число чатов",
        "zh": "不限聊天数量",
    },
    "unlimited.on": {
        "en": "no limit",
        "ru": "без лимита",
        "zh": "无限制",
    },
    "unlimited.off": {
        "en": "up to 100",
        "ru": "до 100",
        "zh": "最多 100",
    },
    "unlimited.danger": {
        "en": "dangerous",
        "ru": "опасно",
        "zh": "危险",
    },
    "unlimited.short": {
        "en": "unlimited",
        "ru": "без лимита",
        "zh": "无限制",
    },
    "confirm.unlimited.title": {
        "en": "Turn on unlimited chats?",
        "ru": "Включить неограниченное число чатов?",
        "zh": "开启不限聊天数量？",
    },
    "confirm.unlimited.body": {
        "en": [
            "The 100-chat cap disappears: you will be able to start any",
            "number of chats in one run. Hundreds of tabs mean hundreds",
            "of requests to arena.ai at once — expect rate limits,",
            "captchas and a real risk of restriction on your account.",
            "Leave it off if you are not sure.",
        ],
        "ru": [
            "Лимит в 100 чатов исчезает: за один прогон можно будет",
            "запустить любое количество чатов. Сотни вкладок — это сотни",
            "запросов к arena.ai сразу: ждите ограничения по частоте,",
            "капчи и реальный риск ограничения аккаунта.",
            "Не включайте, если не уверены.",
        ],
        "zh": [
            "100 个聊天的上限将被取消：一次运行可以启动任意数量的",
            "聊天。数百个标签页意味着同时向 arena.ai 发出数百个请求：",
            "很可能触发限流、验证码，账户也确实有被封禁的风险。",
            "不确定时请保持关闭。",
        ],
    },
    "confirm.unlimited.yes": {
        "en": "Turn on anyway",
        "ru": "Всё равно включить",
        "zh": "仍然开启",
    },
    "confirm.huge.title": {
        "en": "Start {count} chats in one run?",
        "ru": "Запустить {count} чатов за один прогон?",
        "zh": "一次运行 {count} 个聊天？",
    },
    "confirm.huge.body": {
        "en": [
            "That is far beyond the safe 100-chat limit. The browser will",
            "open {count} Arena tabs and {count} fingerprint tabs, and the",
            "run will take hours. Arena may throttle or block the account.",
        ],
        "ru": [
            "Это сильно больше безопасного лимита в 100 чатов. Браузер",
            "откроет {count} вкладок Arena и {count} вкладок отпечатков,",
            "а прогон займёт часы. Arena может ограничить аккаунт.",
        ],
        "zh": [
            "这已远超 100 个聊天的安全上限。浏览器将打开 {count} 个 Arena",
            "标签页和 {count} 个指纹标签页，运行需要数小时。",
            "Arena 可能会限流或限制账户。",
        ],
    },
    "confirm.huge.yes": {
        "en": "Start anyway",
        "ru": "Всё равно начать",
        "zh": "仍然开始",
    },
    "settings.back": {"en": "Back", "ru": "Назад", "zh": "返回"},
    # --------------------------------------------------------- подтверждение
    "confirm.logout.title": {
        "en": "Remove active arena.ai account?",
        "ru": "Удалить активный аккаунт arena.ai?",
        "zh": "移除当前 arena.ai 账户？",
    },
    "confirm.logout.yes": {
        "en": "Remove account",
        "ru": "Удалить аккаунт",
        "zh": "移除账户",
    },
    "confirm.cancel": {"en": "Cancel", "ru": "Отмена", "zh": "取消"},
    "confirm.irreversible": {
        "en": "irreversible",
        "ru": "необратимо",
        "zh": "不可撤销",
    },
    "confirm.safe": {"en": "safe", "ru": "безопасно", "zh": "安全"},
    # ------------------------------------------------------------ вход
    "login.title": {
        "en": "Connecting Arena account",
        "ru": "Подключение аккаунта Arena",
        "zh": "正在连接 Arena 账户",
    },
    "login.profile": {"en": "profile:", "ru": "профиль:", "zh": "配置目录："},
    "login.site": {"en": "site:", "ru": "сайт:", "zh": "站点："},
    "login.theme": {"en": "theme:", "ru": "тема:", "zh": "主题："},
    "login.theme_dark": {"en": "dark", "ru": "тёмная", "zh": "深色"},
    "login.intro": {
        "en": "Browser opened. Sign in to your account:",
        "ru": "Браузер открыт. Войдите в аккаунт:",
        "zh": "浏览器已打开。请登录账户：",
    },
    "login.step1": {
        "en": "Click Log In in the bottom-left corner",
        "ru": "Нажмите Log In в левом нижнем углу",
        "zh": "点击左下角的 Log In",
    },
    "login.step2": {
        "en": "Enter your email and click Continue with email",
        "ru": "Введите почту и нажмите Continue with email",
        "zh": "输入邮箱并点击 Continue with email",
    },
    "login.step3": {
        "en": "Have a password — enter it and click Log In",
        "ru": "Уже есть пароль — введите его и жмите Log In",
        "zh": "已有密码 — 输入后点击 Log In",
    },
    "login.step3_new": {
        "en": "new email: name can be skipped (Create Account),",
        "ru": "новая почта: имя можно пропустить (Create Account),",
        "zh": "新邮箱：姓名可跳过（Create Account），",
    },
    "login.step3_mail": {
        "en": "then email → link → create password",
        "ru": "затем письмо → ссылка → создание пароля",
        "zh": "然后邮件 → 链接 → 设置密码",
    },
    "login.paste1": {
        "en": "Paste the link from the email into this Chromium window",
        "ru": "Ссылку из письма вставляйте в адресную строку этого окна Chromium",
        "zh": "把邮件中的链接粘贴到此 Chromium 窗口",
    },
    "login.paste2": {
        "en": "(Ctrl+L → Ctrl+V → Enter). As soon as you are signed in,",
        "ru": "(Ctrl+L → Ctrl+V → Enter). Как только вход выполнится,",
        "zh": "（Ctrl+L → Ctrl+V → Enter）。登录成功后，",
    },
    "login.paste3": {
        "en": "I will notice it and close the browser.",
        "ru": "я это замечу и закрою браузер.",
        "zh": "我会自动检测并关闭浏览器。",
    },
    "login.waiting": {
        "en": "Waiting for sign-in… (Ctrl+C to cancel)",
        "ru": "Ожидаю вход… (Ctrl+C — отмена)",
        "zh": "等待登录…（Ctrl+C 取消）",
    },
    "login.poll": {
        "en": "[{sec:>3} s] waiting… page: {url}",
        "ru": "[{sec:>3} c] ждём… страница: {url}",
        "zh": "[{sec:>3} 秒] 等待中… 页面：{url}",
    },
    "login.autofill_done": {
        "en": "form filled automatically (ARENA_EMAIL/ARENA_PASSWORD)",
        "ru": "форма заполнена автоматически (ARENA_EMAIL/ARENA_PASSWORD)",
        "zh": "已自动填写表单（ARENA_EMAIL/ARENA_PASSWORD）",
    },
    "login.autofill_email": {
        "en": "email prefilled, just confirm sign-in",
        "ru": "почта подставлена, осталось подтвердить вход",
        "zh": "邮箱已填写，请确认登录",
    },
    "login.autofill_unavailable": {
        "en": "autofill unavailable — please sign in manually",
        "ru": "автозаполнение недоступно — войдите вручную",
        "zh": "无法自动填写 — 请手动登录",
    },
    "login.already": {
        "en": "● Account already authorized in this profile",
        "ru": "● Аккаунт уже авторизован в этом профиле",
        "zh": "● 该配置目录中的账户已授权",
    },
    "login.already_skip": {
        "en": "No need to reconnect — closing the browser.",
        "ru": "Переподключаться не нужно — закрываю браузер.",
        "zh": "无需重新连接 — 正在关闭浏览器。",
    },
    "login.ok": {
        "en": "✓ Signed in — session saved",
        "ru": "✓ Вход выполнен — сессия сохранена",
        "zh": "✓ 登录成功 — 会话已保存",
    },
    "login.closing": {
        "en": "Closing the browser…",
        "ru": "Закрываю браузер…",
        "zh": "正在关闭浏览器…",
    },
    "login.panel_ok": {
        "en": "✓ Arena account connected",
        "ru": "✓ Аккаунт Arena подключён",
        "zh": "✓ Arena 账户已连接",
    },
    "login.panel_fail": {
        "en": "✗ Sign-in failed",
        "ru": "✗ Вход не выполнен",
        "zh": "✗ 登录失败",
    },
    "login.email": {"en": "email:", "ru": "почта:", "zh": "邮箱："},
    "login.theme_line": {"en": "theme:", "ru": "тема:", "zh": "主题："},
    "login.session": {"en": "session:", "ru": "сессия:", "zh": "会话："},
    "login.session_saved": {
        "en": "saved in the browser profile",
        "ru": "сохранена в профиле браузера",
        "zh": "已保存在浏览器配置中",
    },
    # ------------------------------------------------------- ошибки входа
    "err.open_site": {
        "en": "could not open {url}: {error}",
        "ru": "не удалось открыть {url}: {error}",
        "zh": "无法打开 {url}：{error}",
    },
    "err.window_closed": {
        "en": "browser window was closed before sign-in completed",
        "ru": "окно браузера закрыто до завершения входа",
        "zh": "登录完成前浏览器窗口已关闭",
    },
    "err.login_timeout": {
        "en": "sign-in timeout expired",
        "ru": "истекло время ожидания входа",
        "zh": "登录等待超时",
    },
    "err.cancelled": {
        "en": "cancelled by user",
        "ru": "отменено пользователем",
        "zh": "已由用户取消",
    },
    "err.no_playwright": {
        "en": "Playwright is not installed.\n"
        "    Run:  pip install -r requirements.txt\n"
        "          python -m playwright install chromium",
        "ru": "не установлен Playwright.\n"
        "    Выполните:  pip install -r requirements.txt\n"
        "                python -m playwright install chromium",
        "zh": "未安装 Playwright。\n"
        "    请运行：pip install -r requirements.txt\n"
        "            python -m playwright install chromium",
    },
    "err.no_browser": {
        "en": "browser is not installed. Run: python -m playwright install chromium",
        "ru": "не установлен браузер. Выполните: python -m playwright install chromium",
        "zh": "未安装浏览器。请运行：python -m playwright install chromium",
    },
    "err.browser_closed": {
        "en": "browser was closed before sign-in completed",
        "ru": "браузер был закрыт до завершения входа",
        "zh": "登录完成前浏览器已关闭",
    },
    "err.unknown": {
        "en": "unknown error",
        "ru": "неизвестная ошибка",
        "zh": "未知错误",
    },
    # ---------------------------------------------------------- запуск чатов
    "start.no_account": {
        "en": "Arena account is not connected",
        "ru": "Аккаунт Arena не подключён",
        "zh": "Arena 账户未连接",
    },
    "start.no_account_hint": {
        "en": "Choose {item} first.",
        "ru": "Сначала выберите пункт {item}.",
        "zh": "请先选择 {item}。",
    },
    "start.count_title": {
        "en": "How many chats to run?",
        "ru": "Сколько чатов запустить?",
        "zh": "要运行多少个对话？",
    },
    "start.count_hint": {
        "en": "1 to {hi} · Enter to confirm, empty line to cancel",
        "ru": "от 1 до {hi} · Enter — подтвердить, пустая строка — отмена",
        "zh": "1 到 {hi} · Enter 确认，空行取消",
    },
    "start.count_invalid": {
        "en": "enter an integer from {lo} to {hi}",
        "ru": "нужно целое число от {lo} до {hi}",
        "zh": "请输入 {lo} 到 {hi} 之间的整数",
    },
    "start.count_invalid_open": {
        "en": "enter an integer of at least {lo}",
        "ru": "нужно целое число не меньше {lo}",
        "zh": "请输入不小于 {lo} 的整数",
    },
    "start.unlimited_note": {
        "en": "⚠ unlimited chats is on: the 100-chat cap is disabled",
        "ru": "⚠ включено неограниченное число чатов: лимит в 100 снят",
        "zh": "⚠ 已开启不限聊天数量：100 个的上限已取消",
    },
    "start.running": {"en": "Starting {count} chat(s)", "ru": "Запускаю {count} чат(ов)", "zh": "正在启动 {count} 个对话"},
    "start.running_line1": {
        "en": "Each chat: an Arena tab in Agent mode + an lm.ikale.io tab,",
        "ru": "Для каждого чата: вкладка Arena в режиме Agent + вкладка lm.ikale.io,",
        "zh": "每个对话：一个 Agent 模式的 Arena 标签页 + 一个 lm.ikale.io 标签页，",
    },
    "start.running_line2": {
        "en": "3 samples, Verify, then the chat is renamed.",
        "ru": "3 сэмпла, Verify, затем переименование чата.",
        "zh": "3 个样本，Verify，然后重命名对话。",
    },
    "start.running_mode": {
        "en": "Mode: {mode} (change it in Settings)",
        "ru": "Режим: {mode} (меняется в Настройках)",
        "zh": "模式：{mode}（可在设置中更改）",
    },
    "results.summary": {
        "en": "Done: {ok} of {total}",
        "ru": "Готово: {ok} из {total}",
        "zh": "完成：{ok} / {total}",
    },
    "results.chat": {"en": "chat {n}", "ru": "чат {n}", "zh": "对话 {n}"},
    "results.renamed": {
        "en": "Chats renamed on arena.ai.",
        "ru": "Чаты переименованы на arena.ai.",
        "zh": "对话已在 arena.ai 上重命名。",
    },
    "common.bye": {"en": "see you ✦", "ru": "до встречи ✦", "zh": "再见 ✦"},
    "common.continue": {"en": "Enter to continue", "ru": "Enter — продолжить", "zh": "Enter 继续"},
    # ------------------------------------------------------------ прогон
    "flow.tabs_arena": {
        "en": "Arena tab {i}/{n} opened",
        "ru": "Arena {i}/{n} открыта",
        "zh": "Arena 标签页 {i}/{n} 已打开",
    },
    "flow.tabs_ikale": {
        "en": "lm.ikale.io tab {i}/{n} opened",
        "ru": "lm.ikale.io {i}/{n} открыта",
        "zh": "lm.ikale.io 标签页 {i}/{n} 已打开",
    },
    "flow.mode": {
        "en": "{mode}: Arena tabs = {n}, lm.ikale.io tabs = {n}",
        "ru": "{mode}: вкладок Arena = {n}, вкладок lm.ikale.io = {n}",
        "zh": "{mode}：Arena 标签页 = {n}，lm.ikale.io 标签页 = {n}",
    },
    "flow.chat": {"en": "[chat {i}/{n}]", "ru": "[чат {i}/{n}]", "zh": "[对话 {i}/{n}]"},
    "flow.preparing": {
        "en": "preparing tabs: Arena (Agent) + lm.ikale.io",
        "ru": "готовлю вкладки: Arena (Agent) + lm.ikale.io",
        "zh": "准备标签页：Arena (Agent) + lm.ikale.io",
    },
    "flow.no_samples": {
        "en": "no samples found on lm.ikale.io",
        "ru": "на lm.ikale.io не найдены сэмплы",
        "zh": "在 lm.ikale.io 上未找到样本",
    },
    "flow.empty_prompt": {
        "en": "empty prompt in sample {n}",
        "ru": "пустой промпт в сэмпле {n}",
        "zh": "样本 {n} 的提示词为空",
    },
    "flow.sending": {
        "en": "sample {i}/{n}: sending to the agent",
        "ru": "сэмпл {i}/{n}: отправляю агенту",
        "zh": "样本 {i}/{n}：正在发送给智能体",
    },
    "flow.waiting": {
        "en": "sample {i}/{n}: waiting for the agent…",
        "ru": "сэмпл {i}/{n}: жду ответ агента…",
        "zh": "样本 {i}/{n}：等待智能体回复…",
    },
    "flow.inserted": {
        "en": "sample {i}/{n}: reply inserted ({chars} chars)",
        "ru": "сэмпл {i}/{n}: ответ вставлен ({chars} симв.)",
        "zh": "样本 {i}/{n}：回复已填入（{chars} 字符）",
    },
    "flow.verifying": {
        "en": "checking the fingerprint…",
        "ru": "проверяю отпечаток…",
        "zh": "正在检测指纹…",
    },
    "flow.low_confidence": {
        "en": "site warns about low confidence",
        "ru": "сайт предупреждает о низкой уверенности",
        "zh": "站点提示置信度较低",
    },
    "flow.renaming": {
        "en": "renaming the chat → «{name}»",
        "ru": "переименовываю чат → «{name}»",
        "zh": "正在重命名对话 →「{name}」",
    },
    "flow.done": {"en": "done", "ru": "готово", "zh": "完成"},
    "flow.error": {"en": "error", "ru": "ошибка", "zh": "错误"},
    "flow.err_no_context": {
        "en": "Arena account is not connected",
        "ru": "аккаунт Arena не подключён",
        "zh": "Arena 账户未连接",
    },
    "flow.err_not_ready": {
        "en": "Arena input did not appear",
        "ru": "поле ввода Arena не появилось",
        "zh": "Arena 输入框未出现",
    },
    "flow.err_no_reply": {
        "en": "the agent did not reply in time",
        "ru": "агент не ответил за отведённое время",
        "zh": "智能体未在规定时间内回复",
    },
    "flow.err_partial": {
        "en": "not all samples are filled: {label}",
        "ru": "заполнены не все сэмплы: {label}",
        "zh": "并非所有样本都已填写：{label}",
    },
    "flow.err_no_result": {
        "en": "could not read the verification result",
        "ru": "не удалось прочитать результат проверки",
        "zh": "无法读取检测结果",
    },
}

_current = DEFAULT_LANG


def set_language(code: str | None) -> str:
    """Устанавливает язык интерфейса. Неизвестный код → английский."""
    global _current
    _current = code if code in LANGS else DEFAULT_LANG
    return _current


def get_language() -> str:
    return _current


def t(key: str, **kwargs) -> str:
    """Строка по ключу на текущем языке (с фолбэком на английский)."""
    entry = _STRINGS.get(key)
    if not entry:
        return key
    text = entry.get(_current) or entry.get(DEFAULT_LANG) or key
    # многострочные тексты хранятся списком строк — склеиваем в один блок
    if isinstance(text, (list, tuple)):
        text = "\n".join(str(line) for line in text)
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, IndexError, ValueError):
            pass
    return text
