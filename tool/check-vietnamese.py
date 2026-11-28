# -*- coding: utf-8 -*-
"""Quét nội dung HTML để phát hiện câu chưa dịch / Vietglish.

Dùng:  python tool/check-vietnamese.py [-v]
Mã thoát: 0 = không còn lỗi HARD, 1 = còn lỗi HARD.

HARD = heading còn tiếng Anh | cụm Vietglish trong blacklist | mẫu "x1"/"5x"
WARN = cụm tiếng Anh lạ trong câu (tên món/quái chưa dịch) -> xem lại tay
"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Mở rộng phạm vi: mọi trang trong pages/, kể cả walkthrough/quests/temples/reference.
PAGES = [os.path.join(ROOT, 'index.html')] + sorted(
    glob.glob(os.path.join(ROOT, 'pages', '**', '*.html'), recursive=True))

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
    "who goes there", "recovering the hero's sword", "piaffe packed away",
    "find the fifth sage", "guidance from ages past", "secret of the ring ruins", "destroy ganondorf",
    "bring peace to hyrule field", "impa and the geoglyphs", "first gatehouse",
    "fell into a well", "an uninvited guest", "where are the wells", "the hunt for bubbul gems",
    "new serenne stable", "new serenne", "hebra south summit cave", "hebra south summit",
    "hebra summit cave", "eye of the storm", "south summit",
    "south akkala stable", "south akkala", "death mountain west site", "big wheel", "little frox",
    "the sludge-covered statue", "the broken slate", "restoring the zora armor", "clues to the sky",
    "old map", "east reservoir lake", "east akkala plains", "east akkala chasm", "east akkala",
    # dòng ghi nguồn ảnh / bản quyền: giữ nguyên tên nhà cung cấp
    "zelda dungeon wiki", "dungeon wiki", "wikimedia commons", "cc by", "polygon",
    "zeldacentral", "totk guide",
    "gamespot", "the guardian", "ign", "nintendo life",
]

# Tên thử thách / nhiệm vụ mở đền ở pages/shrines.html — tên riêng, giữ nguyên tiếng Anh.
PHRASES += [
    "a pretty stone and five golden apples",
    "a route for a ball",
    "against the flow",
    "aid from above",
    "alignment of the circles",
    "an uplifting device",
    "an upright device",
    "bridging the sands",
    "building with logs",
    "built for rails",
    "courage to jump", "courage to pluck", "courage to fall",
    "dyeing to find it",
    "fire and ice",
    "fire and water",
    "forward or backward?",
    "gravity and velocity",
    "jump the gaps",
    "keys born of water",
    "legend of the soaring spear",
    "long or wide",
    "more than defense",
    "moving the spheres",
    "orbs of water",
    "proving grounds: in reverse",
    "proving grounds: lights out",
    "proving grounds: low gravity",
    "proving grounds: short circuit",
    "proving grounds: the hunt",
    "ride the giant horse",
    "ride the winds",
    "rise and fall",
    "rock for sale",
    "scoop it out",
    "shining in darkness",
    "the ability to combine",
    "the ability to create",
    "the ability to rewind",
    "the ability to rise",
    "the death caldera crystal",
    "the east hebra sky crystal",
    "the gerudo canyon crystal",
    "the gisa crater crystal",
    "the high spring and the light rings",
    "the ice guides you",
    "the lake hylia crystal",
    "the lake intenoch cave crystal",
    "the lanayru road crystal",
    "the necluda sky crystal",
    "the north hebra mountains crystal",
    "the north hyrule sky crystal",
    "the north necluda sky crystal",
    "the northwest hebra cave crystal",
    "the oakle's navel cave crystal",
    "the power of water",
    "the ralis channel crystal",
    "the right roll",
    "the satori mountain crystal",
    "the sky mine crystal",
    "the sokkala sky crystal",
    "the south hyrule sky crystal",
    "the south lanayru sky crystal",
    "the stakes guide you",
    "the tabantha sky crystal",
    "the way up",
    "the west necluda sky crystal",
    "the white bird's guidance",
    "upward and forward",
    "water makes a way",
    "wings on the wind",
]

# Tên riêng/địa danh/thuật ngữ còn gặp trong nội dung (giữ nguyên tiếng Anh).
PHRASES += [
    "demon king",
    "fifth sage",
    "prologue sky",
    "mysterious voice",
    "lucky clover gazette",
    "wellspring island",
    "upland zorana",
    "floating scales",
    "ancient zora waterworks",
    "jiahto toto lake",
    "great deku tree",
    "purah pad",
    "lindor's brow",
    "rospro pass",
    "soldier construct ii",
    "queen gibdo",
    "master kohga",
    "ice chuchu",
    "brightbloom seed",
    "combat training",
    "proving grounds",
    "fan art ganondorf",
    "camera work",
    "zonai device",
    "energy cell",
    "zonaite deposit",
    "mipha court",
    "sidon mipha court",
    "toto lake",
    "scales",
    "sludge like",
    "korok puzzle",
    # Trang bị bộ Vực Sâu: tên món giữ nguyên tiếng Anh như các món khác.
    "tunic of the depths",
    "hood of the depths",
    "gaiters of the depths",
    "sword of the hero",
    "tunic of memories",
    "the rito rope bridge",
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


# Từ tiếng Anh hay lọt vào nội dung (danh từ/động từ game) — cơ sở để WARN chỉ báo cụm có từ tiếng Anh thật.
EN_EXTRA = set("""
armor damage durability ability quest side boss item level area map save load sunny frost flame
attack defense upgrade material weapon shield bow arrow stamina heart wheel rocket spring laser
homing cart sled hook chain chest door key gate switch target ball mirror crystal cave island
route seeds shroom carrot flower horn eye storm mystery courage peace find bring water sky
""".split())


# Âm tiết tiếng Việt không dấu (mang, theo, trong, hang…) — hay bị nhầm là tiếng Anh khi quét WARN.
VI_ASCII = set("""
an than theo trong hang sau khi qua mang cho khu bay xong quanh canh vua ra ngay con sang hai nhanh xoay anh men kim trao tay ta xe chi thanh cao leo hoa bom mua
va de co do la ma na no so to tu vi vo xu yeu vao len xuong truoc tren duoi ngoai giua cung voi deu rat kha hon nhat moi nhung hoac nen boi tai den o
mo mot vai bon nam sau bay chin muoi tram nghin nguoi cai chiec con chau em chi chu bac ong ba me bo anh chi em minh ban
lam viec di dung can phai nen duoc bi se da dang cho lay dat nang tha nhat gap thay nghe nhin noi goi hoi tra loi
nha cua duong loi nui song bien rung dong dat troi may mua nang gio tuyet lua nuoc
dau cuoi truoc sau giua tren duoi trong ngoai canh ben phia huong
rat kha hoi kha nhieu it vai chut phan nua deu cung lai roi van con het
""".split())

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
    """Cụm ASCII còn chứa từ tiếng Anh thông dụng -> chưa dịch.

    Bỏ qua âm tiết tiếng Việt không dấu nằm trong VI_ASCII: "to", "co", "do", "so"...
    là tiếng Việt hợp lệ ("balo to", "có", "đó"), không phải dấu hiệu chưa dịch.
    """
    out = []
    for r in _runs(t):
        bad = [w for w in r
               if w.lower() not in KEEP and w.lower() in COMMON_EN and w.lower() not in VI_ASCII]
        if bad:
            out.append((' '.join(r), bad))
    return out


def _runs_raw(t):
    """Như _runs nhưng KHÔNG bỏ PHRASES và giữ nguyên chữ hoa/thường (nhận diện tên riêng)."""
    runs, run = [], []
    for tok in tokens(t):
        if WORD_RE.fullmatch(tok):
            run.append(tok)
        else:
            if run:
                runs.append(run)
            run = []
    if run:
        runs.append(run)
    return runs


_PHRASES_RE = re.compile("|".join(re.escape(p) for p in _PHRASES_DESC), re.I)


def _runs_raw(t):
    """Tách cụm ASCII sau khi bỏ PHRASES nhưng GIỮ chữ hoa/thường (nhận diện tên riêng)."""
    t = _PHRASES_RE.sub(" ", t)
    runs, run = [], []
    for tok in tokens(t):
        if WORD_RE.fullmatch(tok):
            run.append(tok)
        else:
            if run:
                runs.append(run)
            run = []
    if run:
        runs.append(run)
    return runs


def unknown_runs(t):
    """Cụm ASCII lạ cần xem lại — chỉ báo khi CÓ từ tiếng Anh thật.

    Bỏ qua: cụm toàn tên riêng/âm tiết Việt không dấu, cụm viết hoa toàn bộ (tên riêng),
    và cụm không chứa từ tiếng Anh nào đã biết (phần còn lại chỉ là tên + âm tiết Việt).
    """
    out = []
    for r in _runs_raw(t):
        if len(r) < 2:
            continue
        low = [w.lower() for w in r]
        if all(w in KEEP or w in VI_ASCII for w in low):
            continue
        if all(w[:1].isupper() for w in r):
            continue
        if not any(w in COMMON_EN or w in EN_EXTRA for w in low):
            continue
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


def resolve_targets(args, content_mode):
    """Biến tham số dòng lệnh thành danh sách file cần quét.

    Không truyền gì  -> toàn site (index.html + pages/**/*.html), như trước.
    --content        -> content/**/*.body.html + content/hub.body.html: quét CHỮ TRƯỚC khi build,
                        để sửa câu chữ không phải chạy cả vòng "build rồi quét lại toàn site".
    <file.html>      -> đúng file đó (đường dẫn tương đối tính từ gốc repo hoặc tuyệt đối).
    <slug>           -> pages/<loại>/<slug>.html của slug đó.
    """
    if content_mode:
        return sorted(glob.glob(os.path.join(ROOT, 'content', '**', '*.html'), recursive=True))
    if not args:
        return PAGES
    out = []
    for arg in args:
        if arg.lower().endswith(('.html', '.htm')):
            path = arg if os.path.isabs(arg) else os.path.join(ROOT, arg)
            out.append(path)
            continue
        hits = glob.glob(os.path.join(ROOT, 'pages', '**', arg + '.html'), recursive=True)
        if not hits:
            print('[bỏ qua] không tìm thấy trang cho slug %r' % arg)
            continue
        out.extend(sorted(hits))
    return out


def main():
    verbose = '-v' in sys.argv
    content_mode = '--content' in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    targets = resolve_targets(args, content_mode)
    if not targets:
        print('KHÔNG có file nào để quét')
        return 0
    th = tw = 0
    for p in targets:
        if not os.path.exists(p):
            print('[thiếu] %s' % p)
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
