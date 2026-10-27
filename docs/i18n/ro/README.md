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
git clone https://github.com/LeistDev/arena-model-hunter.git
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

## 🔐 Cum funcționează autentificarea

1. Se deschide o fereastră Chromium **reală** cu profil persistent (`~/.arena-model-hunter/profile`) — Cloudflare respinge browserele headless, așa că aplicația nu folosește niciodată unul.
2. Apeși `Log In` → introduci emailul → `Continue with email`.
   - Cont existent → introdu parola → `Log In`.
   - Email nou → pasul cu numele poate fi sărit → primești un link pe email → lipește-l în bara de adrese (`Ctrl+L`, `Ctrl+V`, Enter) → creează o parolă.
3. Aplicația verifică pagina la fiecare 1,5 s și detectează succesul după trei semne: emailul apare în bara laterală, apare cookie-ul `arena-auth-*`, butonul `Log In` dispare.
4. Apoi salvează `session.json` + `state.json` și **închide browserul**.

Site-ul se deschide mereu în **temă întunecată** (browserul pornește cu `prefers-color-scheme: dark`, iar arena.ai respectă asta).

## ⚡ Modul cu un fir și cu mai multe fire

| Mod | Cum funcționează | Măsurat pe 3 conversații |
|---|---|---|
| **Un singur fir** (implicit) | perechile de file sunt procesate pe rând, fila activă este adusă în față | ≈7,5 min |
| **Mai multe fire** | toate perechile de file rulează simultan, focusul nu este mutat | ≈4,5 min |

În modul cu mai multe fire, Arena primește mai multe cereri deodată, deci limitele și captcha sunt mai probabile. Dacă apar, revino la modul cu un singur fir.

## 🗂️ Structura proiectului

```
arena-model-hunter/
├── main.py             # meniu, setări, scenarii
├── ui.py               # interfață de terminal: cadru, alt-screen, citirea tastelor, redimensionare
├── arena_login.py      # browser, autentificare, detectarea sesiunii, configurare
├── flow.py             # flux Arena ↔ lm.ikale.io, Verify, redenumire
├── i18n.py             # traduceri ale interfeței (en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI: lint și verificarea traducerilor
├── LICENSE
└── docs/i18n/          # acest README în 30 de limbi
```

## 🌍 Variabile de mediu

| Variabilă | Implicit | Rol |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | folderul profilului și al sesiunii |
| `ARENA_HELPER_HOME` | — | numele vechi al variabilei, încă acceptat |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | completare opțională a formularului (nu se salvează niciodată) |
| `ARENA_LOGIN_TIMEOUT` | `900` | secunde de așteptare pentru autentificare |
| `ARENA_URL` | `https://arena.ai/` | URL de pornire |

## 🧰 Întrebări frecvente

- **„Just a moment…” / verificare Cloudflare** — este nevoie de o fereastră vizibilă; nu rula pe un server fără desktop.
- **„Browserul nu este instalat”** — rulează `python -m playwright install chromium`.
- **Captcha sau cereri ignorate în tăcere** — probabil ai atins o limită: activează modul cu un singur fir și încetinește.
- **Vreau să încep de la zero** — Setări → *Șterge contul arena.ai activ* sau șterge `~/.arena-model-hunter`.
- **Vânătoare toată noaptea** — Setări → *Chat-uri nelimitate*, apoi scrie `300` la Start și confirmă; rămâi pe un singur fir și dimineața uită-te la chat-urile redenumite.

## ⚠️ Avertisment

Proiectul este pentru **experimente personale și învățare**. Automatizează un site terț; automatizarea poate încălca termenii arena.ai și ai site-ului cu amprente și poate duce la restricții de cont. Folosește pe propriul risc, nu genera suprasolicitare, în caz de dubiu păstrează modul cu un singur fir și nu publica niciodată datele tale — aplicația nu salvează parola pe disc.

## 📄 Licență

[MIT](LICENSE) — software liber: poate fi folosit, studiat, distribuit și modificat. Dacă distribui programul sau o versiune modificată, trebuie să păstrezi nota de copyright și textul licenței MIT. Nu există garanții.

Copyright (C) 2026 contribuitorii arena model hunter.

