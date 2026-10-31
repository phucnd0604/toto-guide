import re
s=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
urls=set(re.findall(r'https?://[^\s"<>]+', s))
# exclude fonts
nonfont=[u for u in urls if 'fonts.googleapis' not in u and 'fonts.gstatic' not in u]
print("non-font external urls remaining:", len(nonfont))
for u in sorted(nonfont)[:10]:
    print(u)
PY