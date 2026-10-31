import re,glob
titles={}
descs={}
ogt={}
ogd={}
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    t=re.search(r'<title>(.*?)</title>',s)
    d=re.search(r'<meta name="description" content="(.*?)"',s)
    ogtv=re.search(r'<meta property="og:title" content="(.*?)"',s)
    ogdv=re.search(r'<meta property="og:description" content="(.*?)"',s)
    titles[f]=t.group(1) if t else None
    descs[f]=d.group(1) if d else None
    ogt[f]=ogtv.group(1) if ogtv else None
    ogd[f]=ogdv.group(1) if ogdv else None
print('titles unique:',len(set(titles.values())),'/',len(titles))
print('descs unique:',len(set(descs.values())),'/',len(descs))
print('og:title present all:',all(v for v in ogt.values()))
print('og:desc present all:',all(v for v in ogd.values()))
for f in titles:
    if titles[f] is None or descs[f] is None or ogt[f] is None or ogd[f] is None:
        print('MISSING in',f)