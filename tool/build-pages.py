#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh toàn bộ trang trong pages/ từ content/ — một nguồn nội dung duy nhất.

Dùng:
    python tool/build-pages.py                 # sinh/ghi đè pages/
    python tool/build-pages.py --check         # không ghi; lệch với file trên đĩa -> exit 1
    python tool/build-pages.py --out DIR       # ghi ra DIR thay vì pages/ (thử khuôn mẫu)
    python tool/build-pages.py --content DIR   # dùng nguồn nội dung khác (mặc định content/)

Nguồn nội dung:
    content/regions.json                12 nhóm vùng, đúng thứ tự hiển thị
    content/hub.json                    metadata + lời dẫn hub và hai trang chỉ mục
    content/hub.body.html               phần chữ giới thiệu trên hub
    content/<loại>/<slug>.json          metadata một trang
    content/<loại>/<slug>.body.html     thân bài đã dịch
    loại = walkthrough | quests | temples | reference

Quy ước: mọi file trong pages/ là sản phẩm sinh ra — KHÔNG sửa tay, hãy sửa content/ rồi chạy lại.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import posixpath
import re
import sys
import unicodedata

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE_TYPES = ("walkthrough", "quests", "temples", "reference")
TYPE_LABEL = {
    "walkthrough": "Chương",
    "quests": "Nhiệm vụ chính",
    "temples": "Đền Thờ",
    "reference": "Tham chiếu",
}
# id mục trên hub mà mỗi loại trang thuộc về (breadcrumb)
TYPE_SECTION = {
    "walkthrough": "lo-trinh-100",
    "quests": "nhiem-vu-chinh",
    "temples": "den-tho-chinh",
    "reference": "tham-khao",
}
HUB_KEY = "progress-route.html"
INDEX_KEYS = {"quests": "quests.html", "temples": "temples.html"}
EMPTY = {
    "walkthrough": "Chưa có chương nào.",
    "quests": "Chưa có trang nhiệm vụ nào.",
    "temples": "Chưa có trang Đền Thờ nào.",
    "reference": "Chưa có trang tham chiếu nào.",
}
NAV = [
    ("index.html", "Trang chủ"),
    ("pages/mechanics.html", "Cơ chế"),
    ("pages/abilities.html", "Năng lực"),
    ("pages/progress-route.html", "Lộ trình"),
    ("pages/shrines.html", "Đền thờ nhỏ"),
    ("pages/tips.html", "Mẹo"),
    ("pages/faq.html", "FAQ"),
]
FOOTER = (
    "Nội dung biên soạn lại bằng tiếng Việt theo lộ trình zeldacentral; "
    "ảnh minh họa thuộc bản quyền Nintendo, dùng cho mục đích tham khảo."
)
FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700'
    '&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">'
)
H2_RE = re.compile(r"<h2\b([^>]*)>(.*?)</h2>", re.I | re.S)
IMG_OPEN_RE = re.compile(r"<img\b", re.I)


def esc(text):
    return html.escape(str(text), quote=False)


def attr(text):
    return html.escape(str(text), quote=True)


