import re,glob
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    h1=len(re.findall(r'<h1\b',s))
    h2=len(re.findall(r'<h2\b',s))
    h3=len(re.findall(r'<h3\b',s))
    print(f, 'h1=%d h2=%d h3=%d'%(h1,h2,h3))