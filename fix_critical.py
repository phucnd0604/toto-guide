p=r"E:\GameGuide\index.html"
s=open(p,encoding="utf-8").read()
# 1. Fix mojibake ΓÇÖ
s=s.replace("ΓÇÖ","'")
# 2. Fix broken links to temples.html/endgame.html -> remove links (keep text)
import re
s=re.sub(r'<a href="temples\.html(?:#[^"]*)?">(.*?)</a>', r'\1', s)
s=re.sub(r'<a href="endgame\.html(?:#[^"]*)?">(.*?)</a>', r'\1', s)
# 3. Fix #dieu-khien -> #controls
s=s.replace('href="#dieu-khien"','href="#controls"')
# 4. Fix duplicate IDs: fuse, recall, armor, q1-q8
# Rename fuse in abilities section (second occurrence) - but both are in same page now. Rename the abilities one.
# Actually both fuse are in same page. Rename the second (abilities section) to "fuse-ability"
# Find and rename duplicate q1-q8 in FAQ section
# The FAQ section uses q1-q8 as section ids. Rename to faq-q1..faq-q8
s=s.replace('id="q1"','id="q1"')  # keep first (main story)
# Rename FAQ q1-q8 to faq-q1..faq-q8
# Find FAQ section
faq_start=s.find('<section id="faq"')
faq_end=s.find('</section>', faq_start)+len('</section>')
faq_part=s[faq_start:faq_end]
for i in range(1,9):
    faq_part=faq_part.replace('id="q%d"'%i, 'id="faq-q%d"'%i)
    faq_part=faq_part.replace('href="#q%d"'%i, 'href="#faq-q%d"'%i)
s=s[:faq_start]+faq_part+s[faq_end:]
# Rename fuse duplicate: the abilities section fuse id -> fuse-abil
# Find the abilities section
abil_start=s.find('<section id="nang-luc"')
abil_end=s.find('<section id="tutorial"')
abil_part=s[abil_start:abil_end]
# rename id="fuse" to id="fuse-abil" in abilities
abil_part=abil_part.replace('id="fuse"','id="fuse-abil"')
# rename toc link #fuse in abilities sidebar? The sidebar is shared... actually each section has its own sidebar. The abilities sidebar has #fuse. But the main toc doesn't. Let me check.
s=s[:abil_start]+abil_part+s[abil_end:]
# Rename recall duplicate: abilities section recall -> recall-abil
abil_start=s.find('<section id="nang-luc"')
abil_end=s.find('<section id="tutorial"')
abil_part=s[abil_start:abil_end]
abil_part=abil_part.replace('id="recall"','id="recall-abil"')
s=s[:abil_start]+abil_part+s[abil_end:]
# Rename armor duplicate: tips section armor -> armor-tips
tips_start=s.find('<section id="tips"')
tips_end=s.find('<section id="faq"')
tips_part=s[tips_start:tips_end]
tips_part=tips_part.replace('id="armor"','id="armor-tips"')
s=s[:tips_start]+tips_part+s[tips_end:]
open(p,"w",encoding="utf-8").write(s)
print("done")
PY