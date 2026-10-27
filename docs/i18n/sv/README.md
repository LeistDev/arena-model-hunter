<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | **🇸🇪 Svenska** | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Modelljägare för arena.ai: kör en hög agent-chattar, tar fingeravtryck av varje svar, listar ut vilken modell som svarade och döper chatten efter den — på morgonen finns en märkt chatt som kör Claude Opus, GPT-5, Gemini eller den modell du jagade.**

![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![UI](https://img.shields.io/badge/UI-terminal-6E56CF)
![License](https://img.shields.io/badge/license-GPL--3.0-blue)

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

## 🎯 Varför verktyget finns

I agentläge bestämmer arena.ai själv vilken modell som svarar — och det är inte alltid den du vill ha: ibland en toppmodell (Claude Opus och släkten), ibland något betydligt svagare. Verktyget gör lotteriet till en sökning: det öppnar en hög agent-chattar, spelar de tre fingeravtrycksproverna i varje chatt, frågar fingeravtryckssajten vilken modell som svarade och skriver domen i chattens titel (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Låt den gå över natten med så många chattar du vill; på morgonen ligger en märkt lista: öppna chatten vars titel anger modellen du behöver och arbeta vidare i den. Det är poängen — inte automatisering för automatiseringens skull, utan en chatt som verkligen kör på modellen du ville ha.

## ✨ Vad den gör

- **En inloggning — sessionen sparas.** En riktig (inte headless) Chromium öppnas, du loggar in på arena.ai som vanligt; appen upptäcker det, sparar sessionen och stänger webbläsaren själv.
- **N chattar samtidigt.** Du anger ett tal från 1 till 100 — exakt så många `arena.ai/agent`-flikar och lika många `lm.ikale.io`-flikar öppnas.
- **Kopierar åt dig.** Prompten för varje sampel skickas till agenten, svaret väntas in i sin helhet och klistras in i Reply-fältet — tre sampel per chatt.
- **Identifierar modellen.** Klickar Verify på fingeravtryckssajten, läser av bästa kandidaten och konfidensen precis som sajten visar dem, och byter namn på Arena-chatten till `modell konfidens` (till exempel `gpt-6-luna 99.9%`).
- **Två körlägen.** Entrådad (säker, chattar efter varandra) och flertrådad (alla chattar parallellt, 1,5–2× snabbare).
- **Gränssnitt på tre språk.** English, Русский, 中文 — byts i appen, utan omstart.

## 🔄 Så går en körning till

1. **Logga in** — webbläsaren öppnas, du loggar in, appen upptäcker det och stänger fönstret.
2. **Start → antal chattar** — till exempel `3`: tre Arena-flikar och tre fingeravtrycksflikar.
3. **Sampel 1 → 3** — varje prompt går till agenten, varje svar tillbaka till sajten.
4. **Verify** — sajten rangordnar kandidatmodellerna, appen läser av vinnaren och konfidensen.
5. **Namnbyte** — Arena-chatten heter sedan `modell konfidens`, och en sammanfattning visas i konsolen.

## 📋 Krav

- Python **3.10+**
- Windows 10/11, macOS eller Linux
- Ett arena.ai-konto (e-post och lösenord eller länk via mejl)
- ~400 MB ledigt diskutrymme för Chromium från Playwright

## 🚀 Installation

```bash
git clone https://github.com/LeistDev/arena-model-hunter.git
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** därefter räcker det med ett dubbelklick på `run.bat` (slår på UTF-8 så att kyrilliska tecken visas korrekt).
**macOS / Linux:** `./run.sh` eller `python main.py`.

## 🕹️ Användning

```bash
python main.py
```

| Alternativ | Beskrivning |
|---|---|
| **Start** | frågar hur många chattar som ska köras (1–100, eller valfritt antal med obegränsade chattar) och startar hela flödet |
| **Inställningar** | körläge, gränssnittsspråk, ta bort det aktiva arena.ai-kontot |
| **Avsluta** | stänger appen (terminalen visar igen sitt tidigare innehåll) |

Menyn anpassar sig efter läget: så länge inget konto är anslutet visas **Logga in** och markören står på den; efter lyckad inloggning försvinner punkten.

## ⚙️ Inställningar

| Alternativ | Beskrivning |
|---|---|
| **Körläge** | `entrådad` (standard) / `flertrådad` — flertrådad är snabbare men skickar parallella förfrågningar |
| **Språk** | `English` / `Русский` / `中文` — gäller direkt och sparas |
| **Obegränsat antal chattar** ⚠️ | tar bort taket på 100 chattar: `Start` tar vilket tal som helst — farligt, avstängt som standard |
| **Ta bort aktivt arena.ai-konto** | raderar webbläsarprofilen och sessionen, alltså loggar ut |

Inställningarna ligger i `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Obegränsat antal chattar är avstängt som standard, och varningen är inte dekoration.** Med det på kontrollerar `Start` inte längre 1–100 utan tar vilket tal som helst — `250`, `1000`. Varje chatt är två flikar, så stora tal betyder en skur av parallella anrop till arena.ai: exakt det som hastighetsgränser och captcha finns för, med reell risk att kontot begränsas. Slå bara på det om du accepterar det, och stanna i entrådsläge; över 100 krävs en andra bekräftelse med det exakta antalet innan något öppnas.

## 🔐 Så fungerar inloggningen

1. Ett **riktigt** Chromium-fönster öppnas med en beständig profil (`~/.arena-model-hunter/profile`) — Cloudflare avvisar headless webbläsare, så appen använder aldrig någon.
2. Du klickar på `Log In` → skriver in din e-post → `Continue with email`.
   - Befintligt konto → ange lösenordet → `Log In`.
   - Ny e-post → namnsteget kan hoppas över → en länk kommer via mejl → klistra in den i adressfältet (`Ctrl+L`, `Ctrl+V`, Enter) → skapa ett lösenord.
3. Appen kontrollerar sidan var 1,5 sekund och ser att inloggningen lyckats på tre tecken: din e-post syns i sidopanelen, en `arena-auth-*`-kaka skapas och knappen `Log In` försvinner.
4. Sedan sparar den `session.json` + `state.json` och **stänger webbläsaren**.

Sajten öppnas alltid i **mörkt tema** (webbläsaren startas med `prefers-color-scheme: dark`, och arena.ai följer det).

## ⚡ Entrådad och flertrådad

| Läge | Hur det fungerar | Mätt med 3 chattar |
|---|---|---|
| **Entrådad** (standard) | flikparen bearbetas efter varandra, den aktiva fliken lyfts fram | ≈7,5 min |
| **Flertrådad** | alla flikpar körs samtidigt, fokus flyttas aldrig | ≈4,5 min |

I flertrådat läge får Arena flera förfrågningar samtidigt, så gränser och captcha är mer sannolika. Börjar det hända, byt tillbaka till entrådat.

## 🗂️ Projektstruktur

```
arena-model-hunter/
├── main.py             # meny, inställningar, scenarier
├── ui.py               # terminalgränssnitt: ram, alt-screen, tangentläsning, storleksändring
├── arena_login.py      # webbläsare, inloggning, sessionsigenkänning, konfiguration
├── flow.py             # Arena ↔ lm.ikale.io-pipeline, Verify, namnbyte
├── i18n.py             # UI-översättningar (en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI: lint och översättningskontroll
├── LICENSE
└── docs/i18n/          # denna README på 30 språk
```

## 🌍 Miljövariabler

| Variabel | Standard | Syfte |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | mapp för profil och session |
| `ARENA_HELPER_HOME` | — | variabelns gamla namn, fungerar fortfarande |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | valfritt autofyllning av formuläret (sparas aldrig) |
| `ARENA_LOGIN_TIMEOUT` | `900` | sekunder att vänta på inloggning |
| `ARENA_URL` | `https://arena.ai/` | start-URL |

## 🧰 Vanliga frågor

- **”Just a moment…” / Cloudflare-kontroll** — det krävs ett synligt webbläsarfönster; kör inte på en server utan skrivbord.
- **”Webbläsaren är inte installerad”** — kör `python -m playwright install chromium`.
- **Captcha eller förfrågningar skickas tyst inte** — troligen en gräns: slå på entrådat läge och sänk tempot.
- **Jag vill börja om** — Inställningar → *Ta bort aktivt arena.ai-konto*, eller radera `~/.arena-model-hunter`.
- **Jaga hela natten** — Inställningar → *Obegränsat antal chattar*, skriv `300` i Start och bekräfta; kör entrådigt och titta på de omdöpta chattarna på morgonen.

## ⚠️ Ansvarsfriskrivning

Projektet är gjort för **personliga experiment och lärande**. Det automatiserar en tredjepartssajt; automatisering kan bryta mot arena.ai:s och fingeravtryckssajtens villkor och leda till kontobegränsningar. Använd på egen risk, skapa inte onödig belastning, håll dig till entrådat läge vid tvekan, och publicera aldrig dina uppgifter — appen sparar inte lösenordet på disk.

## 📄 Licens

[GNU General Public License v3.0](LICENSE) — fri programvara: du får använda, undersöka, dela och ändra den. Om du distribuerar programmet eller en ändrad version måste det förbli under GPL och källkoden förbli öppen. Ingen garanti ges.

Copyright (C) 2026 bidragsgivare till arena model hunter.

