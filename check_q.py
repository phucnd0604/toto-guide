s=open(r"E:\GameGuide/index.html",encoding="utf-8").read()
for i in range(1,9):
    print("q%d:"%i, s.count('id="q%d"'%i))
PY