import re
html=open('index.html',encoding='utf-8').read()
# split shrine-quests section
i=html.find('id="shrine-quests"')
main=html[:i]
rest=html[i:]
rows_main=re.findall(r'<tr><td>[A-Za-z].*?</td></tr>', main)
rows_rest=re.findall(r'<tr><td>[A-Za-z].*?</td></tr>', rest)
print("shrine rows (before shrine-quests):", len(rows_main))
print("shrine quest rows:", len(rows_rest))
PY