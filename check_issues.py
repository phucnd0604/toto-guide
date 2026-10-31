s=open(r"E:\GameGuide/index.html",encoding="utf-8").read()
print("temples.html:", s.count("temples.html"))
print("endgame.html:", s.count("endgame.html"))
print("dieu-khien:", s.count("dieu-khien"))
print("Gamma:", s.count("Γ"))
print("q2 duplicate:", s.count('id="q2"'))
PY