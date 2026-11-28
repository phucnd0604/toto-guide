# Prompt chuẩn để bàn giao một vé

> Vì sao có file này: prompt của vé T4 vừa **chép lại** quy tắc kỹ thuật đã có trong `tool/README.md`,
> vừa **không nói** luật PR — nên agent đi push thẳng `master` rồi mới bị sửa. Prompt chuẩn giữ
> **tổng quát**: vai trò, thứ tự nạp nguồn, điểm dừng, hợp đồng báo cáo. Chi tiết kỹ thuật để repo
> tự nói (`AGENTS.md`, `tool/README.md`, vé, đặc tả, map).
>
> T5 cho thấy thiếu một thứ nữa: prompt chỉ nói "nạp `using-superpowers` + skill chính", nên các
> bước **kiểm, rà, chốt tích hợp** trôi mất — agent báo "xong" mà chưa tự kiểm, PR chưa qua bước rà
> nào. Từ đây prompt mang thêm **bảng skill theo từng bước**.

## Template

Dán nguyên khối dưới đây, thay các chỗ `<...>`. Mục nào không áp dụng thì **xoá hẳn dòng đó**, đừng để lại
chỗ trống — chỗ trống làm agent đoán.

```text
# Vé <KEY> — <tên ngắn>

Bạn là agent thực hiện vé kế tiếp của dự án. Quy trình chuẩn đã có trong repo — nạp và làm theo,
đừng tự đặt lại quy tắc.

## Vào việc
1. `cd <repo>`; `git status` sạch; `git pull --ff-only`.
2. Nạp skill `using-superpowers`, rồi <skill chính> (<cách gọi, ví dụ "/wayfinder" ở chế độ ...>).
   Skill nào gắn `disable-model-invocation` thì đọc thẳng `~/.dsh/skills/<tên>/SKILL.md`.
   **Không sửa định nghĩa skill.**
3. Đọc nguồn sự thật theo đúng thứ tự này, không đọc lại lịch sử chat:
   `AGENTS.md` → `tool/README.md` → `PROGRESS.md` → vé #<N> → đặc tả #<M> → map #<K>.
4. Claim vé: `gh issue edit <N> --repo <owner/repo> --add-assignee "@me"`.

## Skill theo từng bước

Bảng dưới xếp đúng thứ tự thực hiện; bỏ bước nào thì bỏ **cả skill** của bước đó, đừng làm tắt.
Mô tả từng skill để skill tự nói — danh mục đầy đủ ở `~/.dsh/AGENTS.md`.

| Bước | Skill | Khi nào |
|---|---|---|
| Điều phối cả vé | `using-superpowers` | luôn, ngay đầu |
| Đi theo map | `/wayfinder` chế độ *work through the map*; slash không gọi được thì đọc `~/.dsh/skills/wayfinder/SKILL.md` | vé thuộc một map |
| Chốt điểm mờ | `grilling` + `domain-modeling` | vé có điểm mờ; chốt xong **DỪNG** |
| Lập kế hoạch trong phiên | `writing-plans`, hoặc `executing-plans` khi đã có plan | vé nhiều bước hoặc phải sửa `tool/` |
| Viết nội dung tiếng Việt | `translation`; chuẩn của repo vẫn cao hơn: `docs/translation-standard.md` | vé có chữ |
| Tự kiểm trước khi báo xong | `verification-before-completion` | **luôn**, trước khi viết báo cáo |
| Rà chéo trước PR | `requesting-code-review`, hoặc skill `code-review` | có sửa `tool/` hoặc chạm nhiều trang |
| Chốt cách tích hợp | `finishing-a-development-branch` — chỉ để soạn lựa chọn; quyền quyết định của chủ dự án | trước khi mở PR |
| Viết PR | `pr` | luôn |
| Sửa tài liệu cho agent | `writing-for-agents` | vé sửa `AGENTS.md`, `docs/agents/`, skill |
| Gỡ cổng đỏ khó hiểu | `systematic-debugging` hoặc `diagnosing-bugs` | khi đoán mò vài lượt mà cổng vẫn đỏ |
| Cô lập việc | `using-git-worktrees` | khi worktree hiện tại đang bẩn, cần tách hẳn |

## Việc phải làm
<1–3 câu: sản phẩm của vé là gì. Không kèm hướng dẫn kỹ thuật — cái đó ở tool/README.md và đặc tả.>

## Điểm mờ phải chốt trước khi làm
<Liệt kê đúng những chỗ chưa rõ và yêu cầu: hỏi chủ dự án bằng grilling + domain-modeling rồi DỪNG.
 Xoá mục này nếu vé đã rõ.>

## Định nghĩa "xong"
- Chạy `verification-before-completion` **trước** khi viết báo cáo: bảy cổng PASS và **dán nguyên
  output** (không viết "chắc là pass").
- Làm trên **nhánh riêng**, mở PR bằng skill `pr` (`gh pr create --base master`), chờ CI xanh.
- Có sửa `tool/` thì `requesting-code-review` trước khi mở PR.
- **Dừng trước khi merge**: `finishing-a-development-branch` để soạn trạng thái kèm tuỳ chọn
  (merge / để nguyên / revert) rồi đợi chủ dự án; quyền quyết định merge thuộc chủ dự án.
- Nếu được duyệt merge: kiểm HTTP 200 cho trang mới + 1 ảnh mẫu trên production, rồi cập nhật
  vé (resolution), map và `PROGRESS.md`.

## Không được
- Push thẳng `master`; tự merge PR. (Nhánh `master` có branch protection, push sẽ bị từ chối.)
- Sửa tay file trong `pages/` — sửa `content/` rồi chạy generator.
- Sửa skill trong `~/.dsh/skills`.
- Tin số liệu trong vé hơn tool: <tool lấy số liệu của dự án> là chuẩn.
- Tạo file spec/plan trong repo; bản nháp để trong `.scratch/` (không commit).
```

