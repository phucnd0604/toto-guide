# Design: Trang Progress Route liền mạch (TOTK Guide)

## Intent
Hiện tại nội dung cốt truyện đang rải rác giữa `tutorial`, `early-game`, `main-story`, `temples`, `endgame`. Người chơi gà mờ khó theo dõi thứ tự. Mục tiêu: tạo **một trang canonical** theo thứ tự tiến trình của fextralife (Progress Route + Walkthrough), gộp cả thứ tự và bước chi tiết + ảnh, xóa các trang trùng lặp.

## Goals
- Một trang `pages/progress-route.html` chứa toàn bộ tiến trình từ Prologue → Demon King.
- Mỗi vùng: mục tiêu, các bước granular (walkthrough), mẹo, ảnh minh họa (tái dùng ảnh đã có), liên kết chéo đến shrines/tips khi cần.
- Multi-page vẫn giữ: mechanics, abilities, shrines, tips, faq, index.
- Không link ra domain khác (chỉ Google Fonts).

## Non-goals
- Không thêm shrine solutions mới (đã có ở shrines.html).
- Không dịch lại (giữ tiếng Việt hiện có).
- Không tải ảnh mới từ fextralife (bị chặn transport); tái dùng 34 ảnh hiện có.

## Approach (đã chọn: Hybrid + Phased)
- Nguồn nội dung: fextralife (Game Progress Route + Walkthrough) qua proxy Google Translate; ảnh từ static0.fextralifeimages.com.
- Tạo `pages/progress-route.html` canonical theo 9 vùng fextralife: Prologue/Sky → Central Hyrule → Hebra → Eldin → Lanayru → Master Sword → Gerudo → Fifth Sage → Demon King.
- **Phase A – Index:** Dựng trang với đầy đủ index (danh sách vùng + các bước theo fextralife) làm khung.
- **Phase B – Detail (từng vùng):** Rà soát từng index, build progress route chi tiết + walkthrough + ảnh cho mỗi vùng.
- Phase C: Verify (audit), commit, deploy.
- Xóa 5 trang story cũ (đã làm) để tránh trùng lặp.
- Cập nhật navbar/index trỏ đến `progress-route.html`.
- Giữ `shrines.html`, `tips.html`, `faq.html`, `mechanics.html`, `abilities.html`.

## Cấu trúc trang (theo fextralife)
1. Prologue (Hyrule Castle Ruins → Great Sky Island portal)
2. Great Sky Islands (4 shrine, Temple of Time, Recall, rời đảo)
3. Central Hyrule Part I (Lookout Landing, Purah Pad, Paraglider, tower, Regional Phenomena)
4. Hebra Region – Vow of Tulin (Wind Temple + Colgera)
5. Eldin Region – Vow of Yunobo (Fire Temple + Marbled Gohma)
6. Lanayru Region – Vow of Sidon (Water Temple + Mucktorok)
7. The Master Sword (Korok Forest, Phantom Ganon, Light Dragon)
8. Gerudo Region – Vow of Riju (Lightning Temple + Queen Gibdo)
9. Fifth Sage (Ring Ruins, Dragonhead Island, Mineru construct, Seized Construct)
10. Defeat the Demon King (Hyrule Castle Depths, Ganondorf, Demon Dragon)

Mỗi section: h2 vùng, card với objectives, ol bước chi tiết, tips, figure ảnh, details boss nếu có.

## Files touched
- Create: `pages/progress-route.html`
- Modify: `index.html` (nav + mục lục + quick start), `pages/*.html` (nav)
- Delete: `tutorial.html`, `early-game.html`, `main-story.html`, `temples.html`, `endgame.html`
- Keep: mechanics, abilities, shrines, tips, faq

## Risks
- Migrate lớn: cần không mất nội dung đã viết (đặc biệt temples/main-story đang chỉnh dở).
- Broken links sau khi xóa trang cũ → cập nhật tất cả href.
- Ảnh map theo vùng; một số vùng có ít ảnh → tái dùng ảnh temple tương ứng.

## Approval
Chờ xác nhận từ người dùng trước khi build.