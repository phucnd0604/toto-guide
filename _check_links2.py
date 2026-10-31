import re,glob
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    # find href="#" or empty
    for m in re.finditer(r'href="([^"]*)"',s):
        h=m.group(1)
        if h in ('','#','javascript:void(0)'):
            print('PLACEHOLDER LINK in',f,h)
    # find src empty
    for m in re.finditer(r'src="([^"]*)"',s):
        if m.group(1)=='':
            print('EMPTY SRC in',f)
print('done')
