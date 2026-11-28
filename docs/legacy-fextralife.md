# Bộ 9 vùng fextralife (di sản — chỉ còn hiệu lực tới vé T29)

> Toàn bộ nội dung dưới đây thuộc **bộ 9 vùng fextralife** đang được thay bằng Lộ trình mới
> (43 chương theo zeldacentral, map [#1](https://github.com/phucnd0604/toto-guide/issues/1)).
> Chỉ áp dụng cho tới khi vé chuyển nhà **T29** xoá 9 trang `pages/route-*.html`, thư mục
> `scripts/` và ảnh cũ. Trang mới **không** dùng các quy tắc dưới đây; xem `AGENTS.md` và `tool/README.md`.

## Nguồn nội dung cũ

- Nguồn: fextralife (Game Progress Route + Walkthrough) cho TOTK.
- fextralife bị chặn trực tiếp ở VN → truy cập qua Google Translate proxy:
  `https://translate.google.com/translate?sl=en&tl=vi&u=<URL>`
- Ảnh từ `static0.fextralifeimages.com` (tải về `images/<region>/`, giữ tên file gốc).

## Cấu trúc 9 trang vùng

- Hub `pages/progress-route.html` + 9 trang vùng `pages/route-<slug>.html`
  (slug: prologue, central, hebra, eldin, lanayru, mastersword, gerudo, fifth, final).
- Mỗi trang vùng: cột trái sticky là mục lục + danh sách bước, cột phải là walkthrough.
- Giữ multi-page: mechanics, abilities, shrines, tips, faq, index.
- Mỗi trang: 1 `<h1>`, meta description, alt text tiếng Việt.
- **Ảnh tách riêng theo trang**: `pages/route-<slug>.html` chỉ dùng ảnh trong `images/<slug>/`.
  Cấm dùng chung folder, cấm copy ảnh của vùng khác sang (lỗi đã gặp: 12 ảnh Prologue nằm trong
  `images/central`).
- **Gallery mở sẵn**: ảnh bọc trong `<details ... open>` để người đọc thấy ngay.
- **Vùng text-only là hợp lệ**: vùng không có trang Walkthrough nguồn (Master Sword, Fifth Sage,
  Demon King) thì trang 0 ảnh, khai báo `NO_IMAGE` trong `scripts/check-image-match.py` và ghi lý do ở
  `PROGRESS.md`. Không bịa ảnh, không nhồi banner/logo.

## Kiểm tra trước commit (bộ 9 vùng cũ)

- `python scripts/verify-regions.py` → mỗi vùng `step/want` khớp, `cover` đủ bước, `img = uni`, `ms=0`,
  `en=0`, `ph=0`, layout `2col`.
- `python scripts/check-vietnamese.py` → 0 lỗi HARD.
- HTML balanced, mọi `src` ảnh tồn tại, và không file nào trong `images/<slug>/` bị bỏ không dùng.
- Không còn reference đến trang/file đã xóa.

## Cổng cứng: ảnh ↔ nội dung (bản cũ)

`python scripts/check-image-match.py` phải in **`FAIL=0`** trước khi commit một vùng.

Lý do có cổng này: `verify-regions.py` chỉ đếm ảnh, nên đã có lần `img=uni`, `ms=0` đầy đủ mà ảnh vẫn
sai chỗ — ảnh hang (Pondside Cave, Mining Cave…) nằm dưới tiêu đề đền thờ Gutanbac, và ảnh vùng này lẫn
sang vùng khác. Đếm đủ ảnh **không** thay thế được cổng này.

Ba điều kiện, vi phạm 1 là FAIL:

1. **Không lẫn vùng:** mọi ảnh dùng trong `pages/route-<slug>.html` phải có trong đúng trang nguồn của vùng đó.
2. **Đúng thứ tự:** dãy ảnh trong trang phải là dãy con đúng thứ tự xuất hiện ở nguồn — không đảo.
3. **Đúng mục:** mỗi ảnh phải nằm dưới `<h3>` khớp subsection nguồn. **Không gộp nhiều subsection nguồn vào
   một `<h3>`** (gộp là FAIL: ảnh của mục Cave sẽ hiện dưới heading Shrine).

- Trang nguồn khai báo trong `SOURCES` của script; một vùng có thể trải trên nhiều trang Subcontent — phải khai đủ.
- Chưa có cache thì script tự fetch qua Google Translate proxy (lưu `.tmp-src/`, đã gitignore);
  dùng `--refresh` khi nguồn thay đổi.
- Script chỉ ra mục nguồn đúng, ví dụ:
  `Clear Wind Temple: ảnh walkthrough_hrx50... thuộc mục nguồn "Post Kahatanaum Shrine"` → tách heading rồi chạy lại.
- Vùng **không có nguồn ảnh**: khai báo slug trong `NO_IMAGE` của `scripts/check-image-match.py`; trang phải
  **0 ảnh** — không nhồi banner/logo cho đủ số — và `PROGRESS.md` phải ghi rõ lý do. Hiện có:
  `mastersword`, `fifth`, `final`.
- Vùng có nguồn ảnh mới: bổ sung trang nguồn vào `SOURCES` rồi bật cổng cho vùng đó.

## Quy trình Phase B (di sản)

- Lần lượt từng vùng (index 1): lấy nội dung nguồn → tải ảnh → dịch theo
  `docs/translation-standard.md` → trình bày (index trái + walkthrough phải) → verify-regions +
  check-vietnamese + **check-image-match** → commit riêng → push/deploy → requesting-code-review.
- Lặp executing-plans + requesting-code-review cho tới khi chuẩn xác mới chuyển vùng tiếp.
