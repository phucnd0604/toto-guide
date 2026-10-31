import re
src=open(r"E:\GameGuide\pages\shrines.html",encoding="utf-8").read()
secs=re.findall(r'<section id="shrine-quests">.*?</section>', src, re.S)
fresh=secs[0] if secs else ''
fresh=fresh.replace('../images/','images/').replace('../assets/','assets/')
# strip links
fresh=re.sub(r'<a href="(https?://[^"]*|pages/[^"]*)"[^>]*>(.*?)</a>', r'\2', fresh, flags=re.S)
idx=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
# remove ALL shrine-quests sections
idx=re.sub(r'<section id="shrine-quests">.*?</section>', '', idx, flags=re.S, count=0)
# insert before patterns card
marker='<div class="card">\n    <h3>Mẫu puzzle shrine thường gặp</h3>'
assert marker in idx, "marker not found"
idx=idx.replace(marker, fresh+"\n"+marker, 1)
open(r"E:\GameGuide\index.html","w",encoding="utf-8").write(idx)
# verify
print("shrine-quests sections now:", len(re.findall(r'<section id="shrine-quests">', idx)))
print("En-oma in index:", "En-oma Shrine" in idx)
PY