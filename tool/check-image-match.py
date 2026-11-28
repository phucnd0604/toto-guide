#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cổng cứng: ảnh phải đúng trang, đúng folder, đúng thứ tự và đúng mục H2 so với nguồn.

Bốn điều kiện, vi phạm một điều là FAIL:
  1. Mỗi ảnh dùng trong pages/<loại>/<slug>.html phải nằm trong images/<loại>/<slug>/ của chính trang đó.
  2. Mọi file trong folder ảnh của trang đều được dùng; không thiếu file, không dùng trùng.
  3. Dãy ảnh trong trang là dãy con đúng thứ tự xuất hiện ở nguồn.
  4. Ảnh nằm dưới đúng mục H2 như nguồn. Đối chiếu theo THỨ TỰ mục chứ không theo chữ,
     vì heading đã dịch sang tiếng Việt.

Nguồn đối chiếu lấy từ cache cục bộ (gitignore):
  .tmp-src/<loại>/<slug>.json   {"sections": [{"heading": "...", "images": ["a.webp"]}]}
  .tmp-src/<loại>/<slug>.html   trang nguồn thô, tự tách mục theo <h2>
  --refresh                     tải lại trang nguồn (URL trong metadata) rồi ghi cache .html

Dùng: python tool/check-image-match.py [--refresh] [--refresh-missing] [--type LOẠI] [slug ...]
  --refresh          tải lại toàn bộ trang nguồn
  --refresh-missing  chỉ tải trang nguồn chưa có trong cache (dùng cho CI có cache)
