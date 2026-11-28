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


def main(argv):
    parser = argparse.ArgumentParser(description="Soi cấu trúc một trang nguồn")
    parser.add_argument("slugs", nargs="+")
    parser.add_argument("--type", default="walkthrough", choices=shared.PAGE_TYPES)
    parser.add_argument("--from", dest="source_file", help="đọc file nguồn này thay vì cache .tmp-src")
    parser.add_argument("--no-alt", action="store_true", help="không in alt gốc")
    parser.add_argument("--files", action="store_true", help="chỉ in tên file ảnh đầy đủ theo từng mục (để tải ảnh)")
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
        if args.files:
            text = read(path)
            for index, (heading, images) in enumerate(shared.source_split(text)):
                print("[%02d] %s" % (index, heading or "(trước mục đầu)"))
                for name in images:
                    print("     " + name)
            continue
        inspect(slug, args.type, path, show_alt=not args.no_alt)
    return 1 if missing and missing == len(args.slugs) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
