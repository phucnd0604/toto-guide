# Đọc log phiên để làm retro

Log phiên của DSH nằm ở `~/.dsh/sessions/--<đường-dẫn-đã-mã-hoá>--/<session-id>/session.v4.jsonl.zstd`
(với repo này là `--E-GameGuide--`).

File là **nhiều frame zstd nối tiếp**, mỗi frame một dòng JSONL. Các bẫy:

- `zstdDecompressSync(buf)` (Node) và `zlib.zstd` chỉ giải **frame đầu** → chỉ ra một dòng
  `{"type":"session",...}` và tưởng log rỗng. Phải cắt theo magic `28 b5 2f fd` rồi giải từng khúc.
- Không có `zstandard` trong Python của máy; Node 24 có `zlib.zstdDecompressSync` sẵn.

Đoạn đọc log dùng một lần (Node):

```js
const buf = fs.readFileSync(file);
const MAGIC = Buffer.from([0x28, 0xb5, 0x2f, 0xfd]);
const starts = [];
for (let i = 0; i + 4 <= buf.length; i++) if (buf.compare(MAGIC, 0, 4, i, i + 4) === 0) starts.push(i);
starts.push(buf.length);
let text = "";
for (let k = 0; k < starts.length - 1; k++) text += zlib.zstdDecompressSync(buf.subarray(starts[k], starts[k + 1])).toString("utf8");
```

Mỗi dòng là một record có `type`; để đếm chi phí dùng `tool/call`, `tool/result`, `tool/ptc-dispatch`,
`step/start`, `turn/start`. Tên tool nằm trong trường khác nhau tuỳ bản (với `run_code` chỉ có một tool
bọc mọi thứ, nên đếm `tool/ptc-dispatch` mới thấy lệnh con).
