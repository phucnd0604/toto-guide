import re
html=open('index.html',encoding='utf-8').read()
out=[]
for i,line in enumerate(html.splitlines(),1):
    text=re.sub(r'<[^>]+>',' ',line)
    toks=set(re.findall(r'[A-Za-z]{4,}', text))
    if len(toks)>=6:
        out.append(f"{i} || {text.strip()[:200]}")
open('findeng_out.txt','w',encoding='utf-8').write("\n".join(out))
print("done",len(out))