import re
s=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
urls=set(re.findall(r'https?://[^\s"<>]+', s))
for u in sorted(urls):
    print(u)
PY