def read_text(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def read_json(path, errors):
    if not os.path.exists(path):
        errors.append("thiếu file %s" % rel(path))
        return None
    try:
        return json.loads(read_text(path))
    except ValueError as exc:
        errors.append("%s: JSON lỗi (%s)" % (rel(path), exc))
        return None


def rel(path):
    return os.path.relpath(path, ROOT).replace("\\", "/")


def page_key(entry):
    return "%s/%s.html" % (entry["type"], entry["slug"])


def _link(page_key_value, target):
    """Link tương đối từ một trang trong pages/ tới đường dẫn trong repo."""
    start = posixpath.dirname("pages/" + page_key_value)
    if target == "index.html":
        back = posixpath.relpath(".", start)
        return "./" if back == "." else back + "/"
    return posixpath.relpath(target, start)


def slug_id(text):
    decomposed = unicodedata.normalize("NFD", text)
    stripped = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    stripped = stripped.replace("đ", "d").replace("Đ", "D").lower()
    stripped = re.sub(r"[^a-z0-9]+", "-", stripped).strip("-")
    return stripped or "muc"


def add_heading_ids(body):
    seen = {}

    def repl(match):
        attrs = match.group(1) or ""
        inner = match.group(2)
        if re.search(r"\bid\s*=", attrs):
            return match.group(0)
        base = slug_id(re.sub(r"<[^>]+>", " ", inner))
        seen[base] = seen.get(base, 0) + 1
        hid = base if seen[base] == 1 else "%s-%d" % (base, seen[base])
        return '<h2 id="%s"%s>%s</h2>' % (hid, attrs, inner)

    return H2_RE.sub(repl, body)


def toc_items(body):
    items = []
    for match in re.finditer(r'<h2\b[^>]*\bid="([^"]+)"[^>]*>(.*?)</h2>', body, re.I | re.S):
        text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", match.group(2))).strip()
        items.append((match.group(1), text))
    return items


def head_html(page_key_value, title, desc):
    start = posixpath.dirname("pages/" + page_key_value)
    css = posixpath.relpath("assets/style.css", start)
    return (
        '<meta charset="UTF-8">\n'
        '<meta name="description" content="%s">\n' % attr(desc)
        + '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        + "<title>%s</title>\n" % esc(title)
        + FONTS + "\n"
        + '<link rel="stylesheet" href="%s">\n' % css
        + '<meta property="og:title" content="%s">' % attr(title)
        + '<meta property="og:description" content="%s">' % attr(desc)
        + '<meta property="og:type" content="article">'
        + '<meta name="theme-color" content="#17171C">'
    )


def navbar_html(page_key_value):
    lines = [
        '<header class="navbar">',
        '  <a class="brand" href="%s">TOTK Guide</a>' % _link(page_key_value, "index.html"),
        '  <button class="theme-toggle" aria-label="Đổi giao diện sáng/tối">🌙 Tối</button>',
        '  <button class="nav-toggle" aria-label="Mở menu" aria-expanded="false" '
        'aria-controls="main-nav">☰</button>',
        '  <nav id="main-nav">',
    ]
    for target, label in NAV:
        active = ' class="active"' if target == "pages/progress-route.html" else ""
        lines.append('    <a href="%s"%s>%s</a>' % (_link(page_key_value, target), active, label))
    lines += ["  </nav>", "</header>"]
    return "\n".join(lines)


def page_shell(page_key_value, title, desc, main_html):
    script = posixpath.relpath("assets/app.js", posixpath.dirname("pages/" + page_key_value))
    return (
        "<!DOCTYPE html>\n"
        '<html lang="vi">\n'
        "<head>\n"
        + head_html(page_key_value, title, desc)
        + "\n</head>\n<body>\n"
        + '<a href="#main" class="skip-link">Bỏ qua đến nội dung</a>\n'
        + navbar_html(page_key_value)
        + "\n"
        + main_html
        + "\n<footer><p>%s</p></footer>\n" % esc(FOOTER)
        + '<script src="%s"></script>\n' % script
        + "</body>\n</html>\n"
    )


def card_html(page_key_value, target, num, title, sub, meta_line):
    out = ['<a class="route-card" href="%s">' % _link(page_key_value, target)]
    out.append('  <span class="route-num">%s</span>' % esc(num))
    out.append('  <span class="route-body">')
    out.append("    <strong>%s</strong>" % esc(title))
    if sub:
        out.append("    <em>%s</em>" % esc(sub))
    if meta_line:
        out.append('    <span class="route-meta">%s</span>' % esc(meta_line))
    out += ["  </span>", "</a>"]
    return "\n".join(out)


def validate_meta(kind, slug, meta, region_by_name):
    errs = []
    where = "%s/%s" % (kind, slug)
    if not isinstance(meta, dict):
        return ["%s: metadata phải là object" % where]
    for key in ("title", "desc", "order", "source"):
        if key not in meta:
            errs.append("%s: thiếu %s" % (where, key))
    title, desc = meta.get("title"), meta.get("desc")
    order, source = meta.get("order"), meta.get("source")
    if isinstance(title, str) and not title.strip():
        errs.append("%s: title rỗng" % where)
    if isinstance(desc, str) and not desc.strip():
        errs.append("%s: desc rỗng" % where)
    if not isinstance(order, int) or isinstance(order, bool):
        errs.append("%s: order phải là số nguyên" % where)
    if isinstance(source, str) and not source.startswith("http"):
        errs.append("%s: source phải là URL http(s)" % where)
    if kind in ("walkthrough", "temples"):
        region = meta.get("region")
        if not region:
            errs.append("%s: thiếu region" % where)
        elif region not in region_by_name:
            errs.append("%s: region %r không có trong content/regions.json" % (where, region))
    if kind == "temples" and meta.get("kind") not in ("main-temple", "mine", "final"):
        errs.append("%s: kind phải là main-temple | mine | final" % where)
    if "meta" in meta and not isinstance(meta["meta"], dict):
        errs.append("%s: meta phải là object" % where)
    if not errs and isinstance(desc, str) and not (60 <= len(desc) <= 220):
        errs.append("%s: desc nên dài 60–220 ký tự (đang %d)" % (where, len(desc)))
    return errs


def load_site(content_dir):
    errors, warns = [], []
    regions_raw = read_json(os.path.join(content_dir, "regions.json"), errors)
    regions = []
    if isinstance(regions_raw, list):
        for index, item in enumerate(regions_raw, 1):
            if not isinstance(item, dict) or not all(k in item for k in ("key", "name", "title")):
                errors.append("regions.json mục %d thiếu key/name/title" % index)
                continue
            regions.append(
                {"key": item["key"], "name": item["name"], "title": item["title"], "index": index}
            )
    elif regions_raw is not None:
        errors.append("regions.json phải là một mảng")
    if regions and len(regions) != 12:
        warns.append("regions.json có %d nhóm vùng (đặc tả chốt 12)" % len(regions))
    region_by_name = {r["name"]: r for r in regions}

    entries = []
    for kind in PAGE_TYPES:
        folder = os.path.join(content_dir, kind)
        if not os.path.isdir(folder):
            continue
        json_slugs = {f[:-5] for f in os.listdir(folder) if f.endswith(".json")}
        body_slugs = {f[:-len(".body.html")] for f in os.listdir(folder) if f.endswith(".body.html")}
        for slug in sorted(json_slugs - body_slugs):
            errors.append("%s/%s.json thiếu file .body.html" % (kind, slug))
        for slug in sorted(body_slugs - json_slugs):
            errors.append("%s/%s.body.html thiếu file .json" % (kind, slug))
        for slug in sorted(json_slugs & body_slugs):
            meta = read_json(os.path.join(folder, slug + ".json"), errors)
            body = read_text(os.path.join(folder, slug + ".body.html"))
            if meta is None:
                continue
            meta_errors = validate_meta(kind, slug, meta, region_by_name)
            errors.extend(meta_errors)
            if meta_errors:
                continue
            if "<h1" in body.lower():
                errors.append("%s/%s.body.html: không được chứa <h1>" % (kind, slug))
            if not body.strip():
                errors.append("%s/%s.body.html: thân bài rỗng" % (kind, slug))
            entries.append({"type": kind, "slug": slug, "meta": meta, "body": body})

    by_type = {}
    by_slug = {}
    for kind in PAGE_TYPES:
        items = [e for e in entries if e["type"] == kind]
        items.sort(key=lambda e: (e["meta"]["order"], e["slug"]))
        order_seen = {}
        for entry in items:
            order = entry["meta"]["order"]
            if order in order_seen:
                errors.append(
                    "%s: order %s bị trùng (%s và %s)"
                    % (kind, order, order_seen[order], entry["slug"])
                )
            order_seen[order] = entry["slug"]
            by_slug[(kind, entry["slug"])] = entry
        known = {e["slug"] for e in items}
        for index, entry in enumerate(items):
            meta = entry["meta"]
            prev = meta["prev"] if "prev" in meta else (items[index - 1]["slug"] if index else None)
            nxt = (
                meta["next"]
                if "next" in meta
                else (items[index + 1]["slug"] if index + 1 < len(items) else None)
            )
            if prev is not None and prev not in known:
                errors.append("%s/%s: prev %r không tồn tại" % (kind, entry["slug"], prev))
                prev = None
            if nxt is not None and nxt not in known:
                errors.append("%s/%s: next %r không tồn tại" % (kind, entry["slug"], nxt))
                nxt = None
            entry["prev"], entry["next"] = prev, nxt
        by_type[kind] = items

    hub = read_json(os.path.join(content_dir, "hub.json"), errors) or {}
    hub_body = read_text(os.path.join(content_dir, "hub.body.html"))
    for key in ("title", "lead", "desc", "blocks", "indexes"):
        if key not in hub:
            errors.append("hub.json: thiếu %s" % key)
    if isinstance(hub.get("blocks"), dict):
        for key in ("temples", "quests", "walkthrough", "reference"):
            block = hub["blocks"].get(key)
            if not isinstance(block, dict) or not block.get("title") or not block.get("lead"):
                errors.append("hub.json: blocks.%s thiếu title/lead" % key)
    if isinstance(hub.get("indexes"), dict):
        for key in ("quests", "temples"):
            block = hub["indexes"].get(key)
            if not isinstance(block, dict) or not block.get("title") or not block.get("lead"):
                errors.append("hub.json: indexes.%s thiếu title/lead" % key)
    if "<h1" in hub_body.lower():
        errors.append("hub.body.html: không được chứa <h1>")

    return {
        "regions": regions,
        "region_by_name": region_by_name,
        "entries": entries,
        "by_type": by_type,
        "by_slug": by_slug,
        "hub": hub,
        "hub_body": hub_body,
        "errors": errors,
        "warns": warns,
    }


def build_content_page(entry, ctx):
    kind, slug, meta = entry["type"], entry["slug"], entry["meta"]
    key = page_key(entry)
    body = add_heading_ids(entry["body"])
    toc = toc_items(body)
    nimg = len(IMG_OPEN_RE.findall(body))
    region = ctx["region_by_name"].get(meta.get("region", ""))

    crumb = ['<a href="%s">Lộ trình</a>' % _link(key, "pages/progress-route.html")]
    if kind == "walkthrough" and region:
        crumb.append(
            '<a href="%s#vung-%d">%s</a>'
            % (_link(key, "pages/progress-route.html"), region["index"], esc(region["title"]))
        )
    elif kind in INDEX_KEYS:
        crumb.append(
            '<a href="%s">%s</a>'
            % (_link(key, "pages/" + INDEX_KEYS[kind]), esc(TYPE_LABEL[kind]))
        )
    else:
        crumb.append(
            '<a href="%s#%s">%s</a>'
            % (_link(key, "pages/progress-route.html"), TYPE_SECTION[kind], esc(TYPE_LABEL[kind]))
        )
    crumb.append(esc(meta["title"]))

    chips = []
    quests = (meta.get("meta") or {}).get("quests")
    if kind == "walkthrough" and isinstance(quests, list) and quests:
        chips.append("%d nhiệm vụ" % len(quests))
    if region and kind != "walkthrough":
        chips.append(region["title"])
    chips.append("%d mục" % len(toc))
    chips.append("%d ảnh" % nimg)

    toc_links = "\n".join(
        '        <a href="#%s" title="%s">%s</a>' % (hid, attr(text), esc(text))
        for hid, text in toc
    )
    pager = []
    if entry["prev"]:
        prev_title = ctx["by_slug"][(kind, entry["prev"])]["meta"]["title"]
        pager.append(
            '<a class="pager-prev" href="%s"><span>← Trước</span><strong>%s</strong></a>'
            % (_link(key, "pages/%s/%s.html" % (kind, entry["prev"])), esc(prev_title))
        )
    if entry["next"]:
        next_title = ctx["by_slug"][(kind, entry["next"])]["meta"]["title"]
        pager.append(
            '<a class="pager-next" href="%s"><span>Sau →</span><strong>%s</strong></a>'
            % (_link(key, "pages/%s/%s.html" % (kind, entry["next"])), esc(next_title))
        )
    pager_html = ""
    if pager:
        pager_html = (
            '\n    <nav class="region-pager" aria-label="Trang trước và trang sau">\n      %s\n    </nav>'
            % "\n      ".join(pager)
        )

    main_html = (
        '<div class="container layout">\n'
        '  <header class="region-head">\n'
        '    <p class="crumb">%s</p>\n'
        '    <h1 class="page-title"><span class="num-badge">%s</span> %s</h1>\n'
        '    <p class="page-meta">%s</p>\n'
        "  </header>\n"
        '  <aside class="sidebar rail">\n'
        '    <details class="rail-toc-box" open>\n'
        '      <summary class="toc-title">Mục lục <span class="toc-count">%d mục</span></summary>\n'
        '      <nav class="toc rail-toc" aria-label="Mục lục trang">\n%s\n      </nav>\n'
        "    </details>\n"
        "  </aside>\n"
        '  <main class="content" id="main">\n%s%s\n  </main>\n'
        "</div>"
    ) % (
        " <span>/</span> ".join(crumb),
        esc(meta["order"]),
        esc(meta["title"]),
        "".join("<span>%s</span>" % esc(chip) for chip in chips),
        len(toc),
        toc_links,
        body.strip(),
        pager_html,
    )
    return page_shell(key, "%s – TOTK Guide" % meta["title"], meta["desc"], main_html)


def build_hub(ctx):
    key = HUB_KEY
    hub = ctx["hub"]
    blocks = hub["blocks"]

    temples = [e for e in ctx["by_type"]["temples"] if e["meta"].get("kind") == "main-temple"]
    if temples:
        cards = "\n".join(
            card_html(
                key,
                "pages/temples/%s.html" % e["slug"],
                e["meta"]["order"],
                e["meta"]["title"],
                (ctx["region_by_name"].get(e["meta"].get("region", "")) or {}).get("title", ""),
                "",
            )
            for e in temples
        )
        temples_inner = '<div class="route-grid">\n%s\n</div>' % cards
    else:
        temples_inner = '<p class="empty">%s</p>' % EMPTY["temples"]
    temples_inner += '\n<p class="block-more"><a href="%s">Xem toàn bộ Đền Thờ, mỏ và trận cuối →</a></p>' % _link(
        key, "pages/temples.html"
    )

    quests = ctx["by_type"]["quests"]
    if quests:
        cards = "\n".join(
            card_html(
                key,
                "pages/quests/%s.html" % e["slug"],
                e["meta"]["order"],
                e["meta"]["title"],
                e["meta"].get("summary", ""),
                "",
            )
            for e in quests
        )
        quests_inner = '<div class="route-grid">\n%s\n</div>' % cards
    else:
        quests_inner = '<p class="empty">%s</p>' % EMPTY["quests"]
    quests_inner += '\n<p class="block-more"><a href="%s">Xem toàn bộ nhiệm vụ chính →</a></p>' % _link(
        key, "pages/quests.html"
    )

    groups = []
    for region in ctx["regions"]:
        chapters = [
            e for e in ctx["by_type"]["walkthrough"] if e["meta"].get("region") == region["name"]
        ]
        sums = {"shrines": 0, "caves": 0, "koroks": 0, "chests": 0}
        for chapter in chapters:
            meta = chapter["meta"].get("meta") or {}
            for name in sums:
                try:
                    sums[name] += int(meta.get(name) or 0)
                except (TypeError, ValueError):
                    pass
        head = '  <h3 id="vung-%d">%d. %s <span class="region-count">%d chương</span></h3>' % (
            region["index"],
            region["index"],
            esc(region["title"]),
            len(chapters),
        )
        meta_line = (
            '  <p class="region-meta">%d Đền Thờ Nhỏ · %d Hang · %d Hạt Korok · %d Rương</p>'
            % (sums["shrines"], sums["caves"], sums["koroks"], sums["chests"])
        )
        if chapters:
            cards = "\n".join(
                card_html(
                    key,
                    "pages/walkthrough/%s.html" % e["slug"],
                    e["meta"]["order"],
                    e["meta"]["title"],
                    region["title"],
                    "%d đền · %d hang · %d Korok · %d rương"
                    % (
                        int((e["meta"].get("meta") or {}).get("shrines") or 0),
                        int((e["meta"].get("meta") or {}).get("caves") or 0),
                        int((e["meta"].get("meta") or {}).get("koroks") or 0),
                        int((e["meta"].get("meta") or {}).get("chests") or 0),
                    ),
                )
                for e in chapters
            )
            inner = '<div class="route-grid">\n%s\n  </div>' % cards
        else:
            inner = '  <p class="empty">Chưa có chương nào.</p>'
        groups.append('<div class="region-group">\n%s\n%s\n%s\n</div>' % (head, meta_line, inner))

    references = ctx["by_type"]["reference"]
    if references:
        items = "\n".join(
            '<li><a href="%s">%s</a>%s</li>'
            % (
                _link(key, "pages/reference/%s.html" % e["slug"]),
                esc(e["meta"]["title"]),
                ("<span>%s</span>" % esc(e["meta"]["summary"])) if e["meta"].get("summary") else "",
            )
            for e in references
        )
        reference_inner = '<ul class="ref-list">\n%s\n</ul>' % items
    else:
        reference_inner = '<p class="empty">%s</p>' % EMPTY["reference"]

    sections = []
    for index, name in enumerate(("temples", "quests", "walkthrough", "reference"), 1):
        block = blocks[name]
        inner = {
            "temples": temples_inner,
            "quests": quests_inner,
            "walkthrough": "\n".join(groups),
            "reference": reference_inner,
        }[name]
        sections.append(
            '<section class="route-block" id="%s">\n'
            "  <h2>%d. %s</h2>\n"
            '  <p class="block-lead">%s</p>\n'
            "%s\n"
            "</section>"
            % (TYPE_SECTION[name], index, esc(block["title"]), esc(block["lead"]), inner)
        )

    main_html = (
        '<main class="container" id="main">\n'
        '  <p class="crumb"><a href="%s">Trang chủ</a> <span>/</span> Lộ trình</p>\n'
        '  <h1 class="page-title">%s</h1>\n'
        '  <p class="page-lead">%s</p>\n'
        "%s\n%s\n"
        "</main>"
    ) % (
        _link(key, "index.html"),
        esc(hub["title"]),
        esc(hub["lead"]),
        ctx["hub_body"].strip(),
        "\n".join(sections),
    )
    return page_shell(key, "%s – TOTK Guide" % hub["title"], hub["desc"], main_html)


def build_index(kind, ctx):
    key = INDEX_KEYS[kind]
    config = ctx["hub"]["indexes"][kind]
    items = ctx["by_type"][kind]
    if items:
        rows = []
        for entry in items:
            meta = entry["meta"]
            region = ctx["region_by_name"].get(meta.get("region", ""))
            extra = " · ".join(
                part for part in (region["title"] if region else "", meta.get("summary", "")) if part
            )
            rows.append(
                '<li><a href="%s"><span class="idx-num">%s</span> <span class="idx-title">%s</span></a>%s</li>'
                % (
                    _link(key, "pages/%s/%s.html" % (kind, entry["slug"])),
                    esc(meta["order"]),
                    esc(meta["title"]),
                    ('<span class="idx-meta">%s</span>' % esc(extra)) if extra else "",
                )
            )
        inner = '<ol class="index-list">\n%s\n</ol>' % "\n".join(rows)
    else:
        inner = '<p class="empty">%s</p>' % EMPTY[kind]

    main_html = (
        '<main class="container" id="main">\n'
        '  <p class="crumb"><a href="%s">Lộ trình</a> <span>/</span> %s</p>\n'
        '  <h1 class="page-title">%s</h1>\n'
        '  <p class="page-lead">%s</p>\n'
        "%s\n"
        "</main>"
    ) % (
        _link(key, "pages/progress-route.html"),
        esc(config["title"]),
        esc(config["title"]),
        esc(config["lead"]),
        inner,
    )
    desc = config.get("desc") or ctx["hub"]["desc"]
    return page_shell(key, "%s – TOTK Guide" % config["title"], desc, main_html)


def build_outputs(ctx):
    outputs = {HUB_KEY: build_hub(ctx)}
    for kind in INDEX_KEYS:
        outputs[INDEX_KEYS[kind]] = build_index(kind, ctx)
    for entry in ctx["entries"]:
        outputs[page_key(entry)] = build_content_page(entry, ctx)
    return outputs


def compare(out_dir, outputs):
    problems = []
    for key in sorted(outputs):
        path = os.path.join(out_dir, *key.split("/"))
        if not os.path.exists(path):
            problems.append("thiếu: %s" % key)
        elif read_text(path) != outputs[key]:
            problems.append("lệch: %s" % key)
    owned = {HUB_KEY, *INDEX_KEYS.values()}
    for key in sorted(owned - set(outputs)):
        problems.append("thừa: %s" % key)
    for kind in PAGE_TYPES:
        folder = os.path.join(out_dir, kind)
        if not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder)):
            if name.endswith(".html") and ("%s/%s" % (kind, name)) not in outputs:
                problems.append("thừa: %s/%s" % (kind, name))
    return problems


