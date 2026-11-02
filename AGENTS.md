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
- Trước khi commit: `python scripts/check-vietnamese.py` phải trả về **0 lỗi HARD**.

## Nguồn nội dung
- Nguồn chính: fextralife (Game Progress Route + Walkthrough) cho TOTK.
- fextralife bị chặn trực tiếp ở VN → truy cập qua **Google Translate proxy**:
  `https://translate.google.com/translate?sl=en&tl=vi&u=<URL>`
- Ảnh từ `static0.fextralifeimages.com` (tải về `images/<region>/`, giữ tên file gốc).

## Cấu trúc trang
- Canonical progress route: hub `pages/progress-route.html` + 9 trang vùng `pages/route-<slug>.html`
  (slug: prologue, central, hebra, eldin, lanayru, mastersword, gerudo, fifth, final).
- Mỗi trang vùng: cột trái sticky là mục lục + danh sách bước, cột phải là walkthrough.
- Giữ multi-page: mechanics, abilities, shrines, tips, faq, index.
- Mỗi trang: 1 `<h1>`, meta description, alt text tiếng Việt.
- **Ảnh tách riêng theo trang**: `pages/route-<slug>.html` chỉ dùng ảnh trong `images/<slug>/`. Cấm dùng chung folder, cấm copy ảnh của vùng khác sang (lỗi đã gặp: 12 ảnh Prologue nằm trong `images/central`).

## Kiểm tra trước commit
- `python scripts/verify-regions.py` → mỗi vùng `step/want` khớp, `cover` đủ bước, `img = uni`, `ms=0`, `en=0`, `ph=0`, layout `2col`.
- `python scripts/check-vietnamese.py` → 0 lỗi HARD.
- HTML balanced, mọi `src` ảnh tồn tại, và không file nào trong `images/<slug>/` bị bỏ không dùng.
- Không còn reference đến trang/file đã xóa.

## Quy trình Phase B
- Lần lượt từng vùng (index 1): lấy nội dung nguồn → tải ảnh → dịch theo `docs/translation-standard.md` → trình bày (index trái + walkthrough phải) → verify-regions + check-vietnamese → commit riêng → push/deploy → requesting-code-review.
- Loop executing-plans + requesting-code-review cho đến khi chuẩn xác mới chuyển vùng tiếp.

## Commit & Deploy
- Commit message rõ ràng theo task (Phase/Task + tên vùng).
- Push origin master → Vercel auto-deploy; verify HTTP 200 cho trang và ảnh.

## Agent skills

### Issue tracker

Issue và đặc tả sống trên GitHub Issues của `phucnd0604/toto-guide`, thao tác bằng `gh` CLI. Xem `docs/agents/issue-tracker.md`.

### Triage labels

Dùng bộ 5 label mặc định: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. Xem `docs/agents/triage-labels.md`.

### Domain docs

Single-context: `GLOSSARY.md` + `docs/adr/` ở gốc repo. Xem `docs/agents/domain.md`.

