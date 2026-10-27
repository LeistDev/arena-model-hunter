<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | [🇻🇳 Tiếng Việt](../vi/README.md) | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | **🇰🇷 한국어** | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**arena.ai를 위한 모델 사냥꾼: 에이전트 채팅을 여러 개 돌리고, 모든 답변의 지문을 확인해 어떤 모델이 답했는지 알아낸 뒤 그 이름으로 채팅 이름을 바꿉니다. 아침이면 Claude Opus, GPT-5, Gemini 혹은 찾고 있던 모델로 동작하는 채팅이 라벨과 함께 남아 있습니다.**

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

## 🎯 왜 만들었나

에이전트 모드에서 어떤 모델이 답할지는 arena.ai가 스스로 정하며, 항상 원하는 모델은 아닙니다. 최상위 모델(Claude Opus 등)이 걸릴 때도 있고, 훨씬 약한 모델이 걸릴 때도 있습니다. 이 도구는 그 복권을 탐색으로 바꿉니다. 에이전트 채팅을 여러 개 열고, 각 채팅에서 세 개의 지문 샘플을 모두 돌리고, 지문 사이트에 어떤 모델이 답했는지 물어본 다음 그 판정을 채팅 제목에 적습니다(`claude-opus-4 99.9%`, `gpt-5.2 87%`). 원하는 만큼 채팅을 열어 밤새 돌려 두면, 아침에는 라벨이 붙은 목록이 생깁니다. 필요한 모델 이름이 붙은 채팅을 열어 그대로 작업하면 됩니다. 핵심은 이것입니다. 자동화를 위한 자동화가 아니라, 정말로 원했던 모델 위에서 돌아가는 채팅을 얻는 것.

## ✨ 기능

- **한 번만 로그인하면 세션이 유지됩니다.** 실제(헤드리스 아님) Chromium 창이 열리고 평소처럼 arena.ai에 로그인합니다. 앱이 로그인을 감지해 세션을 저장하고 브라우저를 스스로 닫습니다.
- **N개 채팅 동시 실행.** 1~100 사이의 숫자를 입력하면 정확히 그 수만큼 `arena.ai/agent` 탭과 같은 수의 `lm.ikale.io` 탭이 열립니다.
- **복사·붙여넣기를 대신합니다.** 각 샘플의 프롬프트를 에이전트에게 보내고, 답변이 완전히 끝날 때까지 기다린 뒤 Reply 입력란에 붙여넣습니다. 채팅당 3개 샘플.
- **모델을 판별합니다.** 지문 사이트에서 Verify를 누르고, 사이트가 보여주는 그대로 최상위 후보와 신뢰도를 읽어 Arena 채팅 이름을 `모델 신뢰도`(예: `gpt-6-luna 99.9%`)로 바꿉니다.
- **두 가지 실행 모드.** 단일 스레드(안전, 한 번에 하나)와 멀티 스레드(모두 병렬, 1.5~2배 빠름).
- **3개 언어 인터페이스.** English, Русский, 中文 — 앱 안에서 전환, 재시작 불필요.

## 🔄 실행 과정

1. **로그인** — 브라우저가 열리고 인증하면 앱이 감지해 창을 닫습니다.
2. **시작 → 채팅 수** — 예: `3`이면 Arena 탭 3개와 지문 탭 3개.
3. **샘플 1 → 3** — 각 프롬프트는 에이전트로, 각 답변은 사이트로 돌아갑니다.
4. **Verify** — 사이트가 후보 모델을 순위화하고 앱이 1위와 신뢰도를 읽습니다.
5. **이름 변경** — Arena 채팅이 `모델 신뢰도`가 되고 콘솔에 요약이 표시됩니다.

## 📋 요구 사항

- Python **3.10+**
- Windows 10/11, macOS 또는 Linux
- arena.ai 계정(이메일+비밀번호 또는 메일로 받은 링크)
- Playwright Chromium용 약 400MB 여유 공간

## 🚀 설치

