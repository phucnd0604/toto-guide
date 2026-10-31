p=r"E:\GameGuide\pages\endgame.html"
s=open(p,encoding="utf-8").read()
s=s.replace('<img src="../images/end-quest.jpg" alt="Màn hình sau khi hoàn thành quest chính">','')
s=s.replace('<figcaption>Ganondorf (Wikimedia Commons)</figcaption>','<figcaption>Ganondorf (fan art: Álvaro Fernández González)</figcaption>')
open(p,"w",encoding="utf-8").write(s)
print("done")
PY