<div align="center">

🌐 **Available in:** 🇺🇸 **English** | 🇧🇷 [Português (Brasil)](docs/i18n/pt-BR/README.md) | 🇪🇸 [Español](docs/i18n/es/README.md) | 🇫🇷 [Français](docs/i18n/fr/README.md) | 🇮🇹 [Italiano](docs/i18n/it/README.md) | 🇷🇺 [Русский](docs/i18n/ru/README.md) | 🇨🇳 [中文 (简体)](docs/i18n/zh-CN/README.md) | 🇩🇪 [Deutsch](docs/i18n/de/README.md) | 🇮🇳 [हिन्दी](docs/i18n/in/README.md) | 🇹🇭 [ไทย](docs/i18n/th/README.md) | 🇺🇦 [Українська](docs/i18n/uk-UA/README.md) | 🇸🇦 [العربية](docs/i18n/ar/README.md) | 🇯🇵 [日本語](docs/i18n/ja/README.md) | 🇻🇳 [Tiếng Việt](docs/i18n/vi/README.md) | 🇧🇬 [Български](docs/i18n/bg/README.md) | 🇩🇰 [Dansk](docs/i18n/da/README.md) | 🇫🇮 [Suomi](docs/i18n/fi/README.md) | 🇮🇱 [עברית](docs/i18n/he/README.md) | 🇭🇺 [Magyar](docs/i18n/hu/README.md) | 🇮🇩 [Bahasa Indonesia](docs/i18n/id/README.md) | 🇰🇷 [한국어](docs/i18n/ko/README.md) | 🇲🇾 [Bahasa Melayu](docs/i18n/ms/README.md) | 🇳🇱 [Nederlands](docs/i18n/nl/README.md) | 🇳🇴 [Norsk](docs/i18n/no/README.md) | 🇵🇹 [Português (Portugal)](docs/i18n/pt/README.md) | 🇷🇴 [Română](docs/i18n/ro/README.md) | 🇵🇱 [Polski](docs/i18n/pl/README.md) | 🇸🇰 [Slovenčina](docs/i18n/sk/README.md) | 🇸🇪 [Svenska](docs/i18n/sv/README.md) | 🇵🇭 [Filipino](docs/i18n/phi/README.md) | 🇨🇿 [Čeština](docs/i18n/cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Model hunter for arena.ai: run a batch of agent chats, fingerprint every answer to find out which model replied, and rename the chat after it — so in the morning you have a labelled chat powered by Claude Opus, GPT-5, Gemini or whatever else you were hunting for.**

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

## 🎯 Why this exists

In agent mode arena.ai decides for you which model answers — and it is not always the one you want. Sometimes you get a top-tier model (Claude Opus and its peers), sometimes something far weaker, and you have no way to ask for a specific one.

This tool turns that lottery into a search. It opens a batch of agent chats, replays the three fingerprint samples in every single one, asks the fingerprint site which model answered, and writes the verdict into the chat title — `claude-opus-4 99.9%`, `gpt-5.2 87%`, `gemini-3-pro 64%`. Start it in the evening with as many chats as you like, go to sleep, and in the morning you have a labelled list: open the chat whose title says the model you need and keep working in it.

That is the whole point — not automation for its own sake, but **getting a chat that runs on the model you actually wanted**, without opening a hundred tabs and checking them by hand. If the model you are hunting never showed up, run another batch.

## ✨ What it does

- **Sign in once, stay signed in.** A real (headed) Chromium window opens; you log in to arena.ai as usual. The app watches the page and notices the moment you are in — then saves the session and closes the browser itself.
- **Runs N chats at once.** You type a number (1–100); the app opens exactly that many `arena.ai/agent` tabs plus the same number of `lm.ikale.io` tabs.
- **Replaces copy-paste.** It copies each sample prompt, sends it to the agent, waits for the full answer, and pastes the reply into the matching Reply field — three samples per chat.
- **Names the model for you.** It presses Verify on the fingerprint site, reads the top candidate and its confidence exactly as the site shows them, then renames the Arena chat to `model confidence` (for example `gpt-6-luna 99.9%`).
- **Two run modes.** Single-threaded (safe, one chat at a time) or multi-threaded (all chats in parallel, ~1.5–2× faster).
- **Unlimited mode for overnight runs.** An optional setting removes the 100-chat cap — off by default, because it is genuinely risky.
- **Interface in 3 languages.** English, Русский, 中文 — switchable inside the app, no restart needed.
- **Looks like Claude Code.** Centered frame, alt-screen buffer (no scrollback spam), redraws itself when you resize the window.

## 🔄 How a run works

1. **Sign in** — the browser opens, you authenticate; the app detects it and closes the window.
2. **Start → number of chats** — for example `3`, which means 3 Arena tabs and 3 fingerprint tabs. For a night of hunting type `100` (or more with unlimited mode).
3. **Samples 1 → 3** — each prompt goes to the agent, each reply goes back into the site.
4. **Verify** — the site ranks the candidate models; the app reads the winner and the confidence.
5. **Rename** — the Arena chat gets the name `model confidence`, and you get a summary in the console.

## 📋 Requirements

- Python **3.10+**
- Windows 10/11, macOS or Linux
- An arena.ai account (email + password, or email link)
- ~400 MB free disk for the Playwright Chromium build
- Time and RAM for your batch: every chat is two browser tabs, and 100 chats take hours — that is what overnight runs are for

## 🚀 Installation

```bash
git clone https://github.com/LeistDev/arena-model-hunter.git
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** just double-click `run.bat` afterwards (it enables UTF-8 so Cyrillic and CJK render correctly).
**macOS / Linux:** `./run.sh` or `python main.py`.

## 🕹️ Usage

```bash
python main.py
```

| Menu item | What it does |
|---|---|
| **Start** | asks how many chats to run (1–100) and launches the whole pipeline |
| **Settings** | run mode, interface language, unlimited chats, remove the active arena.ai account |
| **Exit** | quit (the terminal returns to its previous contents) |

The main menu adapts to your state: while no account is connected, **Sign in** is shown and the cursor starts on it; after a successful login the item disappears.

## ⚙️ Settings

| Option | Values | Notes |
|---|---|---|
| **Run mode** | `single-threaded` (default) / `multi-threaded` | multi-threaded is faster but sends parallel requests to Arena |
| **Language** | `English` / `Русский` / `中文` | applied instantly, remembered between launches |
| **Unlimited chats** ⚠️ | `off` (default) / `on` | removes the 100-chat cap: `Start` accepts any number. Dangerous — see below |
| **Remove active arena.ai account** | — | wipes the browser profile and the session, i.e. signs out |

Settings live in `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

### ⚠️ Unlimited chats

Off by default, and it is not a decorative warning. With it on, `Start` stops checking for the 1–100 range and takes any number — `250`, `1000` — and the only thing between you and a thousand tabs is one confirmation screen.

Why it matters: every chat is two tabs, and big numbers mean a burst of parallel requests to arena.ai — exactly the pattern that rate limits and captchas exist for, with a real risk of your account being restricted. Turn it on only if you accept that, and keep the run single-threaded. Everything above 100 asks for a second confirmation with the exact chat count before anything opens.

## 🔐 How signing in works

1. A **real** Chromium window opens with a persistent profile (`~/.arena-model-hunter/profile`) — headless browsers are rejected by Cloudflare, so the app never uses one.
2. You click `Log In` → enter your email → `Continue with email`.
   - Existing account → enter the password → `Log In`.
   - New email → the name step can be skipped → a link arrives by mail → paste it into the address bar (`Ctrl+L`, `Ctrl+V`, Enter) → create a password.
3. The app polls the page every 1.5 s and detects success by: your email appearing in the sidebar, an `arena-auth-*` cookie, and the `Log In` button disappearing.
4. It saves `session.json` + `state.json` and **closes the browser**.

The site always opens in **dark theme** (the browser is launched with `prefers-color-scheme: dark`, which arena.ai follows).

## ⚡ Single-threaded vs multi-threaded

| Mode | Behaviour | Measured on 3 chats |
|---|---|---|
| **Single-threaded** (default) | pairs of tabs are processed one after another, active tab is brought to front | ~7.5 min |
| **Multi-threaded** | every pair of tabs runs at the same time, focus is never moved | ~4.5 min |

Multi-threaded mode hits Arena with several requests simultaneously, so rate limits or captchas are more likely. If that starts happening, switch back to single-threaded.

## 🗂️ Project structure

```
arena-model-hunter/
├── main.py             # menu, settings, scenarios
├── ui.py               # terminal UI: frame, alt-screen, key reading, resize
├── arena_login.py      # browser, sign-in, session detection, config
├── flow.py             # Arena ↔ lm.ikale.io pipeline, Verify, rename
├── i18n.py             # UI translations (en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI: lint + translation checks
├── LICENSE
└── docs/i18n/          # this README in 30 languages
```

## 🌍 Environment variables

| Variable | Default | Purpose |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | profile and session folder |
| `ARENA_HELPER_HOME` | — | old name of the variable, still honoured |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | optional form autofill (never stored) |
| `ARENA_LOGIN_TIMEOUT` | `900` | seconds to wait for sign-in |
| `ARENA_URL` | `https://arena.ai/` | start URL |

## 🧰 Troubleshooting

- **"Just a moment…" / Cloudflare challenge** — the app must run with a visible browser window; do not run it on a server without a desktop.
- **"Browser is not installed"** — run `python -m playwright install chromium`.
- **Captcha or requests silently ignored** — you are probably rate-limited: switch to single-threaded mode and slow down.
- **The chat opened, but the title says a model you did not want** — the fingerprint site rates each answer with a confidence; a low percentage means the reply was not typical. Just run more chats: that is the search.
- **Hunting all night** — Settings → *Unlimited chats*, then type `300` in Start and confirm. Keep it single-threaded; results are waiting in the sidebar in the morning.
- **Want to start over** — Settings → *Remove active arena.ai account*, or delete `~/.arena-model-hunter`.
- **Layout looks off after resizing** — it redraws automatically; if your terminal is very narrow, widen it a little.

## ⚠️ Disclaimer

This project is for **personal experimentation and education**. It automates a third-party website, and what it does — mass-creating chats to hunt for a specific model and keeping that chat for free use — is very likely against arena.ai's terms of service; automated use can lead to rate limits, captchas or the restriction of your account. Use it on your own responsibility, do not hammer the services, do not run it commercially or as a service for others, keep unlimited mode and multi-threading off if you are unsure, and never commit credentials — they are never written to disk by this tool.

## 📄 License

[MIT](LICENSE) — free software: you may use, study, share and modify it. If you distribute it or a modified version, you must keep the copyright notice and the MIT permission text with it. There is no warranty.

Copyright (C) 2026 arena model hunter contributors.

<div align="center">

**[⬆ back to top](#-arena-model-hunter)** · Made for people who like tidy terminals

</div>
