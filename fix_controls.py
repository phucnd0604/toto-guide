p=r"E:\GameGuide\pages\mechanics.html"
s=open(p,encoding="utf-8").read()
s=s.replace('<tr><td>B</td><td>Nhảy / Huỷ / Lùi</td></tr>','<tr><td>B</td><td>Huỷ / Quay lại</td></tr>')
s=s.replace('<tr><td>X</td><td>Leo (giữ) / Bay (Paraglider khi rơi)</td></tr>','<tr><td>X</td><td>Nhảy (giữ) / Bay (Paraglider khi rơi)</td></tr>')
s=s.replace('<tr><td>R</td><td>Rune/Ability nhanh</td></tr>','<tr><td>R</td><td>Ability nhanh</td></tr>')
open(p,"w",encoding="utf-8").write(s)
print("done")
PY