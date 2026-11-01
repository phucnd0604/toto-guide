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
2. Tải toàn bộ ảnh về `images/<region>/` bằng script, đặt tên theo tên file gốc để dễ truy vết.
3. Ghi chú thứ tự ảnh theo thứ tự xuất hiện trong trang (để đặt đúng chỗ).

## Bước 3: Dịch nội dung (QUAN TRỌNG)
- Dịch **toàn bộ** text sang tiếng Việt. Không để sót câu/đoạn tiếng Anh.
- Giữ nguyên: thuật ngữ chuyên môn (Ultrahand, Fuse, Ascend, Recall, Zonai, …) và tên riêng (Link, Zelda, Rauru, tên shrine/temple/NPC, tên item).
- **Không** dịch máy móc (word-for-word). Phải đọc hiểu rồi viết lại bằng tiếng Việt tự nhiên.
- Kiểm tra bằng cách search các từ tiếng Anh còn sót (gather, hammer, ignite, advise, discover, deal, time, cut, straightforward, Keese, pond, hop, etc.) và dịch chúng.
- Dùng @translation skill nếu cần.

## Bước 4: Trình bày (cấu trúc section)
Mỗi vùng là 1 `<section id="<region>">` chứa layout 2 cột:

### 4.1 Layout 2 cột
```html
<div class="region-cols">
  <div class="col-left">
    <h3>Game Progress Route (N bước)</h3>
    <ol>  <!-- index steps, Vietnamese, no images -->
      <li>Tiêu đề bước (tiếng Việt).</li>
      ...
    </ol>
  </div>
  <div class="col-right">
    <!-- detailed walkthrough with h3 sub-sections + images in details -->
  </div>
</div>
```

### 4.2 Walkthrough chi tiết (col-right)
- Chia thành các `<h3>` sub-section (theo fextralife: Prologue, Room of Awakening, Temple of Time, Ukouh Shrine, In-isa Shrine, Gutanbac Shrine, Return to Temple, Nachoyah Shrine).
- Mỗi sub-section có `<p>` mô tả chi tiết (tiếng Việt) + `<details>` chứa ảnh.
- Ảnh đặt **ngay sau bước** mà nó minh họa (khớp thứ tự PDF).

### 4.3 Ảnh inline trong `<details>` (gộp theo bước)
Mỗi bước/sub-section có **một thẻ `<details>` duy nhất** chứa tất cả ảnh minh họa (gộp liên tiếp, không tách nhiều thẻ):
```html
<details style="margin:.4rem 0">
  <summary style="cursor:pointer;color:var(--primary);font-weight:600">📷 Xem ảnh (N)</summary>
  <figure style="margin:.6rem 0">
    <img loading="lazy" decoding="async" src="../images/<region>/<file>.png" alt="Mô tả tiếng Việt" style="max-width:100%">
    <figcaption>Mô tả (Fextralife)</figcaption>
  </figure>
  ...
</details>
```
- `alt` tiếng Việt; `figcaption` tiếng Việt.
- Không border/radius (đã set trong CSS), căn giữa (figure margin auto).
- Nếu nhiều ảnh liên tiếp trong cùng 1 bước → gộp chung 1 `<details>`, không tách.
- **Không để ảnh trùng lặp** trong cùng section.

### 4.4 Mẹo & hoàn tất
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
- **Kiểm tra không còn từ tiếng Anh sót** (search: gather, hammer, ignite, advise, discover, deal, time, cut, straightforward, Keese, pond, hop, surprise, melee, Leo stone, Pick Rushroom, gifts, elevated, Inside tree, Touch glowing, clearing, hop in, etc.)

## Bước 6: Commit & Deploy
1. `git add pages/progress-route.html images/<region>/`
2. `git commit -m "<Region>: detailed walkthrough + images"`
3. `git push origin master` (Vercel auto-deploy).
4. Verify HTTP 200 cho trang và các ảnh mới.

## Checklist trước khi chuyển vùng tiếp
- [ ] Số bước index khớp fextralife.
- [ ] Tất cả ảnh trong PDF/CDN đã tải và đặt đúng chỗ.
- [ ] Nội dung dịch tiếng Việt 100% (trừ thuật ngữ/tên riêng).
- [ ] Không còn từ tiếng Anh sót trong nội dung.
- [ ] Mỗi ảnh bọc trong `<details>` (gộp theo bước).
- [ ] Không ảnh trùng lặp.
- [ ] Audit ALL OK.
- [ ] Commit + push + deploy verified.