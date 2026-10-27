<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | **🇵🇱 Polski** | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Łowca modeli dla arena.ai: uruchamia partię czatów w trybie agent, pobiera odcisk każdej odpowiedzi, ustala, który model odpowiedział, i zmienia nazwę czatu na jego nazwę — rano masz oznaczony czat napędzany przez Claude Opus, GPT-5, Gemini albo model, na który polowałeś.**

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

## 🎯 Po co to jest

W trybie agent arena.ai sam decyduje, który model odpowiada — i wcale nie zawsze jest to ten, którego chcesz: czasem trafi się model z najwyższej półki (Claude Opus i spółka), czasem coś znacznie słabszego. To narzędzie zamienia loterię w poszukiwanie: otwiera partię czatów w trybie agent, w każdym odtwarza trzy próbki odcisku, pyta stronę odcisków, który model odpowiedział, i zapisuje werdykt w tytule czatu (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Zostaw je na noc z dowolną liczbą czatów; rano jest oznaczona lista: otwórz czat, w którego tytule widnieje potrzebny model, i pracuj w nim. O to właśnie chodzi — nie automatyzacja dla automatyzacji, lecz czat, który naprawdę działa na modelu, jakiego chciałeś.

## ✨ Co potrafi

- **Jedno logowanie — sesja zostaje.** Otwiera się prawdziwy (nie headless) Chromium, logujesz się do arena.ai jak zwykle; program zauważa logowanie, zapisuje sesję i sam zamyka przeglądarkę.
- **N czatów naraz.** Podajesz liczbę 1–100 — otwiera się dokładnie tyle kart `arena.ai/agent` i tyle samo kart `lm.ikale.io`.
- **Kopiuje za Ciebie.** Prompt każdej próbki trafia do agenta, odpowiedź jest czekana do końca i wklejana w pole Reply — trzy próbki na czat.
- **Rozpoznaje model.** Klika Verify na stronie z odciskami, odczytuje najlepszego kandydata i pewność dokładnie tak, jak pokazuje je strona, i zmienia nazwę czatu Arena na `model pewność` (np. `gpt-6-luna 99.9%`).
- **Dwa tryby pracy.** Jednowątkowy (bezpieczny, czaty po kolei) i wielowątkowy (wszystkie czaty równolegle, 1.5–2× szybciej).
- **Interfejs w trzech językach.** English, Русский, 中文 — przełączany w programie, bez restartu.

## 🔄 Jak wygląda przebieg

1. **Logowanie** — otwiera się przeglądarka, logujesz się, program to zauważa i zamyka okno.
2. **Start → liczba czatów** — np. `3`: trzy karty Arena i trzy karty z odciskami.
3. **Próbki 1 → 3** — każdy prompt leci do agenta, każda odpowiedź wraca na stronę.
4. **Verify** — strona szereguje modele-kandydatów, program czyta zwycięzcę i pewność.
5. **Zmiana nazwy** — czat Arena dostaje nazwę `model pewność`, a w konsoli pojawia się podsumowanie.

## 📋 Wymagania

- Python **3.10+**
- Windows 10/11, macOS lub Linux
- Konto arena.ai (e-mail i hasło lub link z wiadomości)
- ~400 MB wolnego miejsca na Chromium dla Playwright

## 🚀 Instalacja

```bash
git clone https://github.com/LeistDev/arena-model-hunter.git
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** wystarczy potem dwukrotnie kliknąć `run.bat` (włącza UTF-8, żeby cyrylica wyświetlała się poprawnie).
**macOS / Linux:** `./run.sh` lub `python main.py`.

## 🕹️ Użycie

```bash
python main.py
```

| Opcja | Opis |
|---|---|
| **Start** | pyta, ile czatów uruchomić (1–100, a przy nieograniczonych — dowolną liczbę), i startuje cały proces |
| **Ustawienia** | tryb pracy, język interfejsu, usunięcie aktywnego konta arena.ai |
| **Wyjście** | zamyka program (terminal wraca do poprzedniej zawartości) |

Menu dopasowuje się do stanu: dopóki konto nie jest podłączone, widoczny jest punkt **Zaloguj**, a kursor stoi właśnie na nim; po udanym logowaniu punkt znika.

## ⚙️ Ustawienia

| Opcja | Opis |
|---|---|
| **Tryb pracy** | `jednowątkowy` (domyślnie) / `wielowątkowy` — wielowątkowy jest szybszy, ale wysyła równoległe żądania |
| **Język** | `English` / `Русский` / `中文` — działa od razu i jest zapamiętywany |
| **Nieograniczona liczba czatów** ⚠️ | znosi limit 100 czatów: `Start` przyjmuje dowolną liczbę — niebezpieczne, domyślnie wyłączone |
| **Usuń aktywne konto arena.ai** | czyści profil przeglądarki i sesję, czyli wylogowuje |

Ustawienia są w `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Nieograniczona liczba czatów jest domyślnie wyłączona, a ostrzeżenie nie jest ozdobą.** Po włączeniu `Start` nie sprawdza już zakresu 1–100, tylko przyjmuje dowolną liczbę — `250`, `1000`. Każdy czat to dwie karty, więc duże liczby oznaczają nawał równoległych żądań do arena.ai: dokładnie to, przed czym mają chronić limity tempa i captcha, z realnym ryzykiem ograniczenia konta. Włączaj tylko, jeśli to akceptujesz, i zostań w trybie jednowątkowym; powyżej 100 program prosi o drugie potwierdzenie z dokładną liczbą, zanim cokolwiek się otworzy.

## 🔐 Jak działa logowanie

1. Otwiera się **prawdziwe** okno Chromium z trwałym profilem (`~/.arena-model-hunter/profile`) — Cloudflare odrzuca przeglądarki headless, więc program nigdy ich nie używa.
2. Klikasz `Log In` → wpisujesz e-mail → `Continue with email`.
   - Konto istnieje → wpisz hasło → `Log In`.
   - Nowy e-mail → krok z imieniem można pominąć → przychodzi link na maila → wklej go w pasek adresu (`Ctrl+L`, `Ctrl+V`, Enter) → utwórz hasło.
3. Program odświeża stronę co 1,5 s i rozpoznaje sukces po trzech sygnałach: e-mail pojawia się na pasku bocznym, powstaje ciasteczko `arena-auth-*`, a przycisk `Log In` znika.
4. Potem zapisuje `session.json` + `state.json` i **zamyka przeglądarkę**.

Strona zawsze otwiera się w **ciemnym motywie** (przeglądarka startuje z `prefers-color-scheme: dark`, a arena.ai to respektuje).

## ⚡ Tryb jednowątkowy i wielowątkowy

| Tryb | Jak działa | Pomiar na 3 czatach |
|---|---|---|
| **Jednowątkowy** (domyślnie) | pary kart są obsługiwane po kolei, aktywna karta wychodzi na wierzch | ≈7,5 min |
| **Wielowątkowy** | wszystkie pary kart działają jednocześnie, fokus nie jest przełączany | ≈4,5 min |

W trybie wielowątkowym Arena dostaje kilka żądań naraz, więc limity i captcha są bardziej prawdopodobne. Jeśli się pojawią — wróć do trybu jednowątkowego.

## 🗂️ Struktura projektu

```
arena-model-hunter/
├── main.py             # menu, ustawienia, scenariusze
├── ui.py               # interfejs terminala: ramka, alt-screen, odczyt klawiszy, zmiana rozmiaru
├── arena_login.py      # przeglądarka, logowanie, wykrywanie sesji, konfiguracja
├── flow.py             # potok Arena ↔ lm.ikale.io, Verify, zmiana nazwy
├── i18n.py             # tłumaczenia interfejsu (en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI: lint i kontrola tłumaczeń
├── LICENSE
└── docs/i18n/          # ten README w 30 językach
```

## 🌍 Zmienne środowiskowe

| Zmienna | Domyślnie | Do czego służy |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | folder profilu i sesji |
| `ARENA_HELPER_HOME` | — | stara nazwa zmiennej, nadal obsługiwana |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | opcjonalne wypełnianie formularza (nigdy nie jest zapisywane) |
| `ARENA_LOGIN_TIMEOUT` | `900` | ile sekund czekać na logowanie |
| `ARENA_URL` | `https://arena.ai/` | adres startowy |

## 🧰 Możliwe pytania

- **„Just a moment…” / weryfikacja Cloudflare** — potrzebna jest widoczna przeglądarka; nie uruchamiaj na serwerze bez pulpitu.
- **„Przeglądarka nie jest zainstalowana”** — uruchom `python -m playwright install chromium`.
- **Captcha albo żądania po cichu nie wychodzą** — prawdopodobnie limit: włącz tryb jednowątkowy i zwolnij tempo.
- **Chcę zacząć od zera** — Ustawienia → *Usuń aktywne konto arena.ai* lub usuń `~/.arena-model-hunter`.
- **Polowanie przez całą noc** — Ustawienia → *Nieograniczona liczba czatów*, wpisz `300` w Start i potwierdź; zostań w trybie jednowątkowym, a rano obejrzyj przemianowane czaty.

## ⚠️ Zastrzeżenie

Projekt powstał do **własnych eksperymentów i nauki**. Automatyzuje zewnętrzną stronę; automatyzacja może naruszać regulamin arena.ai oraz strony z odciskami i prowadzić do ograniczeń konta. Używaj na własną odpowiedzialność, nie generuj zbędnego obciążenia, w razie wątpliwości trzymaj tryb jednowątkowy i nigdy nie publikuj swoich danych — program nie zapisuje hasła na dysku.

## 📄 Licencja

[MIT](LICENSE) — wolne oprogramowanie: możesz go używać, badać, udostępniać i zmieniać. Jeśli rozpowszechniasz program lub zmienioną wersję, musisz dołączyć do niej notę o prawach autorskich i treść licencji MIT. Brak gwarancji.

Copyright (C) 2026 współtwórcy arena model hunter.

