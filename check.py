import re, os
html=open('index.html',encoding='utf-8').read()
imgs=re.findall(r'<img[^>]*src="([^"]+)"', html)
print("refs",len(imgs))
miss=[s for s in imgs if not s.startswith('http') and not os.path.exists(s)]
print("missing",len(miss))
for m in miss: print("MISSING",m)
ext=[s for s in imgs if s.startswith('http')]
for e in ext: print("EXT",e)
ids=set(re.findall(r'id="([^"]+)"', html))
hrefs=re.findall(r'href="#([^"]+)"', html)
print("href anchors",len(hrefs),"unique",len(set(hrefs)))
bad=[a for a in set(hrefs) if a not in ids]
print("bad anchors",len(bad))
for b in bad: print("BADANCHOR",b)
links=re.findall(r'href="(https?://[^"]+)"', html)
print("http links",len(links))
for l in links: print("LINK",l)