### Bản ngắn (vé nhỏ, ít rủi ro)

```text
# Vé <KEY> — <tên ngắn>

Làm vé <KEY> theo quy trình chuẩn của repo: nạp using-superpowers + <skill>, đi theo bảng
skill trong docs/agents/ticket-prompt-template.md, đọc AGENTS.md → tool/README.md → PROGRESS.md →
vé #<N> → đặc tả #<M>, claim vé, rồi làm.

Xong thì: verification-before-completion → bảy cổng PASS kèm output; pr → nhánh riêng + PR;
finishing-a-development-branch → DỪNG trước khi merge và báo lại (merge / để nguyên / revert).
Không push thẳng master, không sửa tay pages/, không sửa skill.
```

## Nên có gì, không nên có gì

| Nên có | Không nên có |
|---|---|
| Vai trò + "làm theo quy trình chuẩn của repo" | Chép lại quy tắc cổng, cách build, cấu trúc thư mục (đã có trong `tool/README.md`) |
| Thứ tự nạp nguồn sự thật | Lịch sử chat của vé trước |
| Điểm mờ phải hỏi, kèm chỉ dẫn **dừng lại** | Con số đếm tay (số mục, số ảnh) — lấy bằng tool |
| Định nghĩa "xong" + yêu cầu dán output | Danh sách file phải sửa (agent tự tìm) |
| Bảng skill theo bước, ngắn và đúng thứ tự | Mô tả nội dung từng skill (skill tự nói) |
| Điều cấm: push master, tự merge, sửa `pages/`, sửa skill | Quy trình từng bước dài 50 dòng |
| Ngoại lệ riêng của vé (nếu có), nói rõ là ngoại lệ | Hai bộ quy tắc đá nhau (prompt vs AGENTS.md) |

## Vì sao từng dòng (rút từ sự cố thật)

- **"Dừng trước khi merge"** — T4: agent push thẳng `master` rồi đề nghị deploy, phải làm lại thành PR.
  Nay `master` có branch protection, nhưng luật vẫn phải nằm trong prompt.
- **"Không tin số liệu trong vé hơn tool"** — vé #7 ghi 21 `h3`, nguồn có 36; agent phải tự đối chiếu
  rồi giải thích trong báo cáo.
- **"Dán nguyên output"** — CI đỏ vì nguồn bị chặn mà local vẫn PASS; nếu báo miệng "pass hết" thì
  không ai phát hiện.
- **"Điểm mờ phải hỏi rồi DỪNG"** — T4 có ba điểm mờ (công thức cổng, mục lục hai cấp, bảng tóm tắt);
  chốt trước mới được phép sửa `tool/`.
- **"Không chép chi tiết kỹ thuật"** — prompt T4 dài 60 dòng, vừa lặp `tool/README.md` vừa thiếu luật PR;
  hai nguồn quy tắc là chỗ dễ sinh mâu thuẫn.
- **"Bảng skill theo bước"** — T5: agent làm đúng nội dung nhưng bỏ `translation`,
  `verification-before-completion`, `requesting-code-review` và `finishing-a-development-branch`; báo
  "xong" mà chưa tự kiểm, PR chưa qua bước rà nào. Prompt cũ chỉ nói "nạp using-superpowers + skill
  chính" nên các bước còn lại trôi. Bảng chỉ nêu **bước nào dùng skill nào** — nội dung từng skill để
  skill tự nói, tránh hai nguồn quy tắc.
- **"Không sửa skill"** — người dùng gọi skill bằng slash ngay trong prompt; agent chỉ đọc và thi hành.
