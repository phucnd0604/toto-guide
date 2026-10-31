p=r"E:\GameGuide\index.html"
s=open(p,encoding="utf-8").read()
reps=[
 # Shrine table headers
 ("<th>Trial</th>","<th>Thử thách</th>"),
 ("<th>Type</th>","<th>Loại</th>"),
 ("<th>Location</th>","<th>Vị trí</th>"),
 ("<th>Region</th>","<th>Vùng</th>"),
 # Markdown artifacts
 ("_(in a cave)_","(trong hang)"),
 # Remove "granular" word
 ("(granular)",""),
 ("granular",""),
 # Fix bắn mắt/corn
 ("bắn mắt/corn","bắn mắt/sừng"),
 # Fix Quay về to
 ("Quay về to ","Quay về "),
 # Fix bị gãy lever
 ("gắn icicle vào bị gãy lever","gắn icicle vào cần gạt bị gãy"),
 ("attach vào bị gãy lever","attach vào cần gạt bị gãy"),
 # Fix Hoàn thành sludge
 ("Hoàn thành sludge from waterfall","Dọn bùn từ waterfall"),
 ("Hoàn thành sludge from bubble emitter","Dọn bùn từ bubble emitter"),
 # Fix Construct ostility
 ("Gặp Construct ostility","Gặp Construct hung hăng"),
 # Fix Kyonosis
 ("Kyonosis","Kyononis"),
 # Fix shrine quest count
 ("152 shrines + 32 shrine quests","152 shrines + 31 shrine quests"),
 # Fix corrupted names
 ("Dyeing to Tìm It","Dyeing to Find It"),
 ("Cưỡi the Winds","Ride the Winds"),
 ("Cưỡi the Giant Horse","Ride the Giant Horse"),
 ("Tìm the Fifth Sage","Find the Fifth Sage"),
 # Fix Cold Resistance
 ("Cold Resistance","kháng lạnh"),
 # Fix bệ -> bục
 ("bệ","bục"),
 # Fix ostility
 ("ostility","ostility"),
]
for a,b in reps:
    if a in s:
        s=s.replace(a,b)
open(p,"w",encoding="utf-8").write(s)
print("done")
PY