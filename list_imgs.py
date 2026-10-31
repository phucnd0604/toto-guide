import re
s=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
urls=set(re.findall(r'src="(https?://[^"]+)"', s))
for u in sorted(urls):
    print(u)
out=open(r"E:\GameGuide\img_list.txt","w",encoding="utf-8")
for u in sorted(urls):
    out.write(u+"\n")
out.close()
PY