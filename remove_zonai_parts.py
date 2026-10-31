p=r"E:\GameGuide\pages\tips.html"
s=open(p,encoding="utf-8").read()
s=s.replace('<img src="../images/zonai-parts.svg" alt="Zonai parts list" style="max-width:100%">','')
open(p,"w",encoding="utf-8").write(s)
print("done")
PY