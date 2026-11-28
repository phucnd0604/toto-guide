# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

## Repo này: single-context

- Từ vựng dự án: `GLOSSARY.md` ở gốc repo (chương, nhóm vùng, vé, bản đồ, đặc tả, cổng kiểm tra…).
- Quyết định kiến trúc: `docs/adr/`, đánh số tăng dần.
- Không có `GLOSSARY-MAP.md`, không có context con.

**Phân biệt hai loại glossary.** `GLOSSARY.md` là từ vựng của dự án (cách gọi khái niệm, dùng khi đặt tên vé,
issue, tên module). `docs/translation-standard.md` là chuẩn dịch tiếng Việt cho thuật ngữ trong game
(Ultrahand → Siêu Tay, Shrine → Đền Thờ Nhỏ…), dùng khi viết nội dung site. Viết nội dung thì theo file dịch;
đặt tên công việc thì theo `GLOSSARY.md`. Hai bên lệch nhau thì báo lại, đừng tự chọn.

## Before exploring, read these

- **`GLOSSARY.md`** at the repo root, or
- **`GLOSSARY-MAP.md`** at the repo root if it exists: it points at one `GLOSSARY.md` per context. Read each one relevant to the topic.
- **`docs/adr/`**: read ADRs that touch the area you're about to work in. In multi-context repos, also check `src/<context>/docs/adr/` for context-scoped decisions.

If any of these files don't exist, **proceed silently**. Don't flag their absence; don't suggest creating them upfront. The `/domain-modeling` skill (reached via `/grill-with-docs` and `/improve-codebase-architecture`) creates them lazily when terms or decisions actually get resolved.

## File structure

Single-context repo (most repos):

```
/
├── GLOSSARY.md
├── docs/adr/
│   ├── 0001-event-sourced-orders.md
│   └── 0002-postgres-for-write-model.md
└── src/
```

Multi-context repo (presence of `GLOSSARY-MAP.md` at the root):

```
/
├── GLOSSARY-MAP.md
├── docs/adr/                          ← system-wide decisions
└── src/
    ├── ordering/
    │   ├── GLOSSARY.md
    │   └── docs/adr/                  ← context-specific decisions
    └── billing/
        ├── GLOSSARY.md
        └── docs/adr/
```

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in `GLOSSARY.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal: either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/domain-modeling`).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0007 (event-sourced orders), but worth reopening because…_
