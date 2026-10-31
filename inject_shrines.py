import re
src=open(r"E:\GameGuide\pages\shrines.html",encoding="utf-8").read()
sections=re.findall(r'<section id="[^"]*">.*?</section>', src, re.S)
exclude={'intro','patterns','links'}
wanted=[]
for s in sections:
    m=re.search(r'<section id="([^"]*)">', s)
    if m and m.group(1) not in exclude:
        wanted.append(s)
table_html="\n".join(wanted)
idx=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
idx=idx.replace("  PLACEHOLDER_SHRINE_TABLE\n", table_html+"\n")
open(r"E:\GameGuide\index.html","w",encoding="utf-8").write(idx)
print("Inserted", len(wanted), "region sections")