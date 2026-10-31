import re, pathlib
from collections import Counter
allowed=set("""totk guide shrine temple boss quest main story early game endgame faq tips mechanics abilities tutorial index html css js vercel ign nintendo life zelda central polygon gamespot guardian wikimedia commons svg webp jpg png""".split())
for p in ['pages/main-story.html','pages/temples.html']:
    t=pathlib.Path(p).read_text(encoding='utf-8')
    text=re.sub(r'<[^>]+>',' ',t)
    # remove numbers/punctuation
    words=re.findall(r"[A-Za-z][A-Za-z'-]*", text)
    # unique
    uniq=sorted(set(w.lower() for w in words))
    print('===',p,'unique english tokens:',len(uniq))
    print(', '.join(uniq))