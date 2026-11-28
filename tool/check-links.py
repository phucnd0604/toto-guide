#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cổng link: 0 link nội bộ chết, 0 ảnh thiếu, 0 link ra domain ngoài (trừ Google Fonts).

Quét mọi file .html trong repo (trừ .git, .scratch, node_modules, .tmp-src):
  - href/src nội bộ phải trỏ tới file có thật (chấp nhận cả dạng clean URL không .html);
  - neo #... phải có id/name tương ứng trong trang đích;
  - ảnh (src) phải tồn tại trên đĩa;
  - link http(s) chỉ được trỏ tới fonts.googleapis.com / fonts.gstatic.com.

Dùng: python tool/check-links.py [-v]
Thoát mã 1 nếu có FAIL.
"""
from __future__ import annotations

import html
import os
import re
import sys
from urllib.parse import unquote, urlsplit

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", ".scratch", "node_modules", ".tmp-src", "__pycache__", ".vercel", "content"}
ALLOWED_HOSTS = {"fonts.googleapis.com", "fonts.gstatic.com"}
LINK_RE = re.compile(r"""\b(href|src)\s*=\s*(?:"([^"]*)"|'([^']*)')""", re.I)
ID_RE = r"""\b(?:id|name)\s*=\s*["']%s["']"""


def read_text(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def html_files():
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(files):
            if name.endswith(".html"):
                yield os.path.join(base, name)


def rel(path):
    return os.path.relpath(path, ROOT).replace("\\", "/")


def resolve(full, want_file):
    if want_file:
        return full if os.path.isfile(full) else None
    if os.path.isfile(full):
        return full
    if os.path.isdir(full):
        index = os.path.join(full, "index.html")
        return index if os.path.isfile(index) else None
    for candidate in (full + ".html", os.path.join(full, "index.html")):
        if os.path.isfile(candidate):
            return candidate
    return None


def check_file(path, cache):
    text = read_text(path)
    base = os.path.dirname(path)
    problems = []
    for match in LINK_RE.finditer(text):
        kind = match.group(1).lower()
        raw = match.group(2) if match.group(2) is not None else match.group(3)
        value = html.unescape((raw or "").strip())
        if not value or value.startswith("#"):
            continue
        if value.startswith(("mailto:", "tel:", "javascript:", "data:")):
            continue
        line_no = text.count("\n", 0, match.start()) + 1
        parts = urlsplit(value)
        if parts.scheme in ("http", "https") or value.startswith("//"):
            host = parts.hostname or value.lstrip("/").split("/")[0]
            if host not in ALLOWED_HOSTS:
                problems.append((line_no, "link ra domain ngoài: %s" % value))
            continue
        if parts.scheme and parts.scheme != "file":
            continue
        target = unquote(parts.path)
        if not target:
            continue
        if target.startswith("/"):
            full = os.path.normpath(os.path.join(ROOT, target.lstrip("/")))
        else:
            full = os.path.normpath(os.path.join(base, target))
        found = resolve(full, want_file=(kind == "src"))
        if not found:
            label = "ảnh thiếu" if kind == "src" else "link chết"
            problems.append((line_no, "%s: %s" % (label, value)))
            continue
        if kind == "href" and parts.fragment and found.endswith(".html"):
            if found not in cache:
                cache[found] = read_text(found)
            fragment = unquote(parts.fragment)
            if not re.search(ID_RE % re.escape(fragment), cache[found], re.I):
                problems.append((line_no, "neo #%s không có trong %s" % (fragment, rel(found))))
    return problems


def main():
    verbose = "-v" in sys.argv
    cache = {}
    total_files = total_links = 0
    failures = 0
    for path in html_files():
        total_files += 1
        problems = check_file(path, cache)
        total_links += 1
        if problems:
            failures += len(problems)
            print("[FAIL] %s (%d lỗi)" % (rel(path), len(problems)))
            for line_no, message in problems[:40]:
                print("    %s:%d  %s" % (rel(path), line_no, message))
            if len(problems) > 40:
                print("    ... còn %d lỗi" % (len(problems) - 40))
        elif verbose:
            print("[ok  ] %s" % rel(path))
    print("-" * 64)
    print("Trang quét=%d | FAIL=%d -> %s" % (total_files, failures, "PASS" if failures == 0 else "FAIL"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
