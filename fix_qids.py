p=r"E:\GameGuide\index.html"
s=open(p,encoding="utf-8").read()
faq_start=s.find('<section id="faq"')
faq_end=s.find('</section>', faq_start)+len('</section>')
faq_part=s[faq_start:faq_end]
for i in range(1,9):
    faq_part=faq_part.replace('id="q%d"'%i, 'id="faq-q%d"'%i)
    faq_part=faq_part.replace('href="#q%d"'%i, 'href="#faq-q%d"'%i)
s=s[:faq_start]+faq_part+s[faq_end:]
open(p,"w",encoding="utf-8").write(s)
# verify
chk=open(p,encoding="utf-8").read()
for i in range(1,9):
    print("q%d:"%i, chk.count('id="q%d"'%i))
PY