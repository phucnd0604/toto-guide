# TOTK Guide Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a multi-page, calm warm-themed static guide site for Zelda: Tears of the Kingdom (Vietnamese), covering A-Z without missing major content.

**Architecture:** Static HTML/CSS/JS. Shared `assets/style.css` + `assets/app.js`. One HTML file per major section, consistent navbar/sidebar. Content layered: overview pages with summaries + dedicated detail sections. Accordion (`<details>`) for deep dives. Images from Wikimedia Commons + links to wiki screenshots.

**Tech Stack:** HTML5, CSS3 (custom properties), vanilla JS. Python http.server for local hosting. Google Fonts (Chakra Petch, Inter).

**Spec:** `E:\GameGuide\docs\design.md`

## Global Constraints
- Static only; no build toolchain.
- Vietnamese language.
- Theme: bg #0B1220, card #131C2E, text #E5E7EB, muted #94A3B8, primary amber #F59E0B, accent teal #2DD4BF, border #1F2A3F.
- Fonts: Chakra Petch (headings), Inter (body).
- No copyrighted Nintendo images; only Wikimedia CC + external wiki links.
- Responsive: 375px, 768px, 1024px, 1440px.
- Accessibility: focus visible, reduced-motion respected, semantic headings.

## Review Focus
- Missing content: every main quest (23), temple (6), boss, early-game priority.
- Broken internal links between pages.
- Mobile navigation usability (navbar overflow, sidebar).
- Image alt text and loading.
- Accordion default state (summary visible, details collapsed except first).
- Color contrast >= 4.5:1 for body text.

---

## File Structure
- Create: `assets/style.css` — shared theme + layout + components.
- Create: `assets/app.js` — mobile nav toggle, active link highlight, details persistence.
- Modify: `index.html` — convert to overview + quick start + TOC links.
- Create: `pages/mechanics.html`
- Create: `pages/abilities.html`
- Create: `pages/tutorial.html`
- Create: `pages/early-game.html`
- Create: `pages/main-story.html`
- Create: `pages/temples.html`
- Create: `pages/endgame.html`
- Create: `pages/shrines.html`
- Create: `pages/tips.html`
- Create: `pages/faq.html`

---

### Task 1: Shared stylesheet + JS

**Files:**
- Create: `E:\GameGuide\assets\style.css`
- Create: `E:\GameGuide\assets\app.js`

**Interfaces:**
- Produces: CSS classes `.container`, `.layout`, `.sidebar`, `.card`, `.grid`, `.btn`, `.badge`, `.toc`, `.navbar`, `.page-title`, `.details` styling; JS functions `initNav()`, `initActiveLinks()`.

- [ ] **Step 1: Create assets directory and style.css with theme variables + base + navbar + layout + card + grid + details + responsive.**
- [ ] **Step 2: Create app.js with mobile nav toggle and active-link highlight.**
- [ ] **Step 3: Verify by opening index.html (after Task 2) in browser; no console errors.**

### Task 2: Convert index.html to overview

**Files:**
- Modify: `E:\GameGuide\index.html`

**Interfaces:**
- Consumes: `assets/style.css`, `assets/app.js`.

- [ ] **Step 1: Replace single-page content with overview: hero (calm), quick-start 5 steps, feature cards linking to each page, image (logo), footer.**
- [ ] **Step 2: Verify navbar links resolve.**

### Task 3: Mechanics page

**Files:**
- Create: `E:\GameGuide\pages\mechanics.html`

- [ ] **Step 1: Write page with sections: hearts, stamina, temperature, energy cell, gloom/depths, weather. Include table of controls shortcut.**
- [ ] **Step 2: Verify.**

### Task 4: Abilities page

**Files:**
- Create: `E:\GameGuide\pages\abilities.html`

- [ ] **Step 1: Write Ultrahand, Fuse, Ascend, Recall, Autobuild, others with tips and examples.**
- [ ] **Step 2: Verify.**

### Task 5: Tutorial page

**Files:**
- Create: `E:\GameGuide\pages\tutorial.html`

- [ ] **Step 1: Step-by-step Great Sky Island (5.1-5.6) with image map.**
- [ ] **Step 2: Verify.**

### Task 6: Early-game page

**Files:**
- Create: `E:\GameGuide\pages\early-game.html`

- [ ] **Step 1: Lookout Landing, paraglider, horse, towers, shrines, regions order, early armor.**
- [ ] **Step 2: Verify.**

### Task 7: Main Story page

**Files:**
- Create: `E:\GameGuide\pages\main-story.html`

- [ ] **Step 1: 23 quests as <details> with summary + steps + tips.**
- [ ] **Step 2: Verify all quests present (count 23).**

### Task 8: Temples page

**Files:**
- Create: `E:\GameGuide\pages\temples.html`

- [ ] **Step 1: Wind, Fire, Water, Lightning, Spirit, Hyrule Castle sections with puzzle steps + boss strategy.**
- [ ] **Step 2: Verify.**

### Task 9: Endgame page

**Files:**
- Create: `E:\GameGuide\pages\endgame.html`

- [ ] **Step 1: Master Sword, Dragon's Tears, Ganondorf final, 100% completion checklist. Image Ganondorf.**
- [ ] **Step 2: Verify.**

### Task 10: Shrines page

**Files:**
- Create: `E:\GameGuide\pages\shrines.html`

- [ ] **Step 1: Group 152 shrines by region with name + solution summary + link to wiki. Note: not every shrine detailed; link to full list.**
- [ ] **Step 2: Verify.**

### Task 11: Tips page

**Files:**
- Create: `E:\GameGuide\pages\tips.html`

- [ ] **Step 1: Cooking, Fuse recipes, armor/upgrades, exploration, rupee, Depths, Sky.**
- [ ] **Step 2: Verify.**

### Task 12: FAQ page

**Files:**
- Create: `E:\GameGuide\pages\faq.html`

- [ ] **Step 1: FAQ items as <details>.**
- [ ] **Step 2: Verify.**

---

### Task 13: Polish & cross-check

**Files:**
- Modify: all pages.

- [ ] **Step 1: Check all internal links, navbar, footer, responsive, console errors.**
- [ ] **Step 2: Update start-server.bat (already exists).**
- [ ] **Step 3: Final review.**

---

## Execution Handoff

Plan saved. Which execution approach?
- Subagent-driven (fresh subagent per task + review)
- Native (I implement all in this session, one review at end)

I recommend Native for this content work (many small pages, low risk), because tasks are independent content writing and a single review at the end is sufficient. Does the plan capture what you want, and which approach?