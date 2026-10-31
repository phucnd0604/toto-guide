import re,glob
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    for m in re.finditer(r'<figure[^>]*>(.*?)</figure>',s,re.S):
        fig=m.group(1)
        if 'figcaption' not in fig:
            print(f,'FIGURE WITHOUT CAPTION')
        # check attribution keywords
    # count figures
    print(f,'figures=',s.count('<figure'))