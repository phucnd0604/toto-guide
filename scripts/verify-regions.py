# -*- coding: utf-8 -*-
"""Verify từng vùng trong pages/progress-route.html theo checklist workflow-region.md.

Dùng: python scripts/verify-regions.py [-v] [region_id ...]

Cột:
  step  : số <li> trong index (trái)         want : số bước theo fextralife
  h3    : số mục walkthrough (phải)          words: số từ walkthrough
  cover : số bước index được walkthrough nhắc tới / tổng (chỉ tính vùng 2 cột)
  img   : số thẻ <img>                       uni  : số ảnh không trùng
  ms    : ảnh thiếu file                     xN   : mẫu "x1"/"5x" còn sót
  en    : heading còn tiếng Anh              ph   : placeholder "..."/"sẽ bổ sung"
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, 'pages', 'progress-route.html')

EXPECT = {'prologue': 19, 'central': 27, 'hebra': 31, 'eldin': 25, 'lanayru': 36,
          'mastersword': 14, 'gerudo': 23, 'fifth': 35, 'final': 14}
NAMES = {'prologue': 'Prologue & Sky', 'central': 'Central Hyrule', 'hebra': 'Hebra (Tulin)',
         'eldin': 'Eldin (Yunobo)', 'lanayru': 'Lanayru (Sidon)', 'mastersword': 'Master Sword',
         'gerudo': 'Gerudo (Riju)', 'fifth': 'Fifth Sage', 'final': 'Demon King'}

STOP = set("""đến từ bằng của và với cho trong ngoài trên dưới cạnh gần xong rồi sau trước
ở tại theo để mà thì là có không những các một hai ba bốn năm sáu bảy tám chín mười
về đi tìm nói chuyện nhận mở làm lấy quay hoàn thành đánh bại khám phá kích hoạt gặp trả
nhảy vào giúp sửa tiếp cận đáp xuống bay lên mua bán ngủ dùng đặt thu thập chạm
main quest side shrine temple seeds seed""".split())

BLACK = ['dungeon về', 'take x1', 'orient facing', 'budget stamina', 'spot geoglyph',
         'proceed to', 'access tower', 'deal with', 'get x1', 'hop on', 'cutscene',
         'fast travel', 'raw materials', 'follow quest marker', 'head-on', 'stock up',
         'use horse', 'light of blessing']
COMMON = set("""the a an of to in on at with from by for and or but is are was were be been
will would can could should must may might you your we our they them it its this that these those
there here then than when while after before once if so as not no all any some each every both
more most less very just also only still again now up down out over through into onto off back away
need use get take make go come look find keep put place reach clear complete activate locate talk
follow head climb jump drop cross enter exit open close destroy defeat fight grab pick collect
gather search explore return proceed access spot budget deal stock nearby raw materials simple easy
way thing first second next last main objective step area section dungeon puzzle level note tip tips
good bad new old high low long short big small left right north south east west day night time times""".split())
QUEST_OK = {'camera work in the depths', 'regional phenomena', 'tulin of rito village'}

src = open(PAGE, encoding='utf-8').read()
secs = {}
for m in re.finditer(r'<section id="([a-z]+)">(.*?)</section>', src, re.S):
    secs[m.group(1)] = m.group(2)


def clean(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)).strip()


def toks(s):
    return [w.lower() for w in re.findall(r"[\wÀ-ỹ']+", s, re.U) if len(w) >= 4 and w.lower() not in STOP]


def stats(rid):
    body = secs[rid]
    left_m = re.search(r'<div class="col-left">(.*?)<div class="col-right">', body, re.S)
    twocol = left_m is not None
    idx = left_m.group(1) if twocol else body
    walk = body[left_m.end():] if twocol else body
    lis = [clean(x) for x in re.findall(r'<li>(.*?)</li>', idx, re.S)]
    h3s = [clean(x) for x in re.findall(r'<h3[^>]*>(.*?)</h3>', walk, re.S)]
    flat = clean(walk).lower()
    words = len(flat.split())
    imgs = re.findall(r'src="([^"]+)"', walk)
    uniq = list(dict.fromkeys(imgs))
    missing = [i for i in uniq if not os.path.exists(os.path.normpath(os.path.join(ROOT, 'pages', i)))]
    dup = [i for i in uniq if imgs.count(i) > 1]
    covered, uncovered = 0, []
    if twocol:
        for li in lis:
            kt = toks(li)
            if not kt:
                covered += 1
                continue
            hit = sum(1 for t in kt if t in flat)
            if hit / len(kt) >= 0.5:
                covered += 1
            else:
                uncovered.append(li[:70])
    en_heads = []
    VN = re.compile(r'[ăâđêôơưàáảãạằắẳẵặầấẩẫậèéẻẽẹềếểễệìíỉĩịòóỏõọồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ]')
    for h in h3s + [clean(x) for x in re.findall(r'<h2[^>]*>(.*?)</h2>', body, re.S)]:
        # heading song ngữ hợp lệ: có chú thích tiếng Việt trong ngoặc
        if VN.search(h) and re.search(r'\([^)]*' + VN.pattern + r'[^)]*\)', h):
            continue
        # tách token theo khoảng trắng, chỉ xét cụm gồm toàn từ ASCII
        tk_list = re.split(r'\s+', re.sub(r'[\(\):,;!?"“”]', ' ', h))
        run = []
        def flush(run):
            if len(run) < 2 or not any(w.lower() in COMMON for w in run):
                return False
            return (not VN.search(h)) or len(run) >= 3
        for tk in tk_list + ['']:
            w = tk.strip()
            if w and re.fullmatch(r"[A-Za-z][A-Za-z'\u2019\-]*", w):
                run.append(w)
                continue
            if flush(run):
                en_heads.append(h[:70])
                break
            run = []
        else:
            continue
    text_all = clean(body)
    viet = sum(1 for b in BLACK if b in text_all.lower())
    xn = len(re.findall(r'\b(?:x\d+|\d+x)\b', text_all))
    ph = text_all.count('content continues') + text_all.count('sẽ bổ sung') + text_all.count('...')
    return dict(steps=len(lis), h3=len(h3s), words=words, covered=covered, uncovered=uncovered,
                imgs=len(imgs), uniq=len(uniq), missing=missing, dup=dup, en_heads=en_heads,
                viet=viet, xn=xn, ph=ph, twocol=twocol)


ids = [a for a in sys.argv[1:] if a in EXPECT] or list(EXPECT)
print('%-12s %-16s %4s %4s %3s %6s %7s %4s %4s %3s %3s %3s %3s %-6s' % (
    'region', 'name', 'step', 'want', 'h3', 'words', 'cover', 'img', 'uni', 'ms', 'xN', 'en', 'ph', 'layout'))
bad = 0
for rid in ids:
    s = stats(rid)
    flags = []
    if s['steps'] != EXPECT[rid]:
        flags.append('STEP')
    if s['twocol'] and s['covered'] < s['steps']:
        flags.append('COVER')
    if s['missing'] or s['dup']:
        flags.append('IMG')
    if s['viet'] or s['xn'] or s['en_heads'] or s['ph']:
        flags.append('LANG')
    if not s['twocol']:
        flags.append('LAYT')
    if flags:
        bad += 1
    cov = ('%d/%d' % (s['covered'], s['steps'])) if s['twocol'] else '  n/a'
    print('%-12s %-16s %4d %4d %3d %6d %7s %4d %4d %3d %3d %3d %3d %-6s %s' % (
        rid, NAMES[rid], s['steps'], EXPECT[rid], s['h3'], s['words'], cov,
        s['imgs'], s['uniq'], len(s['missing']), s['xn'], len(s['en_heads']), s['ph'],
        '2col' if s['twocol'] else 'flat', ','.join(flags)))
    if '-v' in sys.argv:
        for u in s['uncovered'][:8]:
            print('      chưa cover:', u)
        for e in s['en_heads'][:8]:
            print('      heading EN:', e)
        for m in s['missing']:
            print('      thiếu ảnh:', m)
        for d in s['dup']:
            print('      ảnh trùng:', d)
print('-' * 100)
print('vùng có vấn đề: %d/%d' % (bad, len(ids)))
