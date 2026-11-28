# tool/ – công cụ chuẩn của dự án

Script, generator và cổng kiểm tra mà quá trình làm việc **luôn** chạy trước khi commit.

Quy ước:
- Mỗi script là một file độc lập trong thư mục này, chạy bằng `python tool/<ten>.py`.
- Không đặt ở đây file tạm, cache hay dữ liệu sinh ra trong lúc chạy → dùng `.scratch/`.
- `scripts/` còn lại là di sản của bộ 9 vùng fextralife, sẽ bị xoá ở vé chuyển nhà (T29).

Bộ cổng dự kiến (vé T0 dựng):
- `build-pages.py` – sinh trang từ nguồn nội dung, có `--check`
- `check-links.py` – link nội bộ và ảnh
- `verify-pages.py` – cấu trúc trang
- `check-image-match.py` – ảnh ↔ trang nguồn
- `check-vietnamese.py` – chuẩn tiếng Việt
