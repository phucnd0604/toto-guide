import re,glob,os
missing=[]
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    for m in re.finditer(r'href="([^"]+)"',s):
        href=m.group(1)
        if href.startswith('http') or href.startswith('#') or href.startswith('mailto'):
            continue
        base=os.path.dirname(f)
        path=os.path.normpath(os.path.join(base,href.split('#')[0]))
        if not os.path.exists(path):
            missing.append((f,href))
print('broken internal links:',len(missing))
for m in missing: print(m)
# anchor targets
anchors=set()
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    for m in re.finditer(r'id="([^"]+)"',s):
        anchors.add(m.group(1))
# check in-page anchor links exist in that file
badanchor=[]
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    ids=set(re.findall(r'id="([^"]+)"',s))
    for m in re.finditer(r'href="([^"]*#[^"]+)"',s):
        href=m.group(1)
        if '#' not in href: continue
        filepart,frag=href.split('#',1)
        if filepart=='':
            if frag not in ids:
                badanchor.append((f,href))
        else:
            # resolve file
            base=os.path.dirname(f)
            path=os.path.normpath(os.path.join(base,filepart))
            if os.path.exists(path):
                ts=open(path,encoding='utf-8').read()
                if frag not in set(re.findall(r'id="([^"]+)"',ts)):
                    badanchor.append((f,href))
print('broken anchors:',len(badanchor))
for b in badanchor[:30]: print(b)