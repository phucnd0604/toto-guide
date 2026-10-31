p=r"E:\GameGuide\index.html"
s=open(p,encoding="utf-8").read()
reps=[
 ('<a href="#tutorial">Tutorial</a>','<a href="#tutorial">Hướng dẫn</a>'),
 ('<a href="#early">Early Game</a>','<a href="#early">Đầu game</a>'),
 ('<a href="#main-story">Main Story</a>','<a href="#main-story">Cốt truyện chính</a>'),
 ('<a href="#temples">Temple</a>','<a href="#temples">Đền thờ</a>'),
 ('<a href="#endgame">Endgame</a>','<a href="#endgame">Cuối game</a>'),
 ('<a href="#shrines">Shrine</a>','<a href="#shrines">Đền thờ nhỏ</a>'),
 ('<a href="#faq">FAQ</a>','<a href="#faq">Câu hỏi thường gặp</a>'),
 ('Tutorial: Great Sky Island','Hướng dẫn: Great Sky Island'),
 ('Main Story – 23 nhiệm vụ chính','Cốt truyện chính – 23 nhiệm vụ'),
 ('Endgame & Master Sword','Cuối game & Master Sword'),
 ('TOTK Guide','Hướng dẫn TOTK'),
 ('🌙 Dark','🌙 Tối'),
]
for a,b in reps:
    if a in s:
        s=s.replace(a,b)
open(p,"w",encoding="utf-8").write(s)
print("done")
PY