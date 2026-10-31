# Design Doc: TOTK Guide Website (Multi-page, calm warm theme)

Date: 2026-10-31

## Intent & why
Tạo website hướng dẫn chơi The Legend of Zelda: Tears of the Kingdom cho người mới (gà mờ), đầy đủ từ A-Z, host static. Tránh bỏ sót nội dung game. Nội dung phân lớp: tóm tắt + mẹo ở trang tổng quan, trang chi tiết riêng cho phần sâu.

## Goals
- Bao phủ: điều khiển, cơ chế, abilities, tutorial Great Sky Island, early game.
- Main Story 23 quest: mỗi quest có tóm tắt + bước làm + mẹo.
- 6 Temple + boss: giải puzzle theo bước.
- Shrine index (152) theo vùng: tên + giải pháp ngắn + link chi tiết.
- Endgame: Master Sword, Dragon's Tears, Ganondorf.
- Tips: nấu ăn, Fuse, giáp/nâng cấp, Depths, Sky, Korok, rupee, 100%.
- UI dịu, ấm (amber/teal), đa trang, responsive, accessible.

## Non-goals
- Không clone wiki đầy đủ (không liệt kê mọi Korok coordinate).
- Không tài khoản/bình luận.
- Không host ảnh bản quyền Nintendo; chỉ ảnh CC (Wikimedia) + link wiki.

## Constraints
- HTML/CSS/JS tĩnh, không build toolchain.
- Host qua python http.server hoặc static host.
- Ảnh: Wikimedia Commons + link Zelda Dungeon Wiki (gen ảnh không khả dụng).
- Ngôn ngữ tiếng Việt.

## Approaches considered
A: một trang accordion. B: nhiều trang. C: lai. Chọn B để dễ quản lý và UX dịu.

## How it gets built (decided)
- Trang: index, mechanics, abilities, tutorial, early-game, main-story, temples, bosses (gộp vào temples), endgame, shrines, tips, faq.
- main-story: mỗi quest là <details> (tóm tắt + bước).
- temples: mỗi temple section với puzzle steps.
- shrines: grouped by region, tên + giải pháp ngắn + link.
- Theme: bg #0B1220, card #131C2E, text #E5E7EB, muted #94A3B8, primary amber #F59E0B, accent teal #2DD4BF, border #1F2A3F. Headings Chakra Petch, body Inter (Google Fonts). Giảm tương phản, thêm spacing.
- Nav: top navbar + sidebar desktop.
- Ảnh: Wikimedia (logo, map, Ganondorf) + link wiki.

## What's left to builder
- Viết nội dung từng trang tiếng Việt.
- Checklist không bỏ sót.
- Test responsive, link, accessibility.

## Approval needed
Chờ người dùng duyệt design doc này. Sau đó invoke writing-plans.