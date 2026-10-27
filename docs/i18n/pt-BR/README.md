<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | **🇧🇷 Português (Brasil)** | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Caçador de modelos para o arena.ai: roda um lote de chats no modo agente, faz a impressão digital de cada resposta, descobre qual modelo respondeu e renomeia o chat com esse nome — de manhã você tem um chat etiquetado rodando Claude Opus, GPT-5, Gemini ou o que estiver caçando.**

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

## 🎯 Por que isso existe

No modo agente o arena.ai decide qual modelo responde, e nem sempre é o que você quer: às vezes vem um modelo de ponta (Claude Opus e companhia), às vezes algo bem mais fraco. Esta ferramenta transforma essa loteria em uma busca — abre um lote de chats no modo agente, repete as três amostras de impressão digital em cada um, pergunta ao site de impressões digitais qual modelo respondeu e grava o veredito no título do chat (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Deixe rodando de noite com quantos chats quiser; de manhã existe uma lista etiquetada: abra o chat cujo título traz o modelo que você precisa e continue trabalhando nele. É esse o ponto: não automação por automação, mas conseguir um chat que roda no modelo que você realmente queria.

## ✨ O que ele faz

- **Um único login — a sessão permanece.** Abre um Chromium real (nunca headless), você entra no arena.ai como sempre; o app detecta, salva a sessão e fecha o navegador sozinho.
- **N conversas ao mesmo tempo.** Você digita um número de 1 a 100 — abrem exatamente essas abas `arena.ai/agent` e o mesmo número de abas `lm.ikale.io`.
- **Copia no seu lugar.** O prompt de cada amostra vai para o agente, a resposta é aguardada por inteiro e colada no campo Reply — três amostras por conversa.
- **Identifica o modelo.** Clica em Verify no site de impressões digitais, lê o melhor candidato e a confiança exatamente como o site mostra e renomeia a conversa do Arena para `modelo confiança` (por exemplo `gpt-6-luna 99.9%`).
- **Dois modos de execução.** Thread única (seguro, conversas uma por vez) e multithread (todas em paralelo, 1,5–2× mais rápido).
- **Interface em três idiomas.** English, Русский, 中文 — trocado dentro do app, sem reiniciar.

## 🔄 Como funciona uma execução

1. **Login** — o navegador abre, você se autentica, o app detecta e fecha a janela.
2. **Iniciar → número de conversas** — por exemplo `3`: três abas do Arena e três abas de impressões digitais.
3. **Amostras 1 → 3** — cada prompt vai para o agente, cada resposta volta para o site.
4. **Verify** — o site ordena os modelos candidatos e o app lê o vencedor e a confiança.
5. **Renomear** — a conversa do Arena passa a se chamar `modelo confiança` e um resumo aparece no console.

## 📋 Requisitos

- Python **3.10+**
- Windows 10/11, macOS ou Linux
- Uma conta arena.ai (e-mail e senha ou link por e-mail)
- ~400 MB livres para o Chromium do Playwright

## 🚀 Instalação

```bash
git clone https://github.com/LeistDev/arena-model-hunter.git
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** depois basta dar um duplo clique em `run.bat` (ativa UTF-8 para o cirílico aparecer corretamente).
**macOS / Linux:** `./run.sh` ou `python main.py`.

## 🕹️ Uso

```bash
python main.py
```

| Opção | Descrição |
|---|---|
| **Iniciar** | pergunta quantos chats rodar (1–100, ou qualquer número com chats ilimitados) e dispara todo o fluxo |
| **Configurações** | modo de execução, idioma da interface, remover a conta arena.ai ativa |
| **Sair** | fecha o app (o terminal volta ao conteúdo anterior) |

O menu se adapta ao estado: enquanto não há conta conectada aparece **Entrar** e o cursor fica nele; após um login bem-sucedido o item desaparece.

## ⚙️ Configurações

| Opção | Descrição |
|---|---|
| **Modo de execução** | `thread única` (padrão) / `multithread` — o multithread é mais rápido, mas envia requisições em paralelo |
| **Idioma** | `English` / `Русский` / `中文` — aplica na hora e fica salvo |
| **Chats ilimitados** ⚠️ | remove o limite de 100 chats: o `Start` aceita qualquer número — perigoso, desligado por padrão |
| **Remover a conta arena.ai ativa** | apaga o perfil do navegador e a sessão, ou seja, faz logout |

As configurações ficam em `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Chats ilimitados vem desligado e é realmente arriscado.** Com ele ligado, o `Start` aceita qualquer número em vez de 1–100 — `250`, `1000`. Cada chat são duas abas, então números grandes significam uma rajada de requisições paralelas ao arena.ai: é exatamente para isso que existem limites de taxa e captchas, e a conta pode ser restringida. Ligue só se aceitar esse risco e mantenha o modo de uma thread; qualquer valor acima de 100 pede uma segunda confirmação com a quantidade exata.

## 🔐 Como funciona o login

1. Abre-se uma janela **real** do Chromium com perfil persistente (`~/.arena-model-hunter/profile`) — o Cloudflare recusa navegadores headless, por isso o app nunca usa um.
2. Você clica em `Log In` → digita o e-mail → `Continue with email`.
   - Conta existente → digite a senha → `Log In`.
   - E-mail novo → a etapa do nome pode ser pulada → chega um link por e-mail → cole-o na barra de endereços (`Ctrl+L`, `Ctrl+V`, Enter) → crie uma senha.
3. O app consulta a página a cada 1,5 s e detecta o sucesso por três sinais: seu e-mail aparece na barra lateral, surge o cookie `arena-auth-*` e o botão `Log In` desaparece.
4. Ele salva `session.json` + `state.json` e **fecha o navegador**.

O site sempre abre no **tema escuro** (o navegador é iniciado com `prefers-color-scheme: dark`, e o arena.ai respeita isso).

## ⚡ Modo thread única e multithread

| Modo | Como funciona | Medido com 3 conversas |
|---|---|---|
| **Thread única** (padrão) | os pares de abas são processados um após o outro, a aba ativa vem para frente | ≈7,5 min |
| **Multithread** | todos os pares de abas rodam ao mesmo tempo, o foco não é trocado | ≈4,5 min |

No multithread o Arena recebe várias requisições ao mesmo tempo, então limites e captcha são mais prováveis. Se acontecer, volte para thread única.

## 🗂️ Estrutura do projeto

```
arena-model-hunter/
├── main.py             # menu, ajustes, cenários
├── ui.py               # interface do terminal: moldura, alt-screen, leitura de teclas, redimensionamento
├── arena_login.py      # navegador, login, detecção de sessão, configuração
├── flow.py             # pipeline Arena ↔ lm.ikale.io, Verify, renomeação
├── i18n.py             # traduções da interface (en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI: lint e verificação das traduções
├── LICENSE
└── docs/i18n/          # este README em 30 idiomas
```

## 🌍 Variáveis de ambiente

| Variável | Padrão | Para que serve |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | pasta do perfil e da sessão |
| `ARENA_HELPER_HOME` | — | nome antigo da variável, ainda aceito |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | preenchimento opcional do formulário (nunca é salvo) |
| `ARENA_LOGIN_TIMEOUT` | `900` | segundos de espera pelo login |
| `ARENA_URL` | `https://arena.ai/` | URL inicial |

## 🧰 Perguntas frequentes

- **«Just a moment…» / verificação Cloudflare** — é preciso uma janela de navegador visível; não rode em servidor sem desktop.
- **«O navegador não está instalado»** — execute `python -m playwright install chromium`.
- **Captcha ou requisições não saem** — provavelmente você bateu num limite: ative thread única e diminua o ritmo.
- **Quero começar do zero** — Configurações → *Remover a conta arena.ai ativa* ou apague `~/.arena-model-hunter`.
- **Caçada a noite toda** — Ajustes → *Chats ilimitados*, digite `300` em Iniciar e confirme; mantenha uma thread e veja os chats renomeados de manhã.

## ⚠️ Aviso

Este projeto é para **experimentos pessoais e aprendizado**. Ele automatiza um site de terceiros; a automação pode violar os termos do arena.ai e do site de impressões digitais e levar a restrições na conta. Use por sua conta e risco, não gere carga desnecessária, em caso de dúvida mantenha thread única e nunca publique seus dados — o app não salva a senha em disco.

## 📄 Licença

[MIT](LICENSE) — software livre: você pode usar, estudar, compartilhar e modificar. Se distribuir o programa ou uma versão modificada, você deve manter o aviso de copyright e o texto da licença MIT junto a ela. Não há garantias.

Copyright (C) 2026 colaboradores do arena model hunter.

