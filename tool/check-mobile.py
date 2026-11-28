#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cổng hiển thị: trang không được tràn ngang ở bề rộng điện thoại và máy tính bảng.

Vì sao có cổng này: T1 đã PASS cả 5 cổng cũ mà trang vẫn tràn ngang trên điện thoại
(một rule CSS đặt `table{min-width:520px}` làm bảng rộng 520px trong khung 375px).
Không cổng nào render trang nên không ai thấy. Cổng này render thật bằng Chrome headless
và so `document.scrollWidth` với `clientWidth`.

Cách chạy: python tool/check-mobile.py [--width 375] [--width 768] [trang.html ...]
  không truyền file -> đo hub, hai trang chỉ mục và mọi trang nội dung trong content/
Thoát mã 1 nếu có trang tràn ngang. Thiếu Chrome/Node -> in "chưa chạy được", exit 0.
"""
from __future__ import annotations

import importlib.util
import json
import os
import shutil
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(ROOT, "pages")
TOLERANCE = 1  # px: làm tròn của trình duyệt


def load_build_module():
    path = os.path.join(ROOT, "tool", "build-pages.py")
    spec = importlib.util.spec_from_file_location("build_pages", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def collect_pages(ctx, build):
    files = [os.path.join(PAGES_DIR, build.HUB_KEY)]
    for key in build.INDEX_KEYS.values():
        files.append(os.path.join(PAGES_DIR, key))
    for entry in ctx["entries"]:
        files.append(os.path.join(PAGES_DIR, entry["type"], entry["slug"] + ".html"))
    root_index = os.path.join(ROOT, "index.html")
    if os.path.isfile(root_index):
        files.append(root_index)
    return [f for f in files if os.path.isfile(f)]


def run_probe(files, widths):
    node = shutil.which("node")
    if not node:
        return None, "không có node trong PATH"
    probe = os.path.join(ROOT, "tool", "mobile-probe.mjs")
    results = []
    for width in widths:
        cmd = [node, probe, "--width", str(width), "--height", "900"] + files
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=600)
        out = (proc.stdout or "").strip()
        if not out:
            return None, "probe không in gì (stderr: %s)" % (proc.stderr or "")[:200]
        data = json.loads(out)
        if isinstance(data, dict) and data.get("error"):
            return None, data["error"]
        results.extend(data)
    return results, None


def main(argv):
    widths = [375, 768]
    args = [a for a in argv if not a.startswith("--")]
    i = 0
    while i < len(argv):
        if argv[i] == "--width" and i + 1 < len(argv):
            widths = [int(argv[i + 1])]
        i += 1

    if args:
        files = [os.path.abspath(a) for a in args]
    else:
        build = load_build_module()
        ctx = build.load_site(os.path.join(ROOT, "content"))
        if ctx["errors"]:
            for message in ctx["errors"]:
                print("LỖI: " + message)
            return 1
        files = collect_pages(ctx, build)

    results, error = run_probe(files, widths)
    if results is None:
        print("CHƯA CHẠY ĐƯỢC cổng hiển thị: %s" % error)
        print("-> không coi là PASS; cần Chrome (hoặc Edge) + node trên máy chạy cổng.")
        return 0

    failures = 0
    for item in results:
        label = os.path.relpath(item["file"], ROOT).replace("\\", "/")
        if "error" in item:
            print("%-52s %dpx  LỖI: %s" % (label[:52], item.get("width", 0), item["error"]))
            failures += 1
            continue
        over = item["scrollWidth"] - item["clientWidth"]
        if over > TOLERANCE:
            print("%-52s %dpx  FAIL tràn %dpx %s"
                  % (label[:52], item["width"], over, item.get("wide") or ""))
            failures += 1
        else:
            print("%-52s %dpx  ok" % (label[:52], item["width"]))

    print("-" * 70)
    print("Đo %d lượt | FAIL=%d -> %s" % (len(results), failures, "PASS" if not failures else "FAIL"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
