# Fix Eldin/desert mislabeling
p=r"E:\GameGuide\pages\mechanics.html"
s=open(p,encoding="utf-8").read()
s=s.replace('<tr><td>Eldin, sa mạc</td><td>Nóng → mất máu</td>','<tr><td>Eldin, núi lửa</td><td>Nóng → mất máu</td>')
open(p,"w",encoding="utf-8").write(s)

# Fix bắn mắt/corn in all pages
for pg in ['main-story','temples','endgame']:
    p=r"E:\GameGuide\pages\%s.html"%pg
    s=open(p,encoding="utf-8").read()
    s=s.replace('bắn mắt/corn','bắn mắt/sừng')
    open(p,"w",encoding="utf-8").write(s)

# Fix 100% completion (900+ -> 1000) in endgame.html and tips.html
for pg in ['endgame','tips']:
    p=r"E:\GameGuide\pages\%s.html"%pg
    s=open(p,encoding="utf-8").read()
    s=s.replace('900+ Korok seeds','1000 Korok seeds')
    open(p,"w",encoding="utf-8").write(s)

# Fix image attribution in endgame.html (ganondorf.jpg is fan art)
p=r"E:\GameGuide\pages\endgame.html"
s=open(p,encoding="utf-8").read()
s=s.replace('<figcaption>Ganondorf (Wikimedia Commons)</figcaption>','<figcaption>Ganondorf (fan art: Álvaro Fernández González)</figcaption>')
open(p,"w",encoding="utf-8").write(s)

# Remove large image references (shrine-list.svg, zonai-parts.svg) from pages
for pg in ['shrines','tips']:
    p=r"E:\GameGuide\pages\%s.html"%pg
    s=open(p,encoding="utf-8").read()
    s=s.replace('<figure><img src="../images/shrine-list.svg" alt="Danh sách shrine"><figcaption>Danh sách shrine (Wikimedia Commons)</figcaption></figure>','')
    s=s.replace('<figure><img src="../images/zonai-parts.svg" alt="Zonai parts"><figcaption>Danh sách Zonai parts</figcaption></figure>','')
    open(p,"w",encoding="utf-8").write(s)

print("done")
PY