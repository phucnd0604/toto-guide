import re
# regenerate shrines.html
exec(open(r"E:\GameGuide\build_shrines.py",encoding="utf-8").read().split('print')[0])
src=open(r"E:\GameGuide\pages\shrines.html",encoding="utf-8").read()
secs=re.findall(r'<section id="shrine-quests">.*?</section>', src, re.S)
fresh=secs[0] if secs else ''
fresh=fresh.replace('../images/','images/').replace('../assets/','assets/')
fresh=re.sub(r'<a href="(https?://[^"]*|pages/[^"]*)"[^>]*>(.*?)</a>', r'\2', fresh, flags=re.S)
idx=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
idx=re.sub(r'<section id="shrine-quests">.*?</section>', '', idx, flags=re.S)
marker='<div class="card">\n    <h3>Mẫu puzzle shrine thường gặp</h3>'
assert marker in idx
idx=idx.replace(marker, fresh+"\n"+marker, 1)
open(r"E:\GameGuide\index.html","w",encoding="utf-8").write(idx)
chk=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
out=open(r"E:\GameGuide\refresh2_out.txt","w",encoding="utf-8")
out.write("shrine-quests sections: "+str(len(re.findall(r'<section id="shrine-quests">', chk)))+"\n")
out.write("zeldacentral shrine urls: "+str(len(re.findall(r'zeldacentral.com/games/tears-of-the-kingdom/shrines', chk)))+"\n")
out.close()
PY