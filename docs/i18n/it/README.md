<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | **🇮🇹 Italiano** | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Cacciatore di modelli per arena.ai: avvia un lotto di chat in modalità agent, calcola l'impronta di ogni risposta, scopre quale modello ha risposto e rinomina la chat con quel nome — la mattina hai una chat etichettata con Claude Opus, GPT-5, Gemini o quello che stavi cercando.**

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

## 🎯 Perché esiste

In modalità agent arena.ai decide da sé quale modello risponde, e non sempre è quello che vuoi: a volte un modello di prima fascia (Claude Opus e simili), a volte qualcosa di molto più debole. Questo strumento trasforma la lotteria in una ricerca: apre un lotto di chat in modalità agent, ripete i tre campioni di impronta in ognuna, chiede al sito delle impronte quale modello ha risposto e scrive il verdetto nel titolo della chat (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Lascialo girare di notte con quante chat vuoi; la mattina hai un elenco etichettato: apri la chat il cui titolo dice il modello che ti serve e lavora lì. È questo il punto: non automazione fine a se stessa, ma ottenere una chat che gira davvero sul modello che volevi.

## ✨ Cosa fa

- **Un solo accesso — la sessione resta.** Si apre un Chromium reale (non headless), accedi ad arena.ai come al solito; l'app rileva l'accesso, salva la sessione e chiude da sola il browser.
- **N chat contemporaneamente.** Inserisci un numero da 1 a 100 — si aprono esattamente tante schede `arena.ai/agent` e altrettante schede `lm.ikale.io`.
- **Copia al posto tuo.** Il prompt di ogni campione va all'agente, la risposta viene attesa per intero e incollata nel campo Reply — tre campioni per chat.
- **Riconosce il modello.** Clicca Verify sul sito delle impronte, legge il miglior candidato e la confidenza esattamente come li mostra il sito, e rinomina la chat Arena in `modello confidenza` (per esempio `gpt-6-luna 99.9%`).
- **Due modalità di esecuzione.** Singolo thread (sicura, chat una alla volta) e multi thread (tutte in parallelo, 1,5–2× più veloce).
- **Interfaccia in tre lingue.** English, Русский, 中文 — si cambia nell'app, senza riavvio.

## 🔄 Come si svolge un'esecuzione

1. **Accesso** — si apre il browser, ti autentichi, l'app lo rileva e chiude la finestra.
2. **Avvia → numero di chat** — per esempio `3`: tre schede Arena e tre schede delle impronte.
3. **Campioni 1 → 3** — ogni prompt va all'agente, ogni risposta torna sul sito.
4. **Verify** — il sito ordina i modelli candidati, l'app legge il vincitore e la confidenza.
5. **Rinomina** — la chat Arena si chiama `modello confidenza` e nella console compare un riepilogo.

## 📋 Requisiti

- Python **3.10+**
- Windows 10/11, macOS o Linux
- Un account arena.ai (email e password oppure link via email)
- ~400 MB liberi per Chromium di Playwright

## 🚀 Installazione

```bash
git clone <this-repo> arena-model-hunter
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** poi basta un doppio clic su `run.bat` (attiva UTF-8 per visualizzare correttamente il cirillico).
**macOS / Linux:** `./run.sh` oppure `python main.py`.

## 🕹️ Utilizzo

```bash
python main.py
```

| Opzione | Descrizione |
|---|---|
| **Avvia** | chiede quante chat avviare (1–100, o qualsiasi numero con le chat illimitate) e avvia tutta la procedura |
| **Impostazioni** | modalità di esecuzione, lingua dell'interfaccia, rimozione dell'account arena.ai attivo |
| **Esci** | chiude l'app (il terminale torna al contenuto precedente) |

Il menu si adatta allo stato: finché non c'è un account collegato compare **Accedi** e il cursore si posiziona lì; dopo un accesso riuscito la voce scompare.

## ⚙️ Impostazioni

| Opzione | Descrizione |
|---|---|
| **Modalità di esecuzione** | `singolo thread` (predefinita) / `multi thread` — la multi thread è più veloce ma invia richieste parallele |
| **Lingua** | `English` / `Русский` / `中文` — si applica subito e viene ricordata |
| **Chat illimitate** ⚠️ | toglie il limite di 100 chat: `Start` accetta qualsiasi numero — pericoloso, disattivato per impostazione predefinita |
| **Rimuovi l'account arena.ai attivo** | cancella il profilo del browser e la sessione, quindi disconnette |

Le impostazioni sono in `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Le chat illimitate sono disattivate per impostazione predefinita e l'avviso è serio.** Con l'opzione attiva, `Start` accetta qualsiasi numero invece di 1–100 — `250`, `1000`. Ogni chat sono due schede, quindi numeri alti significano una raffica di richieste parallele ad arena.ai: è esattamente il motivo per cui esistono limiti di frequenza e captcha, con un rischio reale di restrizione dell'account. Attivala solo se lo accetti e resta in modalità a thread singolo; oltre 100 compare una seconda conferma con il numero esatto prima che si apra qualcosa.

## 🔐 How signing in works

1. A **real** Chromium window opens with a persistent profile (`~/.arena-model-hunter/profile`) — headless browsers are rejected by Cloudflare, so the app never uses one.
2. You click `Log In` → enter your email → `Continue with email`.
   - Existing account → enter the password → `Log In`.
   - New email → the name step can be skipped → a link arrives by mail → paste it into the address bar (`Ctrl+L`, `Ctrl+V`, Enter) → create a password.
3. The app polls the page every 1.5 s and detects success by: your email appearing in the sidebar, an `arena-auth-*` cookie, and the `Log In` button disappearing.
4. It saves `session.json` + `state.json` and **closes the browser**.

The site always opens in **dark theme** (the browser is launched with `prefers-color-scheme: dark`, which arena.ai follows).

## ⚡ Modalità singolo thread e multi thread

| Modalità | Come funziona | Misurato su 3 chat |
|---|---|---|
| **Singolo thread** (predefinita) | le coppie di schede vengono elaborate una dopo l'altra, la scheda attiva passa davanti | ≈7,5 min |
| **Multi thread** | tutte le coppie di schede girano insieme, il focus non viene spostato | ≈4,5 min |

In multi thread Arena riceve più richieste insieme, quindi limiti e captcha sono più probabili. Se succede, torna alla modalità singolo thread.

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

## 🧰 Domande frequenti

- **«Just a moment…» / controllo Cloudflare** — serve una finestra del browser visibile; non avviare su un server senza desktop.
- **«Il browser non è installato»** — esegui `python -m playwright install chromium`.
- **Captcha o richieste ignorate in silenzio** — probabilmente hai raggiunto un limite: passa a singolo thread e rallenta.
- **Voglio ricominciare da zero** — Impostazioni → *Rimuovi l'account arena.ai attivo*, oppure elimina `~/.arena-model-hunter`.
- **Cacciare tutta la notte** — Impostazioni → *Chat illimitate*, digita `300` in Avvia e conferma; resta a thread singolo e la mattina guarda le chat rinominate.

## ⚠️ Avvertenza

Il progetto è pensato per **esperimenti personali e apprendimento**. Automatizza un sito di terze parti; l'automazione può violare i termini di arena.ai e del sito delle impronte e portare a limitazioni dell'account. Usalo a tuo rischio, non generare carichi inutili, in caso di dubbio resta in singolo thread e non pubblicare mai i tuoi dati — l'app non salva la password su disco.

## 📄 Licenza

[MIT](LICENSE) — fai ciò che vuoi, senza garanzie.

<div align="center">

**[⬆ Inizio pagina](#-arena-model-hunter) · 🇺🇸 [Read in English](../../../README.md)**

</div>
