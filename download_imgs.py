import re, os, urllib.request
s=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
urls=sorted(set(re.findall(r'src="(https?://[^"]+)"', s)))
imgdir=r"E:\GameGuide\images"
os.makedirs(imgdir, exist_ok=True)
mapping={}
for u in urls:
    name=os.path.basename(u.split('?')[0])
    # sanitize
    safe=name
    dest=os.path.join(imgdir, safe)
    if not os.path.exists(dest):
        try:
            req=urllib.request.Request(u, headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data=resp.read()
            with open(dest,'wb') as f:
                f.write(data)
            print("OK", safe, len(data))
        except Exception as e:
            print("FAIL", safe, e)
    else:
        print("EXISTS", safe)
    mapping[u]="images/"+safe
# replace in html
for u,local in mapping.items():
    s=s.replace(u, local)
open(r"E:\GameGuide\index.html","w",encoding="utf-8").write(s)
print("Replaced", len(mapping), "urls")
PY