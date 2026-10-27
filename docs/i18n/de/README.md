<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | **🇩🇪 Deutsch** | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Modell-Jäger für arena.ai: startet einen Schwung Agent-Chats, nimmt von jeder Antwort einen Fingerabdruck, findet heraus, welches Modell geantwortet hat, und benennt den Chat danach — morgens wartet ein beschrifteter Chat mit Claude Opus, GPT-5, Gemini oder dem Modell, das du gesucht hast.**

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

## 🎯 Wozu das Ganze

Im Agent-Modus entscheidet arena.ai selbst, welches Modell antwortet — und das ist selten das gewünschte: mal ein Spitzenmodell (Claude Opus und Verwandte), mal deutlich schwächere Kost. Dieses Tool macht aus der Lotterie eine Suche: Es öffnet einen Schwung Agent-Chats, spielt in jedem die drei Fingerabdruck-Samples durch, fragt die Fingerabdruck-Seite, welches Modell geantwortet hat, und schreibt das Ergebnis in den Chat-Titel (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Über Nacht mit beliebig vielen Chats laufen lassen — morgens gibt es eine beschriftete Liste: Öffne den Chat, dessen Titel das benötigte Modell nennt, und arbeite darin weiter. Genau das ist der Punkt: nicht Automatisierung um ihrer selbst willen, sondern ein Chat, der wirklich auf dem Modell läuft, das du wolltest.

## ✨ Was es kann

- **Einmal anmelden — Session bleibt.** Es öffnet sich ein echter (kein Headless-)Chromium, du meldest dich wie gewohnt bei arena.ai an; die App erkennt die Anmeldung, speichert die Session und schließt den Browser selbst.
- **N Chats gleichzeitig.** Du gibst eine Zahl von 1 bis 100 ein — es öffnen sich genau so viele `arena.ai/agent`-Tabs und ebenso viele `lm.ikale.io`-Tabs.
- **Kopiert für dich.** Der Prompt jedes Samples geht an den Agenten, die Antwort wird vollständig abgewartet und ins Reply-Feld eingefügt — drei Samples pro Chat.
- **Erkennt das Modell.** Klickt Verify auf der Fingerabdruck-Seite, liest den besten Kandidaten und die Konfidenz genau so aus, wie die Seite sie zeigt, und benennt den Arena-Chat in `modell konfidenz` um (z. B. `gpt-6-luna 99.9%`).
- **Zwei Betriebsmodi.** Einthreading (sicher, Chats nacheinander) und Multithreading (alle Chats parallel, 1,5–2× schneller).
- **Oberfläche in drei Sprachen.** English, Русский, 中文 — direkt in der App umschaltbar, ohne Neustart.

## 🔄 So läuft ein Durchlauf

1. **Anmelden** — der Browser öffnet sich, du authentifizierst dich, die App erkennt das und schließt das Fenster.
2. **Start → Anzahl der Chats** — zum Beispiel `3`: drei Arena-Tabs und drei Fingerabdruck-Tabs.
3. **Samples 1 → 3** — jeder Prompt geht an den Agenten, jede Antwort zurück auf die Seite.
4. **Verify** — die Seite bewertet die Kandidatenmodelle, die App liest Sieger und Konfidenz.
5. **Umbenennen** — der Arena-Chat heißt danach `modell konfidenz`, in der Konsole erscheint eine Zusammenfassung.

## 📋 Voraussetzungen

- Python **3.10+**
- Windows 10/11, macOS oder Linux
- Ein arena.ai-Konto (E-Mail und Passwort oder Link per Mail)
- ~400 MB freier Speicher für Chromium von Playwright

## 🚀 Installation

```bash
git clone https://github.com/LeistDev/arena-model-hunter.git
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** danach genügt ein Doppelklick auf `run.bat` (aktiviert UTF-8, damit Kyrillisch korrekt dargestellt wird).
**macOS / Linux:** `./run.sh` oder `python main.py`.

## 🕹️ Benutzung

```bash
python main.py
```

| Option | Beschreibung |
|---|---|
| **Start** | fragt, wie viele Chats laufen sollen (1–100, mit unbegrenzten Chats jede Zahl) und startet den ganzen Ablauf |
| **Einstellungen** | Betriebsmodus, Sprache der Oberfläche, aktives arena.ai-Konto entfernen |
| **Beenden** | schließt die App (das Terminal zeigt wieder seinen vorherigen Inhalt) |

Das Menü passt sich dem Zustand an: solange kein Konto verbunden ist, erscheint **Anmelden** und der Cursor steht darauf; nach erfolgreicher Anmeldung verschwindet der Punkt.

## ⚙️ Einstellungen

| Option | Beschreibung |
|---|---|
| **Betriebsmodus** | `einthreading` (Standard) / `multithreading` — Multithreading ist schneller, sendet aber parallele Anfragen |
| **Sprache** | `English` / `Русский` / `中文` — wirkt sofort und wird gemerkt |
| **Unbegrenzte Chats** ⚠️ | hebt das Limit von 100 Chats auf: `Start` nimmt jede Zahl — gefährlich, standardmäßig aus |
| **Aktives arena.ai-Konto entfernen** | löscht Browserprofil und Session, meldet also ab |

Die Einstellungen liegen in `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Unbegrenzte Chats sind standardmäßig aus, und die Warnung ist ernst gemeint.** Ist die Option an, prüft `Start` nicht mehr auf 1–100, sondern nimmt jede Zahl — `250`, `1000`. Jeder Chat sind zwei Tabs, große Zahlen bedeuten also einen Schwall paralleler Anfragen an arena.ai: genau das Muster, gegen das Rate-Limits und Captchas existieren, mit echtem Risiko einer Kontosperrung. Schalte es nur ein, wenn du das akzeptierst, und bleib im Einzelthread-Modus; ab 100 kommt vorher eine zweite Bestätigung mit der genauen Anzahl.

## 🔐 Wie die Anmeldung funktioniert

1. Es öffnet sich ein **echtes** Chromium-Fenster mit dauerhaftem Profil (`~/.arena-model-hunter/profile`) — Cloudflare lehnt Headless-Browser ab, deshalb nutzt die App nie einen.
2. Du klickst auf `Log In` → gibst deine E-Mail ein → `Continue with email`.
   - Bestehendes Konto → Passwort eingeben → `Log In`.
   - Neue E-Mail → der Namensschritt darf übersprungen werden → per Mail kommt ein Link → in die Adresszeile einfügen (`Ctrl+L`, `Ctrl+V`, Enter) → Passwort anlegen.
3. Die App fragt die Seite alle 1,5 s ab und erkennt den Erfolg an drei Zeichen: deine E-Mail erscheint in der Seitenleiste, ein `arena-auth-*`-Cookie taucht auf, der Button `Log In` verschwindet.
4. Sie speichert `session.json` + `state.json` und **schließt den Browser**.

Die Seite öffnet immer im **dunklen Design** (der Browser startet mit `prefers-color-scheme: dark`, und arena.ai folgt dem).

## ⚡ Einthreading und Multithreading

| Modus | Verhalten | Gemessen mit 3 Chats |
|---|---|---|
| **Einthreading** (Standard) | Tab-Paare werden nacheinander abgearbeitet, der aktive Tab kommt nach vorn | ≈7,5 Min. |
| **Multithreading** | alle Tab-Paare laufen gleichzeitig, der Fokus wird nicht verschoben | ≈4,5 Min. |

Im Multithreading bekommt Arena mehrere Anfragen auf einmal, daher sind Limits und Captchas wahrscheinlicher. Falls das passiert, zurück auf Einthreading schalten.

## 🗂️ Projektstruktur

```
arena-model-hunter/
├── main.py             # Menü, Einstellungen, Abläufe
├── ui.py               # Terminal-Oberfläche: Rahmen, Alt-Screen, Tastenlesen, Größenänderung
├── arena_login.py      # Browser, Anmeldung, Sitzungserkennung, Konfiguration
├── flow.py             # Arena ↔ lm.ikale.io-Pipeline, Verify, Umbenennen
├── i18n.py             # UI-Übersetzungen (en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI: Lint und Übersetzungsprüfung
├── LICENSE
└── docs/i18n/          # dieses README in 30 Sprachen
```

## 🌍 Umgebungsvariablen

| Variable | Standard | Zweck |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | Ordner für Profil und Sitzung |
| `ARENA_HELPER_HOME` | — | alter Name der Variable, weiterhin gültig |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | optionales Ausfüllen des Formulars (wird nie gespeichert) |
| `ARENA_LOGIN_TIMEOUT` | `900` | Sekunden Wartezeit auf die Anmeldung |
| `ARENA_URL` | `https://arena.ai/` | Start-URL |

## 🧰 Häufige Fragen

- **„Just a moment…“ / Cloudflare-Prüfung** — es braucht ein sichtbares Browserfenster; nicht auf einem Server ohne Desktop starten.
- **„Browser ist nicht installiert“** — `python -m playwright install chromium` ausführen.
- **Captcha oder Anfragen gehen still nicht raus** — wahrscheinlich ein Limit: auf Einthreading wechseln und langsamer werden.
- **Ich möchte neu anfangen** — Einstellungen → *Aktives arena.ai-Konto entfernen* oder `~/.arena-model-hunter` löschen.
- **Die ganze Nacht jagen** — Einstellungen → *Unbegrenzte Chats*, dann im Start `300` eingeben und bestätigen; Einzelthread beibehalten und morgens die umbenannten Chats ansehen.

## ⚠️ Hinweis

Das Projekt dient **persönlichen Experimenten und Lernzwecken**. Es automatisiert eine fremde Website; Automatisierung kann gegen die Nutzungsbedingungen von arena.ai und der Fingerabdruck-Seite verstoßen und zu Kontoeinschränkungen führen. Nutzung auf eigene Gefahr, keine unnötige Last erzeugen, im Zweifel beim Einthreading bleiben und niemals eigene Zugangsdaten veröffentlichen — die App speichert das Passwort nicht auf der Festplatte.

## 📄 Lizenz

[MIT](LICENSE) — freie Software: du darfst sie nutzen, untersuchen, weitergeben und verändern. Wer das Programm oder eine veränderte Fassung verbreitet, muss den Urheberrechtshinweis und den Text der MIT-Lizenz beilegen. Es gibt keine Gewährleistung.

Copyright (C) 2026 die Mitwirkenden von arena model hunter.

