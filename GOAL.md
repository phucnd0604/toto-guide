# GOAL.md – Mục tiêu chi tiết dự án TOTK Guide

## Mục tiêu tổng quát
Tạo website hướng dẫn chơi The Legend of Zelda: Tears of the Kingdom (TOTK) đầy đủ từ A đến Z, dành cho người mới (gà mờ), bằng tiếng Việt, với ảnh minh họa, host trên domain riêng (xxx.com), không link ra domain khác.

## Tiêu chí verify (phải pass hết)
1. **Nội dung đầy đủ như IGN Walkthrough** (hoặc chi tiết hơn):
   - Điều khiển cơ bản (Switch).
   - Cơ chế cốt lõi (máu, stamina, nhiệt độ, pin Zonai, Gloom, Depths, thời tiết).
   - 4 năng lực chính + Autobuild + các năng lực khác.
   - Tutorial Great Sky Island từng bước.
   - Early game (Lookout Landing, Paraglider, ngựa, tower, vùng).
   - Main Story 23 quest granular (bước làm chi tiết + mẹo + ảnh).
   - 5 Temple + Boss (puzzle steps + boss strategy + ảnh).
   - Endgame (Master Sword, Dragon's Tears, Ganondorf final, 100%).
   - Shrine index 152 + 31 shrine quests (tên + trial + giải pháp ngắn + link chi tiết).
   - Tips (nấu ăn, Fuse recipes, giáp, Depths, Sky, Korok, rupee, 100%).
   - FAQ.
2. **Ảnh minh họa**: mỗi phần có ảnh, alt text tiếng Việt, không broken.
3. **Không link ra domain khác**: toàn bộ nội dung thuộc xxx.com. Chỉ Google Fonts CDN (chấp nhận).
4. **Multi-page**: không dùng single page với anchor scroll-heavy. Mỗi phần 1 trang riêng.
5. **Dark/Light mode**: toggle hoạt động, lưu preference.
6. **Responsive**: 375px, 768px, 1024px, 1440px.
7. **Accessibility**: focus visible, reduced-motion, skip link, semantic headings (h1, h2, h3).
8. **Không có lỗi**: mojibake, broken images, broken anchors, duplicate content, missing content promised.
9. **Image attribution**: ghi rõ nguồn, license cho mỗi ảnh.
10. **Controls accuracy**: đúng mapping nút TOTK.
11. **Meta description**: mỗi trang có meta description chính xác.
12. **Footer**: attribution đầy đủ, link sources.
13. **h1**: mỗi trang 1 h1.

## Trạng thái hiện tại
- **Multi-page site**: 11 trang (index + 10 pages). ✅
- **Self-contained**: 0 external content links. ✅
- **Git repo**: https://github.com/phucnd0604/toto-guide ✅
- **Vercel deploy**: https://toto-guide-five.vercel.app ✅
- **Dark/Light mode**: hoạt động ✅
- **Nội dung chính**: 23 quests, 5 temples+boss, 152 shrines+31 shrine quests, early game, endgame, tips, FAQ, mechanics, abilities, tutorial. ✅
- **Ảnh minh họa**: 30+ ảnh, 0 broken. ✅
- **Controls table**: đã sửa B/X/R mapping. ✅
- **Meta description**: đã thêm cho tất cả pages. ✅
- **Footer**: đã chuẩn hóa. ✅
- **h1**: mỗi trang 1 h1. ✅
- **Large images**: shrine-list.svg (44MB) và zonai-parts.svg (4.5MB) đã xóa khỏi images/. ✅
- **Image attribution**: ganondorf.jpg đã có source URL + license CC BY 4.0. ✅
- **Dragon's Tears**: có bảng vùng nhưng chưa có tọa độ chính xác. ⚠️
- **Shrine solutions**: chưa có giải pháp ngắn per-shrine. ⚠️
- **Shrine Quests details**: chưa có giver/trigger/steps. ⚠️
- **Side quests/Korok/Wells/Caves**: chưa có chi tiết. ⚠️
- **Duplicate content**: quests 7-10 đã expand, duplicate trong quest 11 đã remove. ✅
- **Mixed language**: Tạm bỏ qua (sẽ làm batch riêng). ⏸️

## Các vấn đề tồn động (chưa fix)
1. **Shrine solutions**: ✅ đã thêm cột "Gợi ý giải" cho 152 shrine.
2. **Shrine Quests details**: ✅ đã thêm giver/trigger + bước làm cho 31 shrine quests.
3. **Side quests/Korok/Wells/Caves**: ✅ đã thêm section tóm tắt + mẹo + theo dõi tiến độ.
4. **Dragon's Tears**: ✅ đã thêm tọa độ cho 12 tears.
5. **Image attribution**: ✅ ganondorf.jpg có source URL + license; footer ghi nguồn ảnh.
6. **Large images**: ✅ đã xóa shrine-list.svg và zonai-parts.svg.
7. **Image count**: ✅ mỗi trang ≥3 ảnh, alt tiếng Việt.
8. **Mixed language**: ✅ Đã dịch batch walkthrough/temple (chỉ còn tên riêng/thuật ngữ game). ⏸️ (không còn pending)

## Các bước tiếp theo (theo thứ tự ưu tiên)
1. **Thêm giải pháp ngắn per-shrine** (hoặc link đến guide chi tiết — nhưng no external links, nên inline).
2. **Thêm chi tiết shrine quests** (giver, trigger, steps).
3. **Thêm side quests, Korok, Wells, Caves sections**.
4. **Thêm ảnh minh họa** cho các trang còn ít ảnh.
5. **Fix image attribution** (source URLs, licenses).
6. **Xóa large images** không dùng (shrine-list.svg 44MB).
7. **Review content-only** với sub-agent (model chính opencode-go/beam-free).
8. **Khi content pass** → làm batch dịch (translation).
9. **Deploy lại Vercel** sau khi fix.

## Trạng thái deploy
- GitHub: https://github.com/phucnd0604/toto-guide (pushed)
- Vercel: https://toto-guide-five.vercel.app (deployed, HTTP 200)
- Local server: http://localhost:8000 (chạy start-server.bat)

## Sub-agent review
- Tất cả sub-agent reviewer phải dùng model chính (opencode-go/beam-free), không dùng model khác.
- Review focus vào content (skip translation).
- Nếu không pass → sửa cho tới khi không còn feedback.

## Mục tiêu Phase 3 – Polish, Responsive & Final Verification
**Mục tiêu:** Hoàn thiện trải nghiệm (responsive, accessibility, performance, SEO, attribution per-image), kiểm thử toàn diện, và chốt release.

### Trạng thái hiện tại (2026-10-31)
- Content Phase 2: PASS (shrines, shrine quests, side content, Dragon's Tears, FAQ).
- Translation batch: PASS (walkthrough/temple steps đã dịch; chỉ còn tên riêng/thuật ngữ game).
- Deploy: PASS (Vercel HTTP 200).
- Phase 3 Polish: PASS (responsive, accessibility, performance, SEO, attribution, cross-browser). ✅

### Các bước tiếp theo (ưu tiên)
1. Responsive test & fix (navbar/sidebar, tables horizontal scroll, image sizing) ở 375/768/1024/1440.
2. Accessibility audit: keyboard nav, focus order, skip link, alt text, reduced-motion, semantic headings, color contrast.
3. Performance: kiểm tra kích thước ảnh, lazy loading, font loading; tối ưu CSS/JS.
4. SEO: meta description/title chính xác, canonical? (static), Open Graph cơ bản.
5. Image attribution: ghi rõ nguồn/license cho từng ảnh (hoặc footer tổng hợp + per-figure caption).
6. Cross-browser test (Firefox/Chrome/Edge) + mobile.
7. Final content review với sub-agent model opencode-go/beam-free.
8. Redeploy Vercel + smoke test.

### Tiêu chí pass (Phase 3)
- Responsive pass ở 4 breakpoint, không overflow ngang.
- Accessibility pass (keyboard, focus visible, alt, headings).
- Performance: không ảnh >2MB trong pages, lazy loading cho ảnh dưới fold.
- SEO: mỗi trang có title/meta description unique.
- Attribution rõ nguồn/license.
- Review sub-agent không còn feedback.
- Deploy HTTP 200 + smoke test pass.

---

## Mục tiêu tiếp theo (Phase 2 – Content completeness) [HOÀN THÀNH]
**Mục tiêu:** Hoàn thiện nội dung chi tiết theo GOAL.md, ưu tiên shrine solutions, shrine quests details, side content tóm tắt, tăng ảnh minh họa, rồi review content-only.

### Trạng thái đã xác minh (2026-10-31)
- 11 trang + index, navbar/footer chuẩn, h1/meta OK. ✅
- Ảnh: 30+ webp/jpg/svg, 0 broken (đã kiểm tra tham chiếu). ✅
- Large images đã xóa. ✅
- Image attribution ganondorf đã fix. ✅
- Content còn thiếu: shrine solutions per-shrine; shrine quests giver/trigger/steps; side quests/Korok/Wells/Caves tóm tắt; Dragon's Tears tọa độ; image count một số trang. ⚠️

### Các bước tiếp theo (ưu tiên)
1. Thêm cột "Gợi ý giải" ngắn cho 152 shrine (theo trial/type) hoặc section giải chi tiết theo loại trial.
2. Thêm giver/trigger/steps cho 31 shrine quests.
3. Thêm section tóm tắt Side quests, Korok, Wells, Caves (không liệt kê tọa độ toàn bộ).
4. Bổ sung tọa độ chính cho Dragon's Tears (13 vị trí).
5. Tăng ảnh minh họa cho trang còn ít ảnh (mechanics, abilities, tutorial, early-game, endgame, shrines, tips, faq) bằng ảnh hiện có phù hợp.
6. Review content-only với sub-agent model opencode-go/beam-free; sửa đến khi pass.
7. Deploy lại Vercel.

### Tiêu chí pass (Phase 2)
- Mỗi shrine có tên + trial + loại + vùng + gợi ý giải ngắn.
- Mỗi shrine quest có quest + shrine + vùng + giver/trigger + bước làm ngắn.
- Side content có tóm tắt + mẹo + cách theo dõi tiến độ.
- Dragon's Tears có bảng vùng + tọa độ gần đúng.
- Ảnh: mỗi trang ≥ 3 ảnh, alt tiếng Việt, không broken.
- Không link ra domain khác (chỉ Google Fonts).
- Review sub-agent không còn feedback content.
PY