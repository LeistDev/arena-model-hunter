<div align="center">

🌐 **Available in:** [🇺🇸 English](../../../README.md) | [🇧🇷 Português (Brasil)](../pt-BR/README.md) | [🇪🇸 Español](../es/README.md) | [🇫🇷 Français](../fr/README.md) | [🇮🇹 Italiano](../it/README.md) | [🇷🇺 Русский](../ru/README.md) | [🇨🇳 中文 (简体)](../zh-CN/README.md) | [🇩🇪 Deutsch](../de/README.md) | [🇮🇳 हिन्दी](../in/README.md) | [🇹🇭 ไทย](../th/README.md) | [🇺🇦 Українська](../uk-UA/README.md) | [🇸🇦 العربية](../ar/README.md) | [🇯🇵 日本語](../ja/README.md) | **🇻🇳 Tiếng Việt** | [🇧🇬 Български](../bg/README.md) | [🇩🇰 Dansk](../da/README.md) | [🇫🇮 Suomi](../fi/README.md) | [🇮🇱 עברית](../he/README.md) | [🇭🇺 Magyar](../hu/README.md) | [🇮🇩 Bahasa Indonesia](../id/README.md) | [🇰🇷 한국어](../ko/README.md) | [🇲🇾 Bahasa Melayu](../ms/README.md) | [🇳🇱 Nederlands](../nl/README.md) | [🇳🇴 Norsk](../no/README.md) | [🇵🇹 Português (Portugal)](../pt/README.md) | [🇷🇴 Română](../ro/README.md) | [🇵🇱 Polski](../pl/README.md) | [🇸🇰 Slovenčina](../sk/README.md) | [🇸🇪 Svenska](../sv/README.md) | [🇵🇭 Filipino](../phi/README.md) | [🇨🇿 Čeština](../cs/README.md)

</div>

---

<div align="center">

# ✦ arena model hunter

**Thợ săn mô hình cho arena.ai: chạy một loạt cuộc trò chuyện ở chế độ agent, lấy dấu vân tay từng câu trả lời, xác định mô hình nào đã trả lời và đổi tên cuộc trò chuyện theo mô hình đó — sáng ra bạn có một cuộc trò chuyện được dán nhãn chạy Claude Opus, GPT-5, Gemini hoặc mô hình bạn đang tìm.**

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

## 🎯 Vì sao công cụ này tồn tại

Ở chế độ agent, arena.ai tự quyết định mô hình nào sẽ trả lời, và không phải lúc nào cũng là mô hình bạn muốn: khi thì một mô hình hàng đầu (Claude Opus và đồng loại), khi thì thứ yếu hơn nhiều. Công cụ này biến cuộc xổ số đó thành một cuộc tìm kiếm: mở một loạt cuộc trò chuyện agent, chạy lại ba mẫu dấu vân tay trong từng cuộc, hỏi trang dấu vân tay xem mô hình nào đã trả lời rồi ghi kết luận vào tiêu đề cuộc trò chuyện (`claude-opus-4 99.9%`, `gpt-5.2 87%`). Cứ để nó chạy qua đêm với số cuộc tùy thích; sáng ra đã có danh sách dán nhãn: mở cuộc có tiêu đề là mô hình bạn cần và làm việc trong đó. Ý nghĩa nằm ở đây — không phải tự động hóa cho có, mà là **có được một cuộc trò chuyện thật sự chạy trên mô hình bạn muốn**.

## ✨ Ứng dụng làm gì

- **Đăng nhập một lần — phiên được giữ.** Một cửa sổ Chromium thật (không headless) mở ra, bạn đăng nhập arena.ai như bình thường; ứng dụng phát hiện, lưu phiên và tự đóng trình duyệt.
- **N cuộc trò chuyện cùng lúc.** Bạn nhập số từ 1 đến 100 — mở đúng số tab `arena.ai/agent` và cũng bấy nhiêu tab `lm.ikale.io`.
- **Sao chép thay bạn.** Prompt của từng mẫu được gửi tới agent, chờ câu trả lời đầy đủ rồi dán vào ô Reply — ba mẫu cho mỗi cuộc trò chuyện.
- **Nhận diện mô hình.** Nhấn Verify trên trang dấu vân tay, đọc ứng viên hàng đầu và độ tin cậy đúng như trang hiển thị, rồi đổi tên cuộc trò chuyện Arena thành `mô hình độ tin cậy` (ví dụ `gpt-6-luna 99.9%`).
- **Hai chế độ chạy.** Đơn luồng (an toàn, lần lượt từng cuộc) và đa luồng (tất cả song song, nhanh hơn 1,5–2×).
- **Giao diện ba ngôn ngữ.** English, Русский, 中文 — đổi ngay trong ứng dụng, không cần khởi động lại.

