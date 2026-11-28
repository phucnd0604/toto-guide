#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cổng cấu trúc trang: đúng 1 h1, có meta description, layout 2 cột,
số mục H2 khớp nguồn, heading không còn tiếng Anh, không dùng "xN".

Áp cho mọi trang nội dung trong content/ (walkthrough, quests, temples, reference)
và cho hub + hai trang chỉ mục (kiểm 4 khối, 12 nhóm vùng đúng thứ tự).

Dùng: python tool/verify-pages.py
Thoát mã 1 nếu có HARD.
"""
from __future__ import annotations

import html
import importlib.util
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(ROOT, "pages")
sys.path.insert(0, os.path.join(ROOT, "tool"))
import source_sections as shared  # noqa: E402  (định nghĩa "mục" dùng chung)
VN_RE = re.compile(
    "[ăâđêôơưàáảãạằắẳẵặầấẩẫậèéẻẽẹềếểễệìíỉĩịòóỏõọồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ]",
    re.I,
)
X_RE = re.compile(r"(?:^|[^\w])(?:x\d+|\d+x)(?![\w])", re.I)
META_DESC_RE = re.compile(r'<meta\s+name="description"\s+content="([^"]*)"', re.I)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.I | re.S)
H1_RE = re.compile(r"<h1\b", re.I)
HEADING_RE = re.compile(r"<h([123])\b[^>]*>(.*?)</h\1>", re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")
HUB_BLOCKS = ["den-tho-chinh", "nhiem-vu-chinh", "lo-trinh-100", "tham-khao"]


def load_module(filename, name):
    path = os.path.join(ROOT, "tool", filename)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_text(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def norm_text(fragment):
    return re.sub(r"\s+", " ", TAG_RE.sub(" ", fragment)).strip()


def english_heading(fragment):
    """Heading bị coi là "chưa dịch" theo đúng luật của check-vietnamese, không phải luật riêng.

    Bản cũ tự đặt luật ("không có ký tự Việt + ≥2 từ") nên FAIL cả tên riêng đứng một mình
    như "Lookout Landing" trong khi check-vietnamese vẫn cho qua vì nằm trong PHRASES.
    Hai cổng đá nhau thì người viết không biết tin cổng nào; nay chỉ còn một luật.
    """
    text = norm_text(fragment)
    if VN_RE.search(text):
        return False
    return bool(vn_gate.untranslated(text))


def check_common(label, text, problems, warns):
    h1_count = len(H1_RE.findall(text))
    if h1_count != 1:
        problems.append("%s: cần đúng 1 <h1> (đang %d)" % (label, h1_count))
    desc = META_DESC_RE.search(text)
    if not desc or not desc.group(1).strip():
        problems.append("%s: thiếu meta description" % label)
    elif not 120 <= len(desc.group(1)) <= 158:
        warns.append(
            "%s: meta description dài %d ký tự (chuẩn 120–158)" % (label, len(desc.group(1)))
        )
    title = TITLE_RE.search(text)
    if not title or not title.group(1).strip():
        problems.append("%s: thiếu <title>" % label)


def check_content_page(entry, problems, warns):
    kind, slug = entry["type"], entry["slug"]
    label = "%s/%s" % (kind, slug)
    path = os.path.join(PAGES_DIR, kind, slug + ".html")
    if not os.path.isfile(path):
        problems.append("%s: chưa sinh trang" % label)
        return
    text = read_text(path)
    check_common(label, text, problems, warns)
    for marker in ('class="container layout"', 'class="sidebar rail"', 'class="content"'):
        if marker not in text:
            problems.append("%s: thiếu layout 2 cột (%s)" % (label, marker))
    # Đếm mục theo đúng cách cổng ảnh tách mục: số <h2> cộng vùng trước mục đầu tiên.
    # Nguồn có thể có ảnh nằm trước <h2> đầu (bảng tóm tắt), khi đó đếm <h2> thô sẽ lệch một mục.
    page_sections = image_gate.page_sections(entry)
    section_count = len(page_sections) if page_sections is not None else 0
    source = load_source_sections(kind, slug)
    if source is None:
        warns.append("%s: chưa có cache nguồn để đối chiếu số mục H2" % label)
    elif source["count"] != section_count:
        problems.append(
            "%s: số mục lệch nguồn (%d mục trong trang, %d mục nguồn)"
            % (label, section_count, source["count"])
        )
    for match in HEADING_RE.finditer(text):
        if english_heading(match.group(2)):
            problems.append("%s: heading chưa dịch: %s" % (label, norm_text(match.group(2))[:64]))
    found = X_RE.search(norm_text(text))
    if found:
        problems.append('%s: còn dùng "xN": %s' % (label, found.group(0).strip()))
    check_toc_summary(label, text, problems)


TOC_P_RE = re.compile(r"<h2\b[^>]*>\s*Mục lục\s*</h2>\s*<p>(.*?)</p>", re.I | re.S)
NUM_WORDS = {"một": 1, "hai": 2, "ba": 3, "bốn": 4, "nam": 5, "năm": 5, "sáu": 6,
             "bảy": 7, "tám": 8, "chín": 9, "mười": 10}
NUMBER = (r"(?:\d+|(?:mười\s+)?(?:một|hai|ba|bốn|năm|sáu|bảy|tám|chín))")
SUMMARY_HEADINGS = ("mẹo hoàn thành", "đồ thụ thập", "đồ thu thập", "danh sách kiểm")


def parse_vn_number(text):
    text = text.strip().lower()
    if text.isdigit():
        return int(text)
    parts = text.split()
    if len(parts) == 2 and parts[0] == "mười":
        return 10 + NUM_WORDS.get(parts[1], 0)
    return NUM_WORDS.get(text)


def check_toc_summary(label, text, problems):
    """Câu dẫn dưới <h2>Mục lục</h2> phải khai đúng số mục đi đường và số mục tổng kết.

    Vì sao: số đếm viết tay là thứ trôi ngay khi thêm/bớt một mục — đã sai hai lần ở T2
    ("chín mục đi đường" cho 8 mục, "bảy mục đi đường" cho 8 mục) mà không cổng nào bắt được.
    Đếm mục tổng kết theo heading cuối trang, rồi kiểm cả hai con số trong câu.
    """
    headings = [h for h, _ in shared.page_split(text) if h]
    match = TOC_P_RE.search(text)
    if not match:
        problems.append('%s: thiếu câu dẫn "<p>" ngay sau <h2>Mục lục</h2>' % label)
        return
    sentence = norm_text(match.group(1))
    found = {}
    for key, pattern in (
        ("content", r"(%s)\s+mục đi đường" % NUMBER),
        ("summary", r"(%s)\s+mục tổng kết" % NUMBER),
    ):
        hit = re.search(pattern, sentence, re.I)
        if not hit:
            problems.append(
                '%s: câu dẫn Mục lục phải nêu "… mục đi đường và … mục tổng kết" (đang: %s)'
                % (label, sentence[:90])
            )
            return
        found[key] = parse_vn_number(hit.group(1))
    summary = sum(1 for h in headings if h.strip().lower().startswith(SUMMARY_HEADINGS))
    content = len(headings) - 2 - summary
    if found["content"] != content or found["summary"] != summary:
        problems.append(
            "%s: câu dẫn Mục lục đếm sai (ghi %d mục đi đường + %d mục tổng kết, thật là %d + %d)"
            % (label, found["content"], found["summary"], content, summary)
        )


def load_source_sections(kind, slug):
    source = image_gate.load_sections(kind, slug)
    if source is None or "error" in source:
        return None
    return {"count": len(source["sections"]), "path": source.get("path", "")}


def check_hub(ctx, problems, warns):
    label = "progress-route.html"
    path = os.path.join(PAGES_DIR, label)
    if not os.path.isfile(path):
        problems.append("%s: chưa sinh trang" % label)
        return
    text = read_text(path)
    check_common(label, text, problems, warns)
    ids = re.findall(r'<section class="route-block" id="([^"]+)">', text)
    if ids != HUB_BLOCKS:
        problems.append("%s: 4 khối sai thứ tự hoặc thiếu (%s)" % (label, ", ".join(ids) or "không có"))
    regions = ctx["regions"]
    if len(regions) != 12:
        problems.append("regions.json: phải có 12 nhóm vùng (đang %d)" % len(regions))
    groups = re.findall(
        r'<h3 id="vung-(\d+)">(\d+)\. (.*?) <span class="region-count">(\d+) chương</span></h3>',
        text,
    )
    if len(groups) != len(regions):
        problems.append(
            "%s: cần %d nhóm vùng (đang %d)" % (label, len(regions), len(groups))
        )
    else:
        for (num, printed, title_html, _count), region in zip(groups, regions):
            title = html.unescape(title_html)
            if int(num) != region["index"] or int(printed) != region["index"]:
                problems.append("%s: nhóm vùng sai số thứ tự (%s, %s)" % (label, num, printed))
            if title != region["title"]:
                problems.append(
                    "%s: nhóm %d sai tên (%r ≠ %r)" % (label, region["index"], title, region["title"])
                )


def check_index(ctx, kind, key, problems, warns):
    path = os.path.join(PAGES_DIR, key)
    if not os.path.isfile(path):
        problems.append("%s: chưa sinh trang" % key)
        return
    text = read_text(path)
    check_common(key, text, problems, warns)
    items = len(re.findall(r'<li><a href="[^"]+"><span class="idx-num">', text))
    expected = len(ctx["by_type"][kind])
    if items != expected:
        problems.append(
            "%s: danh sách có %d mục, content/%s có %d trang" % (key, items, kind, expected)
        )
    if expected == 0 and 'class="empty"' not in text:
        problems.append("%s: chưa có trang %s nhưng thiếu thông báo trống" % (key, kind))


def main():
    build = load_module("build-pages.py", "build_pages")
    global image_gate, vn_gate
    image_gate = load_module("check-image-match.py", "check_image_match")
    vn_gate = load_module("check-vietnamese.py", "check_vietnamese")

    ctx = build.load_site(os.path.join(ROOT, "content"))
    if ctx["errors"]:
        for message in ctx["errors"]:
            print("LỖI: " + message)
        return 1

    problems, warns = [], []
    check_hub(ctx, problems, warns)
    for kind, key in build.INDEX_KEYS.items():
        check_index(ctx, kind, key, problems, warns)
    for entry in ctx["entries"]:
        check_content_page(entry, problems, warns)

    for message in problems:
        print("[FAIL] " + message)
    for message in warns:
        print("[warn] " + message)
    if not problems and not warns:
        print("[ok  ] không có lỗi cấu trúc")
    print("-" * 64)
    print(
        "HARD=%d WARN=%d -> %s"
        % (len(problems), len(warns), "PASS" if not problems else "FAIL")
    )
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
