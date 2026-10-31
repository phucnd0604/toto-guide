import re
# get fresh shrine-quests section from shrines.html
src=open(r"E:\GameGuide\pages\shrines.html",encoding="utf-8").read()
secs=re.findall(r'<section id="shrine-quests">.*?</section>', src, re.S)
assert secs, "no fresh section"
fresh=secs[0]
fresh=fresh.replace('../images/','images/').replace('../assets/','assets/')
fresh=re.sub(r'<a href="(https?://[^"]*|pages/[^"]*)"[^>]*>(.*?)</a>', r'\2', fresh, flags=re.S)
# read index
idx=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
# remove ALL shrine-quests sections
idx2=re.sub(r'<section id="shrine-quests">.*?</section>', '', idx, flags=re.S)
assert idx2 != idx, "nothing removed"
# insert fresh before the patterns card marker
marker='<div class="card">\n    <h3>Mẫu puzzle shrine thường gặp</h3>'
assert marker in idx2, "marker missing"
idx2=idx2.replace(marker, fresh+"\n"+marker, 1)
open(r"E:\GameGuide\index.html","w",encoding="utf-8").write(idx2)
# verify
chk=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
out=open(r"E:\GameGuide\fix3_out.txt","w",encoding="utf-8")
out.write("sections: "+str(len(re.findall(r'<section id="shrine-quests">', chk)))+"\n")
out.write("En-oma in shrine-quests: "+str('En-oma Shrine' in chk[chk.find('id="shrine-quests"'):chk.find('id="shrine-quests"')+5000])+"\n")
out.write("zeldacentral shrine urls: "+str(len(re.findall(r'zeldacentral.com/games/tears-of-the-kingdom/shrines', chk)))+"\n")
out.close()
PY