## 🔄 Một lượt chạy diễn ra thế nào

1. **Đăng nhập** — trình duyệt mở ra, bạn xác thực, ứng dụng phát hiện và đóng cửa sổ.
2. **Bắt đầu → số cuộc trò chuyện** — ví dụ `3`: ba tab Arena và ba tab dấu vân tay.
3. **Mẫu 1 → 3** — mỗi prompt đi tới agent, mỗi câu trả lời quay lại trang.
4. **Verify** — trang xếp hạng các mô hình ứng viên, ứng dụng đọc mô hình thắng và độ tin cậy.
5. **Đổi tên** — cuộc trò chuyện Arena mang tên `mô hình độ tin cậy`, và bản tóm tắt hiện trong console.

## 📋 Yêu cầu

- Python **3.10+**
- Windows 10/11, macOS hoặc Linux
- Tài khoản arena.ai (email và mật khẩu hoặc liên kết qua email)
- ~400 MB dung lượng trống cho Chromium của Playwright

## 🚀 Cài đặt

```bash
git clone https://github.com/LeistDev/arena-model-hunter.git
cd arena-model-hunter

pip install -r requirements.txt
python -m playwright install chromium
```

**Windows:** sau đó chỉ cần nhấp đúp vào `run.bat` (bật UTF-8 để chữ Kirin hiển thị đúng).
**macOS / Linux:** `./run.sh` hoặc `python main.py`.

## 🕹️ Cách dùng

```bash
python main.py
```

| Tuỳ chọn | Mô tả |
|---|---|
| **Bắt đầu** | hỏi số cuộc trò chuyện (1–100, hoặc bất kỳ số nào khi bật không giới hạn) rồi chạy toàn bộ quy trình |
| **Cài đặt** | chế độ chạy, ngôn ngữ giao diện, xoá tài khoản arena.ai đang hoạt động |
| **Thoát** | đóng ứng dụng (terminal trở lại nội dung trước đó) |

Menu thích ứng theo trạng thái: khi chưa kết nối tài khoản, mục **Đăng nhập** được hiển thị và con trỏ đặt ở đó; sau khi đăng nhập thành công, mục này biến mất.

## ⚙️ Cài đặt

| Tuỳ chọn | Mô tả |
|---|---|
| **Chế độ chạy** | `đơn luồng` (mặc định) / `đa luồng` — đa luồng nhanh hơn nhưng gửi yêu cầu song song |
| **Ngôn ngữ** | `English` / `Русский` / `中文` — áp dụng ngay và được ghi nhớ |
| **Không giới hạn số cuộc** ⚠️ | bỏ mức trần 100 cuộc: `Start` nhận bất kỳ con số nào — nguy hiểm, mặc định tắt |
| **Xoá tài khoản arena.ai đang hoạt động** | xoá hồ sơ trình duyệt và phiên, tức là đăng xuất |

Cài đặt nằm trong `~/.arena-model-hunter/config.json`:

```json
{ "parallel": false, "lang": "en", "unlimited": false }
```

⚠️ **Không giới hạn số cuộc mặc định tắt, và cảnh báo này không phải cho có.** Khi bật, `Start` thôi kiểm tra khoảng 1–100 và nhận bất kỳ số nào — `250`, `1000`. Mỗi cuộc là hai tab, nên con số lớn nghĩa là một loạt yêu cầu song song dồn tới arena.ai: đúng kiểu mà giới hạn tần suất và captcha sinh ra để chặn, kèm nguy cơ thật về việc tài khoản bị hạn chế. Chỉ bật khi bạn chấp nhận điều đó, và giữ chế độ một luồng; mọi giá trị trên 100 sẽ hỏi xác nhận lần hai với con số chính xác trước khi mở bất cứ thứ gì.

## 🔐 Cách hoạt động của việc đăng nhập

1. Một cửa sổ Chromium **thật** mở ra với hồ sơ lưu bền (`~/.arena-model-hunter/profile`) — Cloudflare từ chối trình duyệt headless, nên ứng dụng không bao giờ dùng.
2. Bạn bấm `Log In` → nhập email → `Continue with email`.
   - Đã có tài khoản → nhập mật khẩu → `Log In`.
   - Email mới → bước nhập tên có thể bỏ qua → thư có liên kết được gửi tới → dán vào thanh địa chỉ (`Ctrl+L`, `Ctrl+V`, Enter) → tạo mật khẩu.
