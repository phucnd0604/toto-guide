s=open(r"C:\Users\phucn\AppData\Local\Temp\opencode\shrines-zc.txt",encoding="utf-16").read()
i=s.find('## Shrine Quests')
j=s.find('## ', i+5)
sec=s[i:j] if j!=-1 else s[i:]
out=open(r"E:\GameGuide\check_end_out.txt","w",encoding="utf-8")
out.write("len sec: "+str(len(sec))+"\n")
out.write(repr(sec[-300:])+"\n")
out.close()
PY