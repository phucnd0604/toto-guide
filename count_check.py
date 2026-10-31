import re
html=open('index.html',encoding='utf-8').read()
# count shrine table rows (excluding header)
rows=re.findall(r'<tr><td>[A-Za-z].*?</td></tr>', html)
print("shrine rows:", len(rows))
# quest divs
quests=re.findall(r'<div class="quest" id="q(\d+)"', html)
print("quests:", len(quests), quests[:5], quests[-3:])
# images
imgs=re.findall(r'<img[^>]*src="([^"]+)"', html)
print("images:", len(imgs))
# sections
secs=re.findall(r'<section id="([^"]+)"', html)
print("sections:", len(secs))
print(secs)
PY