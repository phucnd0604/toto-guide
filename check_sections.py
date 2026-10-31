s=open(r"E:\GameGuide/index.html",encoding="utf-8").read()
print("main-story present:", 'id="main-story"' in s)
print("temples present:", 'id="temples"' in s)
print("quest count:", s.count('class="quest"'))
PY