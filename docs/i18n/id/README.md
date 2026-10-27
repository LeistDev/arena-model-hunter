<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | **🇮🇩 Bahasa Indonesia** | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Pemburu model untuk arena.ai: menjalankan sejumlah chat mode agent, mengambil sidik jari tiap jawaban, mengetahui model mana yang menjawab, lalu mengganti nama chat sesuai model itu — paginya Anda punya chat berlabel yang ditenagai Claude Opus, GPT-5, Gemini, atau model yang sedang Anda cari.**

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

## 🎯 Mengapa alat ini ada

Di mode agent, arena.ai sendiri yang menentukan model mana yang menjawab — dan itu tidak selalu model yang Anda mau: kadang model papan atas (Claude Opus dan sejenisnya), kadang jauh lebih lemah. Alat ini mengubah undian itu menjadi pencarian: membuka sejumlah chat mode agent, memutar tiga sampel sidik jari di setiap chat, menanyakan ke situs sidik jari model mana yang menjawab, lalu menulis putusannya ke judul chat (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Biarkan berjalan semalaman dengan jumlah chat sesuka Anda; paginya sudah ada daftar berlabel: buka chat yang judulnya menyebut model yang Anda butuhkan dan lanjutkan bekerja di sana. Itulah intinya — bukan otomatisasi demi otomatisasi, melainkan mendapatkan chat yang benar-benar berjalan di model yang Anda inginkan.

## ✨ Yang bisa dilakukannya

- **Sekali masuk — sesi tersimpan.** Chromium asli (bukan headless) terbuka, Anda masuk ke arena.ai seperti biasa; aplikasi mendeteksinya, menyimpan sesi, lalu menutup browser sendiri.
- **N obrolan sekaligus.** Anda memasukkan angka 1–100 — tab `arena.ai/agent` terbuka tepat sebanyak itu, dan tab `lm.ikale.io` sama banyaknya.
- **Menyalin untuk Anda.** Prompt setiap sampel dikirim ke agen, jawaban ditunggu sampai selesai lalu ditempel ke kolom Reply — tiga sampel per obrolan.
- **Mengenali model.** Menekan Verify di situs sidik jari, membaca kandidat teratas dan tingkat keyakinan persis seperti yang ditampilkan situs, lalu mengganti nama obrolan Arena menjadi `model keyakinan` (misalnya `gpt-6-luna 99.9%`).
- **Dua mode jalan.** Satu-thread (aman, obrolan bergiliran) dan multi-thread (semua obrolan paralel, 1,5–2× lebih cepat).
- **Antarmuka tiga bahasa.** English, Русский, 中文 — bisa diganti di dalam aplikasi, tanpa restart.

## 🔄 Bagaimana satu proses berjalan

1. **Masuk** — browser terbuka, Anda mengautentikasi, aplikasi mendeteksi dan menutup jendelanya.
2. **Mulai → jumlah obrolan** — misalnya `3`: tiga tab Arena dan tiga tab sidik jari.
3. **Sampel 1 → 3** — setiap prompt dikirim ke agen, setiap jawaban dikembalikan ke situs.
4. **Verify** — situs memberi peringkat model kandidat, aplikasi membaca pemenang dan keyakinannya.
5. **Ganti nama** — obrolan Arena menjadi `model keyakinan`, dan ringkasan muncul di konsol.

## 📋 Kebutuhan

- Python **3.10+**
- Windows 10/11, macOS, atau Linux
- Akun arena.ai (email dan kata sandi atau tautan lewat email)
- ~400 MB ruang kosong untuk Chromium dari Playwright

## 🚀 Instalasi

```bash
git clone https://github.com/LeistDev/arena-model-hunter.git
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** setelah itu cukup klik dua kali `run.bat` (mengaktifkan UTF-8 agar huruf Kiril tampil benar).
**macOS / Linux:** `./run.sh` atau `python main.py`.

## 🕹️ Penggunaan

```bash
python main.py
```

| Opsi | Keterangan |
|---|---|
| **Mulai** | menanyakan berapa chat yang akan dijalankan (1–100, atau angka apa pun dengan chat tanpa batas) lalu menjalankan seluruh proses |
| **Pengaturan** | mode jalan, bahasa antarmuka, hapus akun arena.ai yang aktif |
| **Keluar** | menutup aplikasi (terminal kembali ke isi sebelumnya) |

Menu menyesuaikan keadaan: selama belum ada akun terhubung, item **Masuk** ditampilkan dan kursor berada di sana; setelah berhasil masuk, item itu hilang.

## ⚙️ Pengaturan

| Opsi | Keterangan |
|---|---|
| **Mode jalan** | `satu-thread` (bawaan) / `multi-thread` — multi-thread lebih cepat tetapi mengirim permintaan paralel |
| **Bahasa** | `English` / `Русский` / `中文` — langsung berlaku dan diingat |
| **Chat tanpa batas** ⚠️ | menghapus batas 100 chat: `Start` menerima angka berapa pun — berbahaya, mati secara bawaan |
| **Hapus akun arena.ai aktif** | menghapus profil browser dan sesi, artinya keluar dari akun |

Pengaturan disimpan di `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Chat tanpa batas mati secara bawaan, dan peringatannya bukan hiasan.** Saat dinyalakan, `Start` tidak lagi memeriksa rentang 1–100 melainkan menerima angka apa pun — `250`, `1000`. Satu chat berarti dua tab, jadi angka besar berarti hujan permintaan paralel ke arena.ai: persis pola yang menjadi alasan adanya batas laju dan captcha, dengan risiko nyata akun dibatasi. Nyalakan hanya jika Anda menerimanya, dan tetap di mode satu thread; angka di atas 100 meminta konfirmasi kedua dengan jumlah tepat sebelum apa pun terbuka.

## 🔐 Cara kerja masuk akun

1. Jendela Chromium **asli** terbuka dengan profil permanen (`~/.arena-model-hunter/profile`) — Cloudflare menolak browser headless, jadi aplikasi tidak pernah memakainya.
2. Anda klik `Log In` → masukkan email → `Continue with email`.
   - Akun sudah ada → masukkan kata sandi → `Log In`.
   - Email baru → langkah nama boleh dilewati → tautan dikirim lewat email → tempel di bilah alamat (`Ctrl+L`, `Ctrl+V`, Enter) → buat kata sandi.
3. Aplikasi memeriksa halaman setiap 1,5 detik dan mengenali keberhasilan dari tiga tanda: email Anda muncul di bilah samping, cookie `arena-auth-*` terbentuk, dan tombol `Log In` hilang.
4. Lalu aplikasi menyimpan `session.json` + `state.json` dan **menutup browser**.

Situs selalu terbuka dalam **tema gelap** (browser dijalankan dengan `prefers-color-scheme: dark`, dan arena.ai mengikutinya).

## ⚡ Mode satu-thread dan multi-thread

| Mode | Cara kerja | Diukur pada 3 obrolan |
|---|---|---|
| **Satu-thread** (bawaan) | pasangan tab diproses bergiliran, tab aktif dibawa ke depan | ≈7,5 menit |
| **Multi-thread** | semua pasangan tab berjalan bersamaan, fokus tidak dipindahkan | ≈4,5 menit |

Pada mode multi-thread, Arena menerima beberapa permintaan sekaligus, jadi batas laju dan captcha lebih mungkin muncul. Jika itu terjadi, kembalilah ke mode satu-thread.

## 🗂️ Struktur proyek

```
arena-model-hunter/
├── main.py             # menu, pengaturan, skenario
├── ui.py               # antarmuka terminal: bingkai, alt-screen, pembacaan tombol, ubah ukuran
├── arena_login.py      # browser, masuk akun, deteksi sesi, konfigurasi
├── flow.py             # alur Arena ↔ lm.ikale.io, Verify, ganti nama
├── i18n.py             # terjemahan antarmuka (en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI: lint dan pemeriksaan terjemahan
├── LICENSE
└── docs/i18n/          # README ini dalam 30 bahasa
```

## 🌍 Variabel lingkungan

| Variabel | Bawaan | Kegunaan |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | folder profil dan sesi |
| `ARENA_HELPER_HOME` | — | nama lama variabel ini, masih didukung |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | isi otomatis formulir (tidak pernah disimpan) |
| `ARENA_LOGIN_TIMEOUT` | `900` | detik menunggu proses masuk |
| `ARENA_URL` | `https://arena.ai/` | URL awal |

## 🧰 Pertanyaan umum

- **«Just a moment…» / verifikasi Cloudflare** — perlu jendela browser yang terlihat; jangan jalankan di server tanpa desktop.
- **«Browser belum terpasang»** — jalankan `python -m playwright install chromium`.
- **Captcha atau permintaan tidak terkirim** — kemungkinan terkena batas: aktifkan satu-thread dan perlambat.
- **Ingin mulai dari awal** — Pengaturan → *Hapus akun arena.ai aktif*, atau hapus `~/.arena-model-hunter`.
- **Berburu sepanjang malam** — Pengaturan → *Chat tanpa batas*, lalu ketik `300` di Mulai dan konfirmasi; tetap di mode satu thread dan paginya lihat chat yang sudah diganti nama.

## ⚠️ Penafian

Proyek ini dibuat untuk **eksperimen pribadi dan belajar**. Aplikasi mengotomatiskan situs pihak ketiga; otomatisasi dapat melanggar ketentuan layanan arena.ai dan situs sidik jari serta berujung pada pembatasan akun. Gunakan dengan risiko sendiri, jangan menimbulkan beban berlebih, bila ragu tetap gunakan satu-thread, dan jangan pernah mempublikasikan data Anda — aplikasi tidak menyimpan kata sandi ke disk.

## 📄 Lisensi

[GNU General Public License v3.0](LICENSE) — perangkat lunak bebas: boleh dipakai, dipelajari, dibagikan, dan diubah. Jika Anda menyebarkan program ini atau versi modifikasinya, program harus tetap di bawah GPL dan kode sumbernya tetap terbuka. Tidak ada jaminan.

Copyright (C) 2026 para kontributor arena model hunter.

