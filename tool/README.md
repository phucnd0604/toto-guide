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

### Ảnh: đúng trang, đúng thứ tự, đúng mục

Bốn điều kiện, vi phạm một là FAIL:

1. Mỗi ảnh dùng trong `pages/<loại>/<slug>.html` phải nằm trong `images/<loại>/<slug>/` của chính trang đó.
2. Mọi file trong folder ảnh của trang đều phải được dùng (không thừa, không thiếu).
3. Dãy ảnh trong trang là **dãy con đúng thứ tự** xuất hiện ở nguồn.
4. Ảnh nằm dưới **đúng mục** như nguồn, đối chiếu theo **thứ tự mục** chứ không theo chữ (heading đã dịch).

**Tên file**: cổng so tên đã chuẩn hoá — bỏ hậu tố kích thước (`-1024x576`) và tiền tố `<so>px-`.
Vì vậy file trên đĩa phải đặt tên **không có hậu tố kích thước**, phần còn lại giữ nguyên như nguồn.

### Bản dịch: độ phủ

`check-coverage` so từng mục: mục nguồn ≥20 từ mà bản dịch <30% số từ (hoặc 0 khối `<p>/<li>/<tr>`) thì FAIL.
Đây là lưới bắt lỗi "dịch thiếu đoạn" — các cổng còn lại chỉ kiểm hình dạng nên không thấy.

### Tiếng Việt: bẫy âm tiết không dấu

`check-vietnamese` coi một cụm là "chưa dịch" khi còn từ tiếng Anh thông dụng. Các âm tiết tiếng Việt
không dấu trùng mặt chữ tiếng Anh (`to`, `co`, `do`, `so`, `no`) được miễn trừ qua tập `VI_ASCII`;
gặp từ mới cùng loại thì thêm vào `VI_ASCII`, đừng bẻ câu cho vừa cổng.

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
