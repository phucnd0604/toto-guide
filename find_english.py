import re
for pg in ['temples','main-story','tips','mechanics','abilities','tutorial','early-game','endgame','shrines','faq']:
    s=open(r"E:\GameGuide/pages/%s.html"%pg,encoding="utf-8").read()
    # find words of 4+ ASCII letters
    words=re.findall(r'[A-Za-z]{4,}', s)
    from collections import Counter
    c=Counter(words)
    # filter common HTML/attr words
    skip={'href','class','style','alt','src','https','http','www','zeldacentral','com','webp','images','assets','rel','noopener','target','blank','title','meta','charset','UTF','viewport','width','device','initial','scale','link','preconnect','fonts','googleapis','gstatic','crossorigin','stylesheet','script','lang','content','description','name','property','og','type','text','html'}
    filtered={w:n for w,n in c.items() if w.lower() not in {x.lower() for x in skip}}
    top=sorted(filtered.items(), key=lambda x:-x[1])[:15]
    print(pg, ":", top)
PY