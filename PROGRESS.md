# PROGRESS.md – Mục tiêu & tiến độ dự án TOTK Guide

> File này là **nguồn duy nhất** ghi tiến độ. Cập nhật ngay sau mỗi vùng (bảng trạng thái + mục "Còn tồn đọng").
> Quy trình chi tiết: `docs/workflow-region.md`. Chuẩn dịch: `docs/translation-standard.md`.

## Mục tiêu tổng quát
Website hướng dẫn chơi The Legend of Zelda: Tears of the Kingdom bằng tiếng Việt, đầy đủ theo
Game Progress Route + Walkthrough của fextralife, có ảnh minh họa khớp đúng từng bước,
host trên Vercel, không link ra domain khác.

## Cấu trúc chuẩn (đã chốt)
- 9 vùng = 9 trang riêng `pages/route-<slug>.html`, đúng thứ tự fextralife:
  1. `prologue` – Prologue & Great Sky Island (19 bước)
  2. `central` – Central Hyrule (27)
  3. `hebra` – Hebra (31)
  4. `eldin` – Eldin (25)
  5. `lanayru` – Lanayru (36)
  6. `mastersword` – Master Sword (14)
  7. `gerudo` – Gerudo (23)
  8. `fifth` – Fifth Sage (35)
  9. `final` – Demon King (14)
- Mỗi trang: header chung (crumb + h1 + chip số bước/mục/ảnh) rồi 2 cột trong `.container.layout`:
  - cột trái `aside.sidebar.rail` (sticky): mục lục vùng + danh sách bước index (tiếng Việt, không ảnh);
  - cột phải `main.content`: walkthrough, `<h3>` bám đúng subsection của fextralife,
    ảnh để trong `<details>` đặt **ngay sau đoạn mà ảnh minh họa**.
- Heading `h2`/`h3`: **tiếng Anh gốc + "(chú thích tiếng Việt)"**.
- **Ảnh tách riêng theo trang**: `pages/route-<slug>.html` ↔ `images/<slug>/`, không dùng chung,
  không copy ảnh giữa các vùng. Giữ nguyên tên file gốc fextralife (không thêm tiền tố lạ).

## Tiêu chí verify (bắt buộc pass trước khi coi 1 vùng là xong)
1. `python scripts/verify-regions.py`:
   - `step = want` (số bước index = số bước fextralife) và **`cover` đủ số bước**;
   - `img = uni` (không ảnh trùng), `ms = 0` (không ảnh thiếu file), `uni` = số file trong `images/<slug>/`
     (không file thừa), `en = 0`, `xN = 0`, `ph = 0`, layout `2col`.
2. `python scripts/check-vietnamese.py` → **0 lỗi HARD** cho vùng đó.
3. Thẻ HTML cân bằng; mọi `src="../images/..."` tồn tại; không còn reference tới file đã xoá.
   (Repo **không có** `audit.py` — đừng chạy.)
4. Nội dung 100% tiếng Việt theo `docs/translation-standard.md`: không Vietglish, đại từ "bạn",
   đủ ý đi đâu / làm gì / nhận gì; giữ tên riêng, dịch thuật ngữ theo glossary.
5. Ảnh: mỗi nhóm ảnh nằm đúng subsection nguồn; caption/alt = tên bước + `(ảnh k/N)`;
   không thêm ảnh/logo ngoài nguồn.
6. Commit riêng cho từng vùng → push `master` → Vercel deploy → HTTP 200 cho trang và ảnh mới.

## Trạng thái hiện tại (cập nhật 2026-11-02)
| Vùng | Bước | Độ phủ | Ảnh (img=uni) | Ảnh khớp subsection | Trạng thái |
|---|---|---|---|---|---|
| 1. Prologue & Great Sky Island | 19/19 | 19/19 | 77 | ✅ đã rà soát | ✅ xong |
| 2. Central Hyrule | 27/27 | 27/27 | 34 | ✅ đã rà soát | ✅ xong |
| 3. Hebra | 31/31 | 31/31 | 80 | ✅ đã rà soát | ✅ xong |
| 4. Eldin | 25 | — | 0 | — | ⬜ mới có index phẳng |
| 5. Lanayru | 36 | — | 0 | — | ⬜ mới có index phẳng |
| 6. Master Sword | 14 | — | 0 | — | ⬜ mới có index phẳng |
| 7. Gerudo | 23 | — | 0 | — | ⬜ mới có index phẳng |
| 8. Fifth Sage | 35 | — | 0 | — | ⬜ mới có index phẳng |
| 9. Demon King | 14 | — | 0 | — | ⬜ mới có index phẳng |

Ba vùng đã xong đều `hard=0`, `en=0`, `xN=0`, `ph=0`, `ms=0`, layout `2col`.

### Việc đã làm ngoài nội dung vùng
- Rà soát lại **ảnh theo đúng subsection nguồn** cho vùng 1–3: trước đây ảnh bị chia theo thứ tự file
  nên lệch bước (Prologue/Central còn lẫn ảnh vùng khác; Hebra lệch từ mục 7). Đã tải đủ ảnh còn thiếu
  (Prologue 77, Central 34, Hebra 80), bỏ ảnh trùng/logo ngoài nguồn, chuẩn hoá tên file.
- Tách folder ảnh theo trang: `images/gsi` → `images/prologue`.
- `docs/workflow-region.md`: chuẩn hoá cách lấy nội dung/ảnh (nhiều trang Subcontent, giữ tên file gốc,
  bản full qua trang `File:`, ảnh đặt ngay sau đoạn minh họa, caption theo tên bước).
- `docs/agents/`: cấu hình issue tracker (GitHub Issues), nhãn triage, domain docs.

## Còn tồn đọng
1. **Vùng 4–9** (eldin, lanayru, mastersword, gerudo, fifth, final): chỉ có index phẳng, 0 ảnh,
   không có walkthrough. `verify-regions` báo `stub`; `check-vietnamese` còn HARD:
   eldin 17, lanayru 8, mastersword 9, gerudo 5, fifth 8, final 4.
2. Các trang phụ còn Vietglish/HARD: `shrines.html` 282, `mechanics.html` 9, `tips.html` 5,
   `abilities.html` 2, `index.html` 1, `faq.html` 1.
   Toàn site hiện **351 lỗi HARD**, trong đó 3 vùng đã xong = 0.
3. Một số ảnh vùng 1–3 chỉ có bản 400px (fextralife chặn tải bản gốc / trả 429) — chấp nhận được,
   nâng cấp sau nếu cần nét hơn.

## Thứ tự thực hiện tiếp
1. Vùng 4 Eldin theo quy trình `docs/workflow-region.md` (lấy đủ trang nguồn → tải ảnh vào `images/eldin/`
   → dịch → đặt ảnh đúng subsection → verify → commit/push).
2. Lần lượt 5 → 9, mỗi vùng một commit riêng.
3. Dọn HARD cho shrines / mechanics / abilities / tips / index / faq.
4. Cập nhật lại bảng trạng thái và mục "Còn tồn đọng" trong file này sau mỗi vùng.

## Lệnh kiểm tra nhanh
```
python scripts/verify-regions.py
python scripts/check-vietnamese.py
```
