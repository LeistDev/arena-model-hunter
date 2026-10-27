<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | **🇵🇹 Português (Portugal)** | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Caçador de modelos para o arena.ai: corre um lote de conversas em modo agente, faz a impressão digital de cada resposta, descobre que modelo respondeu e renomeia a conversa com esse nome — de manhã tem uma conversa etiquetada a correr Claude Opus, GPT-5, Gemini ou o modelo que andava a procurar.**

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

## 🎯 Porque isto existe

No modo agente é o arena.ai que decide qual modelo responde — e nem sempre é o que quer: às vezes um modelo de topo (Claude Opus e companhia), às vezes algo bem mais fraco. Esta ferramenta transforma essa lotaria numa busca: abre um lote de conversas em modo agente, repete as três amostras de impressão digital em cada uma, pergunta ao site de impressões digitais que modelo respondeu e escreve o veredicto no título da conversa (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Deixe-o a correr de noite com quantas conversas quiser; de manhã há uma lista etiquetada: abra a conversa cujo título diz o modelo de que precisa e continue a trabalhar nela. É esse o ponto — não automação por automação, mas conseguir uma conversa que corra mesmo no modelo que queria.

## ✨ O que faz

- **Um único início de sessão — a sessão mantém-se.** Abre-se um Chromium real (nunca headless), inicias sessão no arena.ai como sempre; a app deteta, guarda a sessão e fecha o navegador sozinha.
- **N conversas ao mesmo tempo.** Introduzes um número de 1 a 100 — abrem-se exatamente esses separadores `arena.ai/agent` e o mesmo número de separadores `lm.ikale.io`.
- **Copia por ti.** O prompt de cada amostra é enviado ao agente, a resposta é esperada por completo e colada no campo Reply — três amostras por conversa.
- **Identifica o modelo.** Clica em Verify no site das impressões digitais, lê o melhor candidato e a confiança tal como o site os mostra e renomeia a conversa do Arena para `modelo confiança` (por exemplo `gpt-6-luna 99.9%`).
- **Dois modos de execução.** Um só thread (seguro, conversas uma a uma) e multi-thread (todas em paralelo, 1,5–2× mais rápido).
- **Interface em três idiomas.** English, Русский, 中文 — muda-se dentro da app, sem reiniciar.

## 🔄 Como decorre uma execução

1. **Iniciar sessão** — abre-se o navegador, autenticas-te, a app deteta e fecha a janela.
2. **Iniciar → número de conversas** — por exemplo `3`: três separadores Arena e três de impressões digitais.
3. **Amostras 1 → 3** — cada prompt vai para o agente, cada resposta volta ao site.
4. **Verify** — o site ordena os modelos candidatos e a app lê o vencedor e a confiança.
5. **Renomear** — a conversa do Arena passa a chamar-se `modelo confiança` e surge um resumo na consola.

## 📋 Requisitos

- Python **3.10+**
- Windows 10/11, macOS ou Linux
- Uma conta arena.ai (email e palavra-passe ou link por email)
- ~400 MB livres para o Chromium do Playwright

## 🚀 Instalação

```bash
git clone <this-repo> arena-model-hunter
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** depois basta um duplo clique em `run.bat` (ativa UTF-8 para o cirílico aparecer corretamente).
**macOS / Linux:** `./run.sh` ou `python main.py`.

## 🕹️ Utilização

```bash
python main.py
```

| Opção | Descrição |
|---|---|
| **Iniciar** | pergunta quantas conversas correr (1–100, ou qualquer número com conversas ilimitadas) e arranca todo o processo |
| **Definições** | modo de execução, idioma da interface, remover a conta arena.ai ativa |
| **Sair** | fecha a app (o terminal volta ao conteúdo anterior) |

O menu adapta-se ao estado: enquanto não houver conta ligada aparece **Iniciar sessão** e o cursor fica lá; após um início de sessão bem-sucedido esse item desaparece.

## ⚙️ Definições

| Opção | Descrição |
|---|---|
| **Modo de execução** | `um só thread` (predefinido) / `multi-thread` — o multi-thread é mais rápido mas envia pedidos em paralelo |
| **Idioma** | `English` / `Русский` / `中文` — aplica-se de imediato e fica memorizado |
| **Conversas ilimitadas** ⚠️ | retira o limite de 100 conversas: o `Start` aceita qualquer número — perigoso, desligado por omissão |
| **Remover a conta arena.ai ativa** | apaga o perfil do navegador e a sessão, ou seja, termina a sessão |

As definições ficam em `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Conversas ilimitadas vem desligado por omissão e o aviso não é decoração.** Com a opção ligada, o `Start` deixa de verificar 1–100 e aceita qualquer número — `250`, `1000`. Cada conversa são dois separadores, por isso números grandes significam uma rajada de pedidos paralelos ao arena.ai: exatamente o padrão contra o qual existem os limites de taxa e os captcha, com risco real de a conta ser restringida. Ligue só se aceitar isso e mantenha o modo de uma thread; acima de 100 é pedida uma segunda confirmação com o número exato antes de abrir seja o que for.

## 🔐 How signing in works

1. A **real** Chromium window opens with a persistent profile (`~/.arena-model-hunter/profile`) — headless browsers are rejected by Cloudflare, so the app never uses one.
2. You click `Log In` → enter your email → `Continue with email`.
   - Existing account → enter the password → `Log In`.
   - New email → the name step can be skipped → a link arrives by mail → paste it into the address bar (`Ctrl+L`, `Ctrl+V`, Enter) → create a password.
3. The app polls the page every 1.5 s and detects success by: your email appearing in the sidebar, an `arena-auth-*` cookie, and the `Log In` button disappearing.
4. It saves `session.json` + `state.json` and **closes the browser**.

The site always opens in **dark theme** (the browser is launched with `prefers-color-scheme: dark`, which arena.ai follows).

## ⚡ Modo de um só thread e multi-thread

| Modo | Como funciona | Medido com 3 conversas |
|---|---|---|
| **Um só thread** (predefinido) | os pares de separadores são processados um após outro, o separador ativo vem para a frente | ≈7,5 min |
| **Multi-thread** | todos os pares de separadores correm ao mesmo tempo, o foco não é movido | ≈4,5 min |

Em multi-thread o Arena recebe vários pedidos em simultâneo, por isso os limites e o captcha são mais prováveis. Se acontecer, volta ao modo de um só thread.

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

## 🧰 Perguntas frequentes

- **«Just a moment…» / verificação Cloudflare** — é precisa uma janela de navegador visível; não corras num servidor sem ambiente gráfico.
- **«O navegador não está instalado»** — executa `python -m playwright install chromium`.
- **Captcha ou pedidos que não saem** — provavelmente atingiste um limite: ativa um só thread e abranda.
- **Quero recomeçar do zero** — Definições → *Remover a conta arena.ai ativa* ou apaga `~/.arena-model-hunter`.
- **Caçar toda a noite** — Definições → *Conversas ilimitadas*, escreva `300` em Iniciar e confirme; mantenha uma thread e veja de manhã as conversas renomeadas.

## ⚠️ Aviso

Este projeto serve para **experiências pessoais e aprendizagem**. Automatiza um site de terceiros; a automatização pode violar os termos do arena.ai e do site de impressões digitais e originar restrições de conta. Usa por tua conta e risco, não geres carga desnecessária, em caso de dúvida mantém um só thread e nunca publiques os teus dados — a app não guarda a palavra-passe em disco.

## 📄 Licença

[MIT](LICENSE) — faz o que quiseres, sem garantias.

<div align="center">

**[⬆ Topo](#-arena-model-hunter) · 🇺🇸 [Read in English](../../../README.md)**

</div>
