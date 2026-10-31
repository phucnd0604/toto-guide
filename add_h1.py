p=r"E:\GameGuide\index.html"
s=open(p,encoding="utf-8").read()
s=s.replace('<section id="gioi-thieu" class="content">','<h1>Hướng dẫn chơi Zelda: Tears of the Kingdom từ A đến Z</h1>\n<section id="gioi-thieu" class="content">',1)
open(p,"w",encoding="utf-8").write(s)
print("done")
PY