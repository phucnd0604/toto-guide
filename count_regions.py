import re
html=open('index.html',encoding='utf-8').read()
# find each section id and count rows until next section
sections=re.findall(r'<section id="([^"]+)">', html)
# positions
pos=[(sid, html.find('id="%s"'%sid)) for sid in sections]
# count rows in each section block
prev=None
for sid,p in pos:
    pass
# simpler: split by <section
parts=re.split(r'(<section id="[^"]+">)', html)
cur=None
counts={}
for chunk in parts:
    m=re.match(r'<section id="([^"]+)">', chunk)
    if m:
        cur=m.group(1)
        counts[cur]=0
    else:
        if cur:
            counts[cur]+=len(re.findall(r'<tr><td>', chunk))
for k,v in counts.items():
    if v>0:
        print(v, k)
print("total", sum(v for v in counts.values()))
PY