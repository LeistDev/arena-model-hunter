<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | **🇺🇦 Українська** | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Мисливець за моделями для arena.ai: ганяє пачку чатів у agent-режимі, знімає відбиток з кожної відповіді, з'ясовує, яка модель відповіла, і перейменовує чат на її честь — уранці у вас готовий чат із Claude Opus, GPT-5, Gemini або тією нейромережею, яку ви шукали.**

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

## 🎯 Для чого це потрібно

У agent-режимі arena.ai сам вирішує, яка модель відповідає, — і це далеко не завжди та, що вам потрібна: іноді трапляється топова модель (Claude Opus та її сусіди), іноді щось помітно слабше. Скрипт перетворює цю лотерею на пошук: відкриває пачку чатів у agent-режимі, проганяє в кожному по три зразки відбитків, питає в сайту відбитків, яка модель відповіла, і пише вердикт у назву чату — `claude-opus-4 99.9%`, `gpt-5.2 87%`. Залиште його на ніч із будь-якою кількістю чатів; уранці є розмічений список: відкривайте чат, у назві якого потрібна модель, і працюйте в ньому. Сенс саме в цьому — не автоматизація заради автоматизації, а чат, який справді працює на тій моделі, що вам була потрібна.

## ✨ Що вміє

- **Вхід один раз — сесія зберігається.** Відкривається справжній (не headless) Chromium, ви входите в arena.ai як звичайно; програма помічає вхід, зберігає сесію і сама закриває браузер.
- **N чатів одночасно.** Ви вводите число від 1 до 100 — відкривається рівно стільки вкладок `arena.ai/agent` і стільки ж вкладок `lm.ikale.io`.
- **Копіювання замість вас.** Промпт кожного семплу надсилається агенту, відповідь очікується повністю і вставляється в поле Reply — три семпли на чат.
- **Визначає модель.** Натискає Verify на сайті відбитків, бере найкращого кандидата та впевненість так, як їх показує сайт, і перейменовує чат Arena у `модель впевненість` (наприклад `gpt-6-luna 99.9%`).
- **Два режими роботи.** Однопотоковий (безпечний, чати по черзі) і багатопотоковий (усі чати паралельно, у 1.5–2 раза швидше).
- **Інтерфейс трьома мовами.** English, Русский, 中文 — перемикається в самій програмі, без перезапуску.

## 🔄 Як відбувається прогін

1. **Вхід** — відкривається браузер, ви авторизуєтесь, програма це помічає і закриває вікно.
2. **Почати → кількість чатів** — наприклад `3`: три вкладки Arena і три вкладки відбитків.
3. **Семпли 1 → 3** — кожен промпт іде агенту, кожна відповідь повертається на сайт.
4. **Verify** — сайт ранжує моделі-кандидати, програма читає переможця та впевненість.
5. **Перейменування** — чат Arena отримує ім'я `модель впевненість`, у консолі з'являється підсумок.

## 📋 Вимоги

- Python **3.10+**
- Windows 10/11, macOS або Linux
- Акаунт arena.ai (пошта й пароль або посилання з листа)
- ~400 МБ вільного місця під Chromium для Playwright

## 🚀 Встановлення

