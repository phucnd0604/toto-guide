p=r"E:\GameGuide\index.html"
s=open(p,encoding="utf-8").read()
reps=[
 ("Gặp Construct ostility → đánh bằng cành cây hoặc bỏ qua.","Gặp Construct ostility → đánh bằng cành cây hoặc bỏ qua."),
 ("dán hook lên ván → ski-lift","dán hook lên ván → ski-lift"),
 ("Fuse fire fruit vào tên bắn lá","Fuse fire fruit vào tên bắn lá"),
 ("pedestal → cutscene → học Recall","pedestal → cutscene → học Recall"),
 ("Fast travel về Room of Awakening","Fast travel về Room of Awakening"),
 ("Paraglider (VITAL)","Paraglider (VITAL)"),
 ("Interact Shrine mọi shrine đi qua (không cần giải) để mở fast travel","Interact Shrine mọi shrine đi qua (không cần giải) để mở fast travel"),
 ("Quay Temple of Time, examine glyph → cửa mở một phần","Quay Temple of Time, examine glyph → cửa mở một phần"),
 ("Dive through exposed plates to shatter; or arrows. Phase 2 adds tornadoes → steer around. Phá all 3 plates again. ~10 min, high damage.","Dive through exposed plates to shatter; or arrows. Phase 2 adds tornadoes → steer around. Phá all 3 plates again. ~10 min, high damage."),
 ("Teba gives Great Eagle Bow, Tulin = Sage of Wind (Secret Stone). Mayaumekis & Kahatanaum Shrines remain fast travel.","Teba gives Great Eagle Bow, Tulin = Sage of Wind (Secret Stone). Mayaumekis & Kahatanaum Shrines remain fast travel."),
 ("Dive through Colgera's ice plate","Dive through Colgera's ice plate"),
 ("Dive crater, steer to dark ground","Dive crater, steer to dark ground"),
 ("Bring non-wooden gear (wood burns)","Bring non-wooden gear (wood burns)"),
 ("Moragia defeated","Moragia defeated"),
 ("Mucktorok exposed","Mucktorok exposed"),
 ("Queen Gibdo exposed","Queen Gibdo exposed"),
 ("Cần 2 cấp Cold Resistance (Snowquill set)","Cần 2 cấp Cold Resistance (Snowquill set)"),
 ("Weak points = purple sections trên body, covered by ice","Weak points = purple sections trên body, covered by ice"),
 ("Xóa sludge from waterfall, swim up","Xóa sludge from waterfall, swim up"),
 ("Rửa sludge shark with Sidon's water wave / Splash Fruit / water-fused arrow. May need multiple hits. Exposed: stun with arrow before it dives back","Rửa sludge shark with Sidon's water wave / Splash Fruit / water-fused arrow. May need multiple hits. Exposed: stun with arrow before it dives back"),
 ("Cần heat resistance ban ngày + electric resistance (Rubber armor)","Cần heat resistance ban ngày + electric resistance (Rubber armor)"),
 ("Keep moving (charge, sand tornadoes)","Keep moving (charge, sand tornadoes)"),
 ("When Riju's field ready, draw power, fire arrow at Queen inside field → strips armor","When Riju's field ready, draw power, fire arrow at Queen inside field → strips armor"),
 ("Attack, retreat, repeat","Attack, retreat, repeat"),
 ("Vulnerable only after elemental hit strips armor","Vulnerable only after elemental hit strips armor"),
 ("When pale, attack with strongest weapon/arrows","When pale, attack with strongest weapon/arrows"),
 ("At half health","At half health"),
 ("Phase 1: Block (ZL) telegraphed punches","Phase 1: Block (ZL) telegraphed punches"),
 ("Counter with short punches → throws it back","Counter with short punches → throws it back"),
 ("stand near turbine","stand near turbine"),
 ("Pass lasers","Pass lasers"),
 ("cross gap","cross gap"),
 ("defeat Construct","defeat Construct"),
 ("Ascend lên floor above","Ascend lên floor above"),
 ("repair bridge (Ultrahand join planks)","repair bridge (Ultrahand join planks)"),
 ("Move water bubble into gap","Move water bubble into gap"),
 ("carries current","carries current"),
 ("gate opens","gate opens"),
]
for a,b in reps:
    if a in s:
        s=s.replace(a,b)
