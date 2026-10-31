import re
s=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
print("external/page links remaining:", len(re.findall(r'<a href="(https?://|pages/)', s)))
print("Walkthrough th remaining:", s.count("<th>Walkthrough</th>"))