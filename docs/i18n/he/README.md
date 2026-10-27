<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | **🇮🇱 עברית** | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**צייד מודלים ל־arena.ai: מריץ קבוצת שיחות במצב agent, לוקח טביעת אצבע מכל תשובה, מזהה איזה מודל ענה ומשנה את שם השיחה בהתאם — בבוקר מחכה לך שיחה מתויגת שמופעלת ב־Claude Opus, GPT-5, Gemini או במודל שחיפשת.**

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

## 🎯 בשביל מה זה קיים

במצב agent ‏arena.ai מחליט לבד איזה מודל יענה, וזה ממש לא תמיד המודל שאתה רוצה: לפעמים מודל מהשורה הראשונה (Claude Opus וחבריו), לפעמים משהו חלש בהרבה. הכלי הזה הופך את ההגרלה לחיפוש: הוא פותח קבוצת שיחות agent, מריץ בכל אחת מהן את שלוש דגימות טביעת האצבע, שואל את אתר טביעות האצבע איזה מודל ענה, וכותב את הפסיקה בשם השיחה (`claude-opus-4 99.9%`, `gpt-5.2 87%`). השאר אותו פועל בן־לילה עם כמה שיחות שתרצה; בבוקר יש רשימה מתויגת: פתח את השיחה ששמה מציין את המודל שאתה צריך והמשך לעבוד בה. זה כל העניין — לא אוטומציה לשם אוטומציה, אלא שיחה שבאמת רצה על המודל שרצית.

## ✨ מה היא עושה

- **התחברות אחת — הסשן נשמר.** נפתח Chromium אמיתי (לא headless), אתה מתחבר ל־arena.ai כרגיל; האפליקציה מזהה זאת, שומרת את הסשן וסוגרת את הדפדפן בעצמה.
- **N שיחות במקביל.** אתה מזין מספר בין 1 ל־100 — נפתחים בדיוק מספר כזה של לשוניות `arena.ai/agent` ואותו מספר של לשוניות `lm.ikale.io`.
- **מעתיק במקומך.** הפרומפט של כל דגימה נשלח לסוכן, התשובה ממתינה עד הסוף ומוטמעת בשדה Reply — שלוש דגימות לכל שיחה.
- **מזהה את המודל.** לוחץ Verify באתר טביעות האצבע, קורא את המועמד המוביל ואת רמת הביטחון בדיוק כפי שהאתר מציג אותם, ומשנה את שם השיחה ב־Arena ל־`מודל ביטחון` (למשל `gpt-6-luna 99.9%`).
- **שני מצבי הרצה.** חד־תהליכי (בטוח, שיחה אחר שיחה) ורב־תהליכי (כל השיחות במקביל, פי 1.5–2 מהר יותר).
- **ממשק בשלוש שפות.** English, Русский, 中文 — ניתן להחליף בתוך האפליקציה, בלי הפעלה מחדש.

## 🔄 איך נראית הרצה

1. **התחברות** — הדפדפן נפתח, אתה מאמת, האפליקציה מזהה וסוגרת את החלון.
2. **התחלה → מספר שיחות** — למשל `3`: שלוש לשוניות Arena ושלוש לשוניות טביעות אצבע.
3. **דגימות 1 → 3** — כל פרומפט נשלח לסוכן, כל תשובה חוזרת לאתר.
4. **Verify** — האתר מדרג את המודלים המועמדים, והאפליקציה קוראת את המנצח ואת הביטחון.
5. **שינוי שם** — השיחה ב־Arena נקראת `מודל ביטחון`, ובקונסול מופיע סיכום.

## 📋 דרישות

- Python **3.10+**
- Windows 10/11, macOS או Linux
- חשבון arena.ai (אימייל וסיסמה או קישור במייל)
- ~400 MB מקום פנוי ל־Chromium של Playwright

## 🚀 התקנה

