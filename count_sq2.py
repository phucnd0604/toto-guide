import re
s=open(r"E:\GameGuide/pages/shrines.html",encoding="utf-8").read()
i=s.find('id="shrine-quests"')
j=s.find('</section>',i)
seg=s[i:j]
rows=len(re.findall(r'<tr><td>', seg))-1
print("rows:", rows)
PY