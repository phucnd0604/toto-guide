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

## Trạng thái hiện tại (cập nhật 2026-11-23)
| Vùng | Bước | Độ phủ | Ảnh (img=uni) | Ảnh khớp subsection | Trạng thái |
|---|---|---|---|---|---|
| 1. Prologue & Great Sky Island | 19/19 | 19/19 | 77 | ✅ đã rà soát | ✅ xong |
| 2. Central Hyrule | 27/27 | 27/27 | 34 | ✅ đã rà soát | ✅ xong |
| 3. Hebra | 31/31 | 31/31 | 80 | ✅ đã rà soát | ✅ xong |
| 4. Eldin | 25/25 | 25/25 | 63 | ✅ đã rà soát | ✅ xong |
| 5. Lanayru | 36/36 | 36/36 | 84 | ✅ đã rà soát | ✅ xong |
| 6. Master Sword | 14/14 | 14/14 | 0 | — (nguồn không có ảnh) | ✅ xong (text-only) |
| 7. Gerudo | 23/23 | 23/23 | 37 | ✅ đã rà soát | ✅ xong |
| 8. Fifth Sage | 35/35 | 35/35 | 0 | — (nguồn không có ảnh) | ✅ xong (text-only) |
| 9. Demon King | 14/14 | 14/14 | 0 | — (nguồn không có ảnh) | ✅ xong (text-only) |

**Cả 9/9 vùng đã xong**, đều `hard=0`, `en=0`, `xN=0`, `ph=0`, `ms=0`, layout `2col`.
**Vùng 6 Master Sword làm text-only**: fextralife không có trang Walkthrough cho vùng này (chỉ có
`Subcontent:Game_Progress_Route_6_*`, 3 ảnh logo/banner) → trang 0 ảnh, khai báo `NO_IMAGE` trong
`check-image-match.py`. Vùng 8/9 cũng thuộc diện này; vùng 7 Gerudo **có** ảnh thật (128 ảnh).
Ảnh 5 vùng đã đối chiếu với **trang nguồn thật** (`scripts/check-image-match.py` → `FAIL=0`): mỗi ảnh nằm
đúng subsection nguồn, đúng thứ tự xuất hiện, không lẫn ảnh vùng khác.

### Việc đã làm ngoài nội dung vùng
- Rà soát lại **ảnh theo đúng subsection nguồn** cho vùng 1–3: trước đây ảnh bị chia theo thứ tự file
  nên lệch bước (Prologue/Central còn lẫn ảnh vùng khác; Hebra lệch từ mục 7). Đã tải đủ ảnh còn thiếu
  (Prologue 77, Central 34, Hebra 80), bỏ ảnh trùng/logo ngoài nguồn, chuẩn hoá tên file.
- Tách folder ảnh theo trang: `images/gsi` → `images/prologue`.
- `docs/workflow-region.md`: chuẩn hoá cách lấy nội dung/ảnh (nhiều trang Subcontent, giữ tên file gốc,
  bản full qua trang `File:`, ảnh đặt ngay sau đoạn minh họa, caption theo tên bước).
- `docs/agents/`: cấu hình issue tracker (GitHub Issues), nhãn triage, domain docs.
- **Cổng cứng ảnh ↔ nội dung**: thêm `scripts/check-image-match.py` + luật trong `AGENTS.md`. Đếm ảnh
  (`img=uni`, `ms=0`) không bắt được ảnh sai chỗ, nên cổng này đối chiếu trực tiếp trang nguồn.
- Giai đoạn B hoàn tất: vùng 6 Master Sword, 7 Gerudo, 8 Fifth Sage, 9 Demon King đã có walkthrough đầy đủ
  (Gerudo lấy 37 ảnh từ walkthrough nguồn,
  bỏ các subsection thuộc vùng khác như Hyrule Field / Faron / side quest đại tiên).
- Tách các heading bị gộp nhiều subsection nguồn (làm ảnh nằm sai chủ đề): Prologue — Ukouh, In-Isa,
  Gutanbac (Pondside/Mining/Pit/Bottomless Cave tách riêng), Return to Temple of Time; Hebra —
  Get Tulin's Bow / Reach The Top of Hebra Peak, Post Kahatanaum Shrine / Clear Wind Temple.

## Còn tồn đọng
1. ~~Vùng 9~~ — đã xong (Giai đoạn B hoàn tất 9/9 vùng).
2. ~~Giai đoạn C~~ — **xong, toàn site HARD=0**: shrines 282→0, mechanics 9→0, tips 5→0,
   abilities 2→0, index 1→0, faq 1→0. Dịch thuật ngữ theo glossary (Ánh Sáng Chúc Phúc, Đền Thờ Nhỏ,
   Siêu Tay/Hồi Tưởng/Xuyên/Ghép, Bình Thể Lực), giữ tên riêng, viết lại footer credits bằng tiếng Việt.
3. Một số ảnh vùng 1–3 chỉ có bản 400px (fextralife chặn tải bản gốc / trả 429) — chấp nhận được,
   nâng cấp sau nếu cần nét hơn.

## Thứ tự thực hiện tiếp
1. Nâng cấp ảnh 400px ở vùng 1–3 nếu tìm được bản gốc fextralife (nếu không thì giữ nguyên).
2. Rà WARN còn lại (818) nếu muốn sạch hơn nữa — không chặn commit.
4. Cập nhật lại bảng trạng thái và mục "Còn tồn đọng" trong file này sau mỗi vùng.

## Lệnh kiểm tra nhanh
```
python scripts/verify-regions.py
python scripts/check-vietnamese.py
python scripts/check-image-match.py   # FAIL=0 mới được commit (so ảnh với trang nguồn)
```
