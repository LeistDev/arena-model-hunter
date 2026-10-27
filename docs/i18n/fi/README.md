<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | **🇫🇮 Suomi** | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Mallien metsästäjä arena.ai:lle: ajaa kasan agentti-keskusteluja, ottaa jokaisesta vastauksesta sormenjäljen, selvittää mikä malli vastasi ja nimeää keskustelun sen mukaan — aamulla sinulla on merkitty keskustelu, jota pyörittää Claude Opus, GPT-5, Gemini tai se malli, jota metsästät.**

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

## 🎯 Miksi tämä on olemassa

Agentin tilassa arena.ai päättää itse, mikä malli vastaa — eikä se ole aina se, jonka haluat: välillä kärkimalli (Claude Opus ja kumppanit), välillä selvästi heikompi. Tämä työkalu muuttaa arpajaiset hakemiseksi: se avaa kasan agentti-keskusteluja, toistaa kolme sormenjälkinäytettä jokaisessa, kysyy sormenjälkisivustolta mikä malli vastasi ja kirjoittaa tuloksen keskustelun nimeen (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Jätä se pyörimään yön yli niin monella keskustelulla kuin haluat; aamulla edessäsi on merkitty lista: avaa keskustelu, jonka nimessä on tarvitsemasi malli, ja jatka siinä. Juuri siitä on kyse — ei automaatiota automaation vuoksi, vaan keskustelu, joka oikeasti pyörii halutulla mallilla.

## ✨ Mitä se tekee

- **Kirjaudu kerran — istunto säilyy.** Avataan oikea (ei headless) Chromium, kirjaudut arena.ai-palveluun kuten tavallisesti; sovellus huomaa sen, tallentaa istunnon ja sulkee selaimen itse.
- **N keskustelua kerralla.** Syötät luvun 1–100 — avautuu täsmälleen niin monta `arena.ai/agent`-välilehteä ja yhtä monta `lm.ikale.io`-välilehteä.
- **Kopioi puolestasi.** Jokaisen näytteen kehote lähetetään agentille, vastaus odotetaan kokonaan ja liitetään Reply-kenttään — kolme näytettä per keskustelu.
- **Tunnistaa mallin.** Painaa Verify sormenjälkisivustolla, lukee parhaan ehdokkaan ja varmuuden täsmälleen kuten sivusto ne näyttää ja nimeää Arena-keskustelun muotoon `malli varmuus` (esimerkiksi `gpt-6-luna 99.9%`).
- **Kaksi ajotilaa.** Yksisäikeinen (turvallinen, keskustelut peräkkäin) ja monisäikeinen (kaikki keskustelut rinnakkain, 1,5–2× nopeampi).
- **Käyttöliittymä kolmella kielellä.** English, Русский, 中文 — vaihdettavissa sovelluksessa ilman uudelleenkäynnistystä.

## 🔄 Miten ajo etenee

1. **Kirjautuminen** — selain avautuu, kirjaudut sisään, sovellus huomaa sen ja sulkee ikkunan.
2. **Aloita → keskustelujen määrä** — esimerkiksi `3`: kolme Arena-välilehteä ja kolme sormenjälkivälilehteä.
3. **Näytteet 1 → 3** — jokainen kehote menee agentille, jokainen vastaus palaa sivustolle.
4. **Verify** — sivusto järjestää ehdokasmallit, sovellus lukee voittajan ja varmuuden.
5. **Uudelleennimeäminen** — Arena-keskustelu saa nimen `malli varmuus` ja konsoliin tulostuu yhteenveto.

## 📋 Vaatimukset

- Python **3.10+**
- Windows 10/11, macOS tai Linux
- arena.ai-tili (sähköposti ja salasana tai sähköpostilinkki)
- ~400 MB vapaata levytilaa Playwrightin Chromiumille

## 🚀 Asennus

```bash
git clone https://github.com/LeistDev/arena-model-hunter.git
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** sen jälkeen riittää kaksoisklikkaus `run.bat`-tiedostoon (kytkee UTF-8:n, jotta kyrilliset merkit näkyvät oikein).
**macOS / Linux:** `./run.sh` tai `python main.py`.

## 🕹️ Käyttö

```bash
python main.py
```

| Asetus | Kuvaus |
|---|---|
| **Aloita** | kysyy, montako keskustelua ajetaan (1–100 tai rajattomilla keskusteluilla mikä tahansa luku) ja käynnistää koko ketjun |
| **Asetukset** | ajotila, käyttöliittymän kieli, aktiivisen arena.ai-tilin poisto |
| **Lopeta** | sulkee sovelluksen (pääte palaa aiempaan sisältöönsä) |

Valikko mukautuu tilaan: kun tiliä ei ole yhdistetty, näkyy **Kirjaudu sisään** ja kohdistin on siinä; onnistuneen kirjautumisen jälkeen kohta katoaa.

## ⚙️ Asetukset

| Asetus | Kuvaus |
|---|---|
| **Ajotila** | `yksisäikeinen` (oletus) / `monisäikeinen` — monisäikeinen on nopeampi mutta lähettää rinnakkaisia pyyntöjä |
| **Kieli** | `English` / `Русский` / `中文` — astuu voimaan heti ja muistetaan |
| **Rajattomasti keskusteluja** ⚠️ | poistaa 100 keskustelun rajan: `Start` hyväksyy minkä tahansa luvun — vaarallinen, oletuksena pois |
| **Poista aktiivinen arena.ai-tili** | tyhjentää selainprofiilin ja istunnon eli kirjaa ulos |

Asetukset ovat tiedostossa `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Rajattomat keskustelut ovat oletuksena pois, eikä varoitus ole koriste.** Päällä ollessaan `Start` ei enää tarkista väliä 1–100 vaan hyväksyy minkä tahansa luvun — `250`, `1000`. Jokainen keskustelu on kaksi välilehteä, joten suuret luvut tarkoittavat ryöppyä rinnakkaisia pyyntöjä arena.ai:lle: juuri sitä varten nopeusrajat ja captchat ovat, ja tilin rajoitus on todellinen riski. Kytke se päälle vain jos hyväksyt tämän, ja pysy yhden säikeen tilassa; yli 100 vaatii toisen vahvistuksen tarkalla luvulla ennen kuin mitään avautuu.

## 🔐 Miten kirjautuminen toimii

1. Avautuu **oikea** Chromium-ikkuna, jossa on pysyvä profiili (`~/.arena-model-hunter/profile`) — Cloudflare hylkää headless-selaimet, joten sovellus ei koskaan käytä sellaista.
2. Klikkaat `Log In` → syötät sähköpostin → `Continue with email`.
   - Tili on jo olemassa → syötä salasana → `Log In`.
   - Uusi sähköposti → nimivaiheen voi ohittaa → sähköpostiin tulee linkki → liitä se osoiteriville (`Ctrl+L`, `Ctrl+V`, Enter) → luo salasana.
3. Sovellus kysyy sivua 1,5 sekunnin välein ja tunnistaa onnistumisen kolmesta merkistä: sähköpostisi ilmestyy sivupalkkiin, `arena-auth-*`-eväste syntyy ja `Log In` -painike katoaa.
4. Sen jälkeen se tallentaa `session.json` + `state.json` ja **sulkee selaimen**.

Sivusto avautuu aina **tummaan teemaan** (selain käynnistetään asetuksella `prefers-color-scheme: dark`, ja arena.ai noudattaa sitä).

## ⚡ Yksisäikeinen ja monisäikeinen tila

| Tila | Miten toimii | Mitattu 3 keskustelulla |
|---|---|---|
| **Yksisäikeinen** (oletus) | välilehtiparit käsitellään peräkkäin, aktiivinen välilehti tuodaan eteen | ≈7,5 min |
| **Monisäikeinen** | kaikki välilehtiparit ajetaan yhtä aikaa, kohdistusta ei siirretä | ≈4,5 min |

Monisäikeisessä tilassa Arena saa useita pyyntöjä kerralla, joten rajat ja captcha ovat todennäköisempiä. Jos niin käy, palaa yksisäikeiseen tilaan.

## 🗂️ Projektin rakenne

```
arena-model-hunter/
├── main.py             # valikko, asetukset, skenaariot
├── ui.py               # pääte-UX: kehys, alt-screen, näppäinten luku, koon muutos
├── arena_login.py      # selain, kirjautuminen, istunnon tunnistus, asetukset
├── flow.py             # Arena ↔ lm.ikale.io -putki, Verify, uudelleennimeäminen
├── i18n.py             # käyttöliittymän käännökset (en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI: lint ja käännösten tarkistus
├── LICENSE
└── docs/i18n/          # tämä README 30 kielellä
```

## 🌍 Ympäristömuuttujat

| Muuttuja | Oletus | Mihin |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | profiilin ja istunnon kansio |
| `ARENA_HELPER_HOME` | — | muuttujan vanha nimi, toimii edelleen |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | valinnainen lomakkeen automaattitäyttö (ei koskaan tallenneta) |
| `ARENA_LOGIN_TIMEOUT` | `900` | kuinka monta sekuntia kirjautumista odotetaan |
| `ARENA_URL` | `https://arena.ai/` | aloitus-URL |

## 🧰 Usein kysytyt kysymykset

- **”Just a moment…” / Cloudflare-tarkistus** — tarvitaan näkyvä selainikkuna; älä aja palvelimella ilman työpöytää.
- **”Selainta ei ole asennettu”** — suorita `python -m playwright install chromium`.
- **Captcha tai pyynnöt eivät lähde hiljaa** — todennäköisesti raja: kytke yksisäikeinen tila ja hidasta tahtia.
- **Haluan aloittaa alusta** — Asetukset → *Poista aktiivinen arena.ai-tili* tai poista `~/.arena-model-hunter`.
- **Metsästys läpi yön** — Asetukset → *Rajattomasti keskusteluja*, kirjoita `300` kohtaan Aloita ja vahvista; pidä yhden säikeen tila ja katso uudelleennimettyjä keskusteluja aamulla.

## ⚠️ Vastuuvapauslauseke

Projekti on tehty **henkilökohtaiseen kokeiluun ja oppimiseen**. Se automatisoi kolmannen osapuolen sivustoa; automaatio voi rikkoa arena.ai:n ja sormenjälkisivuston käyttöehtoja ja johtaa tilin rajoituksiin. Käytä omalla vastuulla, älä aiheuta tarpeetonta kuormitusta, pidä yksisäikeinen tila jos epäilyttää, äläkä koskaan julkaise tietojasi — sovellus ei tallenna salasanaa levylle.

## 📄 Lisenssi

[MIT](LICENSE) — vapaa ohjelmisto: voit käyttää, tutkia, jakaa ja muokata sitä. Jos jaat ohjelman tai muokatun version, sen on pysyttävä GPL:n alaisena ja lähdekoodin avoimena. Takuuta ei ole.

Copyright (C) 2026 arena model hunterin tekijät.

