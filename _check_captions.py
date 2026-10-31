import re,glob
src_markers=['Zelda Central','Wikimedia','CC BY','Nguồn:','Tự tạo','tự tạo','SVG']
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    for m in re.finditer(r'<figure[^>]*>(.*?)</figure>',s,re.S):
        fig=m.group(1)
        capm=re.search(r'<figcaption>(.*?)</figcaption>',fig,re.S)
        cap=capm.group(1) if capm else '(NO CAPTION)'
        if not any(mk in cap for mk in src_markers):
            print(f,'::',cap)
print('done')