```bash
git clone <this-repo> arena-model-hunter
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** לאחר מכן מספיק לחיצה כפולה על `run.bat` (מפעיל UTF-8 כדי שהקירילית תוצג נכון).
**macOS / Linux:** `./run.sh` או `python main.py`.

## 🕹️ שימוש

```bash
python main.py
```

| אפשרות | תיאור |
|---|---|
| **התחלה** | שואל כמה שיחות להריץ (1–100, או כל מספר עם שיחות ללא הגבלה) ומפעיל את כל התהליך |
| **הגדרות** | מצב הרצה, שפת הממשק, הסרת חשבון arena.ai הפעיל |
| **יציאה** | סוגר את האפליקציה (המסוף חוזר לתוכן הקודם שלו) |

התפריט מתאים את עצמו למצב: כל עוד אין חשבון מחובר מוצג **התחברות** והסמן עומד עליו; לאחר התחברות מוצלחת הפריט נעלם.

## ⚙️ הגדרות

| אפשרות | תיאור |
|---|---|
| **מצב הרצה** | `חד־תהליכי` (ברירת מחדל) / `רב־תהליכי` — הרב־תהליכי מהיר יותר אך שולח בקשות במקביל |
| **שפה** | `English` / `Русский` / `中文` — חלה מיד ונשמרת |
| **שיחות ללא הגבלה** ⚠️ | מסיר את תקרת 100 השיחות: `Start` מקבל כל מספר — מסוכן, כבוי כברירת מחדל |
| **הסרת חשבון arena.ai הפעיל** | מוחק את פרופיל הדפדפן ואת הסשן, כלומר מתנתק |

ההגדרות נשמרות ב־`~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **שיחות ללא הגבלה כבוי כברירת מחדל, והאזהרה כאן אינה קישוט.** כשהוא דלוק, `Start` מפסיק לבדוק את הטווח 1–100 ומקבל כל מספר — `250`, `1000`. כל שיחה היא שני לשוניות, ולכן מספרים גדולים פירושם מטח בקשות מקבילות ל־arena.ai: בדיוק מה שהגבלות קצב וקפצ׳ה נועדו לעצור, עם סיכון אמיתי להגבלה של החשבון. הפעל רק אם אתה מקבל זאת, והישאר במצב חד־תהליכי; כל מספר מעל 100 דורש אישור שני עם המספר המדויק לפני שמשהו נפתח.

## 🔐 How signing in works

1. A **real** Chromium window opens with a persistent profile (`~/.arena-model-hunter/profile`) — headless browsers are rejected by Cloudflare, so the app never uses one.
2. You click `Log In` → enter your email → `Continue with email`.
   - Existing account → enter the password → `Log In`.
   - New email → the name step can be skipped → a link arrives by mail → paste it into the address bar (`Ctrl+L`, `Ctrl+V`, Enter) → create a password.
3. The app polls the page every 1.5 s and detects success by: your email appearing in the sidebar, an `arena-auth-*` cookie, and the `Log In` button disappearing.
4. It saves `session.json` + `state.json` and **closes the browser**.

The site always opens in **dark theme** (the browser is launched with `prefers-color-scheme: dark`, which arena.ai follows).

## ⚡ מצב חד־תהליכי ורב־תהליכי

| מצב | איך זה עובד | נמדד על 3 שיחות |
|---|---|---|
| **חד־תהליכי** (ברירת מחדל) | זוגות הלשוניות מעובדים בזה אחר זה, הלשונית הפעילה מובאת לחזית | ≈7.5 דקות |
| **רב־תהליכי** | כל זוגות הלשוניות פועלים בו־זמנית, הפוקוס אינו מועבר | ≈4.5 דקות |

במצב רב־תהליכי Arena מקבל כמה בקשות בו־זמנית, ולכן מגבלות קצב וקפצ׳ה סבירות יותר. אם זה קורה — חזור למצב חד־תהליכי.

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

## 🧰 שאלות נפוצות

- **„Just a moment…” / אימות Cloudflare** — נדרש חלון דפדפן גלוי; אל תריץ על שרת בלי שולחן עבודה.
- **„הדפדפן לא מותקן”** — הרץ `python -m playwright install chromium`.
- **קפצ׳ה או בקשות שלא נשלחות** — כנראה הגעת למגבלה: עבור למצב חד־תהליכי והאט.
- **רוצה להתחיל מחדש** — הגדרות → *הסרת חשבון arena.ai הפעיל*, או מחק את `~/.arena-model-hunter`.
- **ציד כל הלילה** — הגדרות → *שיחות ללא הגבלה*, ואז הקלד `300` ב«התחלה» ואשר; הישאר במצב חד־תהליכי ובבוקר בדוק את השיחות ששמן שונה.

## ⚠️ כתב ויתור

הפרויקט נועד ל**ניסויים אישיים וללמידה**. הוא מבצע אוטומציה של אתר צד שלישי; אוטומציה עשויה להפר את תנאי השימוש של arena.ai ושל אתר טביעות האצבע ועלולה להוביל להגבלות בחשבון. השתמש באחריותך, אל תיצור עומס מיותר, במקרה של ספק הישאר במצב חד־תהליכי ולעולם אל תפרסם את פרטי הגישה שלך — האפליקציה אינה שומרת את הסיסמה בדיסק.

## 📄 רישיון

[MIT](LICENSE) — עשה כרצונך, ללא אחריות.

<div align="center">

**[⬆ למעלה](#-arena-model-hunter) · 🇺🇸 [Read in English](../../../README.md)**

</div>
