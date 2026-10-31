import re, os, urllib.request
pages=['mechanics','abilities','tutorial','early-game','main-story','temples','endgame','shrines','tips','faq']
imgdir=r"E:\GameGuide\images"
os.makedirs(imgdir, exist_ok=True)
all_urls=set()
for pg in pages:
    src=open(r"E:\GameGuide\pages\%s.html"%pg,encoding="utf-8").read()
    urls=set(re.findall(r'src="(https?://[^"]+)"', src))
    all_urls|=urls
print("total unique:", len(all_urls))
mapping={}
for u in sorted(all_urls):
    name=os.path.basename(u.split('?')[0])
    dest=os.path.join(imgdir, name)
    if not os.path.exists(dest):
        try:
            req=urllib.request.Request(u, headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data=resp.read()
            with open(dest,'wb') as f:
                f.write(data)
            print("OK", name, len(data))
        except Exception as e:
            print("FAIL", name, e)
    else:
        print("EXISTS", name)
    mapping[u]="../images/"+name
# replace in each page
for pg in pages:
    path=r"E:\GameGuide\pages\%s.html"%pg
    s=open(path,encoding="utf-8").read()
    for u,local in mapping.items():
        s=s.replace(u, local)
    # strip external <a> links (keep text)
    s=re.sub(r'<a href="(https?://[^"]*|pages/[^"]*)"[^>]*>(.*?)</a>', r'\2', s, flags=re.S)
    open(path,"w",encoding="utf-8").write(s)
print("done")
PY