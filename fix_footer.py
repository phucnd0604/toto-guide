import re
pages=['mechanics','abilities','tutorial','early-game','main-story','temples','endgame','shrines','tips','faq']
for pg in pages:
    p=r"E:\GameGuide\pages\%s.html"%pg
    s=open(p,encoding="utf-8").read()
    s=re.sub(r'<footer>.*?</footer>', '<footer><p>Hướng dẫn tổng hợp từ IGN Walkthrough, Nintendo Life, Zelda Central, Polygon, GameSpot, The Guardian.</p></footer>', s, flags=re.S)
    open(p,"w",encoding="utf-8").write(s)
print("done")
PY