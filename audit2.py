import re,glob
alts=set()
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    for m in re.finditer(r'alt="([^"]*)"',s):
        alts.add(m.group(1))
for a in sorted(alts):
    print(repr(a))
print('count',len(alts))