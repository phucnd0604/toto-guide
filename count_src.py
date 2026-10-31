import re
s=open(r"C:\Users\phucn\AppData\Local\Temp\opencode\shrines-zc.txt",encoding="utf-16").read()
i=s.find('## Shrine Quests')
j=s.find('## ', i+5)
sec=s[i:j]
rows=[l for l in sec.splitlines() if l.strip().startswith('|') and 'Quest' not in l.split('|')[1] if len(l.split('|'))>2]
# count data rows (exclude header and separator)
data=[l for l in sec.splitlines() if l.strip().startswith('|') and not l.strip().startswith('| Quest') and not l.strip().startswith('| ---')]
print("data rows:", len(data))
PY