```bash
git clone <this-repo> arena-model-hunter
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** далі достатньо подвійного кліку по `run.bat` (там же вмикається UTF-8, щоб кирилиця відображалася коректно).
**macOS / Linux:** `./run.sh` або `python main.py`.

## 🕹️ Використання

```bash
python main.py
```

| Параметр | Опис |
|---|---|
| **Почати** | питає кількість чатів (1–100, а з необмеженим — будь-яку) і запускає весь конвеєр |
| **Налаштування** | режим роботи, мова інтерфейсу, видалення активного акаунта arena.ai |
| **Вихід** | закрити програму (термінал повернеться до попереднього вмісту) |

Меню підлаштовується під стан: поки акаунт не підключено, показується пункт **Увійти**, і курсор стоїть на ньому; після успішного входу пункт зникає.

## ⚙️ Налаштування

| Параметр | Опис |
|---|---|
| **Режим роботи** | `однопотоковий` (за замовчуванням) / `багатопотоковий` — багатопотоковий швидший, але надсилає паралельні запити |
| **Мова** | `English` / `Русский` / `中文` — застосовується одразу й запам'ятовується |
| **Необмежена кількість чатів** ⚠️ | знімає ліміт у 100 чатів: «Почати» приймає будь-яке число — небезпечно, типово вимкнено |
| **Видалити активний акаунт arena.ai** | стирає профіль браузера й сесію, тобто виконує вихід |

Налаштування зберігаються у `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **«Необмежена кількість чатів» типово вимкнена, і попередження тут не для краси.** Коли функція ввімкнена, «Почати» приймає будь-яке число замість 1–100 — `250`, `1000`. Кожен чат — це дві вкладки, тож великі числа означають шквал паралельних запитів до arena.ai: саме для цього існують обмеження частоти та капчі, з реальним ризиком обмеження акаунта. Вмикайте, лише якщо готові до цього, і тримайте однопотоковий режим; для всього, що більше 100, скрипт окремо питає підтвердження з точною кількістю.

## 🔐 How signing in works

1. A **real** Chromium window opens with a persistent profile (`~/.arena-model-hunter/profile`) — headless browsers are rejected by Cloudflare, so the app never uses one.
2. You click `Log In` → enter your email → `Continue with email`.
   - Existing account → enter the password → `Log In`.
   - New email → the name step can be skipped → a link arrives by mail → paste it into the address bar (`Ctrl+L`, `Ctrl+V`, Enter) → create a password.
3. The app polls the page every 1.5 s and detects success by: your email appearing in the sidebar, an `arena-auth-*` cookie, and the `Log In` button disappearing.
4. It saves `session.json` + `state.json` and **closes the browser**.

The site always opens in **dark theme** (the browser is launched with `prefers-color-scheme: dark`, which arena.ai follows).

## ⚡ Однопотоковий і багатопотоковий режими

| Режим | Як працює | Замір на 3 чатах |
|---|---|---|
| **Однопотоковий** (за замовчуванням) | пари вкладок обробляються по черзі, активна вкладка виводиться вперед | ≈7.5 хв |
| **Багатопотоковий** | усі пари вкладок працюють одночасно, фокус не перемикається | ≈4.5 хв |

У багатопотоковому режимі Arena отримує кілька запитів одразу, тому ліміти й капча ймовірніші. Якщо це почалося — поверніться до однопотокового режиму.

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

## 🧰 Можливі питання

- **«Just a moment…» / перевірка Cloudflare** — потрібен видимий браузер; не запускайте на сервері без робочого столу.
- **«Браузер не встановлено»** — виконайте `python -m playwright install chromium`.
- **Капча або запити мовчки не надсилаються** — ймовірно ви вперлися в ліміт: увімкніть однопотоковий режим і знизьте темп.
- **Хочу почати з чистого аркуша** — Налаштування → *Видалити активний акаунт arena.ai* або видаліть `~/.arena-model-hunter`.
- **Полювання на всю ніч** — Налаштування → *Необмежена кількість чатів*, далі в «Почати» введіть `300` і підтвердьте. Тримайте однопотоковий режим, а вранці дивіться перейменовані чати.

## ⚠️ Дисклеймер

Проєкт створено для **особистих експериментів і навчання**. Він автоматизує сторонній сайт; автоматизація може порушувати умови використання arena.ai і сайту відбитків та призвести до обмежень акаунта. Використовуйте на свій ризик, не створюйте зайве навантаження, за сумнівів тримайте однопотоковий режим і ніколи не публікуйте свої дані — програма не зберігає пароль на диск.

## 📄 Ліцензія

[MIT](LICENSE) — робіть що хочете, без гарантій.

<div align="center">

**[⬆ Догори](#-arena-model-hunter) · 🇺🇸 [Read in English](../../../README.md)**

</div>
