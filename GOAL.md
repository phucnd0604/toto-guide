# GOAL.md – Mục tiêu dự án TOTK Guide

## Mục tiêu tổng quát
Website hướng dẫn chơi The Legend of Zelda: Tears of the Kingdom bằng tiếng Việt, đầy đủ theo
Game Progress Route + Walkthrough của fextralife, có ảnh minh họa, host trên Vercel, không link ra domain khác.

## Cấu trúc chuẩn (đã chốt)
- 9 mục lớn = 9 vùng, theo đúng thứ tự fextralife:
  1. Prologue & Great Sky Island (19 bước)
  2. Central Hyrule (27)
  3. Hebra (31)
  4. Eldin (25)
  5. Lanayru (36)
  6. Master Sword (14)
  7. Gerudo (23)
  8. Fifth Sage (35)
  9. Demon King (14)
- Mỗi vùng là 1 `<section>` 2 cột:
  - cột trái: index các bước của Game Progress Route (tiếng Việt, bỏ ảnh);
  - cột phải: walkthrough chi tiết bám đúng beat của fextralife, chia `<h3>` theo từng chặng,
    mỗi chặng có `<details>` gộp toàn bộ ảnh minh họa.
- Heading `h2`/`h3`: **tiếng Anh gốc + "(chú thích tiếng Việt)"**.

## Tiêu chí verify (bắt buộc pass trước khi coi 1 vùng là xong)
1. `python audit.py` → ALL OK (0 broken image/anchor, mỗi trang 1 h1, meta đủ, không link ngoài trừ Google Fonts).
2. `python scripts/check-vietnamese.py` → 0 lỗi HARD cho vùng đó.
3. `python scripts/verify-regions.py <region>`:
   - số bước index = số bước fextralife;
   - **độ phủ = đủ số bước** (mỗi bước index đều được walkthrough nhắc tới);
   - `uni = img` (không ảnh trùng), `ms = 0` (không ảnh thiếu), `en = 0`, `xN = 0`, `ph = 0`;
   - layout `2col`.
4. Nội dung 100% tiếng Việt theo `docs/translation-standard.md`: không Vietglish, đại từ "bạn",
   đủ ý đi đâu / làm gì / nhận gì; giữ tên riêng, dịch thuật ngữ theo glossary.
5. Không còn placeholder ("... content continues", "sẽ bổ sung", "chi tiết hoàn tất" khi chưa xong).
6. Commit riêng cho từng vùng → push `master` → Vercel deploy → HTTP 200 cho trang và ảnh mới.

## Trạng thái hiện tại
| Vùng | Bước | Độ phủ | Ảnh | Trạng thái |
|---|---|---|---|---|
| 1. Prologue & Great Sky Island | 19/19 | 19/19 | 78/78 | ✅ xong |
| 2. Central Hyrule | 27/27 | 27/27 | 46/46 | ✅ xong |
| 3. Hebra | 31/31 | 31/31 | 66/66 | ✅ xong |
| 4. Eldin | 25 | — | 0 | ⬜ mới có index phẳng |
| 5. Lanayru | 36 | — | 0 | ⬜ mới có index phẳng |
| 6. Master Sword | 14 | — | 0 | ⬜ mới có index phẳng |
| 7. Gerudo | 23 | — | 0 | ⬜ mới có index phẳng |
| 8. Fifth Sage | 35 | — | 0 | ⬜ mới có index phẳng |
| 9. Demon King | 14 | — | 0 | ⬜ mới có index phẳng |

Ngoài ra: `pages/shrines.html`, `mechanics.html`, `abilities.html`, `tips.html` còn Vietglish
(chưa xử lý; làm sau khi xong 9 vùng).

## Thứ tự thực hiện tiếp
1. Vùng 4 Eldin → verify → commit/push.
2. Lần lượt 5 → 9, mỗi vùng một commit riêng.
3. Dọn Vietglish các trang phụ (shrines, mechanics, abilities, tips).
4. Cập nhật bảng trạng thái ở trên + `HANDOFF.md` sau mỗi vùng.
