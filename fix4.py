import re
src=open(r"E:\GameGuide\pages\shrines.html",encoding="utf-8").read()
secs=re.findall(r'<section id="shrine-quests">.*?</section>', src, re.S)
fresh=secs[0]
fresh=fresh.replace('../images/','images/').replace('../assets/','assets/')
fresh=re.sub(r'<a href="(https?://[^"]*|pages/[^"]*)"[^>]*>(.*?)</a>', r'\2', fresh, flags=re.S)
idx=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
# find the old shrine-quests section
start=idx.find('<section id="shrine-quests">')
end=idx.find('</section>', start)+len('</section>')
assert start!=-1 and end!=-1
idx=idx[:start]+fresh+idx[end:]
open(r"E:\GameGuide\index.html","w",encoding="utf-8").write(idx)
# verify
chk=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
i=chk.find('id="shrine-quests"')
seg=chk[i:i+300]
out=open(r"E:\GameGuide\fix4_out.txt","w",encoding="utf-8")
out.write(seg+"\n")
out.write("zeldacentral shrine urls: "+str(len(re.findall(r'zeldacentral.com/games/tears-of-the-kingdom/shrines', chk)))+"\n")
out.close()
PY