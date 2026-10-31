s=open(r"E:\GameGuide/index.html",encoding="utf-8").read()
print("len:", len(s))
print("mojibake:", s.count("\ufffd"))
print("quest count:", s.count('class="quest"'))
print("img count:", s.count("<img"))
PY