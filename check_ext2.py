import re
s=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
urls=set(re.findall(r'src="(https?://[^"]+)"', s))
print("external img src remaining:", len(urls))
for u in sorted(urls):
    print(u)
PY