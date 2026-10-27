<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | **🇯🇵 日本語** | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**arena.ai のためのモデル探しツール：エージェントモードのチャットをまとめて実行し、各回答の指紋を照合してどのモデルが答えたのかを割り出し、そのモデル名でチャットを改名します。朝には Claude Opus、GPT-5、Gemini、あるいは探していたモデルで動くチャットが、名前付きで残っています。**

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

## 🎯 なぜ作ったのか

エージェントモードでは、どのモデルが答えるかを arena.ai が勝手に決めます。しかも望んだモデルとは限りません。上位モデル（Claude Opus など）のときもあれば、かなり弱いモデルのときもあります。このツールはその「くじ引き」を「探索」に変えます。エージェントチャットをまとめて開き、どれにも 3 つの指紋サンプルを通し、指紋サイトにどのモデルが答えたかを問い合わせ、判定をチャット名に書き込みます（`claude-opus-4 99.9%`、`gpt-5.2 87%`）。好きなだけチャットを開いて夜通し走らせておけば、朝にはラベル付きの一覧ができています。必要なモデル名が付いたチャットを開いて、そのまま作業してください。狙いはそこです。自動化のための自動化ではなく、本当に欲しかったモデルで動くチャットを手に入れること。

## ✨ できること

- **ログインは一度だけ。** 実際の（ヘッドレスではない）Chromium が開き、いつも通り arena.ai にログインします。アプリがログインを検知してセッションを保存し、自分でブラウザを閉じます。
- **N 個のチャットを同時に。** 1〜100 の数を入力すると、ちょうどその数の `arena.ai/agent` タブと、同じ数の `lm.ikale.io` タブが開きます。
- **コピペを代行。** 各サンプルのプロンプトをエージェントに送り、回答が揃うまで待って Reply 欄に貼り付けます（1 チャットにつき 3 サンプル）。
- **モデルを判定。** フィンガープリントサイトで Verify を押し、サイトが示す候補モデルと信頼度をそのまま読み取り、Arena のチャット名を `モデル 信頼度`（例：`gpt-6-luna 99.9%`）に変更します。
- **2 つの実行モード。** シングルスレッド（安全、1 件ずつ）とマルチスレッド（全件並列、1.5〜2 倍高速）。
- **3 言語のインターフェース。** English、Русский、中文 — アプリ内で切り替え可能、再起動不要。

## 🔄 実行の流れ

1. **ログイン** — ブラウザが開き、認証するとアプリが検知してウィンドウを閉じます。
2. **開始 → チャット数** — 例えば `3`：Arena タブ 3 つとフィンガープリントタブ 3 つ。
3. **サンプル 1 → 3** — 各プロンプトをエージェントへ、各回答をサイトへ戻します。
4. **Verify** — サイトが候補モデルをランキングし、アプリが 1 位と信頼度を読み取ります。
5. **リネーム** — Arena のチャット名が `モデル 信頼度` になり、コンソールに結果が出ます。

## 📋 動作環境

- Python **3.10+**
- Windows 10/11、macOS、Linux
- arena.ai のアカウント（メールとパスワード、またはメールのリンク）
- Playwright の Chromium 用に約 400 MB の空き容量

## 🚀 インストール