3. Ứng dụng kiểm tra trang mỗi 1,5 giây và nhận biết đăng nhập thành công qua ba dấu hiệu: email xuất hiện ở thanh bên, cookie `arena-auth-*` xuất hiện, nút `Log In` biến mất.
4. Sau đó nó lưu `session.json` + `state.json` và **đóng trình duyệt**.

Trang luôn mở ở **giao diện tối** (trình duyệt khởi chạy với `prefers-color-scheme: dark`, và arena.ai tuân theo thiết lập này).

## ⚡ Chế độ đơn luồng và đa luồng

| Chế độ | Cách hoạt động | Đo trên 3 cuộc trò chuyện |
|---|---|---|
| **Đơn luồng** (mặc định) | các cặp tab được xử lý lần lượt, tab đang dùng được đưa lên trước | ≈7,5 phút |
| **Đa luồng** | tất cả các cặp tab chạy đồng thời, không chuyển tiêu điểm | ≈4,5 phút |

Ở chế độ đa luồng, Arena nhận nhiều yêu cầu cùng lúc nên dễ gặp giới hạn và captcha hơn. Nếu điều đó xảy ra, hãy quay lại chế độ đơn luồng.

## 🗂️ Cấu trúc dự án

```
arena-model-hunter/
├── main.py             # menu, cài đặt, kịch bản
├── ui.py               # giao diện terminal: khung, alt-screen, đọc phím, thay đổi kích thước
├── arena_login.py      # trình duyệt, đăng nhập, nhận diện phiên, cấu hình
├── flow.py             # quy trình Arena ↔ lm.ikale.io, Verify, đổi tên
├── i18n.py             # bản dịch giao diện (en / ru / zh)
├── requirements.txt
├── run.bat / run.sh
├── .github/workflows/  # CI: lint và kiểm tra bản dịch
├── LICENSE
└── docs/i18n/          # README này bằng 30 ngôn ngữ
```

## 🌍 Biến môi trường

| Biến | Mặc định | Công dụng |
|---|---|---|
| `ARENA_HUNTER_HOME` | `~/.arena-model-hunter` | thư mục hồ sơ và phiên |
| `ARENA_HELPER_HOME` | — | tên cũ của biến, vẫn được hỗ trợ |
| `ARENA_EMAIL` / `ARENA_PASSWORD` | — | tự điền biểu mẫu (không bao giờ lưu) |
| `ARENA_LOGIN_TIMEOUT` | `900` | số giây chờ đăng nhập |
| `ARENA_URL` | `https://arena.ai/` | URL khởi đầu |

## 🧰 Câu hỏi thường gặp

- **«Just a moment…» / kiểm tra Cloudflare** — cần cửa sổ trình duyệt hiển thị; không chạy trên server không có màn hình.
- **«Trình duyệt chưa được cài»** — chạy `python -m playwright install chromium`.
- **Captcha hoặc yêu cầu không được gửi** — có thể bạn đã chạm giới hạn: bật đơn luồng và chậm lại.
- **Muốn bắt đầu lại từ đầu** — Cài đặt → *Xoá tài khoản arena.ai đang hoạt động*, hoặc xoá `~/.arena-model-hunter`.
- **Săn cả đêm** — Cài đặt → *Không giới hạn số cuộc*, rồi nhập `300` ở Bắt đầu và xác nhận; giữ chế độ một luồng và xem các cuộc đã đổi tên vào buổi sáng.

## ⚠️ Miễn trừ trách nhiệm

Dự án dành cho **thử nghiệm cá nhân và học tập**. Nó tự động hoá một trang web của bên thứ ba; việc tự động hoá có thể vi phạm điều khoản của arena.ai và trang dấu vân tay, đồng thời dẫn tới hạn chế tài khoản. Hãy dùng với rủi ro của riêng bạn, đừng tạo tải không cần thiết, khi phân vân hãy giữ chế độ đơn luồng và không bao giờ công bố dữ liệu của mình — ứng dụng không lưu mật khẩu ra đĩa.

## 📄 Giấy phép

[MIT](LICENSE) — phần mềm tự do: bạn có thể dùng, nghiên cứu, chia sẻ và sửa đổi. Nếu phân phối chương trình hoặc bản đã sửa, bạn phải giữ lại thông báo bản quyền và nội dung giấy phép MIT. Không có bảo hành.

Copyright (C) 2026 những người đóng góp cho arena model hunter.

