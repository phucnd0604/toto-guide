import re
# regenerate shrines.html
exec(open(r"E:\GameGuide\build_shrines.py",encoding="utf-8").read().split('print')[0])
# now shrines.html written
src=open(r"E:\GameGuide\pages\shrines.html",encoding="utf-8").read()
sections=re.findall(r'<section id="[^"]*">.*?</section>', src, re.S)
exclude={'intro','patterns','links'}
wanted=[]
for s in sections:
    m=re.search(r'<section id="([^"]*)">', s)
    if m and m.group(1) not in exclude:
        wanted.append(s)
table_html="\n".join(wanted)
# fix paths
table_html=table_html.replace('../images/','images/').replace('../assets/','assets/')
# remove old shrine region sections from index.html
idx=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
# remove any existing <section id="..."> that are shrine regions (akkala, central-hyrule, eldin, faron, gerudo, hebra, lanayru, necluda, *-sky, shrine-quests)
region_ids=['akkala','central-hyrule','eldin','faron','gerudo','hebra','lanayru','necluda','central-hyrule-sky','akkala-sky','eldin-sky','faron-sky','gerudo-sky','hebra-sky','lanayru-sky','necluda-sky','shrine-quests']
for rid in region_ids:
    idx=re.sub(r'<section id="%s">.*?</section>\n?' % rid, '', idx, flags=re.S)
# insert before patterns? insert before <!-- SHRINE_TABLE_END --> marker? We removed placeholder. Insert before the patterns card instead.
marker='<div class="card">\n    <h3>Mẫu puzzle shrine thường gặp</h3>'
idx=idx.replace(marker, table_html+"\n"+marker, 1)
open(r"E:\GameGuide\index.html","w",encoding="utf-8").write(idx)
print("done, inserted", len(wanted))
PY