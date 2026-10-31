import re
html=open('index.html',encoding='utf-8').read()
text=re.sub(r'<[^>]+>',' ',html)
words=re.findall(r"[A-Za-z][A-Za-z'\-]*", text)
from collections import Counter
c=Counter(w for w in words)
for w,n in sorted(c.items(), key=lambda x:-x[1]):
    print(f"{n:4} {w}")
