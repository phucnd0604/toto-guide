# tool/ – công cụ chuẩn của dự án

Script, generator và cổng kiểm tra mà quá trình làm việc **luôn** chạy trước khi commit.

Quy ước:
- Mỗi script là một file độc lập trong thư mục này, chạy bằng `python tool/<ten>.py`.
- Không đặt ở đây file tạm, cache hay dữ liệu sinh ra trong lúc chạy → dùng `.scratch/`.
- `scripts/` còn lại là di sản của bộ 9 vùng fextralife, sẽ bị xoá ở vé chuyển nhà (T29).

## Bảy cổng (chạy trước mỗi commit)

| Cổng | Tiêu chí |
|---|---|
| `python tool/build-pages.py --check` | 0 file lệch: file trong `pages/` đúng là bản sinh từ `content/` |
| `python tool/check-links.py` | 0 link nội bộ chết, 0 ảnh thiếu, 0 link ra domain ngoài (trừ Google Fonts) |
| `python tool/verify-pages.py` | mỗi trang đúng 1 `h1`, có meta description, layout 2 cột, số mục khớp nguồn (đếm cả vùng trước `<h2>` đầu, như cổng ảnh), heading không còn tiếng Anh, không `xN` |
| `python tool/check-image-match.py` | `FAIL=0`: ảnh đúng trang, đúng folder, đúng thứ tự, đúng mục so với nguồn |
| `python tool/check-vietnamese.py` | `HARD=0` toàn site (`pages/**/*.html` + `index.html`) |
| `python tool/check-mobile.py` | không trang nào tràn ngang ở 375px và 768px (render thật bằng Chrome headless) |
| `python tool/check-coverage.py` | mục nào của nguồn ≥20 từ cũng còn ≥30% số từ trong bản dịch |

Cổng ảnh đọc cache nguồn ở `.tmp-src/<loại>/<slug>.html` hoặc `.json`; thêm `--refresh` để tải lại
từ URL trong metadata. Khi nguồn bị chặn (429), báo rõ "chưa chạy được" — không coi là pass.

Ba đường tải nguồn, thử lần lượt và **đường nào cũng phải qua `looks_like_chapter()`** (có `<h2>` và có
"/uploads/") trước khi ghi cache: trang chương → **WP REST API** `/wp-json/wp/v2/pages?slug=…&_fields=content`
(bọc `content.rendered` trong `<article>`) → proxy Google Translate. Lý do: từ GitHub Actions, đường tải
trang chương bị chặn và chỉ trả về ~12 KB trang chặn; cache ấy từng làm cổng ảnh báo 269 lỗi "không có
trong nguồn" thay vì nói đúng là nguồn không tải được. Cache hỏng nằm sẵn trên đĩa cũng bị coi là thiếu
và tải lại, kể cả khi không truyền `--refresh`.

## Hợp đồng của các cổng (đọc trước khi thiết kế nội dung)

### "Mục" (section) được định nghĩa thế nào

`check-image-match`, `verify-pages` và `check-coverage` cùng tách trang thành các **mục** theo `<h2>`,
và một điểm rất dễ sai:

- Nếu trang có ảnh **nằm trước `<h2>` đầu tiên**, phần đó thành một mục riêng tên `(trước mục đầu)`.
- Vì vậy **số mục của trang = số `<h2>` + 1** khi bảng tóm tắt đầu trang có ảnh (icon boss), và số mục
  của nguồn cũng tính đúng như vậy. Hai bên phải bằng nhau.

Hệ quả cho khuôn chương: nguồn có sẵn mục "Table of Contents" (16 liên kết) và trang có ảnh trước `<h2>`
đầu, nên mỗi chương phải giữ **cả bảng tóm tắt có icon** (trước mục đầu) **lẫn một mục `<h2>` mục lục**
trong bài. Đây là lý do chương T1 có mục "Mục lục" trùng mục lục cột trái — giữ thì đúng nguồn 1:1 và
qua cổng; bỏ thì phải sửa cả hai cổng cùng lúc, không sửa lẻ.

