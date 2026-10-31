import re, pathlib, os
root=pathlib.Path('E:/GameGuide')
pages=list((root/'pages').glob('*.html'))+[root/'index.html']
print('page images external links h1 meta')
for p in sorted(pages):
    t=p.read_text(encoding='utf-8')
    imgs=re.findall(r'<img[^>]*src="([^"]+)"', t)
    # resolve local images
    missing=[]
    for src in imgs:
        if src.startswith('http'):
            missing.append('EXT:'+src)
        else:
            f=(p.parent/src).resolve() if not src.startswith('/') else (root/src.lstrip('/')).resolve()
            # handle ../
            if not f.exists():
                missing.append(src)
    # external content links (a href http not fonts)
    links=re.findall(r'href="(https?://[^"]+)"', t)
    ext=[l for l in links if 'fonts.googleapis' not in l and 'fonts.gstatic' not in l]
    h1=len(re.findall(r'<h1\b', t))
    meta='meta name="description"' in t
    print(f"{p.name}: imgs={len(imgs)} missing={missing} ext_links={ext} h1={h1} meta={meta}")