import re, pathlib
from collections import Counter
for p in ['pages/main-story.html','pages/temples.html']:
    t=pathlib.Path(p).read_text(encoding='utf-8')
    text=re.sub(r'<[^>]+>',' ',t)
    words=re.findall(r"[A-Za-z][A-Za-z'-]{2,}", text)
    c=Counter(w.lower() for w in words)
    print('===',p,'total',len(words),'unique',len(c))
    for w,n in c.most_common(300):
        print(w,n)
    print()