<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | **🇨🇿 Čeština**

</div>

---

<div align="center">

# ✦ arena model hunter

**Lovec modelů pro arena.ai: spouští dávku chatů v režimu agent, snímá otisk každé odpovědi, zjišťuje, který model odpověděl, a přejmenuje chat podle něj — ráno máte označený chat poháněný Claude Opus, GPT-5, Gemini nebo modelem, který jste hledali.**

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

## 🎯 Proč to existuje

V režimu agent arena.ai sám rozhoduje, který model odpoví — a zdaleka to není vždy ten, který chcete: někdy model z nejvyšší kategorie (Claude Opus a spol.), jindy něco výrazně slabšího. Nástroj mění loterii v hledání: otevře dávku chatů v režimu agent, v každém přehraje tři vzorky otisku, zeptá se stránky otisků, který model odpověděl, a verdikt zapíše do názvu chatu (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Nechte ho běžet přes noc s libovolným počtem chatů; ráno je označený seznam: otevřete chat, v jehož názvu je potřebný model, a pracujte v něm. To je smysl — ne automatizace pro automatizaci, ale chat, který skutečně běží na modelu, který jste chtěli.

## ✨ Co umí

- **Jedno přihlášení — session zůstává.** Otevře se skutečný (ne headless) Chromium, přihlásíte se do arena.ai jako obvykle; aplikace přihlášení rozpozná, uloží session a sama zavře prohlížeč.
- **N chatů najednou.** Zadáte číslo 1–100 — otevře se přesně tolik panelů `arena.ai/agent` a stejně panelů `lm.ikale.io`.
- **Kopíruje za vás.** Prompt každého vzorku jde agentovi, odpověď se počká celá a vloží se do pole Reply — tři vzorky na chat.
- **Určí model.** Klikne Verify na webu s otisky, přečte nejlepšího kandidáta a jistotu přesně tak, jak je ukazuje web, a přejmenuje chat na `model jistota` (např. `gpt-6-luna 99.9%`).
- **Dva režimy běhu.** Jednovláknový (bezpečný, chaty po sobě) a vícevláknový (všechny chaty paralelně, 1.5–2× rychleji).
- **Rozhraní ve třech jazycích.** English, Русский, 中文 — přepíná se v aplikaci, bez restartu.

## 🔄 Jak běh probíhá

1. **Přihlášení** — otevře se prohlížeč, přihlásíte se, aplikace to pozná a zavře okno.
2. **Start → počet chatů** — například `3`: tři panely Arena a tři panely s otisky.
3. **Vzorky 1 → 3** — každý prompt letí agentovi, každá odpověď se vrací na web.
4. **Verify** — web seřadí kandidátské modely, aplikace přečte vítěze a jistotu.
5. **Přejmenování** — chat v Arena dostane jméno `model jistota`, v konzoli se objeví souhrn.

## 📋 Požadavky

- Python **3.10+**
- Windows 10/11, macOS nebo Linux
- Účet arena.ai (e-mail a heslo nebo odkaz z mailu)
- ~400 MB volného místa pro Chromium v Playwright

## 🚀 Instalace

```bash
git clone <this-repo> arena-model-hunter
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** pak stačí dvojklik na `run.bat` (zapíná UTF-8, aby se cyrilice zobrazovala správně).
**macOS / Linux:** `./run.sh` nebo `python main.py`.

## 🕹️ Použití

```bash
python main.py
```

| Volba | Popis |
|---|---|
| **Start** | zeptá se, kolik chatů spustit (1–100, u neomezených libovolné číslo), a spustí celý průběh |
| **Nastavení** | režim běhu, jazyk rozhraní, odstranění aktivního účtu arena.ai |
| **Konec** | zavře aplikaci (terminál se vrátí k předchozímu obsahu) |

Menu se přizpůsobuje stavu: dokud není účet připojen, zobrazuje se **Přihlásit** a kurzor na něm stojí; po úspěšném přihlášení položka zmizí.

## ⚙️ Nastavení

| Volba | Popis |
|---|---|
| **Režim běhu** | `jednovláknový` (výchozí) / `vícevláknový` — vícevláknový je rychlejší, ale posílá paralelní požadavky |
| **Jazyk** | `English` / `Русский` / `中文` — projeví se hned a pamatuje se |
| **Neomezený počet chatů** ⚠️ | ruší limit 100 chatů: `Start` přijme libovolné číslo — nebezpečné, ve výchozím stavu vypnuto |
| **Odstranit aktivní účet arena.ai** | smaže profil prohlížeče i session, tedy odhlásí |

Nastavení se ukládá do `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Neomezený počet chatů je ve výchozím stavu vypnutý a varování není ozdoba.** Po zapnutí `Start` nekontroluje rozsah 1–100, ale přijme libovolné číslo — `250`, `1000`. Každý chat jsou dvě karty, takže velká čísla znamenají příval paralelních požadavků na arena.ai: přesně to, před čím mají chránit limity rychlosti a captcha, s reálným rizikem omezení účtu. Zapínejte jen když to přijímáte, a zůstaňte v jednovláknovém režimu; nad 100 program nejprve žádá druhé potvrzení s přesným počtem.

## 🔐 How signing in works

1. A **real** Chromium window opens with a persistent profile (`~/.arena-model-hunter/profile`) — headless browsers are rejected by Cloudflare, so the app never uses one.
2. You click `Log In` → enter your email → `Continue with email`.
   - Existing account → enter the password → `Log In`.
   - New email → the name step can be skipped → a link arrives by mail → paste it into the address bar (`Ctrl+L`, `Ctrl+V`, Enter) → create a password.
3. The app polls the page every 1.5 s and detects success by: your email appearing in the sidebar, an `arena-auth-*` cookie, and the `Log In` button disappearing.
4. It saves `session.json` + `state.json` and **closes the browser**.

The site always opens in **dark theme** (the browser is launched with `prefers-color-scheme: dark`, which arena.ai follows).

## ⚡ Jednovláknový a vícevláknový režim

| Režim | Jak funguje | Měřeno na 3 chatech |
|---|---|---|
| **Jednovláknový** (výchozí) | dvojice panelů se zpracovávají po sobě, aktivní panel jde dopředu | ≈7,5 min |
| **Vícevláknový** | všechny dvojice panelů běží současně, fokus se nepřepíná | ≈4,5 min |

Ve vícevláknovém režimu dostává Arena několik požadavků naráz, takže limity a captcha jsou pravděpodobnější. Pokud se objeví, vraťte se k jednovláknovému režimu.

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

## 🧰 Časté otázky

- **„Just a moment…“ / ověření Cloudflare** — je potřeba viditelné okno prohlížeče; nespouštějte na serveru bez plochy.
- **„Prohlížeč není nainstalován“** — spusťte `python -m playwright install chromium`.
- **Captcha nebo požadavky se tiše neodesílají** — pravděpodobně limit: zapněte jednovláknový režim a zpomalte.
- **Chci začít znovu** — Nastavení → *Odstranit aktivní účet arena.ai* nebo smažte `~/.arena-model-hunter`.
- **Lov po celou noc** — Nastavení → *Neomezený počet chatů*, zadejte `300` ve Spustit a potvrďte; zůstaňte v jednovláknovém režimu a ráno se podívejte na přejmenované chaty.

## ⚠️ Upozornění

Projekt vznikl pro **vlastní experimenty a výuku**. Automatizuje cizí web; automatizace může porušovat podmínky užívání arena.ai i webu s otisky a vést k omezení účtu. Používejte na vlastní riziko, nevytvářejte zbytečnou zátěž, v případě pochybností držte jednovláknový režim a nikdy nezveřejňujte své údaje — aplikace heslo neukládá na disk.

## 📄 Licence

[MIT](LICENSE) — dělejte si, co chcete, bez záruk.

<div align="center">

**[⬆ Nahoru](#-arena-model-hunter) · 🇺🇸 [Read in English](../../../README.md)**

</div>
