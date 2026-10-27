<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | **🇳🇴 Norsk** | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Modelljeger for arena.ai: kjører en haug agent-chatter, tar fingeravtrykk av hvert svar, finner ut hvilken modell som svarte og gir chatten nytt navn etter den — om morgenen har du en merket chat som kjører Claude Opus, GPT-5, Gemini eller modellen du var på jakt etter.**

![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![UI](https://img.shields.io/badge/UI-terminal-6E56CF)
![License](https://img.shields.io/badge/license-MIT-green)

</div>

---

```
   +------------------------------------------------------------------+
   |                                                                  |
   |  *  arena model hunter                                           |
   |     arena.ai automation - v1.0.0                                 |
   |                                                                  |
   |  o Arena account connected  .  you@example.com                   |
   |  ~ mode: single-threaded  .  English                             |
   |                                                                  |
   |  > Start                                                ready    |
   |    Settings                                   account & exit     |
   |    Exit                                                          |
   |                                                                  |
   | arrows select    Enter open    q quit                            |
   |                                                                  |
   +------------------------------------------------------------------+
```

## 🎯 Hvorfor dette finnes

I agent-modus bestemmer arena.ai selv hvilken modell som svarer — og det er slett ikke alltid den du vil ha: noen ganger en toppmodell (Claude Opus og slekten), andre ganger noe langt svakere. Dette verktøyet gjør lotteriet om til en leting: det åpner en haug agent-chatter, spiller de tre fingeravtrykksprøvene i hver eneste, spør fingeravtrykkssiden hvilken modell som svarte, og skriver dommen i chattens tittel (`claude-opus-4 99.9%`, `gpt-5.2 87%`). La den gå over natten med så mange chatter du vil; om morgenen ligger en merket liste klar: åpne chatten der tittelen nevner modellen du trenger, og arbeid videre i den. Det er poenget — ikke automatisering for automatiseringens skyld, men en chat som faktisk kjører på modellen du ville ha.

## ✨ Hva den gjør

- **Én innlogging — sesjonen beholdes.** Det åpnes en ekte (ikke headless) Chromium, du logger inn på arena.ai som vanlig; appen oppdager det, lagrer sesjonen og lukker nettleseren selv.
- **N chatter samtidig.** Du skriver inn et tall fra 1 til 100 — det åpnes nøyaktig så mange `arena.ai/agent`-faner og like mange `lm.ikale.io`-faner.
- **Kopierer for deg.** Prompten til hvert sample sendes til agenten, svaret ventes på i sin helhet og limes inn i Reply-feltet — tre samples per chat.
- **Gjenkjenner modellen.** Klikker Verify på fingeravtrykksiden, leser den beste kandidaten og sikkerheten nøyaktig slik siden viser dem, og gir Arena-chatten navnet `modell sikkerhet` (for eksempel `gpt-6-luna 99.9%`).
- **To kjøremoduser.** Enkelttrådet (trygg, chatter etter hverandre) og flertrådet (alle chatter parallelt, 1,5–2× raskere).
- **Grensesnitt på tre språk.** English, Русский, 中文 — byttes i appen, uten omstart.

## 🔄 Slik foregår en kjøring

1. **Logg inn** — nettleseren åpnes, du logger inn, appen oppdager det og lukker vinduet.
2. **Start → antall chatter** — for eksempel `3`: tre Arena-faner og tre fingeravtrykksfaner.
3. **Samples 1 → 3** — hver prompt går til agenten, hvert svar tilbake til siden.
4. **Verify** — siden rangerer kandidatmodellene, appen leser vinneren og sikkerheten.
5. **Nytt navn** — Arena-chatten heter deretter `modell sikkerhet`, og et sammendrag vises i konsollen.

## 📋 Krav

- Python **3.10+**
- Windows 10/11, macOS eller Linux
- En arena.ai-konto (e-post og passord eller lenke på e-post)
- ~400 MB ledig diskplass til Chromium fra Playwright

## 🚀 Installasjon

```bash
git clone https://github.com/LeistDev/arena-model-hunter.git
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** etterpå holder det med dobbeltklikk på `run.bat` (slår på UTF-8 slik at kyrillisk vises riktig).
**macOS / Linux:** `./run.sh` eller `python main.py`.

## 🕹️ Bruk

```bash
python main.py
```

| Valg | Beskrivelse |
|---|---|
| **Start** | spør hvor mange chatter som skal kjøre (1–100, eller et vilkårlig tall med ubegrensede chatter) og starter hele løpet |
| **Innstillinger** | kjøremodus, språk i grensesnittet, fjern den aktive arena.ai-kontoen |
| **Avslutt** | lukker appen (terminalen viser igjen sitt tidligere innhold) |

Menyen tilpasser seg tilstanden: så lenge ingen konto er tilkoblet vises **Logg inn**, og markøren står på den; etter vellykket innlogging forsvinner punktet.

## ⚙️ Innstillinger

| Valg | Beskrivelse |
|---|---|
| **Kjøremodus** | `enkelttrådet` (standard) / `flertrådet` — flertrådet er raskere, men sender parallelle forespørsler |
| **Språk** | `English` / `Русский` / `中文` — virker umiddelbart og huskes |
| **Ubegrenset antall chatter** ⚠️ | fjerner taket på 100 chatter: `Start` tar et vilkårlig tall — farlig, av som standard |
| **Fjern aktiv arena.ai-konto** | sletter nettleserprofil og sesjon, altså logger ut |

Innstillingene ligger i `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Ubegrenset antall chatter er av som standard, og advarselen er ikke pynt.** Med det på sjekker ikke `Start` lenger 1–100, men tar et vilkårlig tall — `250`, `1000`. Hver chat er to faner, så store tall betyr en byge av parallelle forespørsler til arena.ai: akkurat det rate limits og captcha finnes for, med reell risiko for at kontoen blir begrenset. Slå det bare på hvis du aksepterer det, og bli i enkelttrådsmodus; alt over 100 krever en ekstra bekreftelse med det nøyaktige tallet før noe åpnes.

## 🔐 Slik fungerer innlogging

1. Det åpnes et **ekte** Chromium-vindu med varig profil (`~/.arena-model-hunter/profile`) — Cloudflare avviser headless nettlesere, så appen bruker aldri en.
2. Du klikker `Log In` → skriver inn e-posten → `Continue with email`.
   - Konto finnes → skriv inn passordet → `Log In`.
   - Ny e-post → navnetrinnet kan hoppes over → en lenke kommer på e-post → lim den inn i adressefeltet (`Ctrl+L`, `Ctrl+V`, Enter) → lag et passord.
3. Appen sjekker siden hvert 1,5 sekund og ser at innloggingen lykkes på tre tegn: e-posten din dukker opp i sidepanelet, en `arena-auth-*`-cookie oppstår, og knappen `Log In` forsvinner.
4. Deretter lagrer den `session.json` + `state.json` og **lukker nettleseren**.

Nettstedet åpnes alltid i **mørkt tema** (nettleseren startes med `prefers-color-scheme: dark`, og arena.ai følger det).

## ⚡ Enkelttrådet og flertrådet modus

| Modus | Slik virker det | Målt med 3 chatter |
|---|---|---|
| **Enkelttrådet** (standard) | fanepar behandles etter hverandre, den aktive fanen hentes frem | ≈7,5 min |
| **Flertrådet** | alle fanepar kjører samtidig, fokus flyttes ikke | ≈4,5 min |

I flertrådet modus får Arena flere forespørsler samtidig, så grenser og captcha er mer sannsynlig. Skjer det, bytt tilbake til enkelttrådet.

## 🗂️ Prosjektstruktur

```
arena-model-hunter/
├── main.py             # meny, innstillinger, scenarier
├── ui.py               # terminalgrensesnitt: ramme, alt-screen, tastelesing, endring av vindusstørrelse
├── arena_login.py      # nettleser, innlogging, sesjonsgjenkjenning, konfigurasjon
├── flow.py             # Arena ↔ lm.ikale.io-løype, Verify, nytt navn
├── i18n.py             # UI-oversettelser (en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI: lint og oversettelsessjekk
├── LICENSE
└── docs/i18n/          # denne README på 30 språk
```

## 🌍 Miljøvariabler

| Variabel | Standard | Formål |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | mappe for profil og sesjon |
| `ARENA_HELPER_HOME` | — | gammelt navn på variabelen, virker fortsatt |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | valgfri automatisk utfylling av skjemaet (lagres aldri) |
| `ARENA_LOGIN_TIMEOUT` | `900` | sekunder med venting på innlogging |
| `ARENA_URL` | `https://arena.ai/` | start-URL |

## 🧰 Ofte stilte spørsmål

- **«Just a moment…» / Cloudflare-sjekk** — det kreves et synlig nettleservindu; ikke kjør på en server uten skrivebord.
- **«Nettleseren er ikke installert»** — kjør `python -m playwright install chromium`.
- **Captcha eller forespørsler sendes stille ikke** — sannsynligvis en grense: slå på enkelttrådet og senk tempoet.
- **Jeg vil starte på nytt** — Innstillinger → *Fjern aktiv arena.ai-konto*, eller slett `~/.arena-model-hunter`.
- **Jakt hele natten** — Innstillinger → *Ubegrenset antall chatter*, skriv `300` i Start og bekreft; bli i enkelttrådsmodus og se de omdøpte chattene om morgenen.

## ⚠️ Ansvarsfraskrivelse

Prosjektet er laget for **personlige eksperimenter og læring**. Det automatiserer et tredjepartsside; automatisering kan bryte vilkårene til arena.ai og fingeravtrykksiden og føre til kontobegrensninger. Bruk på eget ansvar, ikke skap unødvendig belastning, hold deg til enkelttrådet ved tvil, og publiser aldri dataene dine — appen lagrer ikke passordet på disk.

## 📄 Lisens

[MIT](LICENSE) — fri programvare: du kan bruke, undersøke, dele og endre den. Hvis du distribuerer programmet eller en endret versjon, må du ta med opphavsrettsmerknaden og teksten til MIT-lisensen. Det gis ingen garanti.

Copyright (C) 2026 bidragsytere til arena model hunter.

