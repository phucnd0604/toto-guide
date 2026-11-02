# Workflow chuẩn – Xây dựng chi tiết 1 vùng (Prologue & Great Sky Island làm mẫu)

## Tổng quan
Mỗi vùng (region) được build theo 6 bước: **Lấy nội dung → Lấy ảnh → Dịch → Trình bày → Kiểm tra → Commit/Deploy**.  
Tham chiếu mẫu đã hoàn thành: `pages/route-prologue.html`.

---

## Bước 1: Lấy nội dung từ fextralife
1. Mở **Game Progress Route** để lấy danh sách bước (index):
   `https://translate.google.com/translate?sl=en&tl=vi&u=https://zeldatearsofthekingdom.wiki.fextralife.com/Game_Progress_Route`
   → tab tương ứng vùng (ví dụ Great Sky Island).
2. Mở **Walkthrough** (`.../Walkthrough`) rồi lấy **tên trang Subcontent thật** từ các link tabber trong HTML — tên không đoán được, ví dụ vùng Prologue trải trên 2 trang:
   - `Subcontent:Walkthrough_1_Prologue`
   - `Subcontent:Walkthrough_2_Great_Sky_Island`
   Một vùng có thể trải trên **nhiều trang** — phải lấy đủ, thiếu trang là thiếu bước/ảnh.
3. Cách fetch: `web_fetch` **cắt ở 100k ký tự** (mất nửa cuối trang). Dùng pwsh `Invoke-WebRequest` tới host đã redirect
   `https://<domain>-wiki-fextralife-com.translate.goog/<Tên_Trang>?_x_tr_sl=en&_x_tr_tl=vi&_x_tr_hl=en`,
   lưu ra `.tmp-src/<part>.html` rồi parse offline (đừng parse bằng mắt).
4. Đếm số bước trong Game Progress Route → đây là số `<li>` trong index.

## Bước 2: Lấy ảnh (dễ sai nhất — đọc kỹ)

**Mỗi trang một folder riêng**: `pages/route-<slug>.html` ↔ `images/<slug>/` (prologue, central, hebra, eldin, …).
Không dùng chung folder, không copy ảnh từ vùng khác sang — ảnh lẫn vùng là lỗi im lặng, verify không bắt được.

Ảnh fextralife **không đánh số theo vùng**: trang 1 có `Walkthrough12-...`, trang 2 có `Walkthrough-gsi12-...`.
Đổi tên kiểu `fx-sky-12` / `Walkthrough-gsi12` là tự tạo nhập nhằng — lần trước chính vì vậy mà ảnh bị gán sai bước.

1. Parse HTML offline, lấy ảnh **theo thứ tự xuất hiện**, kèm **subsection (h3) đang chứa nó**.
   Đây là nguồn chân lý: mỗi ảnh nằm ngay sau đoạn nó minh họa.
2. **Giữ nguyên tên file gốc** của fextralife (`Walkthrough7-...`, `Walkthrough-gsi7-...`), chỉ bỏ tiền tố `400px-` khi đã có bản full.
3. Bản full-size: URL thumbnail chỉ cho 400px. Muốn bản gốc, mở trang `File:<tên file>` và lấy URL
   `.../<hash1>/<hash2>/<tên>.png` trong đó (bản full nằm ở hash khác, **không** suy ra bằng cách xoá `400px-`).
   Không lấy được thì chấp nhận 400px; fextralife trả **429** khi tải dồn → giãn nhịp, đừng retry liên tục.
4. Tải hết về `images/<region>/`. Sau khi đặt ảnh vào trang, **file nào không được dùng thì xoá**
   (ảnh trùng nội dung, logo trang trí không có trong nguồn).

## Bước 3: Dịch nội dung (QUAN TRỌNG)
- Dịch **toàn bộ** text sang tiếng Việt. Không để sót câu/đoạn tiếng Anh.
- Giữ nguyên: thuật ngữ chuyên môn (Ultrahand, Fuse, Ascend, Recall, Zonai, …) và tên riêng (Link, Zelda, Rauru, tên shrine/temple/NPC, tên item).
- **Không** dịch máy móc (word-for-word). Phải đọc hiểu rồi viết lại bằng tiếng Việt tự nhiên.
- Theo **`docs/translation-standard.md`** (bắt buộc): dịch theo ý, cấm Vietglish, đại từ "bạn", đủ ý đi đâu / làm gì / nhận gì.
- **Heading (`h2`, `h3`) giữ tiếng Anh gốc + chú thích tiếng Việt trong ngoặc**, ví dụ
  `Clear Ishodag Shrine (Hoàn thành Đền Thờ Nhỏ Ishodag)`. Heading thuần khái niệm thì chỉ tiếng Việt.
- Kiểm tra tự động thay vì grep tay: `python scripts/check-vietnamese.py` (0 lỗi HARD mới được commit).
- **Cấm** để lại placeholder kiểu "... (content continues: ...)", "sẽ bổ sung", "chi tiết hoàn tất" khi chưa xong.

## Bước 4: Trình bày (cấu trúc trang)
Mỗi vùng là một trang riêng, layout 2 cột (rail index bên trái + walkthrough bên phải):

### 4.1 Layout 2 cột
Mỗi vùng là **một trang riêng** `pages/route-<slug>.html`; index nằm ở rail trái, walkthrough ở `<main>`:

