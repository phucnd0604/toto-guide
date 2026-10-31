p=r"E:\GameGuide\pages\faq.html"
s=open(p,encoding="utf-8").read()
import re
s=re.sub(r'<p>Mở từ quest "Camera Work in the Depths"\?.*?</p>', '<p>Shrine Sensor mở từ quest đầu với Purah/Robbie. Kiểm tra Purah Pad upgrades.</p>', s, flags=re.S)
open(p,"w",encoding="utf-8").write(s)
print("done")
PY