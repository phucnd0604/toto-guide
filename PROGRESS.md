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

- Hub mới: `pages/progress-route.html` — đúng 4 khối, 12 nhóm vùng đúng thứ tự; nhóm 1 (Đảo Trời Lớn) có 1 chương, nhóm 2 (Cánh Đồng Hyrule & Lâu Đài Hyrule) có 3 chương, 10 nhóm còn lại đang trống.
- Trang chỉ mục sinh tự động: `pages/quests.html`, `pages/temples.html`.
- Bảy cổng (thêm 2 cổng ngày 2026-11-28 sau retro T1): `tool/build-pages.py --check` →
  `tool/check-links.py` → `tool/verify-pages.py` → `tool/check-image-match.py` →
  `tool/check-vietnamese.py` → `tool/check-mobile.py` → `tool/check-coverage.py`. Cả bảy PASS với
  4 chương nội dung (671 ảnh, ~31 MB).
- `tool/check-mobile.py` + `tool/mobile-probe.mjs`: render bằng Chrome headless (CDP, không thêm
  dependency), FAIL khi `scrollWidth > clientWidth` ở 375px/768px. Cổng này ra đời vì T1 đã PASS đủ
  5 cổng cũ mà trang vẫn tràn ngang trên điện thoại.
- `tool/check-coverage.py`: bắt lỗi "dịch thiếu đoạn" mà 5 cổng hình dạng không thấy.
- CI `.github/workflows/gates.yml` chạy lại 7 cổng sau mỗi push (cache `.tmp-src/` để không tải lại nguồn).
- `tool/verify-pages.py` đã sửa ở T1: đếm mục theo đúng cách cổng ảnh tách mục (số `<h2>` cộng vùng
  trước mục đầu tiên). Bản cũ đếm `<h2>` thô nên mọi chương có ảnh nằm trước H2 đầu (bảng tóm tắt)
  đều báo lệch nguồn 1 mục và FAIL vĩnh viễn.
- Chương mẫu T1 chốt khuôn: bảng tóm tắt có icon boss (ảnh trước H2 đầu) → Mục lục → Tuyến đường nhanh →
  các mục đi đường đúng thứ tự nguồn → Mẹo hoàn thành → Đồ thu thập; mỗi mục H2 một gallery ảnh
  `<details open>`, caption = mô tả dịch từ alt gốc + `(ảnh k/N)`; icon trong bảng dùng `.inline-icon`.
- T2 giữ đúng khuôn T1, thêm ba điều đã gặp thật, các chương sau áp dụng luôn:
  (1) bảng facts của nguồn **có thể không có ảnh nào** trước H2 đầu (Điểm Quan Sát) → trang chỉ có
  số mục = số `<h2>`, không có vùng "(trước mục đầu)"; (2) nguồn có mục **không có "Completion tips"**
  (Phế Tích Thị Trấn Lâu Đài) → bám nguồn, không tự thêm mục, vì cổng 3/4 so số mục 1:1;
  (3) một ảnh nguồn có thể xuất hiện 2 lần (icon Dark Tunic) → cổng ảnh cấm dùng trùng nên chỉ dùng
  ở vị trí đầu tiên, các chỗ sau bỏ icon.
- T2 cũng sửa `tool/check-vietnamese.py` theo đúng quy ước trong `tool/README.md`: thêm âm tiết Việt
  không dấu `an`, `than` vào `VI_ASCII` và 4 tên nhiệm vụ phụ vào `PHRASES` — thêm vào danh sách
  miễn trừ thay vì bẻ câu cho vừa cổng.
- Retro sau T2 (2026-11-28) — chỉ đổi công cụ, không đổi nội dung:
  `tool/source_sections.py` là định nghĩa "mục" **duy nhất** (ba cổng import, trước đó mỗi cổng tự viết một bản);
  `verify-pages` dùng đúng luật heading của `check-vietnamese` (hết cảnh hai cổng đá nhau vụ tên riêng) và kiểm câu dẫn
  Mục lục có đếm đúng số mục; `check-vietnamese` nhận `--content`/slug/file để quét chữ **trước** khi build;
  `check-image-match --from` dùng nguồn đã có trên đĩa thay vì tải lại; thêm `tool/inspect-source.py` (soi chương nguồn)
  và `tool/shot.py` (chụp ảnh review 375/1280px qua CDP, thay cho `chrome --screenshot` hay hỏng).
  Đã kiểm lại: cả bảy cổng PASS, `pages/` không đổi byte nào.

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

