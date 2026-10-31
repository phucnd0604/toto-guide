p=r"E:\GameGuide\index.html"
s=open(p,encoding="utf-8").read()
s=s.replace("ΓÇÖ","'")
s=s.replace("ΓÇ£",'"').replace("ΓÇ¥",'"')
s=s.replace("ΓÇö","—").replace("ΓÇô","–")
open(p,"w",encoding="utf-8").write(s)
print("done")
PY