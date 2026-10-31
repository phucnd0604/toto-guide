p=r"E:\GameGuide\pages\faq.html"
s=open(p,encoding="utf-8").read()
import re
s=re.sub(r'Xem guide "Can you go straight .*?final boss"\.', 'Có thể nhưng khó (cần chuẩn bị kỹ).', s)
open(p,"w",encoding="utf-8").write(s)
print("done")
PY