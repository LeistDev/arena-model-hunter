<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | **🇲🇾 Bahasa Melayu** | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Pemburu model untuk arena.ai: menjalankan sekumpulan chat mod agent, mengambil cap jari setiap jawapan, mengetahui model mana yang menjawab, lalu menamakan semula chat mengikutnya — paginya anda ada chat berlabel yang dikuasakan Claude Opus, GPT-5, Gemini atau model yang anda cari.**

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

## 🎯 Mengapa alat ini wujud

Dalam mod agent, arena.ai sendiri menentukan model mana yang menjawab — dan ia bukan selalu model yang anda mahu: kadang-kadang model teratas (Claude Opus dan yang setara), kadang-kadang jauh lebih lemah. Alat ini menukar cabutan bertuah itu menjadi pencarian: ia membuka sekumpulan chat mod agent, memainkan ketiga-tiga sampel cap jari dalam setiap chat, bertanya kepada laman cap jari model mana yang menjawab, lalu menulis keputusan itu ke dalam tajuk chat (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Biarkan ia berjalan sepanjang malam dengan berapa banyak chat pun; paginya sudah ada senarai berlabel: buka chat yang tajuknya menyebut model yang anda perlukan dan teruskan kerja di situ. Itulah maksudnya — bukan automasi semata-mata, tetapi mendapatkan chat yang benar-benar berjalan pada model yang anda mahukan.

## ✨ Apa yang dilakukannya

- **Sekali log masuk — sesi kekal.** Chromium sebenar (bukan headless) dibuka, anda log masuk ke arena.ai seperti biasa; aplikasi mengesannya, menyimpan sesi dan menutup pelayar sendiri.
- **N perbualan serentak.** Anda masukkan nombor 1–100 — tab `arena.ai/agent` dibuka tepat sebanyak itu, dan tab `lm.ikale.io` sama banyak.
- **Menyalin untuk anda.** Prompt setiap sampel dihantar kepada agen, jawapan ditunggu sepenuhnya dan ditampal ke medan Reply — tiga sampel setiap perbualan.
- **Mengenal pasti model.** Menekan Verify di laman cap jari, membaca calon teratas dan keyakinan tepat seperti yang dipaparkan laman, lalu menamakan semula perbualan Arena kepada `model keyakinan` (contohnya `gpt-6-luna 99.9%`).
- **Dua mod larian.** Satu-utas (selamat, perbualan bergilir) dan berbilang-utas (semua perbualan selari, 1.5–2× lebih pantas).
- **Antara muka tiga bahasa.** English, Русский, 中文 — boleh ditukar dalam aplikasi tanpa mula semula.

## 🔄 Bagaimana satu larian berjalan

1. **Log masuk** — pelayar dibuka, anda mengesahkan identiti, aplikasi mengesannya dan menutup tetingkap.
2. **Mula → bilangan perbualan** — contohnya `3`: tiga tab Arena dan tiga tab cap jari.
3. **Sampel 1 → 3** — setiap prompt dihantar kepada agen, setiap jawapan dikembalikan ke laman.
4. **Verify** — laman menyusun model calon, aplikasi membaca pemenang dan keyakinan.
5. **Nama semula** — perbualan Arena menjadi `model keyakinan`, dan ringkasan muncul di konsol.

## 📋 Keperluan

- Python **3.10+**
- Windows 10/11, macOS atau Linux
- Akaun arena.ai (e-mel dan kata laluan atau pautan melalui e-mel)
- ~400 MB ruang kosong untuk Chromium Playwright

## 🚀 Pemasangan

```bash
git clone https://github.com/LeistDev/arena-model-hunter.git
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** selepas itu cukup klik dua kali `run.bat` (mengaktifkan UTF-8 supaya huruf Cyrillic dipaparkan betul).
**macOS / Linux:** `./run.sh` atau `python main.py`.

## 🕹️ Penggunaan

```bash
python main.py
```

| Pilihan | Keterangan |
|---|---|
| **Mula** | bertanya berapa banyak chat untuk dijalankan (1–100, atau sebarang nombor dengan chat tanpa had) lalu memulakan keseluruhan proses |
| **Tetapan** | mod larian, bahasa antara muka, buang akaun arena.ai yang aktif |
| **Keluar** | menutup aplikasi (terminal kembali kepada kandungan sebelumnya) |

Menu menyesuaikan keadaan: selagi tiada akaun disambungkan, item **Log masuk** dipaparkan dan kursor berada di situ; selepas berjaya log masuk item itu hilang.

## ⚙️ Tetapan

| Pilihan | Keterangan |
|---|---|
| **Mod larian** | `satu-utas` (lalai) / `berbilang-utas` — berbilang-utas lebih pantas tetapi menghantar permintaan selari |
| **Bahasa** | `English` / `Русский` / `中文` — berkuat kuasa serta-merta dan diingati |
| **Chat tanpa had** ⚠️ | membuang had 100 chat: `Start` menerima sebarang nombor — berbahaya, mati secara lalai |
| **Buang akaun arena.ai aktif** | memadam profil pelayar dan sesi, iaitu log keluar |

Tetapan disimpan dalam `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Chat tanpa had mati secara lalai, dan amaran ini bukan hiasan.** Apabila dihidupkan, `Start` tidak lagi menyemak julat 1–100 tetapi menerima sebarang nombor — `250`, `1000`. Setiap chat ialah dua tab, jadi nombor besar bermaksud hujan permintaan selari ke arena.ai: itulah corak yang menjadi sebab had kadar dan captcha wujud, dengan risiko sebenar akaun dihadkan. Hidupkan hanya jika anda menerimanya, dan kekalkan mod satu benang; apa-apa melebihi 100 meminta pengesahan kedua dengan jumlah tepat sebelum apa pun dibuka.

## 🔐 Cara log masuk berfungsi

1. Tetingkap Chromium **sebenar** dibuka dengan profil kekal (`~/.arena-model-hunter/profile`) — Cloudflare menolak pelayar headless, jadi aplikasi tidak pernah menggunakannya.
2. Anda klik `Log In` → masukkan e-mel → `Continue with email`.
   - Akaun sudah ada → masukkan kata laluan → `Log In`.
   - E-mel baharu → langkah nama boleh dilangkau → pautan dihantar melalui e-mel → tampal dalam bar alamat (`Ctrl+L`, `Ctrl+V`, Enter) → cipta kata laluan.
3. Aplikasi menyemak halaman setiap 1.5 saat dan mengenal pasti kejayaan melalui tiga tanda: e-mel anda muncul di bar sisi, kuki `arena-auth-*` terbentuk, dan butang `Log In` hilang.
4. Kemudian ia menyimpan `session.json` + `state.json` dan **menutup pelayar**.

Laman sentiasa dibuka dalam **tema gelap** (pelayar dimulakan dengan `prefers-color-scheme: dark`, dan arena.ai mengikutinya).

## ⚡ Mod satu-utas dan berbilang-utas

| Mod | Cara ia berfungsi | Diukur pada 3 perbualan |
|---|---|---|
| **Satu-utas** (lalai) | pasangan tab diproses satu demi satu, tab aktif dibawa ke hadapan | ≈7.5 minit |
| **Berbilang-utas** | semua pasangan tab berjalan serentak, fokus tidak dialihkan | ≈4.5 minit |

Dalam mod berbilang-utas, Arena menerima beberapa permintaan serentak, jadi had kadar dan captcha lebih mungkin. Jika berlaku, kembali ke mod satu-utas.

## 🗂️ Struktur projek

```
arena-model-hunter/
├── main.py             # menu, tetapan, senario
├── ui.py               # antara muka terminal: bingkai, alt-screen, bacaan kekunci, saiz semula
├── arena_login.py      # pelayar, log masuk, pengesanan sesi, konfigurasi
├── flow.py             # saluran Arena ↔ lm.ikale.io, Verify, penamaan semula
├── i18n.py             # terjemahan antara muka (en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI: lint dan pemeriksaan terjemahan
├── LICENSE
└── docs/i18n/          # README ini dalam 30 bahasa
```

## 🌍 Pemboleh ubah persekitaran

| Pemboleh ubah | Lalai | Kegunaan |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | folder profil dan sesi |
| `ARENA_HELPER_HOME` | — | nama lama pemboleh ubah, masih disokong |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | isi borang automatik (tidak pernah disimpan) |
| `ARENA_LOGIN_TIMEOUT` | `900` | saat menunggu log masuk |
| `ARENA_URL` | `https://arena.ai/` | URL permulaan |

## 🧰 Soalan lazim

- **«Just a moment…» / pengesahan Cloudflare** — perlu tetingkap pelayar yang kelihatan; jangan jalankan pada pelayan tanpa desktop.
- **«Pelayar belum dipasang»** — jalankan `python -m playwright install chromium`.
- **Captcha atau permintaan tidak dihantar** — mungkin terkena had: aktifkan satu-utas dan perlahan.
- **Mahu mula dari awal** — Tetapan → *Buang akaun arena.ai aktif*, atau padam `~/.arena-model-hunter`.
- **Memburu sepanjang malam** — Tetapan → *Chat tanpa had*, kemudian taip `300` di Mula dan sahkan; kekalkan mod satu benang dan lihat chat yang dinamakan semula pada waktu pagi.

## ⚠️ Penafian

Projek ini untuk **eksperimen peribadi dan pembelajaran**. Ia mengautomasikan laman pihak ketiga; automasi boleh melanggar terma perkhidmatan arena.ai dan laman cap jari serta menyebabkan sekatan akaun. Guna atas risiko sendiri, jangan bebankan berlebihan, jika ragu kekal dalam mod satu-utas, dan jangan sekali-kali menerbitkan data anda — aplikasi tidak menyimpan kata laluan pada cakera.

## 📄 Lesen

[GNU General Public License v3.0](LICENSE) — perisian bebas: boleh digunakan, dikaji, dikongsi dan diubah. Jika anda mengedarkan program atau versi yang diubah, ia mesti kekal di bawah GPL dan kod sumber mesti kekal terbuka. Tiada jaminan.

Copyright (C) 2026 penyumbang arena model hunter.

