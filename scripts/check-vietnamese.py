# -*- coding: utf-8 -*-
"""Quét nội dung HTML để phát hiện câu chưa dịch / Vietglish.

Dùng:  python scripts/check-vietnamese.py [-v]
Mã thoát: 0 = không còn lỗi HARD, 1 = còn lỗi HARD.

HARD = heading còn tiếng Anh | cụm Vietglish trong blacklist | mẫu "x1"/"5x"
WARN = cụm tiếng Anh lạ trong câu (tên món/quái chưa dịch) -> xem lại tay
"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = [os.path.join(ROOT, 'index.html')] + sorted(glob.glob(os.path.join(ROOT, 'pages', '*.html')))

# Từ được phép giữ nguyên: tên riêng, địa danh, nhãn trong game, thương hiệu nguồn.
KEEP = set("""
link zelda rauru sonia ganondorf purah robbie josha impa tulin teba saki harth yunobo sidon riju mineru
hyrule hebra eldin lanayru gerudo necluda akkala faron hylian rito goron zora zorana hateno kakariko
shrine temple stable tower skyview zonai depths gloom lightroot korok bubbul rupee rupees
paraglider ultrahand fuse ascend recall autobuild vow sage boss construct
hinox bokoblin moblin lizalfos lynel keese chuchu talus molduga gleeok colgera moragia gohma gibdo
sword bow shield spear arrow arrows elixir opal amber ruby flint sapphire diamond topaz luminous
brow pass summit cave chasm bridge lake field forest mountain village town landing lookout
master app camera game progress route index part guide wiki fextralife totk botw dlc npc hud faq
ign nintendo life central polygon gamespot fandom reddit youtube switch joycon joy-con stick
soldier steward pebblit chuchu horriblin hinox gleeok zonai zonai
""".split())

# Cụm tên riêng / thương hiệu: bỏ khỏi text trước khi quét (không phải nội dung cần dịch).
PHRASES = [
    "the legend of zelda tears of the kingdom", "tears of the kingdom", "temple of time",
    "great sky island", "hyrule castle", "rito village", "goron city", "zora's domain",
    "gerudo town", "lookout landing", "death mountain", "korok forest", "lost woods",
    "hyrule field", "hyrule ridge", "eventide island", "hateno village", "kakariko village",
    "lurelin village", "tarrey town", "gerudo desert", "hebra mountains", "deep akkala",
    "eldin canyon", "lanayru great spring", "satori mountain", "great plateau", "thyphlo ruins",
    "akkala citadel", "necluda sea", "fextralife dungeon wiki", "ign walkthrough",
    "nintendo life", "zelda central", "game progress route", "master sword",
    "camera work in the depths", "regional phenomena", "tulin of rito village",
    "yunobo of goron city", "sidon of the zora", "riju of gerudo town", "mineru's counsel",
    "a mystery in the depths", "serenade to a great fairy", "misko's treasure",
    "molli the fletcher", "potential princess sightings", "froggy armor set",
    "zelda's golden horse", "to the kingdom of hyrule", "crisis at hyrule castle",
    "dragon's tears", "the dragon's tears", "sky islands", "depths tips",
    "find princess zelda", "the closed door", "the demon king", "the fifth sage",
    "bring peace to hyrule field", "impa and the geoglyphs", "first gatehouse",
    "new serenne stable", "new serenne", "hebra south summit cave", "hebra south summit",
    "hebra summit cave", "eye of the storm", "south summit",
    "south akkala stable", "south akkala", "death mountain west site", "big wheel", "little frox",
    "the sludge-covered statue", "the broken slate", "restoring the zora armor", "clues to the sky",
    "old map", "east reservoir lake", "east akkala plains", "east akkala chasm", "east akkala",
    # dòng ghi nguồn ảnh / bản quyền: giữ nguyên tên nhà cung cấp
    "zelda dungeon wiki", "dungeon wiki", "wikimedia commons", "cc by", "polygon",
    "gamespot", "the guardian", "ign", "nintendo life",
]

# Từ tiếng Anh thông dụng: nếu còn trong câu tiếng Việt => chưa dịch.
COMMON_EN = set("""
the a an of to in on at with from by for and or but is are was were be been being
will would can could should must may might you your yours we our they them their it its
this that these those there here then than when while after before once if so as not no
all any some each every both more most less very just also only still again now
up down out over through into onto off back away about above below across along around
need needs needed use uses used using get gets got take takes took make makes made
go goes going come comes came look looks find finds found keep keeps put puts place places
reach reaches clear clears complete complete activate activates activated
locate locates talk talks speak follow follows head heads climb climbs jump jumps drop drops
cross crosses enter enters exit exits open opens close closes destroy destroys defeat defeats
fight fights kill kills grab grabs pick picks collect collects gather gathers search searches
explore explores return returns proceed proceeds access accesses spot spots budget budgets
deal deals stock stocks nearby raw materials simple easy way ways thing things
first second next last main objective step steps area areas section sections dungeon dungeons
puzzle puzzles level levels note notes tip tips good bad new old high low long short big small
left right north south east west day days night time times hour hours minute minutes
until during within without between among against toward towards behind front under
same other another such own few many much little lot lots basically pretty advanced
opinion different stats stat every group whole he she his her him who whom which what why how where
""".split())

BLACKLIST = [
    'dungeon về', 'take x1', 'orient facing', 'budget stamina', 'spot geoglyph',
    'proceed to', 'access tower', 'deal with', 'get x1', 'hop on', 'cutscene',
    'fast travel', 'raw materials', 'follow quest marker', 'head-on', 'stock up',
    'use horse', 'from rito village', 'light of blessings', 'light of blessing',
]

HEAD_RE = re.compile(r'<h([1-4])\b([^>]*)>(.*?)</h\1>', re.I | re.S)
VN_CHAR = re.compile('[ăâđêôơưàáảãạằắẳẵặầấẩẫậèéẻẽẹềếểễệìíỉĩịòóỏõọồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ]')
TAG_RE = re.compile(r'<[^>]+>')
PUNCT = " \t\r\n.,;:!?()[]{}\"'“”‘’«»…—–-*/|"
X_RE = re.compile(r'(?:^|[^\w])(?:x\d+|\d+x)(?![\w])', re.I)
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'’\-]*")


def text_of(html):
    return re.sub(r'\s+', ' ', TAG_RE.sub(' ', html)).strip()


_PHRASES_DESC = sorted(PHRASES, key=len, reverse=True)


def strip_phrases(t):
    """Bỏ cụm tên riêng, ưu tiên cụm dài trước để không bị cụm ngắn ăn mất."""
    low = t.lower()
    for p in _PHRASES_DESC:
        low = low.replace(p, ' ')
    return low


def tokens(t):
    return [w.strip(PUNCT) for w in t.split() if len(w.strip(PUNCT)) >= 2]


def _runs(t):
    runs, run = [], []
    for tok in tokens(strip_phrases(t)):
        if WORD_RE.fullmatch(tok):
            run.append(tok)
        else:
            if run:
                runs.append(run)
            run = []
    if run:
        runs.append(run)
    return runs


def untranslated(t):
    """Cụm ASCII còn chứa từ tiếng Anh thông dụng -> chưa dịch."""
    out = []
    for r in _runs(t):
        bad = [w for w in r if w.lower() not in KEEP and w.lower() in COMMON_EN]
        if bad:
            out.append((' '.join(r), bad))
    return out


def unknown_runs(t):
    out = []
    for r in _runs(t):
        if len(r) >= 2 and any(w.lower() not in KEEP for w in r):
            out.append(' '.join(r))
    return out


def scan(path):
    rel = os.path.relpath(path, ROOT).replace('\\', '/')
    src = open(path, encoding='utf-8').read()
    hard, warn = [], []

    for m in HEAD_RE.finditer(src):
        line_no = src[:m.start()].count('\n') + 1
        t = text_of(m.group(3))
        # heading song ngữ hợp lệ: tiếng Anh gốc + chú thích tiếng Việt trong ngoặc
        if VN_CHAR.search(t) and re.search(r'\([^)]*' + VN_CHAR.pattern + r'[^)]*\)', t):
            continue
        hits = untranslated(t)
        if hits:
            hard.append((line_no, 'HEADING "%s" (%s)' % (t[:70], ', '.join(hits[0][1][:4]))))

    # Mục lục vùng lặp lại tiêu đề h3 (đã kiểm ở trên) -> bỏ qua để không báo trùng
    skip = set()
    for m in re.finditer(r'<details class="region-toc">.*?</details>', src, re.S):
        first = src[:m.start()].count('\n') + 1
        last = src[:m.end()].count('\n') + 1
        skip.update(range(first, last + 1))

    for i, line in enumerate(src.split('\n'), 1):
        if i in skip:
            continue
        t = text_of(line)
        if not t or re.search(r'<h[1-4]\b', line):
            continue
        low = t.lower()
        hit_b = next((b for b in BLACKLIST if b in low), None)
        if hit_b:
            hard.append((i, 'VIETGLISH "%s": %s' % (hit_b, t[:80])))
        m = X_RE.search(t)
        if m:
            hard.append((i, 'SỐ LIỆU "%s": %s' % (m.group(0).strip(), t[:80])))
        for run, bad in untranslated(t)[:2]:
            hard.append((i, 'CHƯA DỊCH "%s" (%s)' % (run[:60], ', '.join(bad[:4]))))
        for u in unknown_runs(t)[:1]:
            warn.append((i, 'XEM LẠI "%s"' % u[:60]))
    return rel, hard, warn


def main():
    verbose = '-v' in sys.argv
    th = tw = 0
    for p in PAGES:
        if not os.path.exists(p):
            continue
        rel, hard, warn = scan(p)
        th += len(hard); tw += len(warn)
        print('[%s] %-30s hard=%-3d warn=%d' % ('FAIL' if hard else 'ok  ', rel, len(hard), len(warn)))
        for ln, msg in hard[:25]:
            print('    %s:%d  %s' % (rel, ln, msg))
        if verbose:
            for ln, msg in warn[:60]:
                print('    ~ %s:%d  %s' % (rel, ln, msg))
    print('-' * 64)
    print('HARD=%d  WARN=%d  ->  %s' % (th, tw, 'PASS' if th == 0 else 'FAIL'))
    return 0 if th == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
