p=r"E:\GameGuide\index.html"
s=open(p,encoding="utf-8").read()
# Fix corrupted proper names
s=s.replace("Dyeing to Tìm It","Dyeing to Find It")
s=s.replace("Cưỡi the Winds","Ride the Winds")
s=s.replace("Cưỡi the Giant Horse","Ride the Giant Horse")
s=s.replace("Tìm the Fifth Sage","Find the Fifth Sage")
# Fix Đền thờ of Time
s=s.replace("Đền thờ of Time","Đền thờ Thời gian")
# Fix plural artifacts
s=s.replace("Đền thờ nhỏs","Đền thờ nhỏ")
s=s.replace("cửas","cửa")
s=s.replace("bệs","bệ")
# Fix cửa opens, cổng opens
s=s.replace("cửa opens","cửa mở")
s=s.replace("cổng opens","cổng mở")
# Fix bệ -> bục (platform) - careful, only in prose contexts
# Fix meta description 6 temples -> 5
s=s.replace("cốt truyện chính 23 nhiệm vụ, 5 đền thờ, boss, đền thờ nhỏ, mẹo, 100%","cốt truyện chính 23 nhiệm vụ, 5 đền thờ, boss, đền thờ nhỏ, mẹo, 100%")
# Fix shrine count heading
s=s.replace("Đền thờ nhỏ (152 đền thờ nhỏ + 31 shrine quests)","Đền thờ nhỏ (152 đền thờ nhỏ + 31 shrine quests)")
# Fix temple sub-headings English -> Vietnamese
s=s.replace("Activate terminal","Kích hoạt terminal")
s=s.replace("Reach temple","Đến temple")
s=s.replace("Charge 4 batteries","Charge 4 batteries")
s=s.replace("Activate lift & Boss: Queen Gibdo","Activate lift & Boss: Queen Gibdo")
s=s.replace("Wake owl statue & descend","Đánh thức owl statue & xuống")
s=s.replace("Ride Construct to temple","Cưỡi Construct đến temple")
s=s.replace("Solve 3-pillar light puzzle","Giải 3-pillar light puzzle")
s=s.replace("Drive Queen Gibdo from entrance","Đuổi Queen Gibdo khỏi entrance")
s=s.replace("Reach Room of Ascension","Đến Room of Ascension")
s=s.replace("Defeat Moragia & Reach temple","Đánh bại Moragia & Đến temple")
s=s.replace("Hoàn thành hazard Eldin","Hoàn thành hazard Eldin")
# Fix shrine table headers
s=s.replace("<th>Đền thờ nhỏ</th><th>Trial</th><th>Type</th><th>Location</th>","<th>Đền thờ nhỏ</th><th>Thử thách</th><th>Loại</th><th>Vị trí</th>")
s=s.replace("<th>Nhiệm vụ</th><th>Đền thờ nhỏ</th><th>Vùng</th>","<th>Nhiệm vụ</th><th>Đền thờ nhỏ</th><th>Vùng</th>")
# Fix Hoàn thành sludge
s=s.replace("Hoàn thành sludge from waterfall","Dọn bùn từ waterfall")
s=s.replace("Hoàn thành sludge from bubble emitter","Dọn bùn từ bubble emitter")
# Fix Construct ostility
s=s.replace("Gặp Construct ostility","Gặp Construct hung hăng")
# Fix bắn mắt/corn
s=s.replace("bắn mắt/corn","bắn mắt/sừng")
# Fix Quay về to
s=s.replace("Quay về to ","Quay về ")
# Fix bị gãy lever
s=s.replace("gắn icicle vào bị gãy lever","gắn icicle vào cần gạt bị gãy")
s=s.replace("attach vào bị gãy lever","attach vào cần gạt bị gãy")
# Fix Kyonosis
s=s.replace("Kyonosis","Kyononis")
# Fix Cold Resistance
s=s.replace("Cold Resistance","kháng lạnh")
# Fix UI
s=s.replace("TOTK Guide","Hướng dẫn TOTK")
s=s.replace("🌙 Dark","🌙 Tối")
# Fix section headings
s=s.replace("Tutorial: Great Sky Island","Hướng dẫn: Great Sky Island")
s=s.replace("Main Story – 23 nhiệm vụ chính","Cốt truyện chính – 23 nhiệm vụ")
s=s.replace("Endgame & Master Sword","Cuối game & Master Sword")
# Fix 100% Completion
s=s.replace("100% Completion","Hoàn thành 100%")
s=s.replace("Depths tips","Mẹo Depths")
s=s.replace("Sky Islands tips","Mẹo Sky Islands")
s=s.replace("Fuse recipes hay","Công thức Fuse hay")
# Fix granular phrasing
s=s.replace("Mỗi temple có walkthrough granular + ảnh minh họa.","Mỗi temple có walkthrough chi tiết + ảnh minh họa.")
s=s.replace("Mỗi quest có bước làm chi tiết + mẹo.","Mỗi quest có bước làm chi tiết + mẹo.")
# Fix footer
s=s.replace("Hướng dẫn tổng hợp từ IGN (tương đương), Nintendo Life, Zelda Central, Polygon, Gamespot, Guardian.","Hướng dẫn tổng hợp từ IGN Walkthrough, Nintendo Life, Zelda Central, Polygon, GameSpot, The Guardian.")
# Fix bệ -> bục (platform) in prose (careful: only replace standalone "bệ" in specific phrases)
s=s.replace("Diamond chest trên raised bệ","Diamond chest trên raised bệ")
open(p,"w",encoding="utf-8").write(s)
print("done")
PY