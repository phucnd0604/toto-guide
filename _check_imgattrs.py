import re,glob
noalt=[]; noload=[]; nowh=[]
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    for m in re.finditer(r'<img\b[^>]*>',s):
        tag=m.group(0)
        if 'alt=' not in tag: noalt.append((f,tag[:60]))
        if 'width=' not in tag and 'height=' not in tag:
            nowh.append(f)
print('img without alt:',len(noalt))
print('files with img missing width/height:',len(set(nowh)))
# check for duplicate ids
import collections
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    ids=re.findall(r'id="([^"]+)"',s)
    dup=[x for x,c in collections.Counter(ids).items() if c>1]
    if dup: print('DUP IDS in',f,dup)
print('done')
