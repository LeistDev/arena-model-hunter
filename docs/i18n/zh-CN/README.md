<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | **🇨🇳 中文 (简体)** | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**arena.ai 的「模型猎人」：批量运行 agent 对话，给每个回答做指纹比对，识别到底由哪个模型作答，并把模型名写进对话标题——第二天早上，你就有一个跑着 Claude Opus、GPT-5、Gemini 或你正想找的那个模型的对话。**

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

## 🎯 为什么需要它

在 agent 模式下，arena.ai 自己决定由哪个模型回答，而它往往不是你想要的：有时是顶级模型（Claude Opus 之类的），有时明显弱很多。这个脚本把这场抽奖变成一次「搜索」：批量打开 agent 对话，在每个对话里跑完三份指纹样本，再向指纹网站询问是哪个模型作答，然后把结论写进对话标题——`claude-opus-4 99.9%`、`gpt-5.2 87%`。晚上挂着跑，想开多少个对话都行；早上你会看到一份带标签的列表：打开标题里写着所需模型的那个对话，直接在里面干活。重点就在这里——不是为自动化而自动化，而是**真正拿到一个跑着你要的那个模型的对话**。

## ✨ 功能

- **登录一次，会话常驻。** 打开的是真实（非 headless）Chromium 窗口，你照常登录 arena.ai；程序会自动察觉登录成功、保存会话并关闭浏览器。
- **N 个对话并行。** 输入 1–100 的数字，就会打开正好这么多 `arena.ai/agent` 标签页，以及同样数量的 `lm.ikale.io` 标签页。
- **替你复制粘贴。** 把每个样本的提示词发给 Agent，等待完整回答，再填入对应的 Reply 输入框——每个对话三个样本。
- **给出模型结论。** 在指纹网站上点击 Verify，读取网站显示的候选模型与置信度，然后把 Arena 对话重命名为 `模型 置信度`（例如 `gpt-6-luna 99.9%`）。
- **两种运行模式。** 单线程（更稳妥，逐个对话）与多线程（全部并行，快 1.5–2 倍）。
- **三种界面语言。** English、Русский、中文——在程序内切换，无需重启。

## 🔄 一次运行流程

1. **登录** — 打开浏览器，你完成认证，程序自动识别并关闭窗口。
2. **开始 → 对话数量** — 例如 `3`：三个 Arena 标签页和三个指纹标签页。
3. **样本 1 → 3** — 每条提示词发给 Agent，每个回答回填到网站。
4. **Verify** — 网站给出候选模型排名，程序读取冠军与置信度。
5. **重命名** — Arena 对话改名为 `模型 置信度`，控制台显示汇总结果。

## 📋 环境要求

- Python **3.10+**
- Windows 10/11、macOS 或 Linux
- 一个 arena.ai 账号（邮箱+密码，或邮件中的登录链接）
- 约 400 MB 可用空间用于 Playwright 的 Chromium

## 🚀 安装

