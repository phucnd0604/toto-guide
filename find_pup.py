s=open(r"E:\GameGuide/index.html",encoding="utf-8").read()
i=s.find('Pupunke \nShrine')
j=s.rfind('<section',0,i)
k=s.find('</section>',i)
out=open(r"E:\GameGuide/find_pup_out.txt","w",encoding="utf-8")
out.write(repr(s[j:j+60])+"\n")
out.write("end "+str(k)+"\n")
out.close()
PY