<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | **🇩🇰 Dansk** | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Model-jæger til arena.ai: kører en bunke agent-chats, tager fingeraftryk af hvert svar, finder ud af hvilken model der svarede og omdøber chatten efter den — om morgenen har du en mærket chat, der kører Claude Opus, GPT-5, Gemini eller den model, du jagtede.**

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

## 🎯 Hvorfor værktøjet findes

I agent-tilstand bestemmer arena.ai selv, hvilken model der svarer — og det er ikke altid den, du vil have: nogle gange en topmodel (Claude Opus og slægt), andre gange noget markant svagere. Værktøjet gør lotteriet til en søgning: det åbner en bunke agent-chats, spiller de tre fingeraftryksprøver igennem i hver enkelt, spørger fingeraftrykssiden, hvilken model der svarede, og skriver dommen i chattens titel (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Lad den køre natten over med så mange chats, du vil; om morgenen er der en mærket liste: åbn den chat, hvis titel nævner den model, du skal bruge, og arbejd videre i den. Det er pointen — ikke automatisering for automatiseringens skyld, men en chat, der faktisk kører på den model, du gerne ville have.

## ✨ Hvad den gør

- **Én login — sessionen bliver.** Der åbnes en rigtig (ikke headless) Chromium, du logger ind på arena.ai som normalt; appen opdager det, gemmer sessionen og lukker selv browseren.
- **N chats på én gang.** Du indtaster et tal fra 1 til 100 — der åbnes præcis så mange `arena.ai/agent`-faner og lige så mange `lm.ikale.io`-faner.
- **Kopierer for dig.** Prompten fra hver sample sendes til agenten, svaret afventes fuldt og indsættes i Reply-feltet — tre samples pr. chat.
- **Genkender modellen.** Klikker Verify på fingeraftrykssiden, læser den bedste kandidat og sikkerheden præcis som siden viser dem, og omdøber Arena-chatten til `model sikkerhed` (for eksempel `gpt-6-luna 99.9%`).
- **To tilstande.** Enkelttrådet (sikker, chats efter hinanden) og flertrådet (alle chats parallelt, 1,5–2× hurtigere).
- **Grænseflade på tre sprog.** English, Русский, 中文 — skiftes i appen uden genstart.

## 🔄 Sådan foregår et kørsel

1. **Log ind** — browseren åbnes, du logger ind, appen opdager det og lukker vinduet.
2. **Start → antal chats** — for eksempel `3`: tre Arena-faner og tre fingeraftryksfaner.
3. **Samples 1 → 3** — hver prompt går til agenten, hvert svar tilbage til siden.
4. **Verify** — siden rangerer kandidatmodellerne, appen læser vinderen og sikkerheden.
5. **Omdøb** — Arena-chatten hedder derefter `model sikkerhed`, og der vises et resumé i konsollen.

## 📋 Krav

- Python **3.10+**
- Windows 10/11, macOS eller Linux
- En arena.ai-konto (e-mail og adgangskode eller link pr. mail)
- ~400 MB fri diskplads til Chromium fra Playwright

## 🚀 Installation

```bash
git clone https://github.com/LeistDev/arena-model-hunter.git
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** derefter er et dobbeltklik på `run.bat` nok (aktiverer UTF-8, så kyrillisk vises korrekt).
**macOS / Linux:** `./run.sh` eller `python main.py`.

## 🕹️ Brug

```bash
python main.py
```

| Indstilling | Beskrivelse |
|---|---|
| **Start** | spørger, hvor mange chats der skal køre (1–100, eller et vilkårligt tal med ubegrænsede chats) og starter hele forløbet |
| **Indstillinger** | tilstand, grænsefladesprog, fjern den aktive arena.ai-konto |
| **Afslut** | lukker appen (terminalen viser igen sit tidligere indhold) |

Menuen tilpasser sig tilstanden: så længe ingen konto er forbundet, vises **Log ind**, og markøren står på den; efter et vellykket login forsvinder punktet.

## ⚙️ Indstillinger

| Indstilling | Beskrivelse |
|---|---|
| **Tilstand** | `enkelttrådet` (standard) / `flertrådet` — flertrådet er hurtigere, men sender parallelle forespørgsler |
| **Sprog** | `English` / `Русский` / `中文` — virker med det samme og huskes |
| **Ubegrænsede chats** ⚠️ | fjerner loftet på 100 chats: `Start` tager et vilkårligt tal — farligt, slået fra som standard |
| **Fjern aktiv arena.ai-konto** | sletter browserprofil og session, altså logger ud |

Indstillinger ligger i `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Ubegrænsede chats er slået fra som standard, og advarslen er ikke pynt.** Er den tændt, tjekker `Start` ikke længere 1–100, men tager et vilkårligt tal — `250`, `1000`. Hver chat er to faner, så store tal betyder en byge af parallelle kald til arena.ai: præcis det, rate limits og captcha findes for, med reel risiko for at kontoen bliver begrænset. Slå det kun til, hvis du accepterer det, og bliv i enkelt-trådet tilstand; alt over 100 kræver en ekstra bekræftelse med det præcise antal, før noget åbner.

## 🔐 Sådan foregår login

1. Der åbnes et **rigtigt** Chromium-vindue med en permanent profil (`~/.arena-model-hunter/profile`) — Cloudflare afviser headless browsere, så appen bruger aldrig en.
2. Du klikker på `Log In` → indtaster din e-mail → `Continue with email`.
   - Eksisterende konto → indtast adgangskode → `Log In`.
   - Ny e-mail → navnetrinnet kan springes over → der kommer et link på mail → indsæt det i adresselinjen (`Ctrl+L`, `Ctrl+V`, Enter) → opret en adgangskode.
3. Appen tjekker siden hvert 1,5 sekund og ser login lykkes på tre tegn: din e-mail dukker op i sidepanelet, en `arena-auth-*`-cookie opstår, og knappen `Log In` forsvinder.
4. Derefter gemmer den `session.json` + `state.json` og **lukker browseren**.

Siden åbner altid i **mørkt tema** (browseren startes med `prefers-color-scheme: dark`, og arena.ai følger det).

## ⚡ Enkelttrådet og flertrådet tilstand

| Tilstand | Sådan virker det | Målt med 3 chats |
|---|---|---|
| **Enkelttrådet** (standard) | fanepar behandles efter hinanden, den aktive fane hentes frem | ≈7,5 min |
| **Flertrådet** | alle fanepar kører samtidigt, fokus flyttes ikke | ≈4,5 min |

I flertrådet tilstand får Arena flere forespørgsler på én gang, så grænser og captcha er mere sandsynlige. Sker det, skift tilbage til enkelttrådet.

## 🗂️ Projektets struktur

```
arena-model-hunter/
├── main.py             # menu, indstillinger, scenarier
├── ui.py               # terminal-UI: ramme, alt-screen, tastelæsning, ændring af vinduesstørrelse
├── arena_login.py      # browser, login, sessionsgenkendelse, konfiguration
├── flow.py             # Arena ↔ lm.ikale.io-pipeline, Verify, omdøbning
├── i18n.py             # UI-oversættelser (en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI: lint og oversættelsestjek
├── LICENSE
└── docs/i18n/          # denne README på 30 sprog
```

## 🌍 Miljøvariabler

| Variabel | Standard | Formål |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | mappe til profil og session |
| `ARENA_HELPER_HOME` | — | variablens gamle navn, virker stadig |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | valgfri automatisk udfyldning af formularen (gemmes aldrig) |
| `ARENA_LOGIN_TIMEOUT` | `900` | sekunder der ventes på login |
| `ARENA_URL` | `https://arena.ai/` | start-URL |

## 🧰 Ofte stillede spørgsmål

- **„Just a moment…“ / Cloudflare-kontrol** — der kræves et synligt browservindue; kør ikke på en server uden skrivebord.
- **„Browseren er ikke installeret“** — kør `python -m playwright install chromium`.
- **Captcha eller forespørgsler sendes lydløst ikke** — sandsynligvis en grænse: slå enkelttrådet til og sænk tempoet.
- **Jeg vil starte forfra** — Indstillinger → *Fjern aktiv arena.ai-konto*, eller slet `~/.arena-model-hunter`.
- **Jagt hele natten** — Indstillinger → *Ubegrænsede chats*, skriv `300` i Start og bekræft; bliv i enkelt-trådet tilstand og se de omdøbte chats om morgenen.

## ⚠️ Ansvarsfraskrivelse

Projektet er lavet til **personlige eksperimenter og læring**. Det automatiserer et tredjepartssite; automatisering kan være i strid med arena.ai's og fingeraftrykssidens vilkår og kan føre til kontobegrænsninger. Brug på eget ansvar, undgå unødig belastning, hold dig til enkelttrådet ved tvivl, og offentliggør aldrig dine data — appen gemmer ikke adgangskoden på disk.

## 📄 Licens

[MIT](LICENSE) — fri software: du må bruge, undersøge, dele og ændre det. Hvis du distribuerer programmet eller en ændret version, skal du bevare ophavsretsmeddelelsen og MIT-licensteksten sammen med det. Der er ingen garanti.

Copyright (C) 2026 bidragydere til arena model hunter.

