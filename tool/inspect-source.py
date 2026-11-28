#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Soi một trang NGUỒN của zeldacentral: mục, ảnh, alt gốc, bảng facts, đối chiếu folder ảnh.

Vì sao có file này: mỗi chương mới đều cần đúng bốn lần đọc khác nhau của cùng một file nguồn
(tách mục, liệt kê ảnh + alt, bảng facts đầu trang, đếm ảnh trên đĩa). Trước đây mỗi lần là một
script nháp trong .scratch/ — tám file cho ba chương ở T2. Dùng cái này thay cả tám.

Dùng:
  python tool/inspect-source.py lookout-landing hyrule-field       # đọc cache .tmp-src
  python tool/inspect-source.py --from .scratch/src-hyrule-field.html hyrule-field
  python tool/inspect-source.py --no-alt --type walkthrough <slug> # chỉ đếm mục/ảnh
  python tool/inspect-source.py --ticket <slug>    # khối số liệu dán thẳng vào vé
  python tool/inspect-source.py --text <slug>      # nguồn thành văn bản theo mục, để dịch
  python tool/inspect-source.py --text --section 2-4 <slug>   # chỉ một khoảng mục

Cache nguồn do cổng ảnh tạo: python tool/check-image-match.py --refresh <slug>
"""
from __future__ import annotations

import argparse
import html as html_mod
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tool"))
import source_sections as shared  # noqa: E402


def read(path):
    return shared.read_text(path)


def show_facts(table_html):
    if not table_html:
        return ["  (không có bảng facts trước <h2> đầu)"]
    out = []
    for row in re.finditer(r"<tr\b[^>]*>(.*?)</tr>", table_html, re.I | re.S):
        cells = [
            html_mod.unescape(re.sub(r"\s+", " ", shared.TAG_RE.sub(" ", c)).strip())
            for c in re.findall(r"<t[dh]\b[^>]*>(.*?)</t[dh]>", row.group(1), re.I | re.S)
        ]
        cells = [c for c in cells if c]
        if cells:
            out.append("  %-18s %s" % (cells[0][:18], " | ".join(cells[1:]) or cells[0]))
    return out

def clean_inline(fragment):
    """Chữ của một heading: bỏ tag, giải entity, gộp khoảng trắng."""
    text = shared.TAG_RE.sub(" ", fragment)
    return re.sub(r"\s+", " ", html_mod.unescape(text)).strip()


def block_text(fragment):
    """Một khối nội dung thành chữ dễ đọc; ảnh giữ lại thành [IMG …] / [ICON …] đúng chỗ."""
    text = re.sub(r"</p>|<br\s*/?>", "\n", fragment, flags=re.I)
    text = re.sub(r"<li\b[^>]*>", "\n- ", text, flags=re.I)
    text = re.sub(r"<tr\b[^>]*>", "\n| ", text, flags=re.I)
    text = re.sub(r"</t[dh]>", " | ", text, flags=re.I)
    text = re.sub(r"</summary>", "\n", text, flags=re.I)

    def image(match):
        src = shared.SRC_RE.search(match.group(0))
        if not src:
            return ""
        alt = shared.ALT_RE.search(match.group(0))
        kind = "ICON" if "/icons/" in src.group(1) else "IMG"
        label = html_mod.unescape(alt.group(1)) if alt else ""
        return "[%s %s | %s]" % (kind, shared.norm_name(src.group(1)), label)

    text = shared.IMG_TAG_RE.sub(image, text)
    text = html_mod.unescape(shared.TAG_RE.sub("", text))
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text)
    return text.strip()


def dump_text(text, start=0, end=10 ** 6):
    """Trang nguồn thành văn bản theo mục: H2/H3/H4, đoạn, gạch đầu dòng, hàng bảng, ảnh.

    Vì sao có chế độ này: đọc HTML thô để dịch là cách tốn kém nhất — mỗi chương 300–700 KB
    markup trong khi phần chữ chỉ vài chục KB. Bản này giữ đúng thứ tự ảnh xen giữa chữ
    (thứ tự mà cổng ảnh kiểm), nên vẫn đối chiếu được mà đọc nhẹ hơn nhiều lần.
    """
    body = shared.article_html(text)
    first = re.search(r"<h2\b", body, re.I)
    if first:
        body = body[first.start():]
    section = -1
    lines = []
    for token in re.split(r"(<h[234]\b[^>]*>.*?</h[234]>)", body, flags=re.I | re.S):
        head = re.match(r"<h([234])\b[^>]*>(.*?)</h[234]>\s*$", token, re.I | re.S)
        if head:
            if head.group(1) == "2":
                section += 1
            if start <= section <= end:
                lines.append("H%s %s" % (head.group(1), clean_inline(head.group(2))))
            continue
        if not (start <= section <= end):
            continue
        block = block_text(token)
        if block:
            lines.append(block)
    return "\n".join(lines)


def ticket_block(slug, kind, text):
    """Khối số liệu dán thẳng vào vé — thay cho việc đếm tay (đã lệch một lần ở T4: 21 vs 36 h3)."""
    body = shared.article_html(text)
    first = re.search(r"<h2\b", body, re.I)
    article = body[first.start():] if first else body
    sections = shared.source_split(text)
    occurrences = [name for _, images in sections for name in images]
    counts = {}
    for name in occurrences:
        counts[name] = counts.get(name, 0) + 1
    dup = sorted((name, n) for name, n in counts.items() if n > 1)
    pre_region = "có ảnh" if sections and sections[0][0] == "" else "không"
    lines = [
        "## Số liệu nguồn — %s/%s" % (kind, slug),
        "",
        "| Hạng mục | Giá trị |",
        "|---|---|",
        "| Số mục h2 | %d |" % len(re.findall(r"<h2\b", article, re.I)),
        "| Số mục h3 | %d |" % len(re.findall(r"<h3\b", article, re.I)),
        "| Số mục h4 | %d |" % len(re.findall(r"<h4\b", article, re.I)),
        "| Ảnh nằm trước mục h2 đầu | %s |" % pre_region,
        "| Ảnh (lượt xuất hiện) | %d |" % len(occurrences),
        "| Ảnh duy nhất (số file cần tải) | %d |" % len(counts),
        "| Ảnh lặp trong nguồn | %s |" % (", ".join("%s ×%d" % (n, c) for n, c in dup) or "không"),
        "",
        "Dán khối này vào vé. Số liệu viết tay trong vé hay lệch (T4 ghi 21 h3, nguồn có 36); "
        "chuẩn là tool/inspect-source.py.",
    ]
    return "\n".join(lines)


def inspect(slug, kind, path, show_alt=True):
    text = read(path)
    sections = shared.source_split(text)
    alts = dict(shared.image_alts(text))

    # thứ tự + alt gốc theo từng mục (giữ cả ảnh lặp để thấy nguồn lặp ở đâu)
    print("=" * 96)
    print("SLUG %s  (%s)  nguồn: %s" % (slug, kind, os.path.relpath(path, ROOT).replace("\\", "/")))
    print("SỐ MỤC: %d  |  SỐ ẢNH: %d" % (len(sections), sum(len(images) for _, images in sections)))
    print("=" * 96)
    for index, (heading, images) in enumerate(sections):
        label = heading or "(trước mục đầu)"
        print("\n[%02d] %s   — %d ảnh" % (index, label, len(images)))
        if show_alt:
            for k, name in enumerate(images, 1):
                print("     %2d. %-14s %s" % (k, name[:14], alts.get(name, "")))

    print("\n--- bảng facts đầu trang ---")
    for line in show_facts(shared.first_table_before_h2(text)):
        print(line)

    counts = {}
    for _, images in sections:
        for name in images:
            counts[name] = counts.get(name, 0) + 1
    dup = {name: n for name, n in counts.items() if n > 1}
    if dup:
        print("\n--- ảnh LẶP trong nguồn (cổng ảnh cấm dùng trùng) ---")
        for name, n in sorted(dup.items()):
            print("  %s  (xuất hiện %d lần)" % (name, n))

    folder = os.path.join(ROOT, "images", kind, slug)
    if os.path.isdir(folder):
        on_disk = sorted(f.lower() for f in os.listdir(folder))
        need = sorted(set(alts))
        missing = [n for n in need if n not in on_disk]
        extra = [n for n in on_disk if n not in need]
        print("\n--- folder images/%s/%s: %d file ---" % (kind, slug, len(on_disk)))
        for name in missing:
            print("  thiếu file : %s" % name)
        for name in extra:
            print("  thừa file  : %s" % name)
        if not missing and not extra:
            print("  khớp nguồn 1:1")
    else:
        print("\n--- chưa có folder images/%s/%s ---" % (kind, slug))


def parse_section(spec):
    """'2' -> mục 2; '0-3' -> mục 0 tới 3; rỗng -> mọi mục."""
    if not spec:
        return 0, 10 ** 6
    hit = re.match(r"^\s*(\d+)\s*(?:-\s*(\d+))?\s*$", spec)
    if not hit:
        raise SystemExit("--section nhận N hoặc N-M (ví dụ 2 hoặc 0-3)")
    start = int(hit.group(1))
    return start, int(hit.group(2)) if hit.group(2) else start


def main(argv):
    parser = argparse.ArgumentParser(description="Soi cấu trúc một trang nguồn")
    parser.add_argument("slugs", nargs="+")
    parser.add_argument("--type", default="walkthrough", choices=shared.PAGE_TYPES)
    parser.add_argument("--from", dest="source_file", help="đọc file nguồn này thay vì cache .tmp-src")
    parser.add_argument("--no-alt", action="store_true", help="không in alt gốc")
    parser.add_argument("--files", action="store_true", help="chỉ in tên file ảnh đầy đủ theo từng mục (để tải ảnh)")
    parser.add_argument("--ticket", action="store_true", help="in khối số liệu để dán vào vé")
    parser.add_argument("--text", action="store_true", help="in nguồn thành văn bản theo mục (để dịch)")
    parser.add_argument("--section", help="chỉ in mục N hoặc N-M (đếm từ 0, 0 = vùng trước mục đầu)")
    args = parser.parse_args(argv)

    missing = 0
    for slug in args.slugs:
        if args.source_file:
            path = args.source_file if os.path.isabs(args.source_file) else os.path.join(ROOT, args.source_file)
        else:
            path = shared.cache_path(ROOT, args.type, slug)
        if not path or not os.path.exists(path):
            print("CHƯA CÓ NGUỒN cho %s/%s — chạy: python tool/check-image-match.py --refresh %s"
                  % (args.type, slug, slug))
            missing += 1
            continue
        text = read(path)
        if args.ticket:
            print(ticket_block(slug, args.type, text))
            print()
            continue
        if args.text:
            start, end = parse_section(args.section)
            print(dump_text(text, start, end))
            print()
            continue
        if args.files:
            for index, (heading, images) in enumerate(shared.source_split(text)):
                print("[%02d] %s" % (index, heading or "(trước mục đầu)"))
                for name in images:
                    print("     " + name)
            continue
        inspect(slug, args.type, path, show_alt=not args.no_alt)
    return 1 if missing and missing == len(args.slugs) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
