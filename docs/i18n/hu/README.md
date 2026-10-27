<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | **🇭🇺 Magyar** | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Modellvadász az arena.ai-hez: agent-chatek egy kötegét futtatja, minden válaszról ujjlenyomatot vesz, kideríti, melyik modell válaszolt, és arról nevezi el a chatet — reggelre ott a felcímkézett chat Claude Opus-szal, GPT-5-tel, Geminiával vagy azzal a modellel, amelyre vadásztál.**

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

## 🎯 Miért van ez

Agent módban az arena.ai dönti el, melyik modell válaszol — és ez korántsem mindig a kívánt: néha csúcsmodell (Claude Opus és társai), néha jóval gyengébb. Ez az eszköz sorsjátékból kereséssé alakítja a dolgot: agent-chatek kötegét nyitja meg, mindegyikben lejátssza a három ujjlenyomat-mintát, megkérdezi az ujjlenyomat-oldalt, melyik modell válaszolt, és az ítéletet a chat címébe írja (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Hagyd éjszakára annyi chattel, amennyit akarsz; reggel egy felcímkézett lista vár: nyisd meg azt, amelynek címében a szükséges modell szerepel, és dolgozz abban. Pont ez a lényeg — nem automatizálás önmagáért, hanem egy chat, amely tényleg a kívánt modellen fut.

## ✨ Mit tud

- **Egyszeri bejelentkezés — a munkamenet megmarad.** Valódi (nem headless) Chromium nyílik meg, bejelentkezel az arena.ai oldalra a szokásos módon; az alkalmazás észleli, elmenti a munkamenetet és maga zárja be a böngészőt.
- **N beszélgetés egyszerre.** Megadsz egy 1 és 100 közötti számot — pontosan annyi `arena.ai/agent` lap és ugyanannyi `lm.ikale.io` lap nyílik meg.
- **Helyetted másol.** Minden minta promptja az agenthöz kerül, a választ teljesen megvárja, majd beilleszti a Reply mezőbe — három minta beszélgetésenként.
- **Felismeri a modellt.** Megnyomja a Verify gombot az ujjlenyomat-oldalon, kiolvassa a legjobb jelöltet és a bizonyosságot pontosan úgy, ahogy a weboldal mutatja, majd átnevezi az Arena-beszélgetést `modell bizonyosság` névre (például `gpt-6-luna 99.9%`).
- **Két futási mód.** Egyszálú (biztonságos, beszélgetések egymás után) és többszálú (az összes beszélgetés párhuzamosan, 1.5–2× gyorsabb).
- **Három nyelvű felület.** English, Русский, 中文 — az alkalmazásban váltható, újraindítás nélkül.

## 🔄 Hogyan zajlik egy futás

1. **Bejelentkezés** — megnyílik a böngésző, bejelentkezel, az alkalmazás észleli és bezárja az ablakot.
2. **Start → beszélgetések száma** — például `3`: három Arena lap és három ujjlenyomat-lap.
3. **1 → 3. minta** — minden prompt az agenthöz megy, minden válasz visszakerül az oldalra.
4. **Verify** — az oldal rangsorolja a jelölt modelleket, az alkalmazás kiolvassa a győztest és a bizonyosságot.
5. **Átnevezés** — az Arena-beszélgetés neve `modell bizonyosság` lesz, a konzolon összegzés jelenik meg.

## 📋 Követelmények

- Python **3.10+**
- Windows 10/11, macOS vagy Linux
- arena.ai fiók (e-mail és jelszó, vagy e-mailben kapott link)
- ~400 MB szabad hely a Playwright Chromiumhoz

## 🚀 Telepítés

```bash
git clone <this-repo> arena-model-hunter
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** utána elég duplán kattintani a `run.bat` fájlra (UTF-8-at kapcsol, hogy a cirill betűk helyesen jelenjenek meg).
**macOS / Linux:** `./run.sh` vagy `python main.py`.

## 🕹️ Használat

```bash
python main.py
```

| Beállítás | Leírás |
|---|---|
| **Start** | megkérdezi, hány chat fusson (1–100, korlátlan chateknél bármilyen szám), és elindítja az egész folyamatot |
| **Beállítások** | futási mód, felület nyelve, az aktív arena.ai fiók törlése |
| **Kilépés** | bezárja az alkalmazást (a terminál visszakapja korábbi tartalmát) |

A menü az állapothoz igazodik: amíg nincs csatlakoztatott fiók, a **Bejelentkezés** pont látható, és a kurzor rajta áll; sikeres bejelentkezés után a pont eltűnik.

## ⚙️ Beállítások

| Beállítás | Leírás |
|---|---|
| **Futási mód** | `egyszálú` (alapértelmezett) / `többszálú` — a többszálú gyorsabb, de párhuzamos kéréseket küld |
| **Nyelv** | `English` / `Русский` / `中文` — azonnal érvénybe lép és megjegyződik |
| **Korlátlan számú chat** ⚠️ | eltörli a 100 chat-es plafont: a `Start` bármilyen számot elfogad — veszélyes, alapból kikapcsolva |
| **Aktív arena.ai fiók törlése** | törli a böngészőprofilt és a munkamenetet, azaz kijelentkeztet |

A beállítások itt tárolódnak: `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **A korlátlan számú chat alapból ki van kapcsolva, és a figyelmeztetés nem díszítés.** Bekapcsolva a `Start` már nem 1–100 között ellenőriz, hanem bármilyen számot elfogad — `250`, `1000`. Minden chat két lap, tehát a nagy számok párhuzamos kérések özönét jelentik az arena.ai felé: pontosan ezért léteznek a sebességkorlátok és a captchák, és valós a fiók korlátozásának kockázata. Csak akkor kapcsold be, ha ezt vállalod, és maradj egyszálas módban; 100 felett második megerősítést is kér a pontos számmal, mielőtt bármi megnyílna.

## 🔐 How signing in works

1. A **real** Chromium window opens with a persistent profile (`~/.arena-model-hunter/profile`) — headless browsers are rejected by Cloudflare, so the app never uses one.
2. You click `Log In` → enter your email → `Continue with email`.
   - Existing account → enter the password → `Log In`.
   - New email → the name step can be skipped → a link arrives by mail → paste it into the address bar (`Ctrl+L`, `Ctrl+V`, Enter) → create a password.
3. The app polls the page every 1.5 s and detects success by: your email appearing in the sidebar, an `arena-auth-*` cookie, and the `Log In` button disappearing.
4. It saves `session.json` + `state.json` and **closes the browser**.

The site always opens in **dark theme** (the browser is launched with `prefers-color-scheme: dark`, which arena.ai follows).

## ⚡ Egyszálú és többszálú mód

| Mód | Hogyan működik | Mérés 3 beszélgetésen |
|---|---|---|
| **Egyszálú** (alapértelmezett) | a lappárok egymás után dolgozódnak fel, az aktív lap előre kerül | ≈7,5 perc |
| **Többszálú** | az összes lappár egyszerre fut, a fókusz nem váltogat | ≈4,5 perc |

Többszálú módban az Arena egyszerre több kérést kap, ezért a limitek és a captcha valószínűbbek. Ha ez elkezdődik, válts vissza egyszálú módra.

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

## 🧰 Gyakori kérdések

- **„Just a moment…” / Cloudflare-ellenőrzés** — látható böngészőablak kell; ne futtasd asztali környezet nélküli szerveren.
- **„A böngésző nincs telepítve”** — futtasd: `python -m playwright install chromium`.
- **Captcha vagy csendben el nem küldött kérések** — valószínűleg elérted a limitet: kapcsolj egyszálú módra és lassíts.
- **Tiszta lappal kezdenék** — Beállítások → *Aktív arena.ai fiók törlése*, vagy töröld a `~/.arena-model-hunter` mappát.
- **Vadászat egész éjjel** — Beállítások → *Korlátlan számú chat*, majd írd be a `300`-at a Kezdésnél és erősítsd meg; maradj egyszálas módban, és reggel nézd meg az átnevezett chateket.

## ⚠️ Jogi nyilatkozat

A projekt **személyes kísérletezésre és tanulásra** készült. Harmadik fél weboldalát automatizálja; az automatizálás sértheti az arena.ai és az ujjlenyomat-oldal felhasználási feltételeit, és fiókkorlátozáshoz vezethet. Saját felelősségedre használd, ne generálj felesleges terhelést, kétség esetén maradj az egyszálú módnál, és soha ne tedd közzé az adataidat — az alkalmazás nem menti a jelszót lemezre.

## 📄 Licenc

[MIT](LICENSE) — azt csinálsz, amit akarsz, garancia nélkül.

<div align="center">

**[⬆ Fel](#-arena-model-hunter) · 🇺🇸 [Read in English](../../../README.md)**

</div>
