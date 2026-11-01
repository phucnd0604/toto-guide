# AGENTS.md – Quy tắc dự án TOTK Guide

## Ngôn ngữ nội dung
- Toàn bộ nội dung website phải bằng **tiếng Việt**, chỉ giữ nguyên thuật ngữ chuyên môn (Ultrahand, Fuse, Ascend, Recall, Autobuild, Vow, …) và tên riêng (Link, Zelda, Rauru, tên shrine/temple, tên NPC).
- Không để sót câu/đoạn tiếng Anh trong nội dung; nếu trích từ nguồn tiếng Anh phải dịch.

## Nguồn nội dung
- Nguồn chính: fextralife (Game Progress Route + Walkthrough) cho TOTK.
- fextralife bị chặn trực tiếp ở VN → truy cập qua **Google Translate proxy**:
  `https://translate.google.com/translate?sl=en&tl=vi&u=<URL>`
- Ảnh từ `static0.fextralifeimages.com` (tải về `images/`, đặt tên `fx-<region>.png`).

## Cấu trúc trang
- Canonical progress route: `pages/progress-route.html` (9 vùng theo fextralife).
- Giữ multi-page: mechanics, abilities, shrines, tips, faq, index.
- Mỗi trang: 1 `<h1>`, meta description, alt text tiếng Việt.

## Kiểm tra trước commit
- Chạy audit: 0 broken images, 0 broken anchors, 1 h1, meta present, không link ngoài (chỉ Google Fonts).
- Step count phải khớp fextralife cho mỗi vùng.
- HTML balanced, không còn reference đến trang đã xóa.

## Quy trình Phase B
- Lần lượt từng vùng (index 1): tải ảnh → expand section với walkthrough chi tiết + mẹo + ảnh → verify audit → commit riêng → push/deploy → requesting-code-review.
- Loop executing-plans + requesting-code-review cho đến khi chuẩn xác mới chuyển vùng tiếp.

## Commit & Deploy
- Commit message rõ ràng theo task (Phase/Task + tên vùng).
- Push origin master → Vercel auto-deploy; verify HTTP 200 cho trang và ảnh.