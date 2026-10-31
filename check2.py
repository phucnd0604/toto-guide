import re
html=open('index.html',encoding='utf-8').read()
ids=re.findall(r'id="([^"]+)"', html)
from collections import Counter
c=Counter(ids)
print("duplicate ids:")
for k,v in c.items():
    if v>1: print(k,v)
patterns=['\ufffd','Ã','Â']
for p in patterns:
    if p in html:
        print("FOUND PATTERN:",repr(p), html.count(p))
for i,line in enumerate(html.splitlines(),1):
    if '\ufffd' in line:
        print("REPLACEMENT CHAR line",i, line[:120])
print("total lines", len(html.splitlines()))