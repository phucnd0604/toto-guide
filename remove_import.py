p=r"E:\GameGuide\assets\style.css"
s=open(p,encoding="utf-8").read()
import re
s=re.sub(r"@import url\([^)]*\);", "", s)
open(p,"w",encoding="utf-8").write(s)
print("done")
PY