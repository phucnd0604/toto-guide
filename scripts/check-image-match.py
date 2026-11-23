#!/usr/bin/env python3
"""Cổng cứng: ảnh phải nằm đúng chỗ và đúng thứ tự so với trang nguồn fextralife.

verify-regions.py chỉ đếm ảnh (img=uni, ms=0) nên KHÔNG bắt được lỗi ảnh nằm sai mục
hoặc lẫn ảnh vùng khác. Script này đối chiếu trực tiếp với nguồn:

  1. Mỗi ảnh dùng trong pages/route-<slug>.html phải có trong chính trang nguồn của vùng
     (không lẫn vùng khác, không tự chế).
  2. Thứ tự ảnh trong trang phải là dãy con đúng thứ tự của nguồn (không đảo).
  3. Ảnh phải nằm dưới <h3> đúng subsection nguồn — gộp nhiều subsection vào một h3 là FAIL,
     vì ảnh hang/nhà sẽ hiện dưới tiêu đề đền thờ.

Dùng: python scripts/check-image-match.py [slug ...] [--refresh]
Thoát mã 1 nếu có FAIL.
"""
import os
import re
import sys
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROXY = ("https://zeldatearsofthekingdom-wiki-fextralife-com.translate.goog/"
         "{}?_x_tr_sl=en&_x_tr_tl=vi&_x_tr_hl=en")
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/131.0 Safari/537.36"}

# slug -> trang nguồn (Subcontent) chứa walkthrough của vùng
SOURCES = {
    "prologue": ["Subcontent:Walkthrough_1_Prologue", "Subcontent:Walkthrough_2_Great_Sky_Island"],
    "central": ["Subcontent:Walkthrough_3_Central_Hyrule_Region_Part_I"],
    "hebra": ["Subcontent:Walkthrough_4_Hebra_Region"],
    "eldin": ["Subcontent:Walkthrough_5_Eldin_Region"],
    "lanayru": ["Subcontent:Walkthrough_6_Lanayru_Region"],
    # vùng 6-9: bổ sung trang nguồn khi có ảnh
}

STOP = {"the", "of", "and", "to", "a", "in", "for"}
IMG_RE = re.compile(r'<img[^>]+src="([^"]+)"')
HEAD_RE = re.compile(r"<h([23])[^>]*>([\s\S]*?)</h\1>")


def norm_img(url):
    name = urllib.parse.unquote(url.split("/")[-1])
    return re.sub(r"^\d+px-", "", name).lower()


def english(text):
    return re.sub(r"\([^)]*\)", " ", re.sub(r"<[^>]+>", " ", text))


def toks(text):
    words = re.sub(r"[^a-z0-9 ]", " ", english(text).lower()).split()
    return {w for w in words if w and w not in STOP}


def heading_matches(ours, source):
    a, b = toks(ours), toks(source)
    if not a or not b:
        return False
    return len(a & b) / min(len(a), len(b)) >= 0.6


def wiki_body(html):
    i = html.find("mw-parser-output")
    body = html[i:] if i >= 0 else html
    cut = re.search(r"Popular Wikis|Follow us on socials", body)
    return body[:cut.start()] if cut else body


def walk(text, own):
    """Trả [(heading, [tên ảnh...]), ...] theo đúng thứ tự tài liệu."""
    groups, heading, hits = [], "(trước h3 đầu)", []
    events = [(m.start(), "h", m) for m in HEAD_RE.finditer(text)]
    events += [(m.start(), "i", m) for m in IMG_RE.finditer(text)]
    for _, kind, m in sorted(events, key=lambda e: e[0]):
        if kind == "h":
            if hits:
                groups.append((heading, hits))
            heading, hits = re.sub(r"<[^>]+>", "", m.group(2)).strip(), []
        else:
            src = m.group(1)
            if (own and "../images/" in src) or (not own and "static0.fextralifeimages" in src):
                hits.append(norm_img(src))
    if hits:
        groups.append((heading, hits))
    return groups


def fetch(page, refresh):
    cache = os.path.join(ROOT, ".tmp-src", re.sub(r"[^A-Za-z0-9]+", "_", page) + ".html")
    if not refresh and os.path.exists(cache) and os.path.getsize(cache) > 20000:
        return open(cache, encoding="utf-8", errors="replace").read()
    req = urllib.request.Request(PROXY.format(urllib.parse.quote(page, safe=":+_")), headers=UA)
    html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
    os.makedirs(os.path.dirname(cache), exist_ok=True)
    open(cache, "w", encoding="utf-8").write(html)
    return html


def check(slug, refresh):
    ours = walk(open(os.path.join(ROOT, "pages", "route-%s.html" % slug), encoding="utf-8").read().split("<main", 1)[-1], True)
    source = []
    for page in SOURCES[slug]:
        source += walk(wiki_body(fetch(page, refresh)), False)

    group_of, order = {}, {}
    for gi, (heading, imgs) in enumerate(source):
        for name in imgs:
            group_of.setdefault(name, (gi, heading))
            order.setdefault(name, gi * 1000 + len(order))

    fails, last, ours_count = [], -1, 0
    for heading, imgs in ours:
        for name in imgs:
            ours_count += 1
            if "/" in name or not name:
                fails.append("%s: src ảnh lạ %r" % (heading[:30], name))
                continue
            if name not in group_of:
                fails.append("%s: ảnh %s KHÔNG có trong nguồn vùng (lẫn vùng?)" % (heading[:30], name))
                continue
            if order[name] < last:
                fails.append("%s: ảnh %s bị đảo thứ tự so với nguồn" % (heading[:30], name))
            last = max(last, order[name])
            if not heading_matches(heading, group_of[name][1]):
                fails.append('%s: ảnh %s thuộc mục nguồn "%s"'
                             % (heading[:30], name, group_of[name][1][:45]))
    status = "PASS" if not fails else "FAIL"
    print("%-11s %-5s ảnh dùng=%-3d ảnh nguồn=%-3d lỗi=%d" % (slug, status, ours_count, len(order), len(fails)))
    for f in fails[:12]:
        print("    - " + f)
    if len(fails) > 12:
        print("    ... còn %d lỗi" % (len(fails) - 12))
    return fails


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    refresh = "--refresh" in sys.argv
    slugs = args or list(SOURCES)
    bad = 0
    for slug in slugs:
        if slug not in SOURCES:
            print("bỏ qua %s: chưa khai báo trang nguồn trong SOURCES" % slug)
            continue
        bad += 1 if check(slug, refresh) else 0
    print("-" * 70)
    print("FAIL=%d" % bad)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
