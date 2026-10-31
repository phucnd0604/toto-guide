import re
s=open(r"E:\GameGuide/index.html",encoding="utf-8").read()
ext=set(re.findall(r'href="(https?://[^"]+)"', s))
print("external href in index:", len(ext))
for u in sorted(ext):
    print(" ", u)
PY