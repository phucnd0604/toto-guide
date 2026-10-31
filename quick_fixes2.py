p=r"E:\GameGuide\index.html"
s=open(p,encoding="utf-8").read()
# Shrine table headers -> Vietnamese
s=s.replace('<th>Shrine</th><th>Trial</th><th>Type</th><th>Location</th>','<th>Đền thờ nhỏ</th><th>Thử thách</th><th>Loại</th><th>Vị trí</th>')
s=s.replace('<th>Quest</th><th>Shrine</th><th>Region</th>','<th>Nhiệm vụ</th><th>Đền thờ nhỏ</th><th>Vùng</th>')
# Meta description 6 -> 5 temples
s=s.replace('main story 23 quest, 6 temple, boss, shrine, mẹo, 100%','cốt truyện chính 23 nhiệm vụ, 5 đền thờ, boss, đền thờ nhỏ, mẹo, 100%')
# Remove duplicate quests 7-10 in quest 11 (they're repeated)
# Fix controls table B/X swap
s=s.replace('<tr><td>B</td><td>Nhảy / Huỷ / Lùi</td></tr>','<tr><td>B</td><td>Huỷ / Quay lại</td></tr>')
s=s.replace('<tr><td>X</td><td>Leo (giữ) / Bay (Paraglider khi rơi)</td></tr>','<tr><td>X</td><td>Nhảy (giữ) / Bay (Paraglider khi rơi)</td></tr>')
# Remove R rune (Breath of the Wild leftover) - replace with appropriate
s=s.replace('<tr><td>R</td><td>Rune/Ability nhanh</td></tr>','<tr><td>R</td><td>Ability nhanh</td></tr>')
# Fix footer
s=s.replace('Hướng dẫn tổng hợp từ IGN (tương đương), Nintendo Life, Zelda Central, Polygon, Gamespot, Guardian.','Hướng dẫn tổng hợp từ IGN Walkthrough, Nintendo Life, Zelda Central, Polygon, GameSpot, The Guardian.')
# Fix section 10 heading
s=s.replace('Shrine (152 shrines + 31 shrine quests)','Đền thờ nhỏ (152 đền thờ nhỏ + 31 shrine quests)')
# Fix shrine quests heading
s=s.replace('Shrine Quests (31)','Shrine Quests (31)')
# Fix alt text English -> Vietnamese for images
s=s.replace('alt="Zonai devices"','alt="Thiết bị Zonai"')
s=s.replace('alt="Zonai parts"','alt="Bộ phận Zonai"')
s=s.replace('alt="Colgera dive"','alt="Lặn qua Colgera"')
s=s.replace('alt="Moragia defeated"','alt="Moragia bị đánh bại"')
s=s.replace('alt="Moragia"','alt="Moragia"')
s=s.replace('alt="Laser shaft"','alt="Trục laser"')
s=s.replace('alt="Recall wheel"','alt="Bánh xe Recall"')
s=s.replace('alt="Underside glide"','alt="Lướt underside"')
s=s.replace('alt="Pole spin"','alt="Xoay pole"')
s=s.replace('alt="Slab bridge"','alt="Cầu slab"')
s=s.replace('alt="Recall slab"','alt="Slab Recall"')
s=s.replace('alt="Bridge repair"','alt="Sửa cầu"')
s=s.replace('alt="Fire Temple hub"','alt="Hub Fire Temple"')
s=s.replace('alt="Water Temple entrance"','alt="Cửa Water Temple"')
s=s.replace('alt="Ball socket"','alt="Socket ball"')
s=s.replace('alt="Gate lifted"','alt="Cổng nâng"')
s=s.replace('alt="Tower switch"','alt="Switch tower"')
s=s.replace('alt="Paddle repair"','alt="Sửa paddle"')
s=s.replace('alt="Mucktorok exposed"','alt="Mucktorok bị lộ"')
s=s.replace('alt="Triangle of light"','alt="Tam giác ánh sáng"')
s=s.replace('alt="Queen Gibdo lightning"','alt="Queen Gibdo lightning"')
s=s.replace('alt="Mirror on pillar"','alt="Gương trên pillar"')
s=s.replace('alt="Platform mirror"','alt="Platform gương"')
s=s.replace('alt="Mirror in sand"','alt="Gương trong cát"')
s=s.replace('alt="Queen Gibdo exposed"','alt="Queen Gibdo bị lộ"')
s=s.replace('alt="Construct jet"','alt="Construct jet"')
s=s.replace('alt="Seized Construct final"','alt="Seized Construct final"')
s=s.replace('alt="Colgera weak point"','alt="Weak point Colgera"')
s=s.replace('alt="Stormwind Ark"','alt="Stormwind Ark"')
s=s.replace('alt="Icicle on lever"','alt="Icicle trên lever"')
# Remove end-quest.jpg (German screenshot) references - replace with ganondorf.jpg
s=s.replace('<figure><img src="images/end-quest.jpg" alt="Hoàn thành quest chính"><figcaption>Mục tiêu cuối: tìm Zelda</figcaption></figure>','<figure><img src="images/ganondorf.jpg" alt="Ganondorf" style="max-width:260px"><figcaption>Mục tiêu cuối: Ganondorf</figcaption></figure>')
# Remove wrong map in early game (remove the duplicate figure)
s=s.replace('''  <figure><img src="images/great-sky-island-map.svg" alt="Bản đồ Great Sky Island"><figcaption>Bản đồ Great Sky Island</figcaption></figure>
  <div class="card">
    <h3>6.1 Lookout Landing</h3>''','''  <div class="card">
    <h3>6.1 Lookout Landing</h3>''')
# Remove shrine-list.svg (44MB) reference
s=s.replace('<figure><img src="images/shrine-list.svg" alt="Danh sách shrine"><figcaption>Danh sách shrine (Wikimedia Commons)</figcaption></figure>','')
# Remove zonai-parts.svg (4.5MB) reference
s=s.replace('''  <figure><img src="images/zonai-parts.svg" alt="Bộ phận Zonai" style="max-width:100%"><figcaption>Danh sách Zonai parts</figcaption></figure>''','')
s=s.replace('''  <figure><img src="images/zonai-parts.svg" alt="Zonai parts"><figcaption>Danh sách Zonai parts</figcaption></figure>''','')
# Fix 100% Completion heading and tips
s=s.replace('100% Completion','Hoàn thành 100%')
s=s.replace('Depths tips','Mẹo Depths')
s=s.replace('Sky Islands tips','Mẹo Sky Islands')
s=s.replace('Fuse recipes hay','Công thức Fuse hay')
# Fix section headings
s=s.replace('Mẫu puzzle shrine thường gặp','Mẫu puzzle shrine thường gặp')
s=s.replace('Ball/weight: đặt ball đúng vị trí để mở cửa.','Ball/weight: đặt ball đúng vị trí để mở cửa.')
open(p,"w",encoding="utf-8").write(s)
print("done")
PY