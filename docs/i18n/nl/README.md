<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | **🇳🇱 Nederlands** | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Modellenjager voor arena.ai: draait een reeks agent-chats, neemt van elk antwoord een vingerafdruk, achterhaalt welk model antwoordde en hernoemt de chat daarnaar — de volgende ochtend staat er een gelabelde chat met Claude Opus, GPT-5, Gemini of het model waar je naar zocht.**

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

## 🎯 Waarom dit bestaat

In agentmodus bepaalt arena.ai zelf welk model antwoordt — en dat is lang niet altijd het model dat je wilt: soms een topmodel (Claude Opus en verwanten), soms iets veel zwakkers. Deze tool maakt van die loterij een zoektocht: hij opent een reeks agent-chats, speelt in elke chat de drie vingerafdruksamples af, vraagt de vingerafdruksite welk model antwoordde en schrijft de uitslag in de titel van de chat (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Laat hem de nacht over draaien met zoveel chats als je wilt; 's ochtends ligt er een gelabelde lijst: open de chat waarvan de titel het model noemt dat je nodig hebt en werk daarin verder. Dat is het punt — geen automatisering om de automatisering, maar een chat die echt draait op het model dat je wilde.

## ✨ Wat het doet

- **Eén keer inloggen — sessie blijft.** Er opent een echte (geen headless) Chromium, je logt zoals gewoonlijk in bij arena.ai; de app merkt het, slaat de sessie op en sluit de browser zelf.
- **N chats tegelijk.** Je voert een getal van 1 tot 100 in — er openen precies zoveel `arena.ai/agent`-tabs en evenveel `lm.ikale.io`-tabs.
- **Kopieert voor je.** De prompt van elk sample gaat naar de agent, het antwoord wordt volledig afgewacht en in het Reply-veld geplakt — drie samples per chat.
- **Herkent het model.** Klikt Verify op de vingerafdruk-site, leest de beste kandidaat en de confidence precies zoals de site ze toont, en hernoemt de Arena-chat naar `model confidence` (bijvoorbeeld `gpt-6-luna 99.9%`).
- **Twee modi.** Single-threaded (veilig, chats na elkaar) en multi-threaded (alle chats parallel, 1,5–2× sneller).
- **Interface in drie talen.** English, Русский, 中文 — wisselbaar in de app, zonder herstart.

## 🔄 Hoe een run verloopt

1. **Inloggen** — de browser opent, je logt in, de app merkt het en sluit het venster.
2. **Start → aantal chats** — bijvoorbeeld `3`: drie Arena-tabs en drie vingerafdruk-tabs.
3. **Samples 1 → 3** — elke prompt gaat naar de agent, elk antwoord terug naar de site.
4. **Verify** — de site rangschikt de kandidaatmodellen, de app leest de winnaar en de confidence.
5. **Hernoemen** — de Arena-chat heet daarna `model confidence`, in de console verschijnt een samenvatting.

## 📋 Vereisten

- Python **3.10+**
- Windows 10/11, macOS of Linux
- Een arena.ai-account (e-mail en wachtwoord of link per mail)
- ~400 MB vrije schijfruimte voor Chromium van Playwright

## 🚀 Installatie

```bash
git clone <this-repo> arena-model-hunter
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** daarna volstaat een dubbelklik op `run.bat` (zet UTF-8 aan zodat cyrillisch correct wordt weergegeven).
**macOS / Linux:** `./run.sh` of `python main.py`.

## 🕹️ Gebruik

```bash
python main.py
```

| Optie | Omschrijving |
|---|---|
| **Start** | vraagt hoeveel chats er moeten draaien (1–100, of elk getal met onbeperkte chats) en start het hele proces |
| **Instellingen** | modus, taal van de interface, actief arena.ai-account verwijderen |
| **Afsluiten** | sluit de app (de terminal toont weer de vorige inhoud) |

Het menu past zich aan de status aan: zolang er geen account is verbonden verschijnt **Inloggen** en staat de cursor daarop; na een geslaagde login verdwijnt dat item.

## ⚙️ Instellingen

| Optie | Omschrijving |
|---|---|
| **Modus** | `single-threaded` (standaard) / `multi-threaded` — multi-threaded is sneller maar stuurt parallelle verzoeken |
| **Taal** | `English` / `Русский` / `中文` — werkt direct en wordt onthouden |
| **Onbeperkt aantal chats** ⚠️ | haalt de limiet van 100 chats weg: `Start` accepteert elk getal — gevaarlijk, standaard uit |
| **Actief arena.ai-account verwijderen** | wist browserprofiel en sessie, dus logt uit |

Instellingen staan in `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Onbeperkt aantal chats staat standaard uit en de waarschuwing is niet voor de sier.** Staat het aan, dan controleert `Start` niet meer op 1–100 maar accepteert elk getal — `250`, `1000`. Elke chat is twee tabbladen, dus grote getallen betekenen een vlaag parallelle verzoeken naar arena.ai: precies het patroon waarvoor rate limits en captcha's bestaan, met een reëel risico dat je account wordt beperkt. Zet het alleen aan als je dat accepteert, en blijf in single-threadmodus; boven de 100 vraagt de app eerst een tweede bevestiging met het exacte aantal.

## 🔐 How signing in works

1. A **real** Chromium window opens with a persistent profile (`~/.arena-model-hunter/profile`) — headless browsers are rejected by Cloudflare, so the app never uses one.
2. You click `Log In` → enter your email → `Continue with email`.
   - Existing account → enter the password → `Log In`.
   - New email → the name step can be skipped → a link arrives by mail → paste it into the address bar (`Ctrl+L`, `Ctrl+V`, Enter) → create a password.
3. The app polls the page every 1.5 s and detects success by: your email appearing in the sidebar, an `arena-auth-*` cookie, and the `Log In` button disappearing.
4. It saves `session.json` + `state.json` and **closes the browser**.

The site always opens in **dark theme** (the browser is launched with `prefers-color-scheme: dark`, which arena.ai follows).

## ⚡ Single-threaded en multi-threaded

| Modus | Hoe het werkt | Gemeten met 3 chats |
|---|---|---|
| **Single-threaded** (standaard) | tabbladenparen worden na elkaar verwerkt, het actieve tabblad komt naar voren | ≈7,5 min |
| **Multi-threaded** | alle tabbladenparen draaien tegelijk, de focus wordt niet verplaatst | ≈4,5 min |

Bij multi-threaded krijgt Arena meerdere verzoeken tegelijk, dus limieten en captcha's zijn waarschijnlijker. Gebeurt dat, schakel dan terug naar single-threaded.

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

## 🧰 Veelgestelde vragen

- **„Just a moment…” / Cloudflare-controle** — er is een zichtbaar browservenster nodig; niet op een server zonder desktop draaien.
- **„Browser is niet geïnstalleerd”** — voer `python -m playwright install chromium` uit.
- **Captcha of verzoeken worden stil genegeerd** — waarschijnlijk een limiet: zet single-threaded aan en vertraag.
- **Ik wil opnieuw beginnen** — Instellingen → *Actief arena.ai-account verwijderen* of verwijder `~/.arena-model-hunter`.
- **Een hele nacht jagen** — Instellingen → *Onbeperkt aantal chats*, typ `300` bij Start en bevestig; blijf in single-threadmodus en bekijk 's ochtends de hernoemde chats.

## ⚠️ Disclaimer

Dit project is bedoeld voor **persoonlijke experimenten en educatie**. Het automatiseert een site van derden; automatisering kan in strijd zijn met de voorwaarden van arena.ai en van de vingerafdruk-site en kan leiden tot beperkingen van je account. Gebruik op eigen risico, veroorzaak geen onnodige belasting, blijf bij twijfel bij single-threaded en publiceer nooit je gegevens — de app slaat het wachtwoord niet op schijf op.

## 📄 Licentie

[MIT](LICENSE) — doe wat je wilt, zonder garantie.

<div align="center">

**[⬆ Naar boven](#-arena-model-hunter) · 🇺🇸 [Read in English](../../../README.md)**

</div>
