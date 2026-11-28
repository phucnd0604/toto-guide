#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tải toàn bộ ảnh của một chương nguồn vào images/<loại>/<slug>/.

Vì sao có file này: mỗi chương cần 80–270 ảnh, và việc tải tay đã bị viết lại từ đầu ở cả
T3 lẫn T4 (một lần còn viết sai cú pháp). Ở đây gói đúng ba quy ước của cổng ảnh:

  1. chỉ tải ảnh nằm trong bài (phần <article>) của trang nguồn, bỏ logo/banner/quảng cáo;
  2. tên file giữ nguyên gốc, chỉ bỏ hậu tố kích thước -1024x576 (cổng so tên đã chuẩn hoá);
  3. ảnh lặp trong nguồn chỉ tải một lần — cổng ảnh cấm dùng trùng, nên folder ít file hơn
     số lượt ảnh của nguồn (T4: 272 lượt nhưng 268 file).

Dùng:
  python tool/fetch-images.py <slug>                    # tải vào images/walkthrough/<slug>/
  python tool/fetch-images.py --type temples <slug>
  python tool/fetch-images.py --from .scratch/src.html <slug>
  python tool/fetch-images.py --dry-run <slug>          # chỉ in kế hoạch, không tải

Cache nguồn do cổng ảnh tạo: python tool/check-image-match.py --refresh <slug>
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import time
import urllib.error
import urllib.request

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tool"))
import source_sections as shared  # noqa: E402

UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/131.0 Safari/537.36"
    )
}
SITE = "https://zeldacentral.com"
PAUSE = 0.3


def plan_from(text):
    """[(tên file chuẩn hoá, URL gốc)] theo thứ tự tài liệu, mỗi tên giữ lần xuất hiện đầu."""
    body = shared.article_html(text)
    seen = {}
    order = []
    for match in shared.IMG_TAG_RE.finditer(body):
        src = shared.SRC_RE.search(match.group(0))
        if not src or "/uploads/" not in src.group(1):
            continue
        url = src.group(1)
        if not url.startswith("http"):
            url = SITE + url
        name = shared.norm_name(url)
        if name in seen:
            continue
        seen[name] = url
        order.append(name)
    return [(name, seen[name]) for name in order]


def looks_like_chapter(text):
    """Trang chặn vài chục KB thì không có <h2> và ảnh nguồn — đừng tải ảnh từ đó."""
    return bool(re.search(r"<h2\b", text or "", re.I)) and "/uploads/" in (text or "")


def download(url, dest):
    """Thử bản 1024 -> bản gốc -> bản 1280; trả về thông báo lỗi cuối cùng nếu hỏng hết."""
    last = ""
    for target in (url, url.replace("-1024x576", ""), url.replace("-1024x576", "-1280x720")):
        try:
            request = urllib.request.Request(target, headers=UA)
            data = urllib.request.urlopen(request, timeout=90).read()
        except (urllib.error.URLError, ValueError, OSError) as exc:
            last = "%s: %s" % (target, exc)
            time.sleep(PAUSE)
            continue
        if not data:
            last = "%s: rỗng" % target
            continue
        with open(dest, "wb") as fh:
            fh.write(data)
        return None
    return last


def main(argv):
    parser = argparse.ArgumentParser(description="Tải ảnh của một chương nguồn")
    parser.add_argument("slug")
    parser.add_argument("--type", default="walkthrough", choices=shared.PAGE_TYPES)
    parser.add_argument("--from", dest="source_file", help="đọc file nguồn này thay vì cache .tmp-src")
    parser.add_argument("--dry-run", action="store_true", help="chỉ in kế hoạch, không tải")
    args = parser.parse_args(argv)

    if args.source_file:
        path = args.source_file
        if not os.path.isabs(path):
            path = os.path.join(ROOT, path)
    else:
        path = shared.cache_path(ROOT, args.type, args.slug)
    if not path or not os.path.exists(path):
        print(
            "CHƯA CÓ NGUỒN cho %s/%s — chạy: python tool/check-image-match.py --refresh %s"
            % (args.type, args.slug, args.slug)
        )
        return 1

    text = shared.read_text(path)
    if not looks_like_chapter(text):
        print(
            "NGUỒN KHÔNG GIỐNG TRANG CHƯƠNG (%d ký tự) — có thể bị chặn; "
            "chạy lại: python tool/check-image-match.py --refresh %s" % (len(text), args.slug)
        )
        return 1

    plan = plan_from(text)
    folder = os.path.join(ROOT, "images", args.type, args.slug)
    print("KẾ HOẠCH %s/%s: %d ảnh duy nhất -> images/%s/%s/" % (args.type, args.slug, len(plan), args.type, args.slug))
    if args.dry_run:
        for name, url in plan:
            print("  %s  <-  %s" % (name, url))
        return 0

    os.makedirs(folder, exist_ok=True)
    fetched = skipped = 0
    failures = []
    for index, (name, url) in enumerate(plan, 1):
        dest = os.path.join(folder, name)
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            skipped += 1
            continue
        error = download(url, dest)
        if error:
            failures.append((name, error))
            print("  LỖI %s" % name)
            continue
        fetched += 1
        if index % 25 == 0:
            print("  ... %d/%d (mới %d, bỏ qua %d)" % (index, len(plan), fetched, skipped))

    print(
        "XONG %s/%s: tải %d, bỏ qua %d, lỗi %d, tổng %d"
        % (args.type, args.slug, fetched, skipped, len(failures), len(plan))
    )
    for name, error in failures[:20]:
        print("  %s -> %s" % (name, error))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
