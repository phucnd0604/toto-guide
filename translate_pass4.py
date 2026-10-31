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
 ("Dive through exposed plates to shatter; or arrows. Phase 2 adds tornadoes → steer around. Break all 3 plates again. ~10 min, high damage.","Dive through exposed plates to shatter; or arrows. Phase 2 adds tornadoes → steer around. Break all 3 plates again. ~10 min, high damage."),
 ("Hold control stick (roll Yunobo away first). Steer toward each head, command Yunobo charge.","Hold control stick (roll Yunobo away first). Steer toward each head, command Yunobo charge."),
 ("Follow trail: Yona, Jiahto, Sidon → King Dorephan, Floating Scales Island, Ancient Zora Waterworks → raise water → waterfall opens route to Wellspring Island.","Follow trail: Yona, Jiahto, Sidon → King Dorephan, Floating Scales Island, Ancient Zora Waterworks → raise water → waterfall opens route to Wellspring Island."),
 ("Use Wing + Zonai devices cross to Sidon","Use Wing + Zonai devices cross to Sidon"),
 ("activate travel point","activate travel point"),
 ("Faucet1 B1 behind flames (Sidon shield, Hover Stone ball socket)","Faucet1 B1 behind flames (Sidon shield, Hover Stone ball socket)"),
 ("Keep moving (charge, sand tornadoes)","Keep moving (charge, sand tornadoes)"),
 ("When Riju's field ready, draw power, fire arrow at Queen inside field → strips armor","When Riju's field ready, draw power, fire arrow at Queen inside field → strips armor"),
 ("Attack, retreat, repeat","Attack, retreat, repeat"),
 ("Break icicles blocking opening (fire)","Break icicles blocking opening (fire)"),
 ("Inside: large spinning wheel over gap","Inside: large spinning wheel over gap"),
 ("Dùng Recall trên wheel → reverse spin → ride across","Dùng Recall trên wheel → reverse spin → ride across"),
 ("Room tiếp: lever Ultrahand mở bars","Room tiếp: lever Ultrahand mở bars"),
 ("wall 2 gears thiếu connector → shoot down large icicle, attach between gears → gear turn → gate opens → activate turbine","wall 2 gears thiếu connector → shoot down large icicle, attach between gears → gear turn → gate opens → activate turbine"),
 ("Chest Sapphire trong cell (pull through bars bằng Ultrahand)","Chest Sapphire trong cell (pull through bars bằng Ultrahand)"),
 ("Glide down to basement entrance","Glide down to basement entrance"),
 ("Sidon's shield pass flame jets","Sidon's shield pass flame jets"),
 ("Set into socket on far wall, activate Hover Stone → ball stays","Set into socket on far wall, activate Hover Stone → ball stays"),
 ("Glide across spike pit to stone ball","Glide across spike pit to stone ball"),
 ("Attach ball to Hover Stone, carry across gap","Attach ball to Hover Stone, carry across gap"),
 ("Ride updraft to 4F","Ride updraft to 4F"),
 ("Recall disc until gaps line up","Recall disc until gaps line up"),
 ("drive Stake into wall to stop rotation","drive Stake into wall to stop rotation"),
 ("Beam hits target → return upstairs, follow route to last battery, charge with Riju","Beam hits target → return upstairs, follow route to last battery, charge with Riju"),
 ("Phase 1: Block (ZL) telegraphed punches","Phase 1: Block (ZL) telegraphed punches"),
 ("Counter with short punches","Counter with short punches"),
 ("Aim cannon shot at chest (hold ~1s)","Aim cannon shot at chest (hold ~1s)"),
 ("Skydive xuống Hyrule Field → đi bộ đến Lookout Landing (trung tâm map)","Skydive xuống Hyrule Field → đi bộ đến Lookout Landing (trung tâm map)"),
 ("Gặp Purah","Gặp Purah"),
 ("Kích hoạt Skyview Tower tại Lookout Landing để mở bản đồ","Kích hoạt Skyview Tower tại Lookout Landing để mở bản đồ"),
 ("Nói chuyện Purah → nhận nhiệm vụ Regional Phenomena (4 vùng), đánh dấu 4 vùng trên map","Nói chuyện Purah → nhận nhiệm vụ Regional Phenomena (4 vùng), đánh dấu 4 vùng trên map"),
 ("Nói chuyện Robbie → quest Camera Work in the Depths → Depths lần đầu → Autobuild sau","Nói chuyện Robbie → quest Camera Work in the Depths → Depths lần đầu → Autobuild sau"),
 ("Nhận Archaic Warm Greaves (đã nhặt)","Nhận Archaic Warm Greaves (đã nhặt)"),
 ("Đến Castle Ruins theo main quest → về Lookout Landing → Paraglider","Đến Castle Ruins theo main quest → về Lookout Landing → Paraglider"),
 ("Nhận ngựa: đi northwest đến New Serenne Stable (-1349, 0736, 0085)","Nhận ngựa: đi northwest đến New Serenne Stable (-1349, 0736, 0085)"),
 ("Đăng ký ngựa, bắt đầu Pony Points","Đăng ký ngựa, bắt đầu Pony Points"),
 ("Skyview Tower đầu tiên: Lindor's Brow (-1903, 1243, 0297) northwest","Skyview Tower đầu tiên: Lindor's Brow (-1903, 1243, 0297) northwest"),
 ("Vùng dễ, tài nguyên nhiều, gần Rito","Vùng dễ, tài nguyên nhiều, gần Rito"),
 ("Interact Shrine mọi shrine đi qua (không cần giải) để mở fast travel","Interact Shrine mọi shrine đi qua (không cần giải) để mở fast travel"),
 ("Shrine hữu ích sớm: Kyonosis, Ekochiu, Makasura, Sinakawak, Orochium","Shrine hữu ích sớm: Kyonosis, Ekochiu, Makasura, Sinakawak, Orochium"),
 ("Autobuild: theo Robbie → Depths → A Mystery in the Depths → Great Abandoned Central Mine","Autobuild: theo Robbie → Depths → A Mystery in the Depths → Great Abandoned Central Mine"),
 ("Ganondorf pha 1: né đòn, parry, Sage Vows, Master Sword","Ganondorf pha 1: né đòn, parry, Sage Vows, Master Sword"),
 ("Demon Dragon pha 2: bay paraglider, Fuse light vào tên, bắn mắt/corn","Demon Dragon pha 2: bay paraglider, Fuse light vào tên, bắn mắt/corn"),
 ("Skydive bắt Zelda","Skydive bắt Zelda"),
]
for a,b in reps:
    if a in s:
        s=s.replace(a,b)
# generic English word replacements (whole words only via simple replace)
generics=[
 ("Clear ","Xóa "),("Speak ","Nói "),("Open ","Mở "),("Travel ","Đi "),("Defeat ","Đánh bại "),
 ("Pick ","Nhặt "),("attach ","gắn "),("turn ","xoay "),("raise ","nâng "),
 ("Break ","Phá "),("Skydive","Skydive"),("Fast travel","Fast travel"),("examine glyph","examine glyph"),
 ("pedestal","pedestal"),("cutscene","cutscene"),("VITAL","VITAL"),("Interact","Interact"),
 ("Weak points","Weak points"),("covered by ice","covered by ice"),
 ("Reward:","Reward:"),("Reward ","Reward "),
 ("Follow ","Theo "),("Use ","Dùng "),("Cross ","Vượt "),("Climb ","Leo "),
 ("Glide ","Lướt "),("Activate ","Kích hoạt "),("Return ","Quay về "),("Collect ","Nhận "),
 ("Defeat ","Đánh bại "),("Reach ","Đến "),("Open ","Mở "),
]
for a,b in generics:
    if a in s:
        s=s.replace(a,b)
open(p,"w",encoding="utf-8").write(s)
print("done")
PY