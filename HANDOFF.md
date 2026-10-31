# Handoff – TOTK Guide Site

## Tiến độ hiện tại

### Đã hoàn thành
- **Multi-page static site** (11 trang): index.html (overview) + pages/*.html (mechanics, abilities, tutorial, early-game, main-story, temples, endgame, shrines, tips, faq).
- **Self-contained**: tất cả ảnh (30+ webp/jpg/svg) đã download về `images/`, không có external content links (chỉ Google Fonts CDN).
- **Git repo**: khởi tạo local, commit, push lên GitHub: https://github.com/phucnd0604/toto-guide
- **Vercel deploy**: https://toto-guide-five.vercel.app (HTTP 200, CSS/pages load OK).
- **Dark/Light mode toggle** hoạt động (app.js).
- **Nội dung chính**:
  - 23 main quests (main-story.html), granular cho Tulin, Yunobo, Sidon, Riju.
  - 5 Temple + Boss (temples.html) với walkthrough chi tiết + ảnh.
  - 152 Shrine + 31 Shrine Quests (shrines.html) theo vùng.
  - Endgame: Master Sword, Dragon's Tears (13 locations), Ganondorf final.
  - Tips: nấu ăn, Fuse, giáp, Depths, Sky, Korok, 100%.
  - FAQ 8 mục.
  - Early game, mechanics, abilities, tutorial.
- **Ảnh minh họa**: 30+ ảnh (Zelda Central screenshots + Wikimedia SVGs + local SVGs).
- **Controls table** đã sửa (B=X, X=jump, R=throw).
- **Meta description** đã thêm cho tất cả pages.
- **Footer** đã chuẩn hóa.
- **h1** có trên mỗi trang.
- **vercel.json** + **.gitignore** đã tạo.

### Vấn đề tồn động (chưa fix)
1. **Dịch chưa hoàn thiện**: Nhiều bước walkthrough còn tiếng Anh (temple, quest 5-12). Tạm bỏ qua (batch riêng). ⏸️
2. **Nội dung chi tiết**: ✅ Shrine solutions, Shrine Quests details, Side content, Dragon's Tears coordinates đã bổ sung.
3. **Ảnh minh họa**: ✅ mỗi trang ≥3 ảnh, alt tiếng Việt, 0 broken.
4. **Image attribution**: ✅ ganondorf.jpg có source URL + license; footer ghi nguồn ảnh.
5. **Large images**: ✅ đã xóa shrine-list.svg và zonai-parts.svg.
6. **Nav consistency**: ✅ Đã chuẩn hóa navbar across all pages (Vietnamese labels).
7. **Unreachable pages**: ✅ Đã có nav links từ index.html đến tất cả pages.

### Goal đang thực hiện
- **Mục tiêu chính**: Hoàn thiện nội dung guide (chi tiết, không bỏ sót bước nào) với ảnh minh họa.
- **Tạm bỏ qua**: Lỗi dịch (mixed language) — sẽ làm batch riêng sau.
- **Focus hiện tại**: Nội dung completeness, image attribution, missing content.

### Các bước tiếp theo
1. Thêm giải pháp ngắn per-shrine (hoặc link đến guide chi tiết).
2. Thêm chi tiết shrine quests (giver, trigger, steps).
3. Thêm side quests, Korok, Wells, Caves sections.
4. Thêm ảnh minh họa cho các trang còn ít ảnh.
5. Fix image attribution (source URLs, licenses).
6. Xóa large images không dùng (shrine-list.svg 44MB).
7. Review content-only với sub-agent (model chính opencode-go/beam-free).
8. Khi content pass → làm batch dịch (translation).
9. Deploy lại Vercel sau khi fix.

### Trạng thái deploy
- GitHub: https://github.com/phucnd0604/toto-guide (pushed)
- Vercel: https://toto-guide-five.vercel.app (deployed, HTTP 200)
- Local server: http://localhost:8000 (chạy start-server.bat)
PY