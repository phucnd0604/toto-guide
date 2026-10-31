import re,glob
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    skip = 'skip-link' in s and 'href="#main"' in s
    focus = 'focus-visible' in open('assets/style.css',encoding='utf-8').read()
    reduced = 'prefers-reduced-motion' in open('assets/style.css',encoding='utf-8').read()
    print(f,'skip-link=%s'%(skip))
print('focus-visible in css:',focus)
print('reduced-motion in css:',reduced)