```bash
git clone <this-repo> arena-model-hunter
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows：** 以後は `run.bat` をダブルクリックするだけ（UTF-8 を有効化し、キリル文字も正しく表示します）。
**macOS / Linux：** `./run.sh` または `python main.py`。

## 🕹️ 使い方

```bash
python main.py
```

| 項目 | 説明 |
|---|---|
| **開始** | チャット数を尋ね（1〜100、無制限なら任意の数）、一連の処理を開始します |
| **設定** | 実行モード、表示言語、有効な arena.ai アカウントの削除 |
| **終了** | アプリを閉じます（ターミナルは元の内容に戻ります） |

メニューは状態に合わせて変わります。アカウント未接続のときは **ログイン** が表示され、カーソルもそこに置かれます。ログインに成功するとその項目は消えます。

## ⚙️ 設定

| 項目 | 説明 |
|---|---|
| **実行モード** | `シングルスレッド`（既定）/ `マルチスレッド` — マルチは高速ですが並列リクエストを送ります |
| **言語** | `English` / `Русский` / `中文` — 即時反映され、次回も保持されます |
| **チャット数無制限** ⚠️ | 100 チャットの上限を解除し、`Start` が任意の数を受け付けます — 危険、既定はオフ |
| **有効な arena.ai アカウントを削除** | ブラウザプロファイルとセッションを消去（ログアウト）します |

設定は `~/.arena-model-hunter/config.json` に保存されます：

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **チャット数無制限は既定でオフで、警告は飾りではありません。** オンにすると `Start` は 1〜100 のチェックをやめて任意の数を受け付けます（`250`、`1000`）。1 チャットにつきタブ 2 つなので、大きな数は arena.ai への並列リクエストの集中を意味します。レート制限や captcha はまさにそのための仕組みで、アカウント制限の現実的なリスクがあります。納得したうえでだけ有効にし、シングルスレッドのまま使ってください。100 を超える数では、何かが開く前に正確な数を示す二度目の確認が出ます。

## 🔐 How signing in works

1. A **real** Chromium window opens with a persistent profile (`~/.arena-model-hunter/profile`) — headless browsers are rejected by Cloudflare, so the app never uses one.
2. You click `Log In` → enter your email → `Continue with email`.
   - Existing account → enter the password → `Log In`.
   - New email → the name step can be skipped → a link arrives by mail → paste it into the address bar (`Ctrl+L`, `Ctrl+V`, Enter) → create a password.
3. The app polls the page every 1.5 s and detects success by: your email appearing in the sidebar, an `arena-auth-*` cookie, and the `Log In` button disappearing.
4. It saves `session.json` + `state.json` and **closes the browser**.

The site always opens in **dark theme** (the browser is launched with `prefers-color-scheme: dark`, which arena.ai follows).

## ⚡ シングル／マルチスレッド

| モード | 動作 | 3 チャットでの実測 |
|---|---|---|
| **シングルスレッド**（既定） | タブのペアを 1 つずつ処理し、アクティブなタブを前面に出します | 約 7.5 分 |
| **マルチスレッド** | すべてのタブペアを同時に実行し、フォーカスは動かしません | 約 4.5 分 |

マルチスレッドでは Arena に複数リクエストが同時に届くため、レート制限や captcha が起きやすくなります。発生したらシングルスレッドに戻してください。

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

## 🧰 よくある質問

- **「Just a moment…」/ Cloudflare の確認** — 表示されるブラウザウィンドウが必要です。デスクトップのないサーバーでは動かさないでください。
- **「ブラウザがインストールされていません」** — `python -m playwright install chromium` を実行してください。
- **captcha が出る／送信されない** — レート制限の可能性大：シングルスレッドにして速度を落としてください。
- **最初からやり直したい** — 設定 → *有効な arena.ai アカウントを削除*、または `~/.arena-model-hunter` を削除。
- **夜通し探す** — 設定 → *チャット数無制限*、そして「開始」で `300` を入力して確認。シングルスレッドのままにし、朝に改名済みのチャットを見てください。

## ⚠️ 免責事項

本プロジェクトは **個人の実験と学習** のためのものです。第三者のサイトを自動化するため、arena.ai やフィンガープリントサイトの利用規約に反する可能性があり、アカウント制限につながることがあります。自己責任で使用し、不要な負荷をかけず、迷ったらシングルスレッドのままにし、認証情報は決して公開しないでください（本アプリはパスワードをディスクに保存しません）。

## 📄 ライセンス

[MIT](LICENSE) — 好きに使えます。保証はありません。

<div align="center">

**[⬆ トップへ](#-arena-model-hunter) · 🇺🇸 [Read in English](../../../README.md)**

</div>
