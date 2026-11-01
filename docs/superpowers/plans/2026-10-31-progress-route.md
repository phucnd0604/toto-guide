# Progress Route Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Tạo trang `pages/progress-route.html` canonical theo 9 vùng fextralife, index đầy đủ trước, rồi chi tiết từng vùng.

**Architecture:** Một trang HTML tĩnh, sidebar TOC, main content chia section theo vùng. Nguồn: fextralife qua Google Translate proxy; ảnh từ static0.fextralifeimages.com tải về `images/`. Giữ multi-page: mechanics, abilities, shrines, tips, faq, index.

**Tech Stack:** HTML/CSS (assets/style.css), JS (assets/app.js). Không framework.

**Spec:** docs/superpowers/specs/2026-10-31-progress-route-design.md

## Global Constraints
- Tiếng Việt; chỉ Google Fonts CDN external.
- Mỗi trang 1 h1, meta description, alt text tiếng Việt.
- Ảnh không broken; ưu tiên ảnh đã tải.
- Không link ra domain khác ngoài Google Fonts.

## Review Focus
- Index đầy đủ 9 vùng + bước theo fextralife.
- Ảnh map đúng vùng, không broken.
- Không còn link đến trang đã xóa.
- Responsive/anchor không vỡ.

---

### Task 1: Phase A – Full Index scaffold
**Files:** Modify `pages/progress-route.html`
- [ ] Step 1: Thay nội dung hiện tại bằng index đầy đủ: 9 vùng, mỗi vùng danh sách bước (tiêu đề ngắn) theo fextralife, có anchor `#region`.
- [ ] Step 2: Verify audit (images/anchors/h1/meta).
- [ ] Step 3: Commit.

### Task 2: Phase B – Region details (Central Hyrule)
**Files:** Modify `pages/progress-route.html`
- [ ] Step 1: Expand section #central với 27 bước fextralife + ảnh Walkthrough_chr5.
- [ ] Step 2: Tải ảnh về images/.
- [ ] Step 3: Verify + commit.

### Task 3: Phase B – Hebra
- [ ] Expand #hebra (31 bước + ảnh Walkthrough_chr18).

### Task 4: Phase B – Eldin
- [ ] Expand #eldin (25 bước + ảnh game_progress_route3).

### Task 5: Phase B – Lanayru
- [ ] Expand #lanayru (36 bước + ảnh game_progress_route1).

### Task 6: Phase B – Master Sword
- [ ] Expand #mastersword (14 bước + ảnh game_progress_route5).

### Task 7: Phase B – Gerudo
- [ ] Expand #gerudo (23 bước + ảnh game_progress_route4).

### Task 8: Phase B – Fifth Sage
- [ ] Expand #fifth (35 bước + ảnh game_progress_route6).

### Task 9: Phase B – Demon King
- [ ] Expand #final (14 bước + ảnh game_progress_route4).

### Task 10: Phase C – Verify & deploy
- [ ] Run audit script; fix issues.
- [ ] Commit + push + Vercel smoke test.

## Execution Handoff
Plan saved. Please review. Does it capture what you want?