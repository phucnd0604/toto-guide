#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chụp ảnh một trang để tự review (desktop + 375px), không cần Playwright.

Vì sao có file này: quy trình dự án bắt buộc "tự đọc lại trang trên cả desktop và 375px",
nhưng trước đây không có công cụ nào làm việc đó. Cách cũ hay hỏng: CLI của Chrome bị ép
bề rộng tối thiểu (ảnh trông như tràn ngang dù trang không tràn), ảnh lazy không tải nên
gallery ra trắng, và không cắt được vùng giữa trang. Ở T2 vòng thử-sai đó tốn ~11 phút.
Cái này chạy qua CDP với device metrics thật, giống hệt cổng mobile.

Dùng:
  python tool/shot.py lookout-landing                          # 375px, toàn trang
  python tool/shot.py --width 1280 --width 375 hyrule-field     # nhiều bề rộng
  python tool/shot.py --viewport --height 1400 hyrule-castle-town
  python tool/shot.py --anchor "#do-thu-thap-trong-chuong" lookout-landing

Ảnh ghi vào .scratch/shots/ (đã gitignore). In ra đường dẫn từng ảnh.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import shutil
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(ROOT, "pages")
DEFAULT_OUT = os.path.join(ROOT, ".scratch", "shots")


def resolve_targets(args):
    """Slug -> pages/**/<slug>.html; đường dẫn .html giữ nguyên."""
    out = []
    for arg in args:
        if arg.lower().endswith((".html", ".htm")):
            out.append(arg if os.path.isabs(arg) else os.path.join(ROOT, arg))
            continue
        hits = glob.glob(os.path.join(PAGES_DIR, "**", arg + ".html"), recursive=True)
        if not hits:
            print("bỏ qua %r: không có trang nào tên đó trong pages/" % arg)
            continue
        out.extend(sorted(hits))
    return out


def main(argv):
    parser = argparse.ArgumentParser(description="Chụp ảnh trang qua Chrome CDP")
    parser.add_argument("targets", nargs="+", help="slug hoặc đường dẫn .html")
    parser.add_argument("--width", action="append", default=None,
                        help="bề rộng CSS px (lặp lại được; mặc định 375)")
    parser.add_argument("--height", type=int, default=900, help="cao khung nhìn (mặc định 900)")
    parser.add_argument("--viewport", action="store_true", help="chỉ chụp khung nhìn, không chụp cả trang")
    parser.add_argument("--out", default=DEFAULT_OUT, help="thư mục ghi ảnh (mặc định .scratch/shots)")
    parser.add_argument("--anchor", help="cuộn tới mốc này trước khi chụp, ví dụ '#meo-hoan-thanh'")
    parser.add_argument("--no-eager", action="store_true", help="không ép ảnh lazy tải trước khi chụp")
    args = parser.parse_args(argv)

    node = shutil.which("node")
    if not node:
        print("CHƯA CHẠY ĐƯỢC: không có node trong PATH")
        return 1
    files = resolve_targets(args.targets)
    if not files:
        return 1
    widths = args.width or ["375"]
    probe = os.path.join(ROOT, "tool", "mobile-probe.mjs")
    out_dir = args.out if os.path.isabs(args.out) else os.path.join(ROOT, args.out)

    shots = []
    for width in widths:
        cmd = [node, probe, "--width", str(width), "--height", str(args.height), "--shot", out_dir]
        if not args.viewport:
            cmd.append("--full")
        if not args.no_eager:
            cmd.append("--eager")
        if args.anchor:
            cmd += ["--anchor", args.anchor]
        cmd += files
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=900)
        raw = (proc.stdout or "").strip()
        if not raw:
            print("CHƯA CHẠY ĐƯỢC: probe không in gì (stderr: %s)" % (proc.stderr or "")[:200])
            return 1
        try:
            data = json.loads(raw)
        except ValueError:
            print("probe trả về không phải JSON: %s" % raw[:200])
            return 1
        if isinstance(data, dict) and data.get("error"):
            print("CHƯA CHẠY ĐƯỢC: %s" % data["error"])
            return 1
        for item in data:
            if "error" in item:
                print("FAIL %s (%dpx): %s" % (item.get("file"), width, item["error"]))
                continue
            over = item["scrollWidth"] - item["clientWidth"]
            flag = "" if over <= 1 else "  [tràn %dpx: %s]" % (over, ",".join(item.get("wide") or []))
            print("%-46s %dpx  %s%s" % (os.path.relpath(item["file"], ROOT).replace("\\", "/"),
                                        int(width), item.get("shot", ""), flag))
            if item.get("shot"):
                shots.append(item["shot"])
    if shots:
        print("-" * 70)
        print("%d ảnh -> %s" % (len(shots), os.path.relpath(out_dir, ROOT).replace("\\", "/")))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
