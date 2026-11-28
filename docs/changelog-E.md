# Nhật ký & bài học giai đoạn E — dựng lại Lộ trình theo zeldacentral

> Tách khỏi [PROGRESS.md](../PROGRESS.md) ở retro sau T4 (2026-11-28): PROGRESS.md giữ bảng trạng thái và
> việc đang tồn đọng; còn lịch sử, các bẫy của nguồn và bài học từng vé nằm ở đây.

## Bài học từng vé

- Bảy cổng (thêm 2 cổng ngày 2026-11-28 sau retro T1): `tool/build-pages.py --check` →
  `tool/check-links.py` → `tool/verify-pages.py` → `tool/check-image-match.py` →
  `tool/check-vietnamese.py` → `tool/check-mobile.py` → `tool/check-coverage.py`. Cả bảy PASS với
  6 chương nội dung (860 ảnh, ~40 MB).
- `tool/check-mobile.py` + `tool/mobile-probe.mjs`: render bằng Chrome headless (CDP, không thêm
  dependency), FAIL khi `scrollWidth > clientWidth` ở 375px/768px. Cổng này ra đời vì T1 đã PASS đủ
  5 cổng cũ mà trang vẫn tràn ngang trên điện thoại.
- `tool/check-coverage.py`: bắt lỗi "dịch thiếu đoạn" mà 5 cổng hình dạng không thấy.
- CI `.github/workflows/gates.yml` chạy lại 7 cổng sau mỗi push (cache `.tmp-src/` để không tải lại nguồn).
- `tool/verify-pages.py` đã sửa ở T1: đếm mục theo đúng cách cổng ảnh tách mục (số `<h2>` cộng vùng
  trước mục đầu tiên). Bản cũ đếm `<h2>` thô nên mọi chương có ảnh nằm trước H2 đầu (bảng tóm tắt)
  đều báo lệch nguồn 1 mục và FAIL vĩnh viễn.
- Chương mẫu T1 chốt khuôn: bảng tóm tắt có icon boss (ảnh trước H2 đầu) → Mục lục → Tuyến đường nhanh →
  các mục đi đường đúng thứ tự nguồn → Mẹo hoàn thành → Đồ thu thập; mỗi mục H2 một gallery ảnh
  `<details open>`, caption = mô tả dịch từ alt gốc + `(ảnh k/N)`; icon trong bảng dùng `.inline-icon`.
- T2 giữ đúng khuôn T1, thêm ba điều đã gặp thật, các chương sau áp dụng luôn:
  (1) bảng facts của nguồn **có thể không có ảnh nào** trước H2 đầu (Điểm Quan Sát) → trang chỉ có
  số mục = số `<h2>`, không có vùng "(trước mục đầu)"; (2) nguồn có mục **không có "Completion tips"**
  (Phế Tích Thị Trấn Lâu Đài) → bám nguồn, không tự thêm mục, vì cổng 3/4 so số mục 1:1;
  (3) một ảnh nguồn có thể xuất hiện 2 lần (icon Dark Tunic) → cổng ảnh cấm dùng trùng nên chỉ dùng
  ở vị trí đầu tiên, các chỗ sau bỏ icon.
- T2 cũng sửa `tool/check-vietnamese.py` theo đúng quy ước trong `tool/README.md`: thêm âm tiết Việt
  không dấu `an`, `than` vào `VI_ASCII` và 4 tên nhiệm vụ phụ vào `PHRASES` — thêm vào danh sách
  miễn trừ thay vì bẻ câu cho vừa cổng.
- Retro sau T2 (2026-11-28) — chỉ đổi công cụ, không đổi nội dung:
  `tool/source_sections.py` là định nghĩa "mục" **duy nhất** (ba cổng import, trước đó mỗi cổng tự viết một bản);
  `verify-pages` dùng đúng luật heading của `check-vietnamese` (hết cảnh hai cổng đá nhau vụ tên riêng) và kiểm câu dẫn
  Mục lục có đếm đúng số mục; `check-vietnamese` nhận `--content`/slug/file để quét chữ **trước** khi build;
  `check-image-match --from` dùng nguồn đã có trên đĩa thay vì tải lại; thêm `tool/inspect-source.py` (soi chương nguồn)
  và `tool/shot.py` (chụp ảnh review 375/1280px qua CDP, thay cho `chrome --screenshot` hay hỏng).
  Đã kiểm lại: cả bảy cổng PASS, `pages/` không đổi byte nào.
