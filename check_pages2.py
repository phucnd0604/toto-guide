import re
for pg in ['temples','main-story','tips','shrines','mechanics','abilities','tutorial','early-game','endgame','faq']:
    s=open(r"E:\GameGuide/pages/%s.html"%pg,encoding="utf-8").read()
    ext=set(re.findall(r'src="(https?://[^"]+)"', s))
    broken=[u for u in ext if 'zeldacentral' in u or 'wikimedia' in u]
    print(pg, "external img src:", len(broken))
PY