```html
<div class="container layout">
  <aside class="sidebar rail">      <!-- mục lục vùng + <ol class="step-list"> (tiếng Việt, không ảnh) -->
  </aside>
  <main class="content" id="main">
    <h3 id="<region>-s1">...</h3>   <!-- walkthrough: h3 + p + details ảnh -->
  </main>
</div>
```
`scripts/verify-regions.py` nhận diện đúng layout này (cột `2col`); đổi sang cấu trúc khác là báo `flat`.

### 4.2 Walkthrough chi tiết (main)
- Mỗi `<h3>` = **đúng một subsection của nguồn**, không gộp, không tách, **không lệch bậc**.
  Lỗi đã gặp ở Prologue: nội dung giải đố Ukouh nằm dưới h3 "Reach the Temple of Time" còn h3 "Ukouh Shrine"
  lại chứa đoạn tìm In-isa → ảnh theo đó cũng sai chỗ. Kiểm tra: đọc h3 rồi hỏi "đoạn dưới có đúng chủ đề này không?".
- Mỗi subsection: các `<p>` (tiếng Việt) + `<details>` ảnh **đặt ngay sau đoạn mà ảnh minh họa**,
  không dồn hết ảnh xuống cuối mục.
- Số ảnh của một nhóm phải bằng số ảnh nguồn gắn với đoạn đó — không thêm, không bớt.

### 4.3 Ảnh inline trong `<details>` (gộp theo bước)
Mỗi đoạn/bước có **một thẻ `<details>` duy nhất** chứa các ảnh minh họa cho đoạn đó (gộp liên tiếp, không tách nhiều thẻ):
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
- **Không để ảnh trùng lặp**: mỗi file ảnh chỉ xuất hiện đúng 1 lần trong trang (`img` = `uni` ở verify-regions).
- **Caption lấy theo tên bước trong nguồn**, không tự chế chi tiết khung hình (ảnh chụp UI/cutscene rất dễ bị mô tả sai).
  Nhiều ảnh trong một bước thì đánh số: `Đền Thờ Nhỏ Ukouh – bài giải đố 2 (ảnh 1/3)`.
  Muốn caption chi tiết từng khung hình thì **phải mở ảnh ra xem**, không suy từ đoạn văn.
- Không thêm ảnh minh họa/logo không có trong nguồn.

### 4.4 Mẹo & hoàn tất
```html
<p><strong>Mẹo:</strong> ...</p>
<p><em><Region> – chi tiết hoàn tất.</em></p>
```

## Bước 5: Kiểm tra tự động (bắt buộc, tất cả phải pass)
1. **Cân bằng thẻ + ảnh tồn tại** (repo không có `audit.py`): mỗi thẻ mở/đóng bằng nhau, mọi `src="../images/...`
   phải tồn tại, và không còn file ảnh nào trong `images/<region>/` mà trang không dùng.
2. `python scripts/check-vietnamese.py` → **0 lỗi HARD**. Script bắt: heading còn tiếng Anh (đã trừ heading song ngữ có chú thích Việt), cụm Vietglish trong blacklist, mẫu số liệu kiểu `x3`/`5x`. WARN là cụm tiếng Anh lạ cần xem lại.
3. `python scripts/verify-regions.py <region>` → bảng đối chiếu từng vùng:
   - `step/want`: số `<li>` index so với số bước fextralife (EXPECT trong script).
   - `cover`: độ phủ nội dung — mỗi bước index phải xuất hiện trong walkthrough cột phải.
   - `img/uni/ms`: số ảnh dùng, số ảnh khác nhau, ảnh thiếu file.
   - `en`: heading còn tiếng Anh; `xN`: mẫu `x3`; `ph`: placeholder; `layout`: phải là `2col`.
   - Không còn dòng "vùng có vấn đề" cho vùng đang làm.

## Bước 6: Commit & Deploy
1. `git add pages/progress-route.html images/<region>/`
2. `git commit -m "<Region>: detailed walkthrough + images"`
3. `git push origin master` (Vercel auto-deploy).
4. Verify HTTP 200 cho trang và các ảnh mới.

## Checklist trước khi chuyển vùng tiếp
- [ ] `verify-regions.py`: số bước khớp fextralife **và** độ phủ = đủ số bước (vd 19/19).
- [ ] `verify-regions.py`: `en=0`, `xN=0`, `ph=0`, `ms=0`, layout `2col`.
- [ ] Tất cả ảnh trong `images/<region>/` đã dùng hết, không trùng (`uni` = `img`, `ms=0`).
- [ ] Mỗi `<h3>` khớp đúng subsection nguồn (không lệch bậc) và ảnh đặt đúng đoạn nó minh họa.
- [ ] Trang chỉ dùng ảnh trong `images/<slug>/` của chính nó — không có ảnh copy từ vùng khác (kiểm: tên file ảnh phải khớp tiền tố của vùng, ví dụ `chr*` cho Central).
- [ ] Tên file ảnh giữ nguyên gốc fextralife (không tự đổi tên/không có bản trùng độ phân giải).
- [ ] Heading song ngữ đúng chuẩn; nội dung 100% tiếng Việt (trừ tên riêng/thuật ngữ trong glossary).
- [ ] `check-vietnamese.py`: 0 lỗi HARD cho vùng này.
- [ ] Thẻ HTML cân bằng, mọi `src` ảnh tồn tại (repo không có `audit.py`).
- [ ] Commit + push + deploy verified (HTTP 200 trang + ảnh mới).