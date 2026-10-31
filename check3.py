import os,re
html=open('index.html',encoding='utf-8').read()
imgs=re.findall(r'<img[^>]*src="([^"]+)"', html)
bad=[]
for s in imgs:
    if s.startswith('http'): 
        print("external img:",s)
    else:
        if not os.path.exists(s) or os.path.getsize(s)==0:
            bad.append(s)
print("broken/empty:",len(bad))
for b in bad: print(b)
# check mojibake bytes
data=open('index.html','rb').read()
try:
    data.decode('utf-8'); print("utf8 ok")
except Exception as e: print("utf8 error",e)
print("replacement char count", html.count('\ufffd'))
PY