- T3 giữ đúng khuôn T1/T2 cho hai chương (Vực Sâu Trung Tâm Hyrule 16 mục / 104 ảnh; Phần Còn Lại Của
  Lâu Đài Hyrule 16 mục = 15 `<h2>` + vùng trước H2 đầu / 85 ảnh), bảy cổng PASS. Bốn điều gặp thật,
  các đợt sau áp dụng luôn:
  (1) nguồn có **icon xen giữa ảnh chụp** trong cùng một mục (chương Lâu Đài: 19 ảnh, 6 icon h3) →
  giữ nguyên thứ tự ảnh bằng cách chia **một gallery cho mỗi mục `<h3>`**, icon đặt inline ở đầu đoạn;
  (2) một ảnh nguồn lặp ở **hai mục khác nhau** (`royal-shield.webp` ở mục 4 và mục 9) → chỉ dùng ở
  vị trí đầu, folder vì thế có 85 file cho 86 lượt ảnh nguồn;
  (3) nguồn có **`<h3>` rỗng**, không một câu nội dung, không ảnh ("Spot Corvash Canyon Mine") → bỏ
  heading rỗng, cổng không đếm `h3` nên vẫn khớp 1:1;
  (4) heading chứa entity HTML (`&#8217;`) bị generator escape hai lần ở sidebar/TOC → viết **ký tự
  `’` thật** trong heading, đừng dùng entity.
- T4 giữ đúng khuôn T1–T3 cho Vực Sâu Nam Đồng Bằng (17 mục, 77 ảnh), nhưng chương Nam Đồng Bằng
  phải đổi **khuôn trang**: nguồn chia một trang thành **2 phần lớn** (`<h2>`) với tuyến đường nhanh và
  mục đồ thu thập ở cấp `<h3>`, nên cả trang chỉ có 3 `<h2>` (Mục lục + 2 phần) và 36 `<h3>`.
  Bốn điều gặp thật, các đợt sau áp dụng luôn:
  (1) **cổng 3 phải tổng quát hoá**: `check_toc_summary` trước đây trừ cứng 2 mục khung ("Mục lục" +
  "Tuyến đường nhanh") nên chương nhiều phần luôn FAIL dù viết đúng nguồn → nay chỉ trừ những mục khung
  **có mặt**, và câu dẫn nhận "không có mục tổng kết" thay cho "0 mục tổng kết" (7 trang cũ không đổi byte nào);
  (2) mục lục của chương nhiều phần là **danh sách hai cấp** — tự viết `id` cho `<h3>` trong file body
  (generator chỉ thêm `id` cho `<h2>`), nên mục lục rail vẫn gọn 3 dòng còn mục lục trong bài nhảy được
  tới từng mục con;
  (3) **ảnh của bảng facts nằm trong mục `<h2>` đầu tiên của nguồn**, không phải vùng trước mục đầu: chương
  Nam Đồng Bằng chỉ có một ảnh như vậy (`rubber-armor.webp`), đặt ở đầu đoạn dẫn của "Phần 1" để không sinh
  thêm mục thứ tư; icon hồ sơ đứng **trước** `<h3>` của nó trong nguồn nên đặt ở đầu đoạn đầu tiên của mục đó;
  (4) nguồn không có bảng facts và không tổng kết số rương → chủ dự án chốt **dựng bảng tóm tắt từ số liệu
  đếm được trong chính nguồn** và ghi rõ rương "đếm theo mô tả nguồn" (60 rương; 74 hạt Korok ở chương Vực Sâu).
- T4 cũng sửa `tool/check-image-match.py`: GitHub Actions bị chặn ở đường tải trang chương và chỉ nhận về
  ~12 KB trang chặn, nên cổng ảnh báo 269 lỗi "không có trong nguồn" thay vì nói đúng là nguồn không tải được.
  Nay `refresh_cache` thử lần lượt **trang chương → WP REST API** (`/wp-json/wp/v2/pages?slug=…&_fields=content`,
  bọc `content.rendered` trong `<article>`, đã đối chiếu: cùng số mục và cùng thứ tự ảnh với trang thật)
  **→ proxy Google Translate**, và mọi đường đều phải qua `looks_like_chapter()` trước khi ghi cache.
  Cache hỏng nằm sẵn trên đĩa cũng bị coi là thiếu và tải lại.
- T4 sửa thêm `tool/check-vietnamese.py`: 7 cụm vào `PHRASES` (tên nhiệm vụ phụ của hai chương Nam Đồng Bằng)
  và âm tiết Việt không dấu `in` vào `VI_ASCII`; `tool/README.md` ghi lại luật đếm mục của cổng 3.
- T3 sửa thêm `tool/inspect-source.py`: thêm `--files` in **tên file ảnh đầy đủ** theo từng mục
  (bản cũ cắt 14 ký tự nên không tải ảnh được) và sửa lỗi `NameError: seen` khi folder ảnh đã tồn tại;
  `tool/check-vietnamese.py` thêm 6 cụm vào `PHRASES` (5 tên trang bị bộ Vực Sâu + `the rito rope bridge`).
