import re
s=open(r"E:\GameGuide/pages/temples.html",encoding="utf-8").read()
ext=set(re.findall(r'href="(https?://[^"]+)"', s))
for u in sorted(ext):
    print(u)
PY