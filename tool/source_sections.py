#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Một định nghĩa "mục" duy nhất cho mọi cổng đọc trang nguồn / trang đã sinh.

Vì sao có file này: hợp đồng "mục" rất dễ đọc sai — một trang được tách theo <h2>, và
nếu có ảnh nằm TRƯỚC <h2> đầu tiên thì phần đó thành mục riêng tên "(trước mục đầu)".
Bản thân nó đã được mô tả ở tool/README.md, nhưng trước đây mỗi cổng tự viết lại một lần
(check-image-match, check-coverage) nên chỉ cần một chỗ hiểu sai là lệch 1 mục mà không ai thấy.

Mọi cổng PHẢI import từ đây:
  check-image-match.py  -> source_cache() + split_sections()  (đếm mục, so ảnh)
  verify-pages.py       -> split_sections()                   (so số mục trang với nguồn)
  check-coverage.py     -> split_sections() + text_sections()  (so số từ từng mục)

Khác biệt DUY NHẤT được phép: check-coverage đo CHỮ nên bỏ <figure>/<img> và bỏ luôn vùng
"(trước mục đầu)" (vùng đó chỉ có bảng tóm tắt + icon). Đó là lý do có text_sections().
"""
from __future__ import annotations

import html as html_mod
import json
import os
import re
import urllib.parse

H2_RE = re.compile(r"<h2\b[^>]*>(.*?)</h2>", re.I | re.S)
IMG_TAG_RE = re.compile(r"<img\b[^>]*>", re.I | re.S)
SRC_RE = re.compile(r"""\bsrc\s*=\s*["']([^"']+)["']""", re.I | re.S)
ALT_RE = re.compile(r"""\balt\s*=\s*["']([^"']*)["']""", re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")
FIGURE_RE = re.compile(r"<figure\b.*?</figure>", re.I | re.S)

PAGE_TYPES = ("walkthrough", "quests", "temples", "reference")
CACHE_DIRNAME = ".tmp-src"


def read_text(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def norm_text(fragment):
    return re.sub(r"\s+", " ", TAG_RE.sub(" ", fragment)).strip()


def norm_name(value):
    """Tên file ảnh đã chuẩn hoá: bỏ tiền tố <n>px- và hậu tố -1024x576, lower-case."""
    name = urllib.parse.unquote(value.split("?")[0].split("#")[0].split("/")[-1])
    name = re.sub(r"^\d+px-", "", name, flags=re.I)
    name = re.sub(r"-\d+x\d+(?=\.[A-Za-z0-9]+$)", "", name)
    return name.lower()


def article_html(text):
    """Phần thân bài của một trang: <article>, không có thì <main>, cuối cùng là <body>."""
    for tag in ("article", "main"):
        match = re.search(r"<%s\b[^>]*>(.*?)</%s>" % (tag, tag), text, re.I | re.S)
        if match:
            return match.group(1)
    match = re.search(r"<body\b[^>]*>(.*?)</body>", text, re.I | re.S)
    return match.group(1) if match else text


def split_sections(text, keep_image, article=True):
    """Tách thành [(heading, [src gốc của ảnh])] theo thứ tự tài liệu.

    keep_image(src) quyết định ảnh nào được tính. Giữ src GỐC (không chuẩn hoá) vì cổng ảnh
    còn phải kiểm đường dẫn thật; ai cần so tên thì gọi norm_name() — source_split() làm sẵn.
    Mục đầu mang heading "" khi có ảnh nằm trước <h2> đầu tiên, nghĩa là
    số mục = số <h2> + 1 trong trường hợp đó.
    """
    body = article_html(text) if article else text
    events = []
    for match in H2_RE.finditer(body):
        events.append((match.start(), "h", norm_text(match.group(1))))
    for match in IMG_TAG_RE.finditer(body):
        src = SRC_RE.search(match.group(0))
        if src and keep_image(src.group(1)):
            events.append((match.start(), "i", src.group(1)))
    events.sort(key=lambda item: item[0])
    sections = []
    for _, kind, value in events:
        if kind == "h":
            sections.append([value, []])
        else:
            if not sections:
                sections.append(["", []])
            sections[-1][1].append(value)
    return [(heading, images) for heading, images in sections]


def source_split(text):
    """Mục của trang NGUỒN (ảnh nằm trong /uploads/), tên file đã chuẩn hoá."""
    return [
        (heading, [norm_name(src) for src in images])
        for heading, images in split_sections(text, lambda src: "/uploads/" in src)
    ]


def page_split(text):
    """Mục của trang ĐÃ SINH (ảnh nằm trong /images/), giữ src gốc để kiểm đường dẫn."""
    return split_sections(text, lambda src: "/images/" in src)


def text_sections(text):
    """Mục chỉ có CHỮ (bỏ figure/ảnh), và bỏ vùng trước <h2> đầu — dùng cho check-coverage."""
    body = FIGURE_RE.sub(" ", article_html(text))
    body = IMG_TAG_RE.sub(" ", body)
    marks = [m.start() for m in H2_RE.finditer(body)]
    sections = []
    for index, start in enumerate(marks):
        end = marks[index + 1] if index + 1 < len(marks) else len(body)
        heading = norm_text(H2_RE.match(body, start).group(1))
        sections.append((heading, body[start:end]))
    return sections


def cache_path(root, kind, slug):
    base = os.path.join(root, CACHE_DIRNAME, kind, slug)
    for ext in (".json", ".html"):
        if os.path.exists(base + ext):
            return base + ext
    return None


def source_sections(root, kind, slug):
    """Mục của nguồn, đọc từ cache .tmp-src. Trả None khi chưa có cache."""
    path = cache_path(root, kind, slug)
    if path is None:
        return None
    if path.endswith(".json"):
        data = json.loads(read_text(path))
        return [
            (item.get("heading", ""), [norm_name(x) for x in item.get("images", [])])
            for item in data.get("sections", [])
        ]
    return source_split(read_text(path))


def first_table_before_h2(text):
    """Bảng facts ở đầu trang nguồn (trước <h2> đầu tiên), trả HTML hoặc ''."""
    body = article_html(text)
    match = re.search(r"<h2\b", body, re.I)
    pre = body[: match.start()] if match else body
    table = re.search(r"<table\b.*?</table>", pre, re.I | re.S)
    return table.group(0) if table else ""


def image_alts(text):
    """[(tên file chuẩn hoá, alt gốc)] theo thứ tự — dùng cho inspect-source."""
    out = []
    for match in IMG_TAG_RE.finditer(text):
        src = SRC_RE.search(match.group(0))
        if not src or "/uploads/" not in src.group(1):
            continue
        alt = ALT_RE.search(match.group(0))
        out.append((norm_name(src.group(1)), html_mod.unescape(alt.group(1)) if alt else ""))
    return out
