#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng server tĩnh để xem/đo trang local (trình duyệt chặn file://).

Vì sao có script này: Playwright (và nhiều công cụ đo) chặn giao thức file:, nên muốn
soi trang ở bề rộng điện thoại phải phục vụ qua http. Chạy script này rồi mở URL in ra.

Dùng: python tool/preview.py [--port 8765] [--open]
  --port  cổng (mặc định 8765; tự nhảy cổng nếu bận)
  --open  mở trình duyệt tới trang hub
Dừng: Ctrl+C.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import socketserver
import sys
import threading
import webbrowser

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HUB = "pages/progress-route.html"


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):  # giữ output gọn
        pass


def main():
    parser = argparse.ArgumentParser(description="Server tĩnh để xem trang local")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--open", action="store_true", help="mở trình duyệt")
    args = parser.parse_args()

    handler = functools.partial(QuietHandler, directory=ROOT)
    port = args.port
    for _ in range(20):
        try:
            httpd = socketserver.TCPServer(("127.0.0.1", port), handler)
            break
        except OSError:
            port += 1
    else:
        print("Không mở được cổng nào từ %d." % args.port)
        return 1

    url = "http://127.0.0.1:%d/%s" % (port, HUB)
    print("Server tĩnh: http://127.0.0.1:%d/  (gốc repo)" % port)
    print("Hub:         %s" % url)
    print("Ví dụ đo:    node tool/mobile-probe.mjs --width 375 pages/walkthrough/<slug>.html")
    print("Dừng: Ctrl+C")
    if args.open:
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nĐã dừng.")
    finally:
        httpd.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
