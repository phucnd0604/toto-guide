import re,glob
issues=[]
for f in ['index.html']+glob.glob('pages/*.html')+['assets/style.css','assets/app.js']:
    s=open(f,encoding='utf-8').read()
    # check for replacement char
    if '\ufffd' in s:
        issues.append((f,'REPLACEMENT_CHAR'))
    # check for common mojibake sequences
    for pat in ['Ã','Â','áº','á»','áº','Ä','Å','â€“','â€”','â€œ','â€']:
        if pat in s:
            issues.append((f,'MOJIBAKE:'+pat))
            break
print('files with issues:',len(issues))
for i in issues: print(i)
print('done')