Thoát mã 1 nếu có FAIL.
"""
from __future__ import annotations

import importlib.util
import json
import os
import posixpath
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(ROOT, "pages")
CACHE_DIR = os.path.join(ROOT, ".tmp-src")
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/131.0 Safari/537.36"
    )
}
H2_RE = re.compile(r"<h2\b[^>]*>(.*?)</h2>", re.I | re.S)
IMG_RE = re.compile(r"""<img\b[^>]*?\bsrc\s*=\s*["']([^"']+)["']""", re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")


def load_build_module():
    path = os.path.join(ROOT, "tool", "build-pages.py")
    spec = importlib.util.spec_from_file_location("build_pages", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_text(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def norm_text(fragment):
    return re.sub(r"\s+", " ", TAG_RE.sub(" ", fragment)).strip()


def norm_name(value):
    name = urllib.parse.unquote(value.split("?")[0].split("#")[0].split("/")[-1])
    name = re.sub(r"^\d+px-", "", name, flags=re.I)
    name = re.sub(r"-\d+x\d+(?=\.[A-Za-z0-9]+$)", "", name)
    return name.lower()


def article_html(text):
    for tag in ("article", "main"):
        match = re.search(
            r"<%s\b[^>]*>(.*?)</%s>" % (tag, tag), text, re.I | re.S
        )
        if match:
            return match.group(1)
    match = re.search(r"<body\b[^>]*>(.*?)</body>", text, re.I | re.S)
    return match.group(1) if match else text


def parse_sections(text, keep):
    """Tách trang thành các mục H2 theo thứ tự tài liệu; keep(src) quyết định ảnh nào được tính."""
    body = article_html(text)
    events = []
    for match in H2_RE.finditer(body):
        events.append((match.start(), "h", norm_text(match.group(1))))
    for match in IMG_RE.finditer(body):
        src = match.group(1)
        if keep(src):
            events.append((match.start(), "i", src))
    events.sort(key=lambda item: item[0])
    sections = []
    for _, kind, value in events:
        if kind == "h":
            sections.append([value, []])
        else:
            if not sections:
                sections.append(["(trước mục đầu)", []])
            sections[-1][1].append(value)
    return sections


def load_sections(kind, slug):
    base = os.path.join(CACHE_DIR, kind, slug)
    if os.path.exists(base + ".json"):
        try:
            data = json.loads(read_text(base + ".json"))
        except ValueError:
            return {"error": "cache JSON lỗi: %s" % (kind + "/" + slug + ".json")}
        sections = []
        for item in data.get("sections", []):
            sections.append(
                [item.get("heading", ""), [norm_name(x) for x in item.get("images", [])]]
            )
        return {"sections": sections, "path": base + ".json"}
    if os.path.exists(base + ".html"):
        text = read_text(base + ".html")
        sections = parse_sections(text, lambda src: "/uploads/" in src)
        return {
            "sections": [[heading, [norm_name(x) for x in images]] for heading, images in sections],
            "path": base + ".html",
        }
    return None


def proxy_url(url):
    parts = urllib.parse.urlsplit(url)
    host = parts.hostname.replace(".", "-") + ".translate.goog"
    query = parts.query + "&" if parts.query else ""
    query += "_x_tr_sl=en&_x_tr_tl=vi&_x_tr_hl=en"
    return urllib.parse.urlunsplit(("https", host, parts.path, query, ""))


def refresh_cache(kind, slug, url):
    errors = []
    for target in (url, proxy_url(url)):
        try:
            request = urllib.request.Request(target, headers=UA)
            data = urllib.request.urlopen(request, timeout=90).read().decode("utf-8", "replace")
        except (urllib.error.URLError, ValueError, OSError) as exc:
            errors.append("%s: %s" % (target, exc))
            continue
        folder = os.path.join(CACHE_DIR, kind)
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, slug + ".html")
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(data)
        print("  đã cache nguồn %s/%s (%d ký tự)" % (kind, slug, len(data)))
        return True
    print("  KHÔNG tải được nguồn %s/%s:" % (kind, slug))
    for message in errors:
        print("    " + message)
    return False


def page_sections(entry):
    kind, slug = entry["type"], entry["slug"]
    path = os.path.join(PAGES_DIR, kind, slug + ".html")
    if not os.path.isfile(path):
        return None
    text = read_text(path)
    return parse_sections(text, lambda src: "/images/" in src)


def check(entry, refresh, refresh_missing=False):
    kind, slug = entry["type"], entry["slug"]
    source_url = entry["meta"].get("source", "")
    cached = os.path.exists(os.path.join(CACHE_DIR, kind, slug + ".html")) or os.path.exists(
        os.path.join(CACHE_DIR, kind, slug + ".json")
    )
    if source_url and (refresh or (refresh_missing and not cached)):
        refresh_cache(kind, slug, source_url)
    sections = page_sections(entry)
    if sections is None:
        return ["%s/%s: chưa sinh trang" % (kind, slug)]
    fails = []
    folder = os.path.join(ROOT, "images", kind, slug)
    files = sorted(f.lower() for f in os.listdir(folder)) if os.path.isdir(folder) else []
    prefix = "images/%s/%s/" % (kind, slug)

    used, seen = [], set()
    for index, (heading, images) in enumerate(sections):
        for raw in images:
            name = norm_name(raw)
            used.append((index, heading, raw, name))
            resolved = posixpath.normpath(
                posixpath.join("pages", kind, urllib.parse.unquote(raw.split("?")[0]))
            )
            if not resolved.startswith(prefix):
                fails.append("%s: ảnh lẫn trang/không đúng folder: %s" % (heading[:32], raw))
            if name in seen:
                fails.append("%s: ảnh dùng trùng: %s" % (heading[:32], name))
            seen.add(name)

    for _, heading, _, name in used:
        if name not in files:
            fails.append("%s: thiếu file images/%s/%s/%s" % (heading[:32], kind, slug, name))
    for name in files:
        if name not in seen:
            fails.append("%s: file không được dùng: %s" % (kind + "/" + slug, name))

    if used:
        source = load_sections(kind, slug)
        if source is None:
            fails.append(
                "%s: chưa có cache nguồn (.tmp-src/%s/%s.html) — chạy --refresh" % (kind + "/" + slug, kind, slug)
            )
        elif "error" in source:
            fails.append(source["error"])
        else:
            source_sections = source["sections"]
            if len(source_sections) != len(sections):
                fails.append(
                    "%s: số mục H2 lệch nguồn (%d mục trong trang, %d mục nguồn)"
                    % (kind + "/" + slug, len(sections), len(source_sections))
                )
            positions = {}
            counter = 0
            for section_index, (heading, images) in enumerate(source_sections):
                for name in images:
                    if name not in positions:
                        positions[name] = (section_index, counter)
                    counter += 1
            last = -1
            for section_index, heading, _, name in used:
                if name not in positions:
                    fails.append(
                        "%s: ảnh %s không có trong nguồn (lẫn trang?)" % (heading[:32], name)
                    )
                    continue
                source_index, order = positions[name]
                if source_index != section_index:
                    source_heading = source_sections[source_index][0]
                    fails.append(
                        '%s: ảnh %s thuộc mục nguồn "%s"'
                        % (heading[:32], name, source_heading[:48])
                    )
                if order < last:
                    fails.append("%s: ảnh %s bị đảo thứ tự so với nguồn" % (heading[:32], name))
                last = max(last, order)
    return fails


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    refresh = "--refresh" in sys.argv
    refresh_missing = "--refresh-missing" in sys.argv
    type_filter = None
    if "--type" in sys.argv:
        index = sys.argv.index("--type")
        if index + 1 < len(sys.argv):
            type_filter = sys.argv[index + 1]
            if type_filter in args:
                args.remove(type_filter)

    build = load_build_module()
    ctx = build.load_site(os.path.join(ROOT, "content"))
    if ctx["errors"]:
        for message in ctx["errors"]:
            print("LỖI: " + message)
        return 1

    entries = [e for e in ctx["entries"] if not type_filter or e["type"] == type_filter]
    if args:
        wanted = set(args)
        entries = [e for e in entries if e["slug"] in wanted]
        known = {e["slug"] for e in ctx["entries"]}
        for slug in sorted(wanted - known):
            print("bỏ qua %r: không có trong content/" % slug)

    failures = 0
    for entry in entries:
        fails = check(entry, refresh, refresh_missing)
        label = "%s/%s" % (entry["type"], entry["slug"])
        print("%-34s %s" % (label, "PASS" if not fails else "FAIL (%d lỗi)" % len(fails)))
        for message in fails[:12]:
            print("    - " + message)
        if len(fails) > 12:
            print("    ... còn %d lỗi" % (len(fails) - 12))
        failures += 1 if fails else 0

    known = {(e["type"], e["slug"]) for e in ctx["entries"]}
    for kind in build.PAGE_TYPES:
        folder = os.path.join(ROOT, "images", kind)
        if not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder)):
            if os.path.isdir(os.path.join(folder, name)) and (kind, name) not in known:
                print("FAIL: images/%s/%s/ không có trang tương ứng trong content/" % (kind, name))
                failures += 1

    print("-" * 70)
    print("Trang kiểm=%d | FAIL=%d -> %s" % (len(entries), failures, "PASS" if not failures else "FAIL"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