def main(argv=None):
    parser = argparse.ArgumentParser(description="Sinh pages/ từ content/")
    parser.add_argument("--check", action="store_true", help="so bản sinh với file trên đĩa")
    parser.add_argument("--out", help="thư mục đích (mặc định pages/)")
    parser.add_argument("--content", default="content", help="thư mục nguồn nội dung")
    args = parser.parse_args(argv)

    content_dir = args.content
    if not os.path.isabs(content_dir):
        content_dir = os.path.join(ROOT, content_dir)
    out_dir = args.out or os.path.join(ROOT, "pages")
    if not os.path.isabs(out_dir):
        out_dir = os.path.join(ROOT, out_dir)

    ctx = load_site(content_dir)
    if ctx["errors"]:
        for message in ctx["errors"]:
            print("LỖI: " + message)
        print("-> dừng, chưa sinh trang nào.")
        return 1
    for message in ctx["warns"]:
        print("CẢNH BÁO: " + message)

    outputs = build_outputs(ctx)
    if args.check:
        problems = compare(out_dir, outputs)
        for message in problems:
            print("  " + message)
        print("%d trang | %d file lệch -> %s" % (len(outputs), len(problems), "FAIL" if problems else "PASS"))
        return 1 if problems else 0

    for key in sorted(outputs):
        path = os.path.join(out_dir, *key.split("/"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(outputs[key])
    counts = {kind: len(ctx["by_type"][kind]) for kind in PAGE_TYPES}
    print(
        "Đã sinh %d trang vào %s (chương %d, nhiệm vụ %d, đền %d, tham chiếu %d)"
        % (
            len(outputs),
            rel(out_dir),
            counts["walkthrough"],
            counts["quests"],
            counts["temples"],
            counts["reference"],
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
