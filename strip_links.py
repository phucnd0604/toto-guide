import re
p=r"E:\GameGuide\index.html"
s=open(p,encoding="utf-8").read()
# Remove external and cross-page links, keep in-page # anchors
s=re.sub(r'<a href="(https?://[^"]*|pages/[^"]*)"[^>]*>(.*?)</a>', r'\2', s, flags=re.S)
# Remove Walkthrough column header and cells
s=s.replace('<th>Walkthrough</th>','')
s=re.sub(r'<td><a [^>]*>Chi tiết</a></td>','<td>—</td>', s)
# Actually remove the whole Walkthrough column cells (already replaced above); remove leftover '<td>—</td>' in shrine tables? keep as dash
open(p,'w',encoding='utf-8').write(s)
print("done")
PY