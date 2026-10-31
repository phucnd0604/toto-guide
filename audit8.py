import glob
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    print(f,'footer' , s.count('<footer>'), 'skip' , s.count('skip-link'))