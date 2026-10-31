import re,glob,os
missing=[]
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    for m in re.finditer(r'src="([^"]+)"',s):
        src=m.group(1)
        if src.startswith('http'): continue
        base=os.path.dirname(f)
        path=os.path.normpath(os.path.join(base,src))
        if not os.path.exists(path):
            missing.append((f,src))
print('broken img src:',len(missing))
for m in missing: print(m)
# also check any svg referenced
print('done')
