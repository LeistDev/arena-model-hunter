<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | **🇸🇰 Slovenčina** | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Lovec modelov pre arena.ai: spúšťa dávku chatov v režime agent, sníma odtlačok každej odpovede, zisťuje, ktorý model odpovedal, a premenuje chat podľa neho — ráno máte označený chat poháňaný Claude Opus, GPT-5, Gemini alebo modelom, ktorý ste hľadali.**

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

## 🎯 Prečo to existuje

V režime agent arena.ai sám rozhoduje, ktorý model odpovie — a zďaleka to nie je vždy ten, ktorý chcete: niekedy model z najvyššej kategórie (Claude Opus a spol.), inokedy niečo výrazne slabšie. Nástroj mení lotériu na hľadanie: otvorí dávku chatov v režime agent, v každom prehrá tri vzorky odtlačku, opýta sa stránky odtlačkov, ktorý model odpovedal, a verdikt zapíše do názvu chatu (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Nechajte ho bežať cez noc s ľubovoľným počtom chatov; ráno je označený zoznam: otvorte chat, v ktorého názve je potrebný model, a pracujte v ňom. To je pointa — nie automatizácia pre automatizáciu, ale chat, ktorý naozaj beží na modeli, ktorý ste chceli.

## ✨ Čo dokáže

- **Jedno prihlásenie — session zostáva.** Otvorí sa skutočný (nie headless) Chromium, prihlásite sa do arena.ai ako obvykle; aplikácia prihlásenie rozpozná, uloží session a sama zavrie prehliadač.
- **N chatov naraz.** Zadáte číslo 1–100 — otvorí sa presne toľko panelov `arena.ai/agent` a rovnako panelov `lm.ikale.io`.
- **Kopíruje za vás.** Prompt každého vzoru ide agentovi, odpoveď sa počká celá a vloží sa do poľa Reply — tri vzory na chat.
- **Určí model.** Klikne Verify na webe s odtlačkami, prečíta najlepšieho kandidáta a istotu presne tak, ako ich web zobrazuje, a premenuje chat na `model istota` (napr. `gpt-6-luna 99.9%`).
- **Dva režimy behu.** Jednovláknový (bezpečný, chaty po sebe) a viacvláknový (všetky chaty paralelne, 1.5–2× rýchlejšie).
- **Rozhranie v troch jazykoch.** English, Русский, 中文 — prepína sa v aplikácii, bez reštartu.

## 🔄 Ako beh prebieha

1. **Prihlásenie** — otvorí sa prehliadač, prihlásite sa, aplikácia to zistí a zavrie okno.
2. **Štart → počet chatov** — napríklad `3`: tri panely Arena a tri panely s odtlačkami.
3. **Vzory 1 → 3** — každý prompt letí agentovi, každá odpoveď sa vracia na web.
4. **Verify** — web zoradí kandidátske modely, aplikácia prečíta víťaza a istotu.
5. **Premenovanie** — chat v Arena dostane meno `model istota`, v konzole sa objaví súhrn.

## 📋 Požiadavky

- Python **3.10+**
- Windows 10/11, macOS alebo Linux
- Účet arena.ai (e-mail a heslo alebo odkaz z mailu)
- ~400 MB voľného miesta pre Chromium v Playwright

## 🚀 Inštalácia

```bash
git clone <this-repo> arena-model-hunter
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** potom stačí dvojklik na `run.bat` (zapína UTF-8, aby sa cyrilika zobrazovala správne).
**macOS / Linux:** `./run.sh` alebo `python main.py`.

## 🕹️ Použitie

```bash
python main.py
```

| Voľba | Popis |
|---|---|
| **Štart** | opýta sa, koľko chatov spustiť (1–100, pri neobmedzených ľubovoľné číslo), a spustí celý priebeh |
| **Nastavenia** | režim behu, jazyk rozhrania, odstránenie aktívneho účtu arena.ai |
| **Koniec** | zatvorí aplikáciu (terminál sa vráti k predchádzajúcemu obsahu) |

Menu sa prispôsobuje stavu: kým nie je účet pripojený, zobrazuje sa **Prihlásiť** a kurzor na ňom stojí; po úspešnom prihlásení položka zmizne.

## ⚙️ Nastavenia

| Voľba | Popis |
|---|---|
| **Režim behu** | `jednovláknový` (predvolený) / `viacvláknový` — viacvláknový je rýchlejší, ale posiela paralelné požiadavky |
| **Jazyk** | `English` / `Русский` / `中文` — prejaví sa hneď a pamätá sa |
| **Neobmedzený počet chatov** ⚠️ | ruší limit 100 chatov: `Start` prijme ľubovoľné číslo — nebezpečné, predvolene vypnuté |
| **Odstrániť aktívny účet arena.ai** | zmaže profil prehliadača aj session, teda odhlási |

Nastavenia sa ukladajú do `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Neobmedzený počet chatov je predvolene vypnutý a varovanie nie je ozdoba.** Po zapnutí `Start` nekontroluje rozsah 1–100, ale prijme ľubovoľné číslo — `250`, `1000`. Každý chat sú dve karty, takže veľké čísla znamenajú príval paralelných požiadaviek na arena.ai: presne to, pred čím majú chrániť limity rýchlosti a captcha, s reálnym rizikom obmedzenia účtu. Zapínajte len ak to prijímate, a zostaňte v jednovláknovom režime; nad 100 program najprv žiada druhé potvrdenie s presným počtom.

## 🔐 Ako funguje prihlásenie

1. Otvorí sa **skutočné** okno Chromium s trvalým profilom (`~/.arena-model-hunter/profile`) — Cloudflare odmieta headless prehliadače, preto ich program nikdy nepoužíva.
2. Kliknete `Log In` → zadáte e-mail → `Continue with email`.
   - Účet už existuje → zadajte heslo → `Log In`.
   - Nový e-mail → krok s menom možno preskočiť → príde odkaz e-mailom → vložte ho do adresného riadka (`Ctrl+L`, `Ctrl+V`, Enter) → vytvorte heslo.
3. Program kontroluje stránku každých 1,5 s a úspech rozpozná podľa troch znakov: e-mail sa objaví v bočnom paneli, vznikne cookie `arena-auth-*`, tlačidlo `Log In` zmizne.
4. Potom uloží `session.json` + `state.json` a **zatvorí prehliadač**.

Stránka sa vždy otvára v **tmavej téme** (prehliadač sa spúšťa s `prefers-color-scheme: dark` a arena.ai to rešpektuje).

## ⚡ Jednovláknový a viacvláknový režim

| Režim | Ako funguje | Merané na 3 chatoch |
|---|---|---|
| **Jednovláknový** (predvolený) | dvojice panelov sa spracúvajú po sebe, aktívny panel ide dopredu | ≈7,5 min |
| **Viacvláknový** | všetky dvojice panelov bežia súčasne, fokus sa neprepína | ≈4,5 min |

Vo viacvláknovom režime dostáva Arena niekoľko požiadaviek naraz, takže limity a captcha sú pravdepodobnejšie. Ak sa začnú, vráťte sa k jednovláknovému režimu.

## 🗂️ Štruktúra projektu

```
arena-model-hunter/
├── main.py             # menu, nastavenia, scenáre
├── ui.py               # terminálové rozhranie: rám, alt-screen, čítanie klávesov, zmena veľkosti
├── arena_login.py      # prehliadač, prihlásenie, rozpoznanie relácie, konfigurácia
├── flow.py             # tok Arena ↔ lm.ikale.io, Verify, premenovanie
├── i18n.py             # preklady rozhrania (en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI: lint a kontrola prekladov
├── LICENSE
└── docs/i18n/          # tento README v 30 jazykoch
```

## 🌍 Premenné prostredia

| Premenná | Predvolené | Na čo slúži |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | priečinok profilu a relácie |
| `ARENA_HELPER_HOME` | — | starý názov premennej, stále funguje |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | voliteľné vyplnenie formulára (nikdy sa neukladá) |
| `ARENA_LOGIN_TIMEOUT` | `900` | koľko sekúnd čakať na prihlásenie |
| `ARENA_URL` | `https://arena.ai/` | počiatočná URL |

## 🧰 Časté otázky

- **„Just a moment…“ / overenie Cloudflare** — treba viditeľné okno prehliadača; nespúšťajte na serveri bez plochy.
- **„Prehliadač nie je nainštalovaný“** — spustite `python -m playwright install chromium`.
- **Captcha alebo požiadavky sa ticho neodosielajú** — pravdepodobne limit: zapnite jednovláknový režim a spomaľte.
- **Chcem začať odznova** — Nastavenia → *Odstrániť aktívny účet arena.ai* alebo zmažte `~/.arena-model-hunter`.
- **Lov po celú noc** — Nastavenia → *Neobmedzený počet chatov*, zadajte `300` v Spustiť a potvrďte; zostaňte v jednovláknovom režime a ráno si pozrite premenované chaty.

## ⚠️ Upozornenie

Projekt vznikol pre **vlastné experimenty a vzdelávanie**. Automatizuje cudzí web; automatizácia môže porušovať podmienky používania arena.ai aj webu s odtlačkami a viesť k obmedzeniu účtu. Používajte na vlastné riziko, nevytvárajte zbytočnú záťaž, v prípade pochybností držte jednovláknový režim a nikdy nezverejňujte svoje údaje — aplikácia heslo neukladá na disk.

## 📄 Licencia

[GNU General Public License v3.0](LICENSE) — slobodný softvér: môžete ho používať, študovať, šíriť a meniť. Ak šírite program alebo upravenú verziu, musí zostať pod GPL a zdrojový kód musí zostať otvorený. Bez záruky.

Copyright (C) 2026 prispievatelia arena model hunter.