- Ghi chú dữ liệu: chương Vực Sâu không vào Đền Thờ Nhỏ nào (chỉ thắp Rễ Sáng) nên card trên hub ghi
  "0 đền · 1 hang · 3 Korok · 12 rương" — đúng nguồn, giữ nguyên số 0 thay vì ẩn trường.

## Việc đã làm ngoài nội dung vùng (bộ 9 vùng fextralife)

### Việc đã làm ngoài nội dung vùng
- Rà soát lại **ảnh theo đúng subsection nguồn** cho vùng 1–3: trước đây ảnh bị chia theo thứ tự file
  nên lệch bước (Prologue/Central còn lẫn ảnh vùng khác; Hebra lệch từ mục 7). Đã tải đủ ảnh còn thiếu
  (Prologue 77, Central 34, Hebra 80), bỏ ảnh trùng/logo ngoài nguồn, chuẩn hoá tên file.
- Tách folder ảnh theo trang: `images/gsi` → `images/prologue`.
- Bài học lấy nội dung/ảnh (nhiều trang Subcontent, giữ tên file gốc, bản full qua trang `File:`,
  ảnh đặt ngay sau đoạn minh họa, caption theo tên bước): đã chuyển vào đặc tả [#33](https://github.com/phucnd0604/toto-guide/issues/33).
- `docs/agents/`: cấu hình issue tracker (GitHub Issues), nhãn triage, domain docs.
- **Cổng cứng ảnh ↔ nội dung**: thêm `scripts/check-image-match.py` + luật trong `AGENTS.md`. Đếm ảnh
  (`img=uni`, `ms=0`) không bắt được ảnh sai chỗ, nên cổng này đối chiếu trực tiếp trang nguồn.
- Giai đoạn B hoàn tất: vùng 6 Master Sword, 7 Gerudo, 8 Fifth Sage, 9 Demon King đã có walkthrough đầy đủ
  (Gerudo lấy 37 ảnh từ walkthrough nguồn,
  bỏ các subsection thuộc vùng khác như Hyrule Field / Faron / side quest đại tiên).
- Tách các heading bị gộp nhiều subsection nguồn (làm ảnh nằm sai chủ đề): Prologue — Ukouh, In-Isa,
  Gutanbac (Pondside/Mining/Pit/Bottomless Cave tách riêng), Return to Temple of Time; Hebra —
  Get Tulin's Bow / Reach The Top of Hebra Peak, Post Kahatanaum Shrine / Clear Wind Temple.

## Nhật ký giai đoạn A–D (bộ 9 vùng fextralife)

## Nhật ký giai đoạn

- **A – chốt ảnh ↔ nội dung (2026-11-23)**: thêm `scripts/check-image-match.py` + cổng trong `AGENTS.md`;
  tách heading bị gộp ở Prologue (Ukouh, In-Isa, Gutanbac + 4 hang, Return to Temple of Time) và Hebra
  (Post Kahatanaum, Reach The Top of Hebra Peak); mở sẵn toàn bộ gallery (`<details open>`).
  Commit: `85f5616`, `3da9436`, `c2e1105`, `8109e09`.
- **B – 4 vùng còn thiếu (2026-11-23)**: Master Sword 14 bước, Gerudo 23 bước + 37 ảnh, Fifth Sage 35 bước,
  Demon King 14 bước; thêm chế độ `NO_IMAGE` cho vùng không có nguồn ảnh; hub báo 9/9 vùng đầy đủ.
  Commit: `78aae7b`, `47d68e5`, `af3718a`, `4f9fe28`, `b431e6f`.
- **C – dọn ngôn ngữ (2026-11-23)**: shrines 282→0, mechanics 9→0, tips 5→0, abilities 2→0, index 1→0,
  faq 1→0; thêm 72 tên thử thách/nhiệm vụ vào allowlist của checker. Commit: `c2ec4e0`, `dfb9630`,
  `ce370ab`, `511ab03`, `cc94717`, `cf2c396`, `4424e38`.

- **D – sạch hoá (2026-11-23)**: bỏ 33 link `index.html` (dùng `/` và `../`) → hết redirect 308 mỗi lần về trang chủ;
  WARN 814→0: checker thêm bộ lọc âm tiết Việt không dấu (`VI_ASCII`) + danh sách từ tiếng Anh (`EN_EXTRA`),
  bỏ qua cụm tên riêng, rồi dịch nốt 39 chỗ tiếng Anh lọt (damage/durability/armor/quest/boss…).
