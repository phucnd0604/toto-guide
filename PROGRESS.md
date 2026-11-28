# PROGRESS.md – Mục tiêu & tiến độ dự án TOTK Guide

> File này là **nguồn duy nhất** ghi tiến độ. Cập nhật ngay sau mỗi vùng (bảng trạng thái + mục "Còn tồn đọng").
> Quy trình chi tiết: bản đồ việc [#1](https://github.com/phucnd0604/toto-guide/issues/1) và đặc tả [#33](https://github.com/phucnd0604/toto-guide/issues/33). Chuẩn dịch: `docs/translation-standard.md`.

## Giai đoạn E — dựng lại Lộ trình theo zeldacentral (bắt đầu 2026-11-28)

Bộ 9 vùng fextralife bên dưới **vẫn là site đang chạy** cho tới vé chuyển nhà (T29). Trang mới nằm trong
`content/` và `pages/walkthrough|quests|temples|reference`, chưa link từ menu cho tới cutover.

| Vé | Nội dung | Trạng thái |
|---|---|---|
| T0 | Hạ tầng: generator, template, 5 cổng, hub khung | ✅ xong 2026-11-28 (đã duyệt, đã merge `master`) |
| T1 | Đảo Trời Lớn (1 chương, chương mẫu chốt khuôn) | ✅ xong 2026-11-28 (đã duyệt; commit `c266294` trên `master`, deploy HTTP 200) |
| T2 | Hyrule Field & Hyrule Castle (1/3): Điểm Quan Sát, Đồng Bằng Hyrule, Phế Tích Thị Trấn Lâu Đài | ✅ xong 2026-11-28 (đã duyệt; commit `77eb6b5` trên `master`, deploy HTTP 200) |
| T3 | Hyrule Field & Hyrule Castle (2/3): Vực Sâu Trung Tâm Hyrule, Phần Còn Lại Của Lâu Đài Hyrule | ✅ xong 2026-11-28 (đã duyệt; commit `9c8e701` + `2f90602` trên `master`, deploy HTTP 200) |
| T4 | Hyrule Field & Hyrule Castle (3/3): Nam Đồng Bằng Hyrule, Vực Sâu Nam Đồng Bằng Hyrule | ✅ xong 2026-11-28 (duyệt qua PR #35, merge `040590a`; 9 + 2 Đền Thờ Nhỏ, 60 + 22 rương, 268 + 77 ảnh, bảy cổng PASS, CI xanh) |
| T5 | Tabantha & Sườn Hyrule (1/2): Biên Giới Tabantha, Đền Thờ Bị Lãng Quên, Hẻm Núi Tanagar & Sườn Hyrule | ✅ xong 2026-11-28 (duyệt qua PR #37; 3 chương, 7 Đền Thờ Nhỏ, 4 hang, 25 hạt Korok, 42 rương, 274 ảnh / 13,1 MB, bảy cổng PASS, CI xanh) |

- Hub mới: `pages/progress-route.html` — đúng 4 khối, 12 nhóm vùng đúng thứ tự; nhóm 1 (Đảo Trời Lớn) có 1 chương, nhóm 2 (Cánh Đồng Hyrule & Lâu Đài Hyrule) **đủ 7 chương (2–8)** sau T4, nhóm 3 (Tabantha & Sườn Hyrule) có **3/6 chương (9–11)** sau T5, 9 nhóm còn lại đang trống.
- Trang chỉ mục sinh tự động: `pages/quests.html`, `pages/temples.html`.
- Bài học từng vé (khuôn trang, bốn loại bẫy của nguồn, các bản vá cổng), việc đã làm ngoài nội dung
  vùng và nhật ký giai đoạn A–D đã tách sang **[docs/changelog-E.md](docs/changelog-E.md)** — mỗi vé đọc
  file này một lần là đủ, không cần đọc lại toàn bộ lịch sử.

- Bảy cổng (thêm 2 cổng sau retro T1): `build-pages.py --check` → `check-links.py` → `verify-pages.py` → `check-image-match.py` → `check-vietnamese.py` → `check-mobile.py` → `check-coverage.py`; hợp đồng từng cổng ở `tool/README.md`. CI `.github/workflows/gates.yml` chạy lại cả bảy sau mỗi push và mỗi PR.
- Khuôn chương đã chốt (T1–T4): bảng tóm tắt → Mục lục → Tuyến đường nhanh → các mục đi đường đúng thứ
  tự nguồn → Mẹo hoàn thành → Đồ thu thập; một gallery `<details open>` mỗi mục, caption = alt dịch +
  `(ảnh k/N)`, icon trong bảng dùng `.inline-icon`. Chương nhiều phần dùng mục lục hai cấp; chương chỉ
  có `<h3>` bên trong các mục lớn (Tanagar) vẫn dùng **mục lục một cấp theo `<h2>`**, `<h3>` giữ đúng
  thứ tự trong bài và không cần `id` tay. Khối quảng bá của nguồn ("Track them") không phải mục —
  xem `IGNORED_SOURCE_HEADINGS` và `tool/README.md`.
- Bộ ảnh hiện có: **11 chương, 1479 file, ~69 MB**.

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
- Gallery ảnh để `<details ... open>` — mở sẵn, người đọc thấy ảnh ngay (chốt 2026-11-23).
- Heading `h2`/`h3`: nguồn có heading tiếng Anh thì viết **tiếng Anh gốc + "(chú thích tiếng Việt)"**;
  vùng text-only (nguồn chỉ có danh sách bước) thì heading **thuần tiếng Việt**.
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
5. `python scripts/check-image-match.py` → **`FAIL=0`**: mỗi ảnh nằm đúng trang nguồn của vùng, không lẫn vùng,
   đúng thứ tự, đúng subsection nguồn; vùng text-only khai báo `NO_IMAGE` và phải ra `NO-IMAGE ... OK`.
6. Ảnh: caption/alt = tên bước + `(ảnh k/N)`;
   không thêm ảnh/logo ngoài nguồn.
7. Commit riêng cho từng vùng → push `master` → Vercel deploy → HTTP 200 cho trang và ảnh mới.

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
Ảnh 6 vùng có ảnh (1–5 và 7) đã đối chiếu với **trang nguồn thật**
đúng subsection nguồn, đúng thứ tự xuất hiện, không lẫn ảnh vùng khác.

## Còn tồn đọng
1. ~~Vùng 9~~ — đã xong (Giai đoạn B hoàn tất 9/9 vùng).
2. ~~Giai đoạn C~~ — **xong, toàn site HARD=0**: shrines 282→0, mechanics 9→0, tips 5→0,
   abilities 2→0, index 1→0, faq 1→0. Dịch thuật ngữ theo glossary (Ánh Sáng Chúc Phúc, Đền Thờ Nhỏ,
   Siêu Tay/Hồi Tưởng/Xuyên/Ghép, Bình Thể Lực), giữ tên riêng, viết lại footer credits bằng tiếng Việt.
3. Một số ảnh vùng 1–3 chỉ có bản 400px (fextralife chặn tải bản gốc / trả 429) — chấp nhận được,
   nâng cấp sau nếu cần nét hơn.
4. Còn **6 WARN** của `tool/check-vietnamese.py` ở 4 trang cũ (cụm tên riêng có sẵn: "ra Blue Horn",
   "con Frost Talus", "boss Tinh", "Phantom Armor mua", "Mighty Zonaite Shield trong"). Ba trang T5 đều
   `warn=0`; WARN không chặn cổng — dọn khi có vé riêng.

## Thứ tự thực hiện tiếp
1. Nâng cấp ảnh 400px ở vùng 1–3 nếu tìm được bản gốc fextralife (nếu không thì giữ nguyên).
2. ~~Rà WARN~~ — đã xong: **WARN=0** (checker chỉ còn báo cụm có từ tiếng Anh thật).
4. Cập nhật lại bảng trạng thái và mục "Còn tồn đọng" trong file này sau mỗi vùng.

## Lệnh kiểm tra nhanh
```
python scripts/verify-regions.py
python scripts/check-vietnamese.py
python scripts/check-image-match.py   # FAIL=0 mới được commit (so ảnh với trang nguồn)
```