### Việc đã làm ngoài nội dung vùng
- Rà soát lại **ảnh theo đúng subsection nguồn** cho vùng 1–3: trước đây ảnh bị chia theo thứ tự file
  nên lệch bước (Prologue/Central còn lẫn ảnh vùng khác; Hebra lệch từ mục 7). Đã tải đủ ảnh còn thiếu
  (Prologue 77, Central 34, Hebra 80), bỏ ảnh trùng/logo ngoài nguồn, chuẩn hoá tên file.
- Tách folder ảnh theo trang: `images/gsi` → `images/prologue`.
- Bài học lấy nội dung/ảnh (nhiều trang Subcontent, giữ tên file gốc, bản full qua trang `File:`,
  ảnh đặt ngay sau đoạn minh họa, caption theo tên bước): đã chuyển vào đặc tả [#33](https://github.com/phucnd0604/toto-guide/issues/33).
- `docs/agents/`: cấu hình issue tracker (GitHub Issues), nhãn triage, domain docs.
- **Cổng cứng ảnh ↔ nội dung**: thêm `scripts/check-image-match.py` + luật trong `AGENTS.md`. Đếm ảnh
  (`img=uni`, `ms=0`) không bắt được ảnh sai chỗ, nên cổng này đối chiếu trực tiếp trang nguồn.
- Giai đoạn B hoàn tất: vùng 6 Master Sword, 7 Gerudo, 8 Fifth Sage, 9 Demon King đã có walkthrough đầy đủ
  (Gerudo lấy 37 ảnh từ walkthrough nguồn,
  bỏ các subsection thuộc vùng khác như Hyrule Field / Faron / side quest đại tiên).
- Tách các heading bị gộp nhiều subsection nguồn (làm ảnh nằm sai chủ đề): Prologue — Ukouh, In-Isa,
  Gutanbac (Pondside/Mining/Pit/Bottomless Cave tách riêng), Return to Temple of Time; Hebra —
  Get Tulin's Bow / Reach The Top of Hebra Peak, Post Kahatanaum Shrine / Clear Wind Temple.

## Nhật ký giai đoạn

- **A – chốt ảnh ↔ nội dung (2026-11-23)**: thêm `scripts/check-image-match.py` + cổng trong `AGENTS.md`;
  tách heading bị gộp ở Prologue (Ukouh, In-Isa, Gutanbac + 4 hang, Return to Temple of Time) và Hebra
  (Post Kahatanaum, Reach The Top of Hebra Peak); mở sẵn toàn bộ gallery (`<details open>`).
  Commit: `85f5616`, `3da9436`, `c2e1105`, `8109e09`.
- **B – 4 vùng còn thiếu (2026-11-23)**: Master Sword 14 bước, Gerudo 23 bước + 37 ảnh, Fifth Sage 35 bước,
  Demon King 14 bước; thêm chế độ `NO_IMAGE` cho vùng không có nguồn ảnh; hub báo 9/9 vùng đầy đủ.
  Commit: `78aae7b`, `47d68e5`, `af3718a`, `4f9fe28`, `b431e6f`.
- **C – dọn ngôn ngữ (2026-11-23)**: shrines 282→0, mechanics 9→0, tips 5→0, abilities 2→0, index 1→0,
  faq 1→0; thêm 72 tên thử thách/nhiệm vụ vào allowlist của checker. Commit: `c2ec4e0`, `dfb9630`,
  `ce370ab`, `511ab03`, `cc94717`, `cf2c396`, `4424e38`.

- **D – sạch hoá (2026-11-23)**: bỏ 33 link `index.html` (dùng `/` và `../`) → hết redirect 308 mỗi lần về trang chủ;
  WARN 814→0: checker thêm bộ lọc âm tiết Việt không dấu (`VI_ASCII`) + danh sách từ tiếng Anh (`EN_EXTRA`),
  bỏ qua cụm tên riêng, rồi dịch nốt 39 chỗ tiếng Anh lọt (damage/durability/armor/quest/boss…).

## Còn tồn đọng
1. ~~Vùng 9~~ — đã xong (Giai đoạn B hoàn tất 9/9 vùng).
2. ~~Giai đoạn C~~ — **xong, toàn site HARD=0**: shrines 282→0, mechanics 9→0, tips 5→0,
   abilities 2→0, index 1→0, faq 1→0. Dịch thuật ngữ theo glossary (Ánh Sáng Chúc Phúc, Đền Thờ Nhỏ,
   Siêu Tay/Hồi Tưởng/Xuyên/Ghép, Bình Thể Lực), giữ tên riêng, viết lại footer credits bằng tiếng Việt.
3. Một số ảnh vùng 1–3 chỉ có bản 400px (fextralife chặn tải bản gốc / trả 429) — chấp nhận được,
   nâng cấp sau nếu cần nét hơn.

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
