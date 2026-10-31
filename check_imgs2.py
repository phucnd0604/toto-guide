import re, os
for pg in ['mechanics','abilities','tutorial','early-game','main-story','temples','endgame','shrines','tips','faq']:
    s=open(r"E:\GameGuide/pages/%s.html"%pg,encoding="utf-8").read()
    imgs=re.findall(r'<img[^>]*src="([^"]+)"', s)
    broken=0
    for i in imgs:
        path=os.path.join(r"E:\GameGuide", i.replace("../",""))
        if not os.path.exists(path):
            broken+=1
    print(pg, "imgs:", len(imgs), "broken:", broken)
PY