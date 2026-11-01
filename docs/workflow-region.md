# Workflow chuẩn – Xây dựng chi tiết 1 vùng (Prologue & Great Sky Island làm mẫu)

## Tổng quan
Mỗi vùng (region) được build theo 6 bước: **Lấy nội dung → Lấy ảnh → Dịch → Trình bày → Kiểm tra → Commit/Deploy**.  
Tham chiếu mẫu đã hoàn thành: section `#prologue` trong `pages/progress-route.html`.

---

## Bước 1: Lấy nội dung từ fextralife
1. Mở **Game Progress Route** để lấy danh sách bước (index):
   `https://translate.google.com/translate?sl=en&tl=vi&u=https://zeldatearsofthekingdom.wiki.fextralife.com/Game_Progress_Route`
   → tab tương ứng vùng (ví dụ Great Sky Island).
2. Mở **Walkthrough** tab tương ứng để lấy walkthrough chi tiết:
   `https://translate.google.com/translate?sl=en&tl=vi&u=https://zeldatearsofthekingdom.wiki.fextralife.com/Walkthrough#tabber-<Region>`
   Và/hoặc Subcontent page:
   `https://translate.google.com/translate?sl=en&tl=vi&u=https://zeldatearsofthekingdom.wiki.fextralife.com/Subcontent:Walkthrough_<N>_<Region>`
3. Lưu text đã dịch về file `fextralife/<region>.txt` để tham chiếu.
4. Đếm số bước trong Game Progress Route → đây là số `<li>` trong index.

## Bước 2: Lấy ảnh
1. Từ trang Walkthrough (đã fetch qua proxy), trích tất cả URL ảnh dạng:
   `https://static0.fextralifeimages.com/file/zeldatearsofthekingdom/.../<filename>.png`
   (bao gồm cả thumbnail 400px và full).
2. Tải toàn bộ ảnh về `images/gsi/` (hoặc `images/<region>/`) bằng script, đặt tên theo tên file gốc để dễ truy vết.
3. Ghi chú thứ tự ảnh theo thứ tự xuất hiện trong trang (để đặt đúng chỗ).

## Bước 3: Dịch nội dung
- Dịch toàn bộ text sang **tiếng Việt**.
- Giữ nguyên: thuật ngữ chuyên môn (Ultrahand, Fuse, Ascend, Recall, Zonai, …) và tên riêng (Link, Zelda, Rauru, tên shrine/temple/NPC).
- Không để sót câu tiếng Anh.

## Bước 4: Trình bày (cấu trúc section)
Mỗi vùng là 1 `<section id="<region>">` chứa 1 `<div class="card">`:

### 4.1 Index (đánh số)
```html
<ol>
  <li><strong>Tiêu đề bước (tiếng Việt).</strong> Mô tả chi tiết bước...</li>
  ...
</ol>
```
- Mỗi `<li>` bắt đầu bằng `<strong>` tiêu đề bước, sau đó mô tả chi tiết.
- Số `<li>` phải khớp số bước trong Game Progress Route.

### 4.2 Ảnh inline trong `<details>`
Mỗi ảnh được bọc trong thẻ đóng để trang gọn:
```html
<details style="margin:.4rem 0">
  <summary style="cursor:pointer;color:var(--primary);font-weight:600">📷 Xem ảnh</summary>
  <figure style="margin:.6rem 0">
    <img loading="lazy" decoding="async" src="../images/<region>/<file>.png" alt="Mô tả tiếng Việt" style="max-width:100%">
    <figcaption>Mô tả (Fextralife)</figcaption>
  </figure>
</details>
```
- Ảnh đặt **ngay sau bước** mà nó minh họa (khớp thứ tự PDF).
- `alt` tiếng Việt; `figcaption` tiếng Việt.
- Không border/radius (đã set trong CSS), căn giữa (figure margin auto).

### 4.3 Mẹo & hoàn tất
```html
<p><strong>Mẹo:</strong> ...</p>
<p><em><Region> – chi tiết hoàn tất.</em></p>
```

## Bước 5: Kiểm tra (audit)
Chạy script audit:
- 0 broken images (mọi src resolve được).
- 0 broken anchors.
- Mỗi trang 1 `<h1>`, meta description present.
- Không link ngoài (chỉ Google Fonts).
- Số `<li>` trong index khớp fextralife.
- HTML balanced.

## Bước 6: Commit & Deploy
1. `git add pages/progress-route.html images/<region>/`
2. `git commit -m "<Region>: detailed walkthrough + images"`
3. `git push origin master` (Vercel auto-deploy).
4. Verify HTTP 200 cho trang và các ảnh mới.

## Checklist trước khi chuyển vùng tiếp
- [ ] Số bước index khớp fextralife.
- [ ] Tất cả ảnh trong PDF/CDN đã tải và đặt đúng chỗ.
- [ ] Nội dung dịch tiếng Việt (trừ thuật ngữ/tên riêng).
- [ ] Mỗi ảnh bọc trong `<details>`.
- [ ] Audit ALL OK.
- [ ] Commit + push + deploy verified.