**Khối quảng bá của trang nguồn không phải "mục".** Từ T5, trang nguồn có thể kết thúc bằng một khối
site-chrome (ví dụ `<h2>Track them</h2>` + bảng 5 link guide của zeldacentral + "Create a free account"):
nó không nằm trong mục lục của chính nguồn và ruột chỉ là quảng bá. Danh sách `IGNORED_SOURCE_HEADINGS`
trong `tool/source_sections.py` bỏ khối đó ở **cả hai phía** (nguồn và trang đã sinh), nên số mục vẫn
khớp 1:1 mà bản dịch không phải bê quảng cáo vào. Gặp khối cùng loại ở chương khác thì thêm heading đã
chuẩn hoá vào danh sách đó — đừng bỏ riêng một cổng, và đừng bỏ mục mà không ghi vào đây.

### Ảnh: đúng trang, đúng thứ tự, đúng mục

Bốn điều kiện, vi phạm một là FAIL:

1. Mỗi ảnh dùng trong `pages/<loại>/<slug>.html` phải nằm trong `images/<loại>/<slug>/` của chính trang đó.
2. Mọi file trong folder ảnh của trang đều phải được dùng (không thừa, không thiếu).
3. Dãy ảnh trong trang là **dãy con đúng thứ tự** xuất hiện ở nguồn.
4. Ảnh nằm dưới **đúng mục** như nguồn, đối chiếu theo **thứ tự mục** chứ không theo chữ (heading đã dịch).

**Tên file**: cổng so tên đã chuẩn hoá — bỏ hậu tố kích thước (`-1024x576`) và tiền tố `<so>px-`.
Vì vậy file trên đĩa phải đặt tên **không có hậu tố kích thước**, phần còn lại giữ nguyên như nguồn.

## Chạy nhanh khi đang viết nội dung

Bảy cổng là cổng chặn trước commit, nhưng khi đang viết một chương thì chạy cả bộ sau mỗi câu
là quá chậm: mỗi vòng "sửa chữ → build → quét toàn site" tốn vài phút. Năm cổng nhận phạm vi
hẹp, dùng để lấy phản hồi sớm:

```
python tool/check-vietnamese.py --content                # quét chữ trong content/ TRƯỚC khi build
python tool/check-vietnamese.py great-sky-island          # một slug
python tool/check-vietnamese.py pages/walkthrough/x.html  # một file
python tool/check-image-match.py lookout-landing          # một slug
python tool/check-coverage.py lookout-landing             # một slug
python tool/check-mobile.py --width 375 pages/walkthrough/lookout-landing.html   # một trang
```

Đo cả site bằng cổng mobile mất 1–2 phút mỗi lượt; đang viết thì đo đúng trang vừa sửa, cuối cùng
mới chạy cả bộ. Cổng ảnh và cổng phủ đều nhận đúng một slug như trên.

Khi nguồn đã có sẵn trên đĩa (ví dụ bản tải tay trong `.scratch/`), bảo cổng ảnh dùng file đó
thay vì tải lại — nhận đúng một slug:

```
python tool/check-image-match.py --from .scratch/src-lookout-landing.html lookout-landing
```

## Soi nguồn và chụp trang

Ba việc lặp lại ở mọi chương, trước đây mỗi việc là một script nháp:

```
python tool/inspect-source.py lookout-landing          # mục + ảnh + alt gốc + bảng facts + đối chiếu folder
python tool/inspect-source.py --no-alt hyrule-field    # chỉ đếm mục/ảnh
python tool/inspect-source.py --ticket hyrule-field    # khối số liệu dán thẳng vào vé
python tool/inspect-source.py --text hyrule-field      # nguồn thành văn bản theo mục, để dịch
python tool/inspect-source.py --text --section 3-9 hyrule-field   # chỉ một khoảng mục
python tool/fetch-images.py hyrule-field               # tải toàn bộ ảnh 1024px vào images/walkthrough/<slug>/
python tool/shot.py lookout-landing                    # 375px, cả trang -> .scratch/shots/
python tool/shot.py --width 1280 --width 375 hyrule-field
python tool/shot.py --viewport --height 1400 --anchor "#meo-hoan-thanh" lookout-landing
```

