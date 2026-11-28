#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cổng độ phủ: mỗi mục của trang nguồn phải có nội dung tương ứng trong bản dịch.

Vì sao có cổng này: 5 cổng cũ chỉ kiểm hình dạng (số mục, ảnh, heading, blacklist).
Bỏ sót hẳn một đoạn của nguồn thì cả 5 cổng vẫn PASS. Cổng này so số từ và số khối
văn bản của từng mục: mục nguồn có ≥ MIN_SOURCE_WORDS từ mà bản dịch còn < 30% số từ
hoặc 0 khối văn bản -> FAIL.

Dùng: python tool/check-coverage.py [--content content] [--pages pages] [slug ...]
Thoát mã 1 nếu có mục rơi nội dung. Không có cache nguồn -> in "chưa chạy được", exit 0.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.path.join(ROOT, ".tmp-src")
H2_RE = re.compile(r"<h2\b[^>]*>(.*?)</h2>", re.I | re.S)
IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
FIG_RE = re.compile(r"<figure\b.*?</figure>", re.I | re.S)
IDEAL_RE = re.compile(r"<aside\b.*?</aside>", re.I | re.S)
MIN_SOURCE_WORDS = 20
MIN_RATIO = 0.30


def load_module(filename, name):
    path = os.path.join(ROOT, "tool", filename)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_text(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def words(fragment):
    text = re.sub(r"<[^>]+>", " ", fragment)
    text = text.replace("&nbsp;", " ").replace("&amp;", "&")
    return [w for w in re.split(r"\s+", text) if w.strip()]


def split_sections(text, keep_article):
    """Trả [(heading, html)] cho từng mục; bỏ ảnh để chỉ đo phần chữ."""
    body = keep_article(text)
    body = FIG_RE.sub(" ", body)
    body = IMG_RE.sub(" ", body)
    marks = [m.start() for m in H2_RE.finditer(body)]
    sections = []
    for index, start in enumerate(marks):
        end = marks[index + 1] if index + 1 < len(marks) else len(body)
        heading = re.sub(r"<[^>]+>", " ", H2_RE.match(body, start).group(1)).strip()
        sections.append((heading, body[start:end]))
    return sections


def source_sections(kind, slug, image_gate):
    base = os.path.join(CACHE_DIR, kind, slug)
    if os.path.exists(base + ".html"):
        text = read_text(base + ".html")
        return split_sections(text, image_gate.article_html)
    if os.path.exists(base + ".json"):
        data = json.loads(read_text(base + ".json"))
        return [(item.get("heading", ""), "<p>" + " ".join(str(x) for x in item.get("text", [])) + "</p>")
                for item in data.get("sections", [])]
    return None


def page_sections(kind, slug, pages_dir):
    path = os.path.join(pages_dir, kind, slug + ".html")
    if not os.path.isfile(path):
        return None
    text = read_text(path)
    main = re.search(r'<main class="content" id="main">(.*?)</main>', text, re.S)
    body = main.group(1) if main else text
    body = IDEAL_RE.sub(" ", body)
    return split_sections(body, lambda t: t)


def check(entry, pages_dir, image_gate):
    kind, slug = entry["type"], entry["slug"]
    label = "%s/%s" % (kind, slug)
    src = source_sections(kind, slug, image_gate)
    if src is None:
        return None, label
    page = page_sections(kind, slug, pages_dir)
    if page is None:
        return ["%s: chưa sinh trang" % label], label
    fails = []
    if len(src) != len(page):
        fails.append("%s: số mục lệch nguồn (trang %d, nguồn %d)" % (label, len(page), len(src)))
    for index, (heading, html) in enumerate(src):
        src_words = len(words(html))
        if src_words < MIN_SOURCE_WORDS:
            continue
        if index >= len(page):
            fails.append('%s: thiếu mục "%s"' % (label, heading[:40]))
            continue
        page_heading, page_html = page[index]
        page_words = len(words(page_html))
        blocks = len(re.findall(r"<p\b|<li\b|<tr\b", page_html, re.I))
        ratio = page_words / float(src_words) if src_words else 1.0
        if ratio < MIN_RATIO or blocks == 0:
            fails.append(
                '%s: mục "%s" mất nội dung (nguồn %d từ, trang %d từ = %d%%, %d khối)'
                % (label, heading[:38], src_words, page_words, round(ratio * 100), blocks)
            )
    return fails, label


def main():
    parser = argparse.ArgumentParser(description="Kiểm độ phủ bản dịch so với trang nguồn")
    parser.add_argument("--content", default="content")
    parser.add_argument("--pages", default="pages")
    parser.add_argument("slugs", nargs="*")
    args = parser.parse_args()

    content_dir = args.content if os.path.isabs(args.content) else os.path.join(ROOT, args.content)
    pages_dir = args.pages if os.path.isabs(args.pages) else os.path.join(ROOT, args.pages)

    build = load_module("build-pages.py", "build_pages")
    image_gate = load_module("check-image-match.py", "check_image_match")
    ctx = build.load_site(content_dir)
    if ctx["errors"]:
        for message in ctx["errors"]:
            print("LỖI: " + message)
        return 1

    entries = ctx["entries"]
    if args.slugs:
        wanted = set(args.slugs)
        entries = [e for e in entries if e["slug"] in wanted]

    failures = 0
    checked = 0
    no_cache = 0
    for entry in entries:
        fails, label = check(entry, pages_dir, image_gate)
        if fails is None:
            no_cache += 1
            print("%-38s CHƯA CHẠY ĐƯỢC (không có cache nguồn trong .tmp-src)" % label)
            continue
        checked += 1
        print("%-38s %s" % (label, "PASS" if not fails else "FAIL (%d mục)" % len(fails)))
        for message in fails[:10]:
            print("    - " + message)
        failures += 1 if fails else 0

    print("-" * 70)
    print("Trang kiểm=%d | chưa có cache=%d | FAIL=%d -> %s"
          % (checked, no_cache, failures, "PASS" if not failures else "FAIL"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
