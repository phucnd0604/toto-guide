import re
# remove all shrine-quests sections
idx=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
idx=re.sub(r'<section id="shrine-quests">.*?</section>\n?', '', idx, flags=re.S)
# get fresh shrine-quests section from shrines.html
src=open(r"E:\GameGuide\pages\shrines.html",encoding="utf-8").read()
secs=re.findall(r'<section id="shrine-quests">.*?</section>', src, re.S)
fresh=secs[0] if secs else ''
fresh=fresh.replace('../images/','images/').replace('../assets/','assets/')
# strip links from fresh
fresh=__import__('re').sub(r'<a href="(https?://[^"]*|pages/[^"]*)"[^>]*>(.*?)</a>', r'\2', fresh, flags=re.S)
# insert before patterns card
marker='<div class="card">\n    <h3>Mẫu puzzle shrine thường gặp</h3>'
idx=idx.replace(marker, fresh+"\n"+marker, 1)
open(r"E:\GameGuide\index.html","w",encoding="utf-8").write(idx)
print("done")
PY