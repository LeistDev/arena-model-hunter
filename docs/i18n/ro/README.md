<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | **🇷🇴 Română** | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Vânător de modele pentru arena.ai: rulează un lot de chat-uri în modul agent, ia amprenta fiecărui răspuns, află ce model a răspuns și redenumește chat-ul după el — dimineața ai un chat etichetat care rulează Claude Opus, GPT-5, Gemini sau modelul pe care îl căutai.**

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

## 🎯 De ce există

În modul agent, arena.ai decide singur ce model răspunde — și nu e deloc mereu cel dorit: uneori un model de top (Claude Opus și semenii lui), alteori ceva mult mai slab. Unealta transformă loteria într-o căutare: deschide un lot de chat-uri în modul agent, rulează cele trei mostre de amprentă în fiecare, întreabă site-ul de amprente ce model a răspuns și scrie verdictul în titlul chat-ului (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Lasă-l peste noapte cu câte chat-uri vrei; dimineața ai o listă etichetată: deschide chat-ul al cărui titlu spune modelul de care ai nevoie și lucrează acolo. Asta e ideea — nu automatizare de dragul automatizării, ci un chat care rulează chiar pe modelul pe care îl voiai.

## ✨ Ce face

- **O singură autentificare — sesiunea rămâne.** Se deschide un Chromium real (nu headless), te autentifici pe arena.ai ca de obicei; aplicația observă autentificarea, salvează sesiunea și închide singură browserul.
- **N conversații simultan.** Introduci un număr de la 1 la 100 — se deschid exact atâtea file `arena.ai/agent` și tot atâtea file `lm.ikale.io`.
- **Copiază în locul tău.** Promptul fiecărui eșantion merge la agent, răspunsul este așteptat complet și lipit în câmpul Reply — trei eșantioane per conversație.
- **Identifică modelul.** Apasă Verify pe site-ul cu amprente, citește candidatul principal și încrederea exact cum le afișează site-ul, apoi redenumește conversația Arena în `model încredere` (de exemplu `gpt-6-luna 99.9%`).
- **Două moduri de rulare.** Un singur fir (sigur, conversații pe rând) și mai multe fire (toate conversațiile în paralel, de 1.5–2× mai rapid).
- **Interfață în trei limbi.** English, Русский, 中文 — se schimbă din aplicație, fără repornire.

## 🔄 Cum decurge o rulare

1. **Autentificare** — se deschide browserul, te autentifici, aplicația observă și închide fereastra.
2. **Start → numărul de conversații** — de exemplu `3`: trei file Arena și trei file cu amprente.
3. **Eșantioane 1 → 3** — fiecare prompt pleacă la agent, fiecare răspuns se întoarce pe site.
4. **Verify** — site-ul clasează modelele candidate, aplicația citește câștigătorul și încrederea.
5. **Redenumire** — conversația din Arena primește numele `model încredere`, iar în consolă apare un rezumat.

## 📋 Cerințe

- Python **3.10+**
- Windows 10/11, macOS sau Linux
- Cont arena.ai (e-mail și parolă sau link din e-mail)
- ~400 MB spațiu liber pentru Chromium din Playwright

## 🚀 Instalare

```bash
git clone <this-repo> arena-model-hunter
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** apoi este suficient un dublu clic pe `run.bat` (activează UTF-8, ca alfabetul chirilic să se afișeze corect).
**macOS / Linux:** `./run.sh` sau `python main.py`.

## 🕹️ Utilizare

```bash
python main.py
```

| Opțiune | Descriere |
|---|---|
| **Start** | întreabă câte chat-uri să ruleze (1–100 sau orice număr cu chat-uri nelimitate) și pornește întregul flux |
| **Setări** | modul de rulare, limba interfeței, ștergerea contului arena.ai activ |
| **Ieșire** | închide aplicația (terminalul revine la conținutul anterior) |

Meniul se adaptează stării: cât timp nu există cont conectat, apare **Autentificare** și cursorul stă pe el; după o autentificare reușită, elementul dispare.

## ⚙️ Setări

| Opțiune | Descriere |
|---|---|
| **Mod de rulare** | `un singur fir` (implicit) / `mai multe fire` — cel cu mai multe fire e mai rapid, dar trimite cereri paralele |
| **Limbă** | `English` / `Русский` / `中文` — se aplică imediat și este reținută |
| **Chat-uri nelimitate** ⚠️ | elimină limita de 100 de chat-uri: `Start` acceptă orice număr — periculos, oprit implicit |
| **Șterge contul arena.ai activ** | șterge profilul browserului și sesiunea, adică te deconectează |

Setările sunt salvate în `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Chat-urile nelimitate sunt oprite implicit, iar avertismentul nu e decor.** Când e pornit, `Start` nu mai verifică intervalul 1–100 și acceptă orice număr — `250`, `1000`. Fiecare chat înseamnă două file, deci numerele mari înseamnă un val de cereri paralele către arena.ai: exact tiparul pentru care există limitele de rată și captcha, cu risc real de restricționare a contului. Pornește-l doar dacă accepți asta și rămâi în modul cu un singur fir; peste 100 apare o a doua confirmare cu numărul exact înainte să se deschidă ceva.

## 🔐 How signing in works

1. A **real** Chromium window opens with a persistent profile (`~/.arena-model-hunter/profile`) — headless browsers are rejected by Cloudflare, so the app never uses one.
2. You click `Log In` → enter your email → `Continue with email`.
   - Existing account → enter the password → `Log In`.
   - New email → the name step can be skipped → a link arrives by mail → paste it into the address bar (`Ctrl+L`, `Ctrl+V`, Enter) → create a password.
3. The app polls the page every 1.5 s and detects success by: your email appearing in the sidebar, an `arena-auth-*` cookie, and the `Log In` button disappearing.
4. It saves `session.json` + `state.json` and **closes the browser**.

The site always opens in **dark theme** (the browser is launched with `prefers-color-scheme: dark`, which arena.ai follows).

## ⚡ Modul cu un fir și cu mai multe fire

| Mod | Cum funcționează | Măsurat pe 3 conversații |
|---|---|---|
| **Un singur fir** (implicit) | perechile de file sunt procesate pe rând, fila activă este adusă în față | ≈7,5 min |
| **Mai multe fire** | toate perechile de file rulează simultan, focusul nu este mutat | ≈4,5 min |

În modul cu mai multe fire, Arena primește mai multe cereri deodată, deci limitele și captcha sunt mai probabile. Dacă apar, revino la modul cu un singur fir.

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

## 🧰 Întrebări frecvente

- **„Just a moment…” / verificare Cloudflare** — este nevoie de o fereastră vizibilă; nu rula pe un server fără desktop.
- **„Browserul nu este instalat”** — rulează `python -m playwright install chromium`.
- **Captcha sau cereri ignorate în tăcere** — probabil ai atins o limită: activează modul cu un singur fir și încetinește.
- **Vreau să încep de la zero** — Setări → *Șterge contul arena.ai activ* sau șterge `~/.arena-model-hunter`.
- **Vânătoare toată noaptea** — Setări → *Chat-uri nelimitate*, apoi scrie `300` la Start și confirmă; rămâi pe un singur fir și dimineața uită-te la chat-urile redenumite.

## ⚠️ Avertisment

Proiectul este pentru **experimente personale și învățare**. Automatizează un site terț; automatizarea poate încălca termenii arena.ai și ai site-ului cu amprente și poate duce la restricții de cont. Folosește pe propriul risc, nu genera suprasolicitare, în caz de dubiu păstrează modul cu un singur fir și nu publica niciodată datele tale — aplicația nu salvează parola pe disc.

## 📄 Licență

[MIT](LICENSE) — fă ce vrei, fără garanții.

<div align="center">

**[⬆ Sus](#-arena-model-hunter) · 🇺🇸 [Read in English](../../../README.md)**

</div>
