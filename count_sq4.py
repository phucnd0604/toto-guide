import re
s=open(r"E:\GameGuide/index.html",encoding="utf-8").read()
i=s.find('id="shrine-quests"')
j=s.find('</section>',i)
seg=s[i:j]
print("tr td rows:", len(re.findall(r'<tr><td>', seg)))
PY