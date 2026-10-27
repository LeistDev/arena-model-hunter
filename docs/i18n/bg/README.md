<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | **🇧🇬 Български** | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Ловец на модели за arena.ai: пуска пакет чатове в agent режим, снема отпечатък от всеки отговор, разбира кой модел е отговорил и преименува чата на негово име — на сутринта имате готов чат с Claude Opus, GPT-5, Gemini или модела, който търсехте.**

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

## 🎯 Защо съществува

В agent режим arena.ai сам решава кой модел отговаря и това далеч не винаги е желаният: понякога се пада топ модел (Claude Opus и подобните), понякога нещо значително по-слабо. Инструментът превръща тази лотария в търсене: отваря пакет чатове в agent режим, пуска по три проби за отпечатък във всеки, пита сайта за отпечатъци кой модел е отговорил и записва присъдата в името на чата (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Оставете го за през нощта с колкото чатове искате; на сутринта имате обозначен списък: отворете чата, в чието име стои нужният модел, и работете в него. Смисълът е точно в това — не автоматизация заради автоматизацията, а чат, който наистина работи на модела, който ви трябваше.

## ✨ Какво прави

- **Едно влизане — сесията остава.** Отваря се истински (не headless) Chromium, вие влизате в arena.ai както обикновено; програмата забелязва влизането, запазва сесията и сама затваря браузъра.
- **N чата наведнъж.** Въвеждате число от 1 до 100 — отварят се точно толкова раздела `arena.ai/agent` и същият брой раздели `lm.ikale.io`.
- **Копира вместо вас.** Промптът на всеки семпъл се изпраща на агента, отговорът се изчаква изцяло и се поставя в полето Reply — три семпъла на чат.
- **Разпознава модела.** Натиска Verify в сайта за отпечатъци, взема най-добрия кандидат и увереността точно както ги показва сайтът, и преименува чата в Arena на `модел увереност` (например `gpt-6-luna 99.9%`).
- **Два режима на работа.** Еднопоточен (безопасен, чатовете един по един) и многопоточен (всички чатове паралелно, 1.5–2× по-бързо).
- **Интерфейс на три езика.** English, Русский, 中文 — сменя се в самата програма, без рестарт.

## 🔄 Как протича един цикъл

1. **Влизане** — отваря се браузърът, вие се авторизирате, програмата го забелязва и затваря прозореца.
2. **Старт → брой чатове** — например `3`: три раздела Arena и три раздела за отпечатъци.
3. **Семпли 1 → 3** — всеки промпт отива при агента, всеки отговор се връща в сайта.
4. **Verify** — сайтът класира моделите-кандидати, програмата чете победителя и увереността.
5. **Преименуване** — чатът в Arena получава име `модел увереност`, а в конзолата се показва обобщение.

## 📋 Изисквания

- Python **3.10+**
- Windows 10/11, macOS или Linux
- Акаунт в arena.ai (имейл и парола или връзка от писмо)
- ~400 МБ свободно място за Chromium на Playwright

## 🚀 Инсталиране

```bash
git clone <this-repo> arena-model-hunter
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** след това е достатъчно двойно кликване върху `run.bat` (там се включва UTF-8, за да се показва кирилицата правилно).
**macOS / Linux:** `./run.sh` или `python main.py`.

## 🕹️ Използване

```bash
python main.py
```

| Опция | Описание |
|---|---|
| **Старт** | пита колко чата да пусне (1–100, а с неограничени — произволно число) и стартира цялата последователност |
| **Настройки** | режим на работа, език на интерфейса, премахване на активния акаунт arena.ai |
| **Изход** | затваря програмата (терминалът се връща към предишното съдържание) |

Менюто се съобразява със състоянието: докато няма свързан акаунт, се показва **Вход** и курсорът е върху него; след успешно влизане елементът изчезва.

## ⚙️ Настройки

| Опция | Описание |
|---|---|
| **Режим на работа** | `еднопоточен` (по подразбиране) / `многопоточен` — многопоточният е по-бърз, но изпраща паралелни заявки |
| **Език** | `English` / `Русский` / `中文` — прилага се веднага и се запомня |
| **Неограничен брой чатове** ⚠️ | премахва лимита от 100 чата: „Начало“ приема произволно число — опасно, изключено по подразбиране |
| **Премахни активния акаунт arena.ai** | изтрива профила на браузъра и сесията, тоест излиза от акаунта |

Настройките се пазят в `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **„Неограничен брой чатове“ е изключено по подразбиране и предупреждението не е за украса.** Когато е включено, „Начало“ приема произволно число вместо 1–100 — `250`, `1000`. Всеки чат е два таба, така че големите числа означават шквал от паралелни заявки към arena.ai: точно това, срещу което съществуват ограниченията на честотата и captcha, с реален риск от ограничаване на акаунта. Включвайте го само ако приемате това, и оставете еднопоточен режим; за всичко над 100 програмата иска второ потвърждение с точното число.

## 🔐 How signing in works

1. A **real** Chromium window opens with a persistent profile (`~/.arena-model-hunter/profile`) — headless browsers are rejected by Cloudflare, so the app never uses one.
2. You click `Log In` → enter your email → `Continue with email`.
   - Existing account → enter the password → `Log In`.
   - New email → the name step can be skipped → a link arrives by mail → paste it into the address bar (`Ctrl+L`, `Ctrl+V`, Enter) → create a password.
3. The app polls the page every 1.5 s and detects success by: your email appearing in the sidebar, an `arena-auth-*` cookie, and the `Log In` button disappearing.
4. It saves `session.json` + `state.json` and **closes the browser**.

The site always opens in **dark theme** (the browser is launched with `prefers-color-scheme: dark`, which arena.ai follows).

## ⚡ Еднопоточен и многопоточен режим

| Режим | Как работи | Измерено на 3 чата |
|---|---|---|
| **Еднопоточен** (по подразбиране) | двойките раздели се обработват един след друг, активният раздел се извежда отпред | ≈7.5 мин |
| **Многопоточен** | всички двойки раздели работят едновременно, фокусът не се мести | ≈4.5 мин |

В многопоточен режим Arena получава няколко заявки наведнъж, затова лимити и капча са по-вероятни. Ако това започне — върнете се към еднопоточния режим.

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

## 🧰 Възможни въпроси

- **„Just a moment…“ / проверка на Cloudflare** — нужен е видим браузър; не стартирайте на сървър без работен плот.
- **„Браузърът не е инсталиран“** — изпълнете `python -m playwright install chromium`.
- **Капча или заявките не се изпращат** — вероятно сте стигнали лимит: включете еднопоточен режим и намалете темпото.
- **Искам да започна наново** — Настройки → *Премахни активния акаунт arena.ai* или изтрийте `~/.arena-model-hunter`.
- **Лов през цялата нощ** — Настройки → *Неограничен брой чатове*, после в „Начало“ въведете `300` и потвърдете. Дръжте еднопоточен режим и на сутринта вижте преименуваните чатове.

## ⚠️ Отказ от отговорност

Проектът е за **лични експерименти и обучение**. Той автоматизира чужд сайт; автоматизацията може да нарушава условията за ползване на arena.ai и на сайта за отпечатъци и да доведе до ограничения на акаунта. Използвайте на собствен риск, не създавайте излишно натоварване, при съмнение дръжте еднопоточния режим и никога не публикувайте данните си — програмата не записва паролата на диск.

## 📄 Лиценз

[MIT](LICENSE) — правете каквото искате, без гаранции.

<div align="center">

**[⬆ Нагоре](#-arena-model-hunter) · 🇺🇸 [Read in English](../../../README.md)**

</div>