```bash
git clone <this-repo> arena-model-hunter
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** 이후에는 `run.bat`을 더블클릭하면 됩니다(UTF-8을 켜서 키릴 문자도 제대로 표시).
**macOS / Linux:** `./run.sh` 또는 `python main.py`.

## 🕹️ 사용법

```bash
python main.py
```

| 옵션 | 설명 |
|---|---|
| **시작** | 채팅 수를 묻고(1–100, 무제한이면 아무 숫자나) 전체 과정을 시작합니다 |
| **설정** | 실행 모드, 인터페이스 언어, 활성 arena.ai 계정 삭제 |
| **종료** | 앱을 닫습니다(터미널은 이전 내용으로 돌아갑니다) |

메뉴는 상태에 맞춰 바뀝니다. 계정이 연결되지 않았을 때는 **로그인** 항목이 나타나고 커서가 그곳에 있습니다. 로그인에 성공하면 그 항목은 사라집니다.

## ⚙️ 설정

| 옵션 | 설명 |
|---|---|
| **실행 모드** | `단일 스레드`(기본) / `멀티 스레드` — 멀티가 더 빠르지만 병렬 요청을 보냅니다 |
| **언어** | `English` / `Русский` / `中文` — 즉시 적용되고 기억됩니다 |
| **채팅 수 무제한** ⚠️ | 채팅 100개 상한을 해제해 `Start`가 아무 숫자나 받습니다 — 위험, 기본값은 꺼짐 |
| **활성 arena.ai 계정 삭제** | 브라우저 프로필과 세션을 지워 로그아웃합니다 |

설정은 `~/.arena-model-hunter/config.json`에 저장됩니다:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **채팅 수 무제한은 기본값이 꺼짐이며, 경고는 장식이 아닙니다.** 켜면 `Start`가 1–100 검사를 멈추고 아무 숫자나 받습니다(`250`, `1000`). 채팅 하나에 탭 두 개이므로 큰 숫자는 arena.ai로 동시에 몰리는 요청 폭주를 뜻합니다. 속도 제한과 캡차가 존재하는 바로 그 패턴이며 계정 제한 위험이 실제로 있습니다. 감수할 수 있을 때만 켜고 단일 스레드 모드를 유지하세요. 100을 넘으면 열기 전에 정확한 개수를 담은 두 번째 확인을 요구합니다.

## 🔐 로그인은 어떻게 동작하나

1. 영구 프로필을 쓰는 **실제** Chromium 창이 열립니다(`~/.arena-model-hunter/profile`). Cloudflare가 헤드리스 브라우저를 거부하기 때문에 앱은 절대 헤드리스로 실행하지 않습니다.
2. `Log In` 을 누르고 → 이메일을 입력하고 → `Continue with email`.
   - 기존 계정 → 비밀번호 입력 → `Log In`.
   - 새 이메일 → 이름 단계는 건너뛸 수 있음 → 메일로 링크가 오면 → 주소창에 붙여넣기(`Ctrl+L`, `Ctrl+V`, Enter) → 비밀번호 생성.
3. 앱은 1.5초마다 페이지를 확인하며 세 가지 신호로 로그인 성공을 판단합니다: 사이드바에 이메일이 나타남, `arena-auth-*` 쿠키 생성, `Log In` 버튼 사라짐.
4. 그다음 `session.json` 과 `state.json` 을 저장하고 **브라우저를 닫습니다**.

사이트는 항상 **다크 테마**로 열립니다(브라우저를 `prefers-color-scheme: dark` 로 실행하며 arena.ai가 이를 따릅니다).

## ⚡ 단일 스레드와 멀티 스레드

| 모드 | 동작 방식 | 3개 채팅 측정 |
|---|---|---|
| **단일 스레드** (기본) | 탭 쌍을 하나씩 처리하고 활성 탭을 앞으로 가져옵니다 | 약 7.5분 |
| **멀티 스레드** | 모든 탭 쌍을 동시에 실행하며 포커스를 옮기지 않습니다 | 약 4.5분 |

멀티 스레드에서는 Arena가 여러 요청을 동시에 받으므로 속도 제한이나 captcha가 더 잘 생깁니다. 그런 경우 단일 스레드로 되돌리세요.

## 🗂️ 프로젝트 구조

```
arena-model-hunter/
├── main.py             # 메뉴, 설정, 시나리오
├── ui.py               # 터미널 UI: 프레임, alt-screen, 키 입력, 창 크기 변경
├── arena_login.py      # 브라우저, 로그인, 세션 감지, 설정
├── flow.py             # Arena ↔ lm.ikale.io 파이프라인, Verify, 이름 변경
├── i18n.py             # UI 번역(en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI: 린트와 번역 검사
├── LICENSE
└── docs/i18n/          # 이 README의 30개 언어판
```

## 🌍 환경 변수

| 변수 | 기본값 | 용도 |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | 프로필과 세션 폴더 |
| `ARENA_HELPER_HOME` | — | 변수의 옛 이름, 계속 지원됨 |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | 선택적 폼 자동 채우기(저장되지 않음) |
| `ARENA_LOGIN_TIMEOUT` | `900` | 로그인을 기다리는 시간(초) |
| `ARENA_URL` | `https://arena.ai/` | 시작 URL |

## 🧰 자주 묻는 질문

- **「Just a moment…」/ Cloudflare 확인** — 보이는 브라우저 창이 필요합니다. 데스크톱이 없는 서버에서는 실행하지 마세요.
- **「브라우저가 설치되지 않았습니다」** — `python -m playwright install chromium`을 실행하세요.
- **captcha가 뜨거나 요청이 조용히 무시됨** — 대개 속도 제한입니다. 단일 스레드로 바꾸고 속도를 낮추세요.
- **처음부터 다시 하고 싶다면** — 설정 → *활성 arena.ai 계정 삭제*, 또는 `~/.arena-model-hunter` 폴더를 삭제하세요.
- **밤새 사냥하기** — 설정 → *채팅 수 무제한*, 이어서 시작 화면에서 `300`을 입력하고 확인하세요. 단일 스레드를 유지하고 아침에 이름이 바뀐 채팅을 확인하면 됩니다.

## ⚠️ 면책 고지

이 프로젝트는 **개인 실험과 학습**을 위한 것입니다. 제3자 사이트를 자동화하므로 arena.ai 및 지문 사이트의 이용 약관에 위배될 수 있고 계정 제한으로 이어질 수 있습니다. 본인 책임하에 사용하고, 불필요한 부하를 만들지 말고, 확신이 없으면 단일 스레드를 유지하며, 자격 증명을 절대 공개하지 마세요(앱은 비밀번호를 디스크에 저장하지 않습니다).

## 📄 라이선스

[GNU General Public License v3.0](LICENSE) — 자유 소프트웨어입니다. 사용·연구·공유·수정할 수 있습니다. 프로그램이나 수정본을 배포하면 GPL을 유지해야 하고 소스 코드도 계속 공개되어야 합니다. 보증은 없습니다.

Copyright (C) 2026 arena model hunter 기여자.

