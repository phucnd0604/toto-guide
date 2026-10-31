import re,glob
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    figs=re.findall(r'<figure[^>]*>(.*?)</figure>',s,re.S)
    nocap=sum(1 for x in figs if 'figcaption' not in x)
    print(f,'figures=%d no_caption=%d'%(len(figs),nocap))