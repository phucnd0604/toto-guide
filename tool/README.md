# tool/ – công cụ chuẩn của dự án

Script, generator và cổng kiểm tra mà quá trình làm việc **luôn** chạy trước khi commit.

Quy ước:
- Mỗi script là một file độc lập trong thư mục này, chạy bằng `python tool/<ten>.py`.
- Không đặt ở đây file tạm, cache hay dữ liệu sinh ra trong lúc chạy → dùng `.scratch/`.
- `scripts/` còn lại là di sản của bộ 9 vùng fextralife, sẽ bị xoá ở vé chuyển nhà (T29).

## Năm cổng (chạy trước mỗi commit)

| Cổng | Tiêu chí |
|---|---|
| `python tool/build-pages.py --check` | 0 file lệch: file trong `pages/` đúng là bản sinh từ `content/` |
| `python tool/check-links.py` | 0 link nội bộ chết, 0 ảnh thiếu, 0 link ra domain ngoài (trừ Google Fonts) |
| `python tool/verify-pages.py` | mỗi trang đúng 1 `h1`, có meta description, layout 2 cột, số mục H2 khớp nguồn, heading không còn tiếng Anh, không `xN` |
| `python tool/check-image-match.py` | `FAIL=0`: ảnh đúng trang, đúng folder, đúng thứ tự, đúng mục H2 so với nguồn |
| `python tool/check-vietnamese.py` | `HARD=0` toàn site (`pages/**/*.html` + `index.html`) |

Cổng ảnh đọc cache nguồn ở `.tmp-src/<loại>/<slug>.html` hoặc `.json`; thêm `--refresh` để tải lại
từ URL trong metadata. Khi nguồn bị chặn (429), báo rõ "chưa chạy được" — không coi là pass.

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
  "title": "Đảo Trời Lớn: Đền Thờ Nhỏ, Korok và rương",
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