`--ticket` in ra số `<h2>`, `<h3>`, `<h4>`, số ảnh (lượt xuất hiện / file duy nhất) và danh sách ảnh
lặp — dán nguyên khối vào vé. Đừng đếm tay: vé T4 ghi 21 `h3` trong khi nguồn có 36.

`--text` đổi 300–700 KB markup thành vài chục KB chữ mà **vẫn giữ ảnh đúng chỗ** (`[IMG …]`,
`[ICON …]`), nên vừa đọc để dịch vừa đối chiếu được thứ tự ảnh.

`tool/fetch-images.py` tải đúng những ảnh nằm trong bài, bỏ hậu tố `-1024x576`, và **chỉ tải một lần**
ảnh lặp trong nguồn — đúng ba quy ước của cổng ảnh.

`tool/shot.py` gọi `tool/mobile-probe.mjs` (CDP, cùng đường đo với cổng mobile) nên bề rộng là
thật, ảnh lazy được ép tải trước khi chụp. Đừng dùng `chrome --screenshot --window-size=375`:
Chrome ép bề rộng tối thiểu nên ảnh trông như tràn ngang dù trang không tràn.

## Định nghĩa "mục" chỉ nằm ở một chỗ

`tool/source_sections.py` là bản duy nhất tách trang thành mục; cả ba cổng đọc mục đều import
từ đó (`check-image-match`, `verify-pages`, `check-coverage`). Khác biệt duy nhất có chủ ý:
`check-coverage` đo **chữ** nên bỏ `<figure>/<img>` và bỏ vùng "(trước mục đầu)" — vùng đó chỉ
có bảng tóm tắt + icon, không có câu nào để đo.

Hai luật của `verify-pages` đáng biết vì chúng có thể FAIL:

- **Heading** bị coi là "chưa dịch" theo đúng luật của `check-vietnamese` (bỏ `PHRASES` rồi
  tìm từ tiếng Anh thông dụng). Nhờ vậy tên riêng đứng một mình như "Lookout Landing" hay
  "Boss Bokoblin" qua được, còn "Table of Contents" thì không. Heading cũng viết **ký tự thật**
  (`&`, `’`), không dùng entity HTML: `slug_id()` sinh `id` từ chính chuỗi heading nên `&amp;`
  cho ra id có chữ "amp" và mục lục trỏ sai — không cổng nào bắt được.
- **Câu dẫn dưới `<h2>Mục lục</h2>`** phải khai đúng số mục: "… N mục đi đường và M mục tổng
  kết", trong đó M là số heading cuối trang bắt đầu bằng "Mẹo hoàn thành" / "Đồ thu thập" /
  "Danh sách kiểm". Số đếm viết tay đã sai hai lần ở T2 mà không cổng nào bắt được.
  N đếm bằng **số heading trừ những mục khung CÓ MẶT** ("Mục lục", "Tuyến đường nhanh") rồi trừ M.
  Bản cũ trừ cứng 2 mục khung, nên chương nhiều phần (một `<h2>Mục lục` + các `<h2>` phần lớn,
  tuyến đường nhanh nằm ở `<h3>` đúng như nguồn) bị đếm lệch một mục: viết đúng nguồn vẫn FAIL.
  Chương nhiều phần được phép tự viết `id` cho `<h3>` để mục lục trong bài thành danh sách hai
  cấp; generator chỉ tự thêm `id` cho `<h2>` nên mục lục rail vẫn chỉ có các mục lớn.
  Câu dẫn cũng nhận "… và **không có** mục tổng kết" thay cho "0 mục tổng kết".

### Bản dịch: độ phủ

`check-coverage` so từng mục: mục nguồn ≥20 từ mà bản dịch <30% số từ (hoặc 0 khối `<p>/<li>/<tr>`) thì FAIL.
Đây là lưới bắt lỗi "dịch thiếu đoạn" — các cổng còn lại chỉ kiểm hình dạng nên không thấy.

