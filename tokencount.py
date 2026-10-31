import re
html=open('index.html',encoding='utf-8').read()
# remove tags
text=re.sub(r'<[^>]+>',' ',html)
# tokens of ascii letters
toks=re.findall(r'[A-Za-z][A-Za-z\'-]*', text)
from collections import Counter
c=Counter(t.lower() for t in toks)
# print top tokens
for w,n in c.most_common(80):
    print(f"{w}: {n}")
PY