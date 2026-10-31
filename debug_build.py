import re
src=open(r"C:\Users\phucn\AppData\Local\Temp\opencode\shrines-zc.txt",encoding="utf-16").read()
sections=re.split(r'\n## ', src)
for sec in sections[1:]:
    first_line=sec.split('\n',1)[0].strip()
    if 'Shrine Quests' not in first_line:
        continue
    body=sec.split('\n',1)[1] if '\n' in sec else ''
    rows=[]
    buf=''
    for line in body.split('\n'):
        s=line.strip()
        if s.startswith('|'):
            if buf: buf+='\n'+s
            else: buf=s
            if s.endswith('|'):
                rows.append(buf); buf=''
        else:
            if buf: rows.append(buf); buf=''
    if buf: rows.append(buf)
    print("total rows (incl header):", len(rows))
    print("data rows (excl header/sep):", len([r for r in rows if not r.strip().startswith('| Quest') and not r.strip().startswith('| ---')]))
    # print any row that doesn't contain 'Shrine'
    for r in rows:
        if 'Shrine' not in r:
            print("NO Shrine:", repr(r[:60]))
PY