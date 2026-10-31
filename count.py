import re, pathlib
t=pathlib.Path('E:/GameGuide/pages/shrines.html').read_text(encoding='utf-8')
# count table rows with td
rows=re.findall(r'<tr><td>', t)
print('shrine-ish rows:', len(rows))
# shrine quests rows? count after shrine-quests section
part=t.split('id="shrine-quests"')[1]
qrows=re.findall(r'<tr><td>', part)
print('quest rows:', len(qrows))