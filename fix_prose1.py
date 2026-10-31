p=r"E:\GameGuide\index.html"
s=open(p,encoding="utf-8").read()
reps=[
 # Quest 5 Tulin step 8
 ("Locks 1-5 (see Wind Temple): (1) attach icicle to lever raise gate, gust turbine; (2) ride updraft to tower roof, open panels, drop through lasers, paraglider to side opening, gust; (3) break icicles, Recall spinning platform, attach icicle between gears, gust; (4) glide left side hull, lower passage, drop to underside, defeat Construct, gust; (5) gust cross gap, Ascend, attach stone slab to cog, rotate until door opens, Recall cog, climb through quickly, gust last turbine. Return to terminal → open hatch.",
  "Mở 5 khóa (xem Đền thờ Gió): (1) gắn icicle vào cần gạt bị gãy nâng cổng, gust turbine; (2) lướt luồng khí nóng lên mái tháp cao phía bắc, mở cửa kim loại, rơi qua lasers, paraglider đến side opening, gust; (3) phá icicles, Recall spinning platform, gắn icicle giữa gears, gust; (4) lướt left side hull, lower passage, rơi xuống underside, đánh bại Construct, gust; (5) gust cross gap, Ascend, gắn stone slab vào cog, xoay cho đến khi door opens, Recall cog, leo qua nhanh, gust turbine cuối. Quay về terminal → mở hatch."),
 ("3 large ice plates. Dive through exposed plates to shatter; hoặc arrows. Phase 2 adds tornadoes → steer around. Phá all 3 plates again. ~10 min, high damage. Mang healing meals không ghi đè kháng lạnh.",
  "3 large ice plates. Lặn qua exposed plates to shatter; hoặc arrows. Phase 2 adds tornadoes → steer around. Phá all 3 plates again. ~10 min, high damage. Mang healing meals không ghi đè kháng lạnh."),
 ("Mở chest trên yellow structure đầu. Nói chuyện Huck ở summit. Tiếp tục lên floating islands.",
  "Mở rương trên yellow structure đầu. Nói chuyện Huck ở summit. Tiếp tục lên floating islands."),
 ("Ship sails = launch pads. Ascend qua pillars.",
  "Ship sails = launch pads. Ascend qua pillars."),
 ("Mayaumekis & Kahatanaum Shrines remain fast travel.",
  "Mayaumekis & Kahatanaum Shrines remain fast travel."),
]
for a,b in reps:
    if a in s:
        s=s.replace(a,b)
open(p,"w",encoding="utf-8").write(s)
print("done")
PY