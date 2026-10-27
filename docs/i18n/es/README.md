<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | **🇪🇸 Español** | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Cazador de modelos para arena.ai: lanza un lote de chats en modo agente, analiza la huella de cada respuesta, averigua qué modelo contestó y renombra el chat con ese nombre — por la mañana tienes un chat etiquetado con Claude Opus, GPT-5, Gemini o el que estuvieras buscando.**

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

## 🎯 Para qué existe

En modo agente arena.ai decide qué modelo responde, y no siempre es el que quieres: a veces es un modelo de primera línea (Claude Opus y compañía), a veces algo mucho más flojo. Esta herramienta convierte esa lotería en una búsqueda: abre un lote de chats en modo agente, repite las tres muestras de huella en cada uno, pregunta al sitio de huellas qué modelo respondió y escribe el veredicto en el título del chat (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Déjalo toda la noche con tantos chats como quieras; por la mañana hay una lista etiquetada: abre el chat cuyo título dice el modelo que necesitas y trabaja en él. Ese es el punto: no automatizar por automatizar, sino conseguir un chat que funcione con el modelo que de verdad querías.

## ✨ Qué hace

- **Un solo inicio de sesión — la sesión se mantiene.** Se abre un Chromium real (nunca headless), inicias sesión en arena.ai como siempre; la app lo detecta, guarda la sesión y cierra el navegador por sí sola.
- **N chats a la vez.** Escribes un número del 1 al 100 — se abren exactamente esas pestañas de `arena.ai/agent` y el mismo número de pestañas de `lm.ikale.io`.
- **Copia por ti.** El prompt de cada muestra se envía al agente, se espera la respuesta completa y se pega en el campo Reply — tres muestras por chat.
- **Identifica el modelo.** Pulsa Verify en el sitio de huellas, lee el mejor candidato y la confianza tal como los muestra el sitio y renombra el chat de Arena a `modelo confianza` (por ejemplo `gpt-6-luna 99.9%`).
- **Dos modos de ejecución.** Un solo hilo (seguro, chats uno por uno) y multihilo (todos los chats en paralelo, 1,5–2× más rápido).
- **Interfaz en tres idiomas.** English, Русский, 中文 — se cambia dentro de la app, sin reiniciar.

## 🔄 Cómo transcurre una ejecución

1. **Iniciar sesión** — se abre el navegador, te autenticas, la app lo detecta y cierra la ventana.
2. **Iniciar → número de chats** — por ejemplo `3`: tres pestañas de Arena y tres de huellas.
3. **Muestras 1 → 3** — cada prompt va al agente y cada respuesta vuelve al sitio.
4. **Verify** — el sitio clasifica los modelos candidatos y la app lee el ganador y la confianza.
5. **Renombrar** — el chat de Arena pasa a llamarse `modelo confianza` y en la consola aparece un resumen.

## 📋 Requisitos

- Python **3.10+**
- Windows 10/11, macOS o Linux
- Una cuenta de arena.ai (correo y contraseña o enlace por correo)
- ~400 MB libres para el Chromium de Playwright

## 🚀 Instalación

```bash
git clone <this-repo> arena-model-hunter
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** después basta con hacer doble clic en `run.bat` (activa UTF-8 para que el cirílico se vea bien).
**macOS / Linux:** `./run.sh` o `python main.py`.

## 🕹️ Uso

```bash
python main.py
```

| Opción | Descripción |
|---|---|
| **Iniciar** | pregunta cuántos chats lanzar (1–100, o cualquier número con chats ilimitados) y arranca todo el proceso |
| **Ajustes** | modo de ejecución, idioma de la interfaz, eliminar la cuenta activa de arena.ai |
| **Salir** | cierra la app (el terminal recupera su contenido anterior) |

El menú se adapta al estado: mientras no hay cuenta conectada aparece **Iniciar sesión** y el cursor se coloca ahí; tras un inicio de sesión correcto ese elemento desaparece.

## ⚙️ Ajustes

| Opción | Descripción |
|---|---|
| **Modo de ejecución** | `un solo hilo` (por defecto) / `multihilo` — el multihilo es más rápido pero envía peticiones en paralelo |
| **Idioma** | `English` / `Русский` / `中文` — se aplica al instante y se recuerda |
| **Chats ilimitados** ⚠️ | quita el límite de 100 chats: `Start` acepta cualquier número — peligroso, desactivado por defecto |
| **Eliminar la cuenta activa de arena.ai** | borra el perfil del navegador y la sesión, es decir, cierra sesión |

Los ajustes se guardan en `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Los chats ilimitados están desactivados por defecto y el aviso va en serio.** Con la opción activa, `Start` acepta cualquier número en vez de 1–100 — `250`, `1000`. Cada chat son dos pestañas, así que cifras grandes significan una ráfaga de peticiones en paralelo a arena.ai: justo el patrón por el que existen los límites de tasa y los captchas, con riesgo real de que restrinjan la cuenta. Actívalo solo si lo aceptas y mantén el modo de un solo hilo; cualquier valor por encima de 100 pide una segunda confirmación con la cantidad exacta.

## 🔐 How signing in works

1. A **real** Chromium window opens with a persistent profile (`~/.arena-model-hunter/profile`) — headless browsers are rejected by Cloudflare, so the app never uses one.
2. You click `Log In` → enter your email → `Continue with email`.
   - Existing account → enter the password → `Log In`.
   - New email → the name step can be skipped → a link arrives by mail → paste it into the address bar (`Ctrl+L`, `Ctrl+V`, Enter) → create a password.
3. The app polls the page every 1.5 s and detects success by: your email appearing in the sidebar, an `arena-auth-*` cookie, and the `Log In` button disappearing.
4. It saves `session.json` + `state.json` and **closes the browser**.

The site always opens in **dark theme** (the browser is launched with `prefers-color-scheme: dark`, which arena.ai follows).

## ⚡ Modo de un solo hilo y multihilo

| Modo | Cómo funciona | Medido con 3 chats |
|---|---|---|
| **Un solo hilo** (por defecto) | las parejas de pestañas se procesan una tras otra, la pestaña activa pasa al frente | ≈7,5 min |
| **Multihilo** | todas las parejas de pestañas corren a la vez, el foco no se mueve | ≈4,5 min |

En multihilo, Arena recibe varias peticiones a la vez, así que los límites y el captcha son más probables. Si ocurre, vuelve al modo de un solo hilo.

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

## 🧰 Preguntas frecuentes

- **«Just a moment…» / verificación de Cloudflare** — hace falta una ventana de navegador visible; no lo ejecutes en un servidor sin escritorio.
- **«El navegador no está instalado»** — ejecuta `python -m playwright install chromium`.
- **Captcha o peticiones que no salen** — probablemente alcanzaste un límite: activa un solo hilo y baja el ritmo.
- **Quiero empezar de cero** — Ajustes → *Eliminar la cuenta activa de arena.ai* o borra `~/.arena-model-hunter`.
- **Cazar toda la noche** — Ajustes → *Chats ilimitados*, escribe `300` en Iniciar y confirma; mantén un solo hilo y mira por la mañana los chats renombrados.

## ⚠️ Aviso legal

Este proyecto es para **experimentos personales y aprendizaje**. Automatiza un sitio de terceros; la automatización puede infringir los términos de arena.ai y del sitio de huellas y provocar restricciones en la cuenta. Úsalo bajo tu responsabilidad, no generes carga innecesaria, ante la duda mantén un solo hilo y nunca publiques tus datos — la app no guarda la contraseña en disco.

## 📄 Licencia

[MIT](LICENSE) — haz lo que quieras, sin garantías.

<div align="center">

**[⬆ Arriba](#-arena-model-hunter) · 🇺🇸 [Read in English](../../../README.md)**

</div>
