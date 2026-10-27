<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | **🇷🇺 Русский** | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Охотник за моделями для arena.ai: гоняет пачку чатов в agent-режиме, снимает отпечаток с каждого ответа, выясняет, какая модель ответила, и переименовывает чат в её честь — утром у вас готовый чат с Claude Opus, GPT-5, Gemini или той нейросетью, которую вы искали.**

![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![UI](https://img.shields.io/badge/UI-terminal-6E56CF)
![License](https://img.shields.io/badge/license-MIT-green)

</div>

---

```
   ╭──────────────────────────────────────────────────────────────────╮
   │                                                                  │
   │  ✦  arena model hunter                                           │
   │     arena.ai automation · v1.0.0                                 │
   │                                                                  │
   │  ● Arena account connected  ·  you@example.com                   │
   │  ◷ mode: single-threaded  ·  English                             │
   │                                                                  │
   │  ▸ Start                                                ready    │
   │    Settings                                   account & exit    │
   │    Exit                                                          │
   │                                                                  │
   │ ↑ ↓  select    ↵  open    q  quit                                │
   │                                                                  │
   ╰──────────────────────────────────────────────────────────────────╯
```

## 🎯 Зачем это нужно

В agent-режиме arena.ai сам решает, какая модель отвечает, — и это далеко не всегда та, что вам нужна: иногда попадается топовая модель (Claude Opus и её соседи), иногда что-то заметно слабее. Скрипт превращает эту лотерею в поиск: открывает пачку чатов в agent-режиме, прогоняет в каждом по три сэмпла отпечатков, спрашивает у сайта отпечатков, какая модель ответила, и пишет вердикт в название чата — `claude-opus-4 99.9%`, `gpt-5.2 87%`. Оставьте его на ночь с любым количеством чатов; утром есть размеченный список: открывайте чат, в названии которого нужная модель, и работайте в нём. Смысл именно в этом — не автоматизация ради автоматизации, а чат, который действительно работает на той модели, которая вам была нужна.

## ✨ Что умеет

- **Вход один раз — сессия остаётся.** Открывается настоящий (не headless) Chromium, вы входите в arena.ai как обычно; программа замечает вход, сохраняет сессию и сама закрывает браузер.
- **N чатов одновременно.** Вы вводите число от 1 до 100 — открывается ровно столько вкладок `arena.ai/agent` и столько же вкладок `lm.ikale.io`.
- **Копирование вместо вас.** Промпт каждого сэмпла отправляется агенту, ответ дожидается целиком и вставляется в поле Reply — три сэмпла на чат.
- **Определяет модель.** Нажимает Verify на сайте отпечатков, забирает лучшего кандидата и уверенность в том виде, как их показывает сайт, и переименовывает чат Arena в `модель уверенность` (например `gpt-6-luna 99.9%`).
- **Два режима работы.** Однопоточный (безопасный, чаты по очереди) и многопоточный (все чаты параллельно, быстрее в 1.5–2 раза).
- **Интерфейс на трёх языках.** English, Русский, 中文 — переключается в самой программе, без перезапуска.

## 🔄 Как проходит прогон

1. **Вход** — открывается браузер, вы авторизуетесь, программа это замечает и закрывает окно.
2. **Начать → количество чатов** — например `3`: три вкладки Arena и три вкладки отпечатков.
3. **Сэмплы 1 → 3** — каждый промпт уходит агенту, каждый ответ возвращается на сайт.
4. **Verify** — сайт ранжирует модели-кандидаты, программа читает победителя и уверенность.
5. **Переименование** — чат Arena получает имя `модель уверенность`, в консоли появляется итог.

## 📋 Требования

- Python **3.10+**
- Windows 10/11, macOS или Linux
- Аккаунт arena.ai (почта и пароль либо ссылка из письма)
- ~400 МБ свободного места под Chromium для Playwright

## 🚀 Установка

```bash
git clone <this-repo> arena-model-hunter
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** дальше достаточно двойного клика по `run.bat` (там же включается UTF-8, чтобы кириллица отображалась корректно).
**macOS / Linux:** `./run.sh` или `python main.py`.

## 🕹️ Использование

```bash
python main.py
```

| Параметр | Описание |
|---|---|
| **Начать** | спрашивает число чатов (1–100, а с безлимитом — любое) и запускает весь конвейер |
| **Настройки** | режим работы, язык интерфейса, удаление активного аккаунта arena.ai |
| **Выход** | закрыть программу (терминал вернётся к прежнему содержимому) |

Меню подстраивается под состояние: пока аккаунт не подключён, показывается пункт **Войти**, и курсор стоит на нём; после успешного входа пункт исчезает.

## ⚙️ Настройки

| Параметр | Описание |
|---|---|
| **Режим работы** | `однопоточный` (по умолчанию) / `многопоточный` — многопоточный быстрее, но шлёт параллельные запросы |
| **Язык** | `English` / `Русский` / `中文` — применяется сразу и запоминается |
| **Неограниченное число чатов** ⚠️ | снимает лимит в 100 чатов: «Начать» принимает любое число — опасно, по умолчанию выключено |
| **Удалить активный аккаунт arena.ai** | стирает профиль браузера и сессию, то есть выполняет выход |

Настройки хранятся в `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **«Неограниченное число чатов» по умолчанию выключено, и предупреждение здесь не для красоты.** Когда функция включена, «Начать» принимает любое число вместо 1–100 — `250`, `1000`. Каждый чат — это две вкладки, поэтому большие числа означают шквал параллельных запросов к arena.ai: ровно то, ради чего существуют ограничения по частоте и капчи, с реальным риском ограничения аккаунта. Включайте, только если готовы к этому, и оставляйте однопоточный режим; для всего, что больше 100, скрипт отдельно спрашивает подтверждение с точным количеством.

## 🔐 How signing in works

1. A **real** Chromium window opens with a persistent profile (`~/.arena-model-hunter/profile`) — headless browsers are rejected by Cloudflare, so the app never uses one.
2. You click `Log In` → enter your email → `Continue with email`.
   - Existing account → enter the password → `Log In`.
   - New email → the name step can be skipped → a link arrives by mail → paste it into the address bar (`Ctrl+L`, `Ctrl+V`, Enter) → create a password.
3. The app polls the page every 1.5 s and detects success by: your email appearing in the sidebar, an `arena-auth-*` cookie, and the `Log In` button disappearing.
4. It saves `session.json` + `state.json` and **closes the browser**.

The site always opens in **dark theme** (the browser is launched with `prefers-color-scheme: dark`, which arena.ai follows).

## ⚡ Однопоточный и многопоточный режимы

| Режим | Как работает | Замер на 3 чатах |
|---|---|---|
| **Однопоточный** (по умолчанию) | пары вкладок обрабатываются по очереди, активная вкладка выводится вперёд | ≈7.5 мин |
| **Многопоточный** | все пары вкладок работают одновременно, фокус не переключается | ≈4.5 мин |

В многопоточном режиме Arena получает несколько запросов сразу, поэтому лимиты и капча вероятнее. Если это началось — вернитесь в однопоточный режим.

## 🗂️ Project structure

```
arena-model-hunter/
├── main.py           # menu, settings, scenarios
├── ui.py             # terminal UI: frame, alt-screen, key reading, resize
├── arena_login.py    # browser, sign-in, session detection
├── flow.py           # Arena ↔ lm.ikale.io pipeline, Verify, rename
├── i18n.py           # UI translations (en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI: lint + translation checks
├── LICENSE
└── docs/i18n/        # this README in 30 languages
```

## 🌍 Environment variables

| Variable | Default | Purpose |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | profile and session folder |
| `ARENA_HELPER_HOME` | — | old name of the variable, still honoured |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | optional form autofill (never stored) |
| `ARENA_LOGIN_TIMEOUT` | `900` | seconds to wait for sign-in |
| `ARENA_URL` | `https://arena.ai/` | start URL |

## 🧰 Возможные вопросы

- **«Just a moment…» / проверка Cloudflare** — нужен видимый браузер; не запускайте на сервере без рабочего стола.
- **«Браузер не установлен»** — выполните `python -m playwright install chromium`.
- **Капча или запросы молча не отправляются** — скорее всего вы упёрлись в лимит: включите однопоточный режим и снизьте темп.
- **Хочу начать с чистого листа** — Настройки → *Удалить активный аккаунт arena.ai* либо удалите `~/.arena-model-hunter`.
- **Охота на всю ночь** — Настройки → *Неограниченное число чатов*, затем в «Начать» введите `300` и подтвердите. Держите однопоточный режим, а утром смотрите переименованные чаты.

## ⚠️ Дисклеймер

Проект создан для **личных экспериментов и обучения**. Он автоматизирует сторонний сайт; автоматизация может нарушать условия использования arena.ai и сайта отпечатков и привести к ограничениям аккаунта. Используйте на свой риск, не создавайте лишнюю нагрузку, при сомнениях держите однопоточный режим и никогда не публикуйте свои данные — программа не сохраняет пароль на диск.

## 📄 Лицензия

[MIT](LICENSE) — делайте что хотите, без гарантий.

<div align="center">

**[⬆ Наверх](#-arena-model-hunter) · 🇺🇸 [Read in English](../../../README.md)**

</div>
