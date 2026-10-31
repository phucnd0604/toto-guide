import re,glob,os
missing=[]
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    for m in re.finditer(r'<img[^>]*src="([^"]+)"',s):
        src=m.group(1)
        base=os.path.dirname(f)
        path=os.path.normpath(os.path.join(base,src))
        if not os.path.exists(path):
            missing.append((f,src))
print('missing images:',len(missing))
for m in missing: print(m)

lazy=0; total=0
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    for m in re.finditer(r'<img\b[^>]*>',s):
        total+=1
        if 'loading="lazy"' in m.group(0):
            lazy+=1
print('img total',total,'lazy',lazy)

noalt=0
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    for m in re.finditer(r'<img\b[^>]*>',s):
        if 'alt=' not in m.group(0):
            noalt+=1
print('img without alt',noalt)