### Tiếng Việt: bẫy âm tiết không dấu

`check-vietnamese` coi một cụm là "chưa dịch" khi còn từ tiếng Anh thông dụng. Các âm tiết tiếng Việt
không dấu trùng mặt chữ tiếng Anh (`to`, `co`, `do`, `so`, `no`) được miễn trừ qua tập `VI_ASCII`;
gặp từ mới cùng loại thì thêm vào `VI_ASCII`, đừng bẻ câu cho vừa cổng.

**Dấu nháy:** `PHRASES` viết bằng dấu nháy thẳng, còn heading theo chuẩn dịch dùng `’` thật. Checker
chuẩn hoá `‘ ’` về `'` trước khi so (`norm_quotes()`), nên tên như "The Dragon’s Tears" vẫn khớp mà
không phải khai hai biến thể.

## Nguồn nội dung & cách sinh trang

```
content/
  regions.json                   12 nhóm vùng, đúng thứ tự hiển thị trên hub
  hub.json                       metadata + lời dẫn hub + hai trang chỉ mục
  hub.body.html                  phần chữ giới thiệu trên hub
  <loại>/<slug>.json             metadata một trang
  <loại>/<slug>.body.html        thân bài đã dịch (các <h2>, <p>, <details open>, <figure>)
  loại = walkthrough | quests | temples | reference
```

Metadata tối thiểu:

```json
{
  "title": "Đảo Trời Lớn: Đền Thờ Nhỏ, Hạt Korok và rương",
  "desc": "Meta description tiếng Việt, 120–158 ký tự.",
  "region": "Great Sky Island",
  "order": 1,
  "source": "https://zeldacentral.com/games/tears-of-the-kingdom/walkthrough/great-sky-island/",
  "meta": { "quests": ["The Closed Door"], "shrines": 4, "caves": 4, "koroks": 17, "chests": 25 },
  "prev": null,
  "next": "lookout-landing"
}
```

- `region` bắt buộc với `walkthrough` và `temples`; giá trị phải khớp `name` trong `regions.json`.
- `temples` cần thêm `kind`: `main-temple` (4 đền chính) | `mine` | `final`.
- `prev`/`next` bỏ trống thì generator tự nối theo `order`; khai báo thì phải trỏ tới slug có thật cùng loại.
- `summary` (tuỳ chọn): một dòng tóm tắt hiện trên hub/trang chỉ mục.
- Ảnh trong `.body.html` dùng đường dẫn tính từ trang đích: `../../images/<loại>/<slug>/<tên-file>.webp`.
- Sửa `content/` rồi chạy `python tool/build-pages.py`; **không sửa tay** file trong `pages/`.

Hai trang chỉ mục `pages/quests.html` và `pages/temples.html` cùng hub được sinh từ metadata
(`order`, `region`, `meta`) nên thêm/bớt trang là danh sách tự cập nhật.

Thử khuôn mẫu mà không đụng `pages/`: `python tool/build-pages.py --content .scratch/content --out .scratch/out`.

## Xem và đo trang local

Trình duyệt và Playwright đều **chặn `file://`**, nên muốn soi trang thật thì phục vụ qua HTTP:

```
python tool/preview.py                 # http://127.0.0.1:8765/pages/progress-route.html
python tool/check-mobile.py --width 375 pages/walkthrough/<slug>.html   # đo 1 trang
```

`check-mobile.py` gọi `tool/mobile-probe.mjs` (Node + Chrome DevTools Protocol, không cần npm install).
Thiếu Chrome/Node thì cổng in "chưa chạy được" và không tính là PASS.

## Ghi chú vận hành

- `PYTHONIOENCODING=utf-8` trước mọi script khi in tiếng Việt trên Windows (console cp1252).
- Cache nguồn ở `.tmp-src/` (gitignore) do chính cổng ảnh tạo; `--refresh` để tải lại.
- Log phiên để làm retro: `docs/agents/session-log.md` (file là nhiều frame zstd nối tiếp).