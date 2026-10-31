import re
html=open('index.html',encoding='utf-8').read()
# count shrine table rows after header in shrine sections? Count <tr><td>...Shrine</td>
rows=re.findall(r'<tr><td>[A-Za-z].*?Shrine</td>', html)
print("shrine rows:", len(rows))
# region headings
for m in re.finditer(r'<section id="([^"]+)"><h2><span class="num">📍</span> ([^<]+)\((\d+)\)</h2>', html):
    print(m.group(1), m.group(2).strip(), m.group(3))
PY