import re
for pg in ['temples','main-story','tips','shrines','mechanics','abilities','tutorial','early-game','endgame','faq']:
    s=open(r"E:\GameGuide/pages/%s.html"%pg,encoding="utf-8").read()
    ext=set(re.findall(r'href="(https?://[^"]+)"', s))
    print(pg, "external href:", len(ext))
PY