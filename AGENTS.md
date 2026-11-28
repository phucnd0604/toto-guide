# AGENTS.md – Quy tắc dự án TOTK Guide

## Ngôn ngữ nội dung (bắt buộc)
- Toàn bộ nội dung hiển thị trên site phải là **tiếng Việt tự nhiên**, đọc như người Việt viết — không phải bản dịch máy.
- **Chuẩn dịch đầy đủ: `docs/translation-standard.md`** (nguyên tắc viết lại câu, bảng thuật ngữ, blacklist Vietglish, ví dụ before/after). Đọc file đó trước khi viết hoặc sửa nội dung.
- 5 điều không được vi phạm:
  1. Dịch theo **ý** rồi viết lại thành câu tiếng Việt hoàn chỉnh; cấm câu nửa Việt nửa Anh (Vietglish).
  2. Thuật ngữ trong bảng glossary phải dịch đúng như bảng (Ultrahand → Siêu Tay, Ascend → Xuyên, Shrine → Đền Thờ Nhỏ, Skyview Tower → Tháp Quan Sát, Light of Blessing → Ánh Sáng Chúc Phúc, …).
  3. Chỉ giữ nguyên tên riêng: nhân vật, vùng, địa điểm, Đền Thờ Nhỏ/Đền Thờ, quái, tên nhiệm vụ, item đặc thù. Phần từ chung đi kèm thì dịch (Rito Village → Làng Rito).
  4. Không dùng `x1/x3`; viết "1", "3" hoặc "1 chiếc", "3 viên".
  5. Heading, tiêu đề, alt text, figcaption, summary cũng phải tiếng Việt.
- Trước khi commit: `python tool/check-vietnamese.py` phải trả về **0 lỗi HARD**.

## Thư mục làm việc & nơi lưu đặc tả (chốt 2026-11-28)
- **`.scratch/`** – file tạm, file sinh ra trong quá trình làm việc, file rác, bản nháp. Đã gitignore, **không commit**.
- **`tool/`** – script, công cụ chuẩn của dự án cần chạy trong quá trình làm việc (generator, các cổng kiểm tra). **Có commit**.
- **`scripts/`** – di sản của bộ 9 vùng fextralife, xoá ở vé chuyển nhà (T29). Tool mới **không** đặt ở đây.
- **Đặc tả, plan, ticket sống trên GitHub Issues**, không tạo file spec/plan trong repo:
  - Bản đồ công việc: https://github.com/phucnd0604/toto-guide/issues/1
  - Đặc tả kỹ thuật: https://github.com/phucnd0604/toto-guide/issues/33
  - Không thêm file mới vào `docs/superpowers/specs/` hay `docs/superpowers/plans/` (thư mục này đã xoá).

## Nguồn nội dung
- Nguồn chính: **zeldacentral.com**, mỗi chương một trang
  `https://zeldacentral.com/games/tears-of-the-kingdom/walkthrough/<slug>/`.
- Tải trực tiếp được. Chỉ khi bị 429 mới dùng proxy Google Translate:
  `https://translate.google.com/translate?sl=en&tl=vi&u=<URL>`.
- Ảnh: `zeldacentral.com/wp-content/uploads/totk/images/...`; tải bản 1024px, lưu vào
  `images/<loại>/<slug>/` với **tên gốc đã bỏ hậu tố kích thước `-1024x576`** (cổng ảnh so theo tên đã chuẩn hoá).
- Bộ 9 vùng fextralife đã ngừng dùng; quy tắc cũ nằm ở `docs/legacy-fextralife.md`, chỉ còn hiệu lực tới T29.

## Cổng kiểm tra (bảy cổng, bắt buộc trước mỗi commit)
Trang trong `pages/` là **sản phẩm sinh ra** từ `content/`: sửa `content/<loại>/<slug>.json` +
`.body.html` rồi chạy `python tool/build-pages.py`. Không sửa tay file trong `pages/`.

1. `python tool/build-pages.py --check` → 0 file lệch
2. `python tool/check-links.py` → 0 link chết, 0 ảnh thiếu, 0 link ra domain ngoài (trừ Google Fonts)
3. `python tool/verify-pages.py` → HARD=0
4. `python tool/check-image-match.py` → FAIL=0 (đối chiếu cache nguồn `.tmp-src/`; `--refresh` để tải lại)
5. `python tool/check-vietnamese.py` → HARD=0 toàn site
6. `python tool/check-mobile.py` → không trang nào tràn ngang ở 375px/768px (cần Chrome headless)
7. `python tool/check-coverage.py` → mục nào của nguồn cũng còn nội dung trong bản dịch

- Chi tiết hợp đồng từng cổng (cách tách "mục", cách đối chiếu ảnh, cách chuẩn hoá tên file):
  **`tool/README.md`**.
- Ảnh của một trang nằm đúng trong `images/<loại>/<slug>/`; mọi file trong folder phải được dùng,
  không dùng chéo giữa các trang.
- 3 script trong `scripts/` là di sản bộ 9 vùng; kết quả của chúng **không** dùng làm bằng chứng cho trang mới.

## Xem và đo trang local
- `python tool/preview.py` → mở `http://127.0.0.1:8765/pages/progress-route.html`
  (trình duyệt và Playwright **chặn `file://`**, nên phải xem qua server này).
- `python tool/check-mobile.py --width 375 <trang.html>` đo một trang cụ thể.

## Commit & Deploy
- Commit message rõ ràng theo vé; mỗi vé một commit (hoặc vài commit trong cùng vé).
- Push `origin master` → Vercel auto-deploy; kiểm HTTP 200 cho trang mới và 1 ảnh mẫu.
- CI `.github/workflows/gates.yml` chạy lại các cổng sau mỗi lần push.

## Agent skills

### Issue tracker

Issue và đặc tả sống trên GitHub Issues của `phucnd0604/toto-guide`, thao tác bằng `gh` CLI. Xem `docs/agents/issue-tracker.md`.

### Triage labels

Dùng bộ 5 label mặc định: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. Xem `docs/agents/triage-labels.md`.

### Domain docs

Single-context: từ vựng dự án ở `GLOSSARY.md`, quyết định kiến trúc ở `docs/adr/`, chuẩn dịch tiếng Việt ở
`docs/translation-standard.md`. Xem `docs/agents/domain.md`.

### Log phiên (khi làm retro)

Log phiên là nhiều frame zstd nối tiếp và công cụ giải nén thông thường chỉ đọc frame đầu. Cách đọc:
`docs/agents/session-log.md`.
