<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | **🇵🇭 Filipino** | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Mangangaso ng modelo para sa arena.ai: nagpapatakbo ng isang batch ng agent chat, kumukuha ng fingerprint ng bawat sagot, inaalam kung aling modelo ang sumagot at pinapalitan ng pangalan ang chat ayon dito — pagdating ng umaga may chat ka nang may label na pinapatakbo ng Claude Opus, GPT-5, Gemini o ng modelong hinahanap mo.**

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

## 🎯 Bakit ito umiiral

Sa agent mode, ang arena.ai ang nagpapasya kung aling modelo ang sasagot — at madalas hindi ito ang gusto mo: kung minsan isang nangungunang modelo (Claude Opus at mga kauri nito), kung minsan mas mahina pa. Ginagawang paghahanap ng tool na ito ang dating parang lottery: nagbubukas ito ng batch ng agent chat, inuulit ang tatlong fingerprint sample sa bawat isa, tinatanong ang fingerprint site kung aling modelo ang sumagot, at isinusulat ang hatol sa pamagat ng chat (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Iwanan mo itong tumakbo magdamag sa kahit ilang chat; sa umaga may listahan ka nang may label: buksan ang chat na ang pamagat ay nagsasabi ng modelong kailangan mo at magpatuloy doon. Iyon ang punto — hindi automation para sa automation lang, kundi makakuha ng chat na talagang tumatakbo sa modelong gusto mo.

## ✨ Ano ang ginagawa nito

- **Isang sign-in — nananatili ang session.** Bumubukas ang tunay (hindi headless) na Chromium, nagla-log in ka sa arena.ai gaya ng dati; napansin ito ng app, sine-save ang session at sarili nitong isinasara ang browser.
- **N chats nang sabay.** Maglalagay ka ng numero mula 1 hanggang 100 — eksaktong ganoon karaming `arena.ai/agent` tab at ganoon din karaming `lm.ikale.io` tab ang bubukas.
- **Nangongopya para sa iyo.** Ipinapadala sa agent ang prompt ng bawat sample, hinihintay ang buong sagot at ipinapasok sa Reply field — tatlong sample bawat chat.
- **Kinikilala ang modelo.** Pinipindot ang Verify sa fingerprint site, binabasa ang nangungunang kandidato at ang confidence kung paano ipinapakita ng site, at pinapalitan ng pangalan ang Arena chat sa `modelo confidence` (halimbawa `gpt-6-luna 99.9%`).
- **Dalawang mode.** Single-threaded (ligtas, isa-isa ang chats) at multi-threaded (sabay-sabay, 1.5–2× mas mabilis).
- **Interface sa tatlong wika.** English, Русский, 中文 — mapapalitan sa loob ng app, walang restart.

## 🔄 Paano nangyayari ang isang run

1. **Sign in** — bubukas ang browser, mag-a-authenticate ka, mapapansin ito ng app at isasara ang window.
2. **Start → bilang ng chats** — halimbawa `3`: tatlong Arena tab at tatlong fingerprint tab.
3. **Samples 1 → 3** — bawat prompt papunta sa agent, bawat sagot babalik sa site.
4. **Verify** — niraranggo ng site ang mga kandidatong modelo, binabasa ng app ang panalo at ang confidence.
5. **Palit ng pangalan** — magiging `modelo confidence` ang Arena chat, at may buod sa console.

## 📋 Mga kailangan

- Python **3.10+**
- Windows 10/11, macOS o Linux
- Account sa arena.ai (email at password o link sa email)
- ~400 MB na libreng espasyo para sa Chromium ng Playwright

## 🚀 Pag-install

```bash
git clone https://github.com/LeistDev/arena-model-hunter.git
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** pagkatapos, i-double click lang ang `run.bat` (ini-on ang UTF-8 para tama ang pagpapakita ng Cyrillic).
**macOS / Linux:** `./run.sh` o `python main.py`.

## 🕹️ Paggamit

```bash
python main.py
```

| Opsyon | Paglalarawan |
|---|---|
| **Start** | tatanong kung ilang chat ang patatakbuhin (1–100, o kahit anong numero kapag walang limitasyon) at inilulunsad ang buong proseso |
| **Settings** | mode ng pagtakbo, wika ng interface, alisin ang aktibong arena.ai account |
| **Exit** | isinasara ang app (babalik ang terminal sa dating nilalaman) |

Umaangkop ang menu sa estado: habang walang nakakonektang account, makikita ang **Sign in** at nandoon ang cursor; pagkatapos ng matagumpay na pag-log in, nawawala ang item na iyon.

## ⚙️ Settings

| Opsyon | Paglalarawan |
|---|---|
| **Mode ng pagtakbo** | `single-threaded` (default) / `multi-threaded` — mas mabilis ang multi-threaded pero sabay-sabay ang requests |
| **Wika** | `English` / `Русский` / `中文` — agad na gumagana at natatandaan |
| **Walang limitasyong chat** ⚠️ | tinatanggal ang 100-chat na limitasyon: tumatanggap ang `Start` ng kahit anong numero — mapanganib, patay bilang default |
| **Alisin ang aktibong arena.ai account** | binubura ang browser profile at session, ibig sabihin nag-log out |

Nasa `~/.arena-model-hunter/config.json` ang mga setting:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Patay bilang default ang walang limitasyong chat, at hindi palamuti lang ang babalang ito.** Kapag naka-on, hindi na sinusuri ng `Start` ang 1–100 kundi tumatanggap ng kahit anong numero — `250`, `1000`. Dalawang tab ang bawat chat, kaya maraming numero ay malaking bugso ng sabay-sabay na request sa arena.ai: ito mismo ang dahilan kung bakit may rate limit at captcha, at totoong may panganib na malimitahan ang account. I-on lang kung tinatanggap mo iyon, at manatili sa single-thread na mode; anumang higit sa 100 ay humihingi muna ng pangalawang kumpirmasyon na may eksaktong bilang bago may bumukas.

## 🔐 Paano gumagana ang pag-sign in

1. Bubukas ang **tunay** na Chromium window na may permanenteng profile (`~/.arena-model-hunter/profile`) — tinatanggihan ng Cloudflare ang headless browser, kaya hindi ito ginagamit ng app.
2. Pindutin ang `Log In` → ilagay ang email → `Continue with email`.
   - May account na → ilagay ang password → `Log In`.
   - Bagong email → maaaring laktawan ang hakbang sa pangalan → may link na darating sa email → i-paste sa address bar (`Ctrl+L`, `Ctrl+V`, Enter) → gumawa ng password.
3. Sinusuri ng app ang pahina tuwing 1.5 segundo at nakikita ang tagumpay sa tatlong senyales: lumalabas ang email sa sidebar, may `arena-auth-*` cookie, at nawawala ang `Log In` button.
4. Pagkatapos, sine-save nito ang `session.json` + `state.json` at **isinasara ang browser**.

Palaging bumubukas ang site sa **dark theme** (sinisimulan ang browser gamit ang `prefers-color-scheme: dark`, at sinusunod ito ng arena.ai).

## ⚡ Single-threaded at multi-threaded

| Mode | Paano gumagana | Sinukat sa 3 chats |
|---|---|---|
| **Single-threaded** (default) | isa-isang pinoproseso ang mga pares ng tab, inihaharap ang aktibong tab | ≈7.5 min |
| **Multi-threaded** | sabay-sabay tumatakbo ang lahat ng pares ng tab, hindi inililipat ang focus | ≈4.5 min |

Sa multi-threaded, sabay-sabay ang requests sa Arena, kaya mas malamang ang rate limit at captcha. Kung mangyari iyon, bumalik sa single-threaded.

## 🗂️ Istruktura ng proyekto

```
arena-model-hunter/
├── main.py             # menu, settings, mga senaryo
├── ui.py               # UI ng terminal: frame, alt-screen, pagbasa ng keys, pag-resize
├── arena_login.py      # browser, sign-in, pagkilala sa session, config
├── flow.py             # Arena ↔ lm.ikale.io pipeline, Verify, pag-rename
├── i18n.py             # mga salin ng UI (en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI: lint at pagsusuri ng salin
├── LICENSE
└── docs/i18n/          # ang README na ito sa 30 wika
```

## 🌍 Mga environment variable

| Variable | Default | Para saan |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | folder ng profile at session |
| `ARENA_HELPER_HOME` | — | lumang pangalan ng variable, sinusuportahan pa rin |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | opsyonal na awtomatikong pagsagot sa form (hindi kailanman sine-save) |
| `ARENA_LOGIN_TIMEOUT` | `900` | segundong paghihintay sa sign-in |
| `ARENA_URL` | `https://arena.ai/` | panimulang URL |

## 🧰 Mga madalas na tanong

- **«Just a moment…» / Cloudflare check** — kailangan ng nakikitang browser window; huwag patakbuhin sa server na walang desktop.
- **«Hindi naka-install ang browser»** — patakbuhin ang `python -m playwright install chromium`.
- **Captcha o tahimik na hindi naipapadala ang requests** — malamang naabot ang limit: i-on ang single-threaded at bawasan ang bilis.
- **Gusto kong magsimula muli** — Settings → *Alisin ang aktibong arena.ai account*, o burahin ang `~/.arena-model-hunter`.
- **Mangangaso buong gabi** — Settings → *Walang limitasyong chat*, pagkatapos i-type ang `300` sa Start at kumpirmahin; manatili sa single-thread at tingnan ang mga na-rename na chat sa umaga.

## ⚠️ Disclaimer

Ang proyektong ito ay para sa **personal na eksperimento at pag-aaral**. Ina-automate nito ang third-party site; maaaring lumabag ang automation sa terms of service ng arena.ai at ng fingerprint site at humantong sa paghihigpit ng account. Gamitin sa sariling peligro, huwag magdulot ng sobrang load, kapag may duda manatili sa single-threaded, at huwag kailanman ilathala ang iyong data — hindi nagse-save ng password sa disk ang app.

## 📄 Lisensya

[MIT](LICENSE) — libreng software: maaaring gamitin, pag-aralan, ibahagi at baguhin. Kung ipapamahagi mo ang programa o binagong bersyon, dapat mong isama ang paunawa ng karapatang-ari at ang teksto ng lisensyang MIT. Walang garantiya.

Copyright (C) 2026 mga kontribyutor ng arena model hunter.

