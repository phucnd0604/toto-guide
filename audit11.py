import re,glob
ext=set()
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    for m in re.finditer(r'(?:src|href)="(https?://[^"]+)"',s):
        ext.add(m.group(1))
for u in sorted(ext):
    print(u)