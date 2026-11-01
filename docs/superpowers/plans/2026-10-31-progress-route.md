# Progress Route Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Tạo trang `pages/progress-route.html` canonical theo 9 vùng fextralife, index đầy đủ trước (Phase A DONE), rồi chi tiết từng vùng (Phase B).

**Architecture:** Một trang HTML tĩnh, sidebar TOC, main content chia section theo vùng. Nguồn: fextralife qua Google Translate proxy; ảnh từ static0.fextralifeimages.com tải về `images/`. Giữ multi-page: mechanics, abilities, shrines, tips, faq, index.

**Tech Stack:** HTML/CSS (assets/style.css), JS (assets/app.js).

**Spec:** docs/superpowers/specs/2026-10-31-progress-route-design.md

## Global Constraints
- Tiếng Việt; chỉ Google Fonts CDN external.
- Mỗi trang 1 h1, meta description, alt text tiếng Việt.
- Ảnh không broken; ưu tiên ảnh đã tải.
- Không link ra domain khác ngoài Google Fonts.

## Review Focus
- Index đầy đủ 9 vùng + bước theo fextralife (Phase A DONE, verified).
- Ảnh map đúng vùng, không broken.
- Không còn link đến trang đã xóa.
- Responsive/anchor không vỡ.

---

## Phase A (DONE)
- Full index 9 regions, step counts verified vs fextralife (Sky 19, Central 27, Hebra 31, Eldin 25, Lanayru 36, Master Sword 14, Gerudo 23, Fifth Sage 35, Demon King 14).
- Reviewer approved (1 Important fixed: Lanayru 34->36). Commit 4eff15b.

## Phase B – Chi tiết từng vùng (lần lượt từng index 1)
Mỗi task: tải ảnh về images/, expand section tương ứng với walkthrough chi tiết (bước + mẹo + ảnh), verify audit, commit.

### Task B1: Central Hyrule (27 bước)
**Files:** Modify `pages/progress-route.html`; add `images/fx-central-hyrule.png`
**Image URL:** https://static0.fextralifeimages.com/file/zeldatearsofthekingdom/thumb/7/79/Walkthrough_chr5_zelda_tears_of_the_kingdom_wiki_guide-min.png/300px-Walkthrough_chr5_zelda_tears_of_the_kingdom_wiki_guide-min.png
- [ ] Step 1: Tải ảnh về images/fx-central-hyrule.png.
- [ ] Step 2: Expand section #central: 27 bước + mẹo + figure ảnh.
- [ ] Step 3: Verify audit (images/anchors/h1/meta).
- [ ] Step 4: Commit.

### Task B2: Hebra – Tulin (31 bước)
**Files:** Modify `pages/progress-route.html`; add `images/fx-hebra.png`
**Image URL:** https://static0.fextralifeimages.com/file/zeldatearsofthekingdom/thumb/3/3d/Walkthrough_chr18_zelda_tears_of_the_kingdom_wiki_guide-min.png/300px-Walkthrough_chr18_zelda_tears_of_the_kingdom_wiki_guide-min.png
- [ ] Step 1: Tải ảnh.
- [ ] Step 2: Expand #hebra: 31 bước + mẹo + ảnh.
- [ ] Step 3: Verify + commit.

### Task B3: Eldin – Yunobo (25 bước)
**Files:** Modify `pages/progress-route.html`; add `images/fx-eldin.png`
**Image URL:** https://static0.fextralifeimages.com/file/zeldatearsofthekingdom/thumb/3/33/Game_progress_route3_zelda_totk_wiki_guide-min.png/300px-Game_progress_route3_zelda_totk_wiki_guide-min.png
- [ ] Step 1: Tải ảnh.
- [ ] Step 2: Expand #eldin: 25 bước + mẹo + ảnh.
- [ ] Step 3: Verify + commit.

### Task B4: Lanayru – Sidon (36 bước)
**Files:** Modify `pages/progress-route.html`; add `images/fx-lanayru.png`
**Image URL:** https://static0.fextralifeimages.com/file/zeldatearsofthekingdom/thumb/1/12/Game_progress_route1_zelda_totk_wiki_guide-min.png/300px-Game_progress_route1_zelda_totk_wiki_guide-min.png
- [ ] Step 1: Tải ảnh.
- [ ] Step 2: Expand #lanayru: 36 bước + mẹo + ảnh.
- [ ] Step 3: Verify + commit.

### Task B5: Master Sword (14 bước)
**Files:** Modify `pages/progress-route.html`; add `images/fx-mastersword.png`
**Image URL:** https://static0.fextralifeimages.com/file/zeldatearsofthekingdom/thumb/7/7f/Game_progress_route5_zelda_totk_wiki_guide-min.png/300px-Game_progress_route5_zelda_totk_wiki_guide-min.png
- [ ] Step 1: Tải ảnh.
- [ ] Step 2: Expand #mastersword: 14 bước + mẹo + ảnh.
- [ ] Step 3: Verify + commit.

### Task B6: Gerudo – Riju (23 bước)
**Files:** Modify `pages/progress-route.html`; add `images/fx-gerudo.png`
**Image URL:** https://static0.fextralifeimages.com/file/zeldatearsofthekingdom/thumb/6/6f/Game_progress_route4_zelda_totk_wiki_guide-min.png/300px-Game_progress_route4_zelda_totk_wiki_guide-min.png
- [ ] Step 1: Tải ảnh.
- [ ] Step 2: Expand #gerudo: 23 bước + mẹo + ảnh.
- [ ] Step 3: Verify + commit.

### Task B7: Fifth Sage – Mineru (35 bước)
**Files:** Modify `pages/progress-route.html`; add `images/fx-fifth.png`
**Image URL:** https://static0.fextralifeimages.com/file/zeldatearsofthekingdom/thumb/7/7c/Game_progress_route6_zelda_totk_wiki_guide-min.png/300px-Game_progress_route6_zelda_totk_wiki_guide-min.png
- [ ] Step 1: Tải ảnh.
- [ ] Step 2: Expand #fifth: 35 bước + mẹo + ảnh.
- [ ] Step 3: Verify + commit.

### Task B8: Demon King (14 bước)
**Files:** Modify `pages/progress-route.html`; add `images/fx-demonking.png`
**Image URL:** https://static0.fextralifeimages.com/file/zeldatearsofthekingdom/thumb/6/6f/Game_progress_route4_zelda_totk_wiki_guide-min.png/300px-Game_progress_route4_zelda_totk_wiki_guide-min.png
- [ ] Step 1: Tải ảnh.
- [ ] Step 2: Expand #final: 14 bước + mẹo + ảnh.
- [ ] Step 3: Verify + commit.

### Task B9: Phase B review & deploy
- [ ] Run full audit; fix issues.
- [ ] Commit + push + Vercel smoke test.

## Execution Handoff
Plan updated for Phase B. Please review. Does it capture what you want? Choose execution approach (subagent-driven or native) to start B1.