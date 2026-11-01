# Handoff – TOTK Guide Site

Cập nhật: sau khi tách 9 vùng thành 9 trang riêng + đổi bảng màu "khắc" (đá vàng).

## Trạng thái thực tế của site
- Repo: https://github.com/phucnd0604/toto-guide (branch `master`)
- Deploy: https://toto-guide-five.vercel.app (Vercel auto-deploy khi push)
- Cấu trúc: `index.html` + `pages/{mechanics,abilities,shrines,tips,faq}.html`
  + hub `pages/progress-route.html` + 9 trang vùng
  `pages/route-{prologue,central,hebra,eldin,lanayru,mastersword,gerudo,fifth,final}.html`
- Ảnh: `images/gsi` (79), `images/central` (47), `images/hebra` (66)
- Menu "Lộ trình" trên navbar là **submenu 9 vùng** (hover trên desktop, bấm ▾ trên mobile).
- Mỗi trang vùng: header chung (crumb + h1 + chip N bước / N mục / N ảnh / trạng thái) rồi 2 cột —
  cột trái sticky (`aside.rail`): "Mục lục vùng" (gập được, có scrollspy) + "Danh sách N bước";
  cột phải cuộn: walkthrough (`<h3>` song ngữ + `<details>` chứa ảnh).
- `scripts/verify-regions.py` đọc thẳng 9 file `pages/route-*.html`; vùng chưa có walkthrough hiện `stub`.

## Đã hoàn thành
### Vùng 1-2-3 (đã verify bằng script)
| Vùng | Bước index | Độ phủ | Ảnh dùng | Heading EN | xN | Placeholder |
|---|---|---|---|---|---|---|
| 1. Prologue & Great Sky Island | 19/19 | 19/19 | 78/78 | 0 | 0 | 0 |
| 2. Central Hyrule | 27/27 | 27/27 | 46/46 | 0 | 0 | 0 |
| 3. Hebra | 31/31 | 31/31 | 66/66 | 0 | 0 | 0 |

- Toàn bộ heading `h2`/`h3` đã chuyển **song ngữ**: tiếng Anh gốc + "(chú thích tiếng Việt)".
- Nội dung viết lại theo `docs/translation-standard.md`: không còn Vietglish, đại từ "bạn", đủ ý đi đâu / làm gì / nhận gì.
- Central được mở rộng từ 3 lên 9 mục con: Lookout Landing, Lâu Đài Hyrule & Hoz, Tháp Quan Sát & Dù Lượn,
  U Ám & Daval, Đền Thờ Nhỏ Jiosin, Camera Work in the Depths, Chụp tượng & trả nhiệm vụ,
  Impa và Hình Vẽ Mặt Đất, các việc phụ quanh Lookout Landing.
- Hebra: 19 mục con bám beat fextralife, thêm mục "Side Stops in Hebra" (Giọt Lệ Rồng, Forgotten Temple,
  Mayausiy, Makurukis, Meeshy/Misko's Treasure, Flight Range/Kaneli, Molli the Fletcher, Eye of the Storm).

### Công cụ / tài liệu
- `docs/translation-standard.md` – chuẩn dịch: 7 nguyên tắc, quy tắc tên riêng, quy tắc heading song ngữ, 3 bảng thuật ngữ, blacklist Vietglish.
- `docs/workflow-region.md` – workflow 6 bước, bước 5 kiểm tra tự động bằng 3 script.
- `AGENTS.md` – 5 điều cấm + bắt buộc chạy `scripts/check-vietnamese.py` 0 lỗi HARD trước commit.
- `scripts/audit.py` (audit.py gốc) – broken images/anchors, h1, meta, external links.
- `scripts/check-vietnamese.py` – HARD: heading EN, Vietglish blacklist, mẫu xN; WARN: cụm EN lạ.
- `scripts/verify-regions.py` – bảng đối chiếu bước index / độ phủ / ảnh / heading / placeholder / layout cho từng vùng.
- `fextralife/*.txt` – text nguồn đã extract từ PDF walkthrough (dùng khi viết lại nội dung).

## Còn tồn đọng
1. **Vùng 4-9** (eldin, lanayru, mastersword, gerudo, fifth, final) mới có index dạng card phẳng,
   0 ảnh, ghi "Chi tiết walkthrough sẽ bổ sung ở Phase B". Cần làm đúng quy trình như vùng 3:
   tải ảnh → extract text nguồn → viết walkthrough → verify.
2. `scripts/check-vietnamese.py` toàn site còn **25 lỗi HARD**, tất cả nằm trong vùng 4-9
   (Vietglish kiểu "main quest", "spot geoglyph", "5x Arrow", "Proceed to chasm").
3. `pages/shrines.html` (282 HARD) và `mechanics/abilities/tips` còn Vietglish — chưa xử lý, ngoài phạm vi vùng 1-3.

## Bước tiếp theo
1. Vùng 4 Eldin: 25 bước → làm đủ quy trình, rồi 5 Lanayru (36), 6 Master Sword (14), 7 Gerudo (23), 8 Fifth Sage (35), 9 Demon King (14).
2. Dọn Vietglish ở shrines.html + mechanics/abilities/tips theo cùng chuẩn dịch.
3. Cập nhật lại bảng tiến độ ở trên và HANDOFF này sau mỗi vùng.

## Lệnh kiểm tra nhanh
```
python audit.py
python scripts/check-vietnamese.py
python scripts/verify-regions.py -v prologue central hebra
```