```bash
git clone https://github.com/LeistDev/arena-model-hunter.git
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows：** 之后双击 `run.bat` 即可（它会开启 UTF-8，保证西里尔字母正常显示）。
**macOS / Linux：** `./run.sh` 或 `python main.py`。

## 🕹️ 使用

```bash
python main.py
```

| 选项 | 说明 |
|---|---|
| **开始** | 询问要运行多少个对话（1–100；开启不限数量后可为任意数字）并启动整个流程 |
| **设置** | 运行模式、界面语言、移除当前 arena.ai 账号 |
| **退出** | 关闭程序（终端恢复原有内容） |

菜单会随状态变化：未连接账号时显示**登录**并把光标停在该项；登录成功后该项自动消失。

## ⚙️ 设置

| 选项 | 说明 |
|---|---|
| **运行模式** | `单线程`（默认）/ `多线程` — 多线程更快，但会并行发送请求 |
| **语言** | `English` / `Русский` / `中文` — 立即生效并会记住 |
| **不限聊天数量** ⚠️ | 取消 100 个对话的上限：「开始」可接受任意数字——危险，默认关闭 |
| **移除当前 arena.ai 账号** | 清除浏览器配置与会话，即退出登录 |

设置保存在 `~/.arena-model-hunter/config.json`：

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **「不限聊天数量」默认关闭，这个警告不是摆设。** 打开后，「开始」不再限制 1–100，而是接受任意数字——`250`、`1000`。每个对话要两个标签页，数字一大就意味着同时向 arena.ai 发出一大批请求：这正是限流和验证码存在的理由，账户被限制的风险是真实存在的。只有在你接受这个风险时才开启，并保持单线程模式；超过 100 时，脚本会先弹出一个写明数量的二次确认。

## 🔐 登录是怎么完成的

1. 会打开一个**真实的** Chromium 窗口并使用持久化配置目录（`~/.arena-model-hunter/profile`）：Cloudflare 不接受无头浏览器，所以程序从不使用无头模式。
2. 你点击 `Log In` → 输入邮箱 → `Continue with email`。
   - 已有账号 → 输入密码 → `Log In`。
   - 新邮箱 → 姓名这一步可以跳过 → 邮件里会收到链接 → 粘贴到地址栏（`Ctrl+L`、`Ctrl+V`、回车）→ 设置密码。
3. 程序每 1.5 秒检查一次页面，通过三个信号确认登录成功：邮箱出现在侧边栏、出现 `arena-auth-*` cookie、`Log In` 按钮消失。
4. 随后保存 `session.json` 和 `state.json`，并**关闭浏览器**。

站点始终以**深色主题**打开：浏览器以 `prefers-color-scheme: dark` 启动，arena.ai 会跟随这个设置。

## ⚡ 单线程与多线程

| 模式 | 工作方式 | 3 个对话实测 |
|---|---|---|
| **单线程**（默认） | 成对的标签页逐个处理，活动标签页会被切到前台 | ≈7.5 分钟 |
| **多线程** | 所有标签页同时运行，不切换焦点 | ≈4.5 分钟 |

多线程模式下 Arena 会同时收到多个请求，更容易触发限流或验证码。如果出现这种情况，请切回单线程。

## 🗂️ 项目结构

```
arena-model-hunter/
├── main.py             # 菜单、设置、流程
├── ui.py               # 终端界面：边框、备用屏幕、按键读取、窗口缩放
├── arena_login.py      # 浏览器、登录、会话检测、配置
├── flow.py             # Arena ↔ lm.ikale.io 流程、Verify、重命名
├── i18n.py             # 界面翻译（en / ru / zh）
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI：代码检查与翻译校验
├── LICENSE
└── docs/i18n/          # 本 README 的 30 种语言版本
```

## 🌍 环境变量

| 变量 | 默认值 | 用途 |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | 配置目录与会话目录 |
| `ARENA_HELPER_HOME` | — | 变量的旧名称，仍然有效 |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | 可选的表单自动填充（从不保存） |
| `ARENA_LOGIN_TIMEOUT` | `900` | 等待登录的秒数 |
| `ARENA_URL` | `https://arena.ai/` | 起始网址 |

## 🧰 常见问题

- **「Just a moment…」/ Cloudflare 验证** — 需要一个可见的浏览器窗口；不要在无桌面的服务器上运行。
- **「浏览器未安装」** — 执行 `python -m playwright install chromium`。
- **出现验证码或消息没发出去** — 多半是被限流：切到单线程并放慢节奏。
- **想从头开始** — 设置 → *移除当前 arena.ai 账号*，或删除 `~/.arena-model-hunter`。
- **整夜狩猎** — 设置 → *不限聊天数量*，然后在「开始」里输入 `300` 并确认；保持单线程，早上再来看已被重命名的对话。

## ⚠️ 免责声明

本项目仅用于**个人实验与学习**。它会自动化第三方网站；自动化可能违反 arena.ai 与指纹网站的服务条款，并可能导致账号受限。请自行承担风险，不要制造额外负载，拿不准时请保持单线程模式，也绝不要公开你的凭据——程序不会把密码写入磁盘。

## 📄 许可证

[GNU General Public License v3.0](LICENSE) — 自由软件：可以自由使用、研究、分享和修改。分发本程序或修改版本时必须继续遵循 GPL，源码也必须保持公开。不提供任何担保。

Copyright (C) 2026 arena model hunter 贡献者。