# Revert broken shrine quest names (keep English quest names)
s=s.replace("Dyeing to Tìm It","Dyeing to Find It")
s=s.replace("Cưỡi the Winds","Ride the Winds")
s=s.replace("Cưỡi the Giant Horse","Ride the Giant Horse")
# Translate specific English words in prose
s=s.replace("ostility","ostility")
s=s.replace("broken","bị gãy")
s=s.replace("stole","đã cắp")
s=s.replace("checkpoint","checkpoint")
s=s.replace("Temp","Temp")
s=s.replace("cold resistance","kháng lạnh")
s=s.replace("gives","cho")
s=s.replace("remain fast travel","remain fast travel")
# fix figcaption English
s=s.replace('<figcaption>Dive through Colgera\'s ice plate</figcaption>','<figcaption>Lặn qua phiến băng của Colgera</figcaption>')
s=s.replace('<figcaption>Moragia defeated</figcaption>','<figcaption>Moragia bị đánh bại</figcaption>')
s=s.replace('<figcaption>Mucktorok exposed</figcaption>','<figcaption>Mucktorok bị lộ</figcaption>')
s=s.replace('<figcaption>Queen Gibdo exposed</figcaption>','<figcaption>Queen Gibdo bị lộ</figcaption>')
s=s.replace('<figcaption>Colgera dive</figcaption>','<figcaption>Lặn qua Colgera</figcaption>')
s=s.replace('<figcaption>Moragia defeated</figcaption>','<figcaption>Moragia bị đánh bại</figcaption>')
s=s.replace("Cần 2 cấp Cold Resistance (Snowquill set).","Cần 2 cấp Cold Resistance (Snowquill set).")
s=s.replace("Weak points = purple sections trên body, covered by ice.","Weak points = purple sections trên body, covered by ice.")
s=s.replace("Xóa sludge from waterfall, swim up.","Xóa sludge from waterfall, swim up.")
s=s.replace("Rửa sludge shark with Sidon's water wave / Splash Fruit / water-fused arrow.","Rửa sludge shark with Sidon's water wave / Splash Fruit / water-fused arrow.")
s=s.replace("May need multiple hits.","May need multiple hits.")
s=s.replace("Exposed: stun with arrow before it dives back.","Exposed: stun with arrow before it dives back.")
s=s.replace("Cần heat resistance ban ngày + electric resistance (Rubber armor).","Cần heat resistance ban ngày + electric resistance (Rubber armor).")
s=s.replace("Keep moving (charge, sand tornadoes).","Keep moving (charge, sand tornadoes).")
s=s.replace("When Riju's field ready, draw power, fire arrow at Queen inside field → strips armor.","When Riju's field ready, draw power, fire arrow at Queen inside field → strips armor.")
s=s.replace("Attack, retreat, repeat.","Attack, retreat, repeat.")
s=s.replace("Vulnerable only after elemental hit strips armor.","Vulnerable only after elemental hit strips armor.")
s=s.replace("When pale, attack with strongest weapon/arrows.","When pale, attack with strongest weapon/arrows.")
s=s.replace("At half health","At half health")
s=s.replace("Phase 1: Block (ZL) telegraphed punches.","Phase 1: Block (ZL) telegraphed punches.")
s=s.replace("Counter with short punches → throws it back.","Counter with short punches → throws it back.")
# UI terms
s=s.replace("auto-save có, save thủ công trước boss","auto-save có, save thủ công trước boss")
s=s.replace("Paraglider (VITAL)","Paraglider (VITAL)")
s=s.replace("Interact Shrine mọi shrine đi qua (không cần giải) để mở fast travel","Interact Shrine mọi shrine đi qua (không cần giải) để mở fast travel")
s=s.replace("Quay Temple of Time, examine glyph → cửa mở một phần","Quay Temple of Time, examine glyph → cửa mở một phần")
# Early game directions
s=s.replace("đi northwest đến","đi northwest đến")
open(p,"w",encoding="utf-8").write(s)
print("done")
PY