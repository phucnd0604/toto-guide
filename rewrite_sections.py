import re
html=open(r"E:\GameGuide\index.html",encoding="utf-8").read()

# New Main Story section (clean Vietnamese)
main_story = '''<section id="main-story" class="content">
  <h2><span class="num">07</span> Main Story – 23 nhiệm vụ chính</h2>
  <p>Theo thứ tự Zelda Central. Mỗi quest có bước làm chi tiết + mẹo. Temple puzzle chi tiết xem phần Temple.</p>
  <figure><img src="images/end-quest.jpg" alt="Hoàn thành quest chính"><figcaption>Mục tiêu cuối: tìm Zelda</figcaption></figure>

  <div class="quest" id="q1"><div class="title">1. The Closed Door</div><div class="meta">Great Sky Island</div>
  <details open><summary>Chi tiết</summary>
    <ol><li>Hoàn thành Ukouh Shrine (Ultrahand), In-isa Shrine (Fuse), Gutanbac Shrine (Ascend).</li><li>Nhận Energy Cell.</li><li>Quay Temple of Time, examine glyph → cửa mở một phần.</li><li>Vào trong → pedestal → cutscene → học Recall.</li><li>Dùng Recall trên bánh xe nước phía sau để ra sau temple.</li></ol>
    <p><strong>Mẹo:</strong> Thu thập 4 Light of Blessing → đổi Heart Container tại Goddess Statue.</p>
  </details></div>

  <div class="quest" id="q2"><div class="title">2. To the Kingdom of Hyrule</div><div class="meta">Surface</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Nhảy từ Temple of Time, skydive xuống Hyrule Field.</li><li>Đi bộ theo đường chính đến Lookout Landing (trung tâm map).</li><li>Gặp Purah.</li></ol>
    <p><strong>Mẹo:</strong> Tránh enemy lớn; nhặt nguyên liệu dọc đường.</p>
  </details></div>

  <div class="quest" id="q3"><div class="title">3. Find Princess Zelda</div><div class="meta">Lookout Landing / Temple of Time</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Nhận Purah Pad.</li><li>Mở Temple of Time (đã học Recall).</li><li>Hoàn thành Nachoyah Shrine (Recall test: chỉnh kim đồng hồ chồng lên nhau cùng chiều).</li><li>Nhận Heart Container từ Goddess Statue.</li></ol>
  </details></div>

  <div class="quest" id="q4"><div class="title">4. Regional Phenomena</div><div class="meta">4 vùng</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Đến Hebra, Eldin, Lanayru, Gerudo.</li><li>Hoàn thành mỗi Temple (xem phần Temple).</li><li>Báo cáo Purah tại Lookout Landing.</li></ol>
    <p><strong>Thứ tự khuyến nghị:</strong> Rito (Wind) → Goron (Fire) → Zora (Water) → Gerudo (Lightning).</p>
  </details></div>

  <div class="quest" id="q5"><div class="title">5. Tulin of Rito Village</div><div class="meta">Hebra – Wind Temple</div>
  <details open><summary>Chi tiết</summary>
    <ol>
      <li><strong>Nói chuyện Teba & Tulin:</strong> Đến Rito Village (Lake Totori, NW Lookout Landing). Cầu chính bị gãy → thả Hylian Pine Cone vào lửa để tạo luồng khí nóng rồi lướt, hoặc xây cầu/lướt từ Rospro Pass Skyview Tower. Leo lên upper village nói chuyện Teba, Saki, Tulin. Teba chỉ Harth ở Hebra Trailhead Lodge (~-3581,2252,0141). Activate Gatakis Shrine trước.</li>
      <li><strong>Tìm Harth:</strong> Đi theo đường về phía bắc. Lodge đánh dấu bằng 2 đống lửa. Harth: Tulin đi với Laissa & Gesane đến Hebra South Summit Cave. Leo 2 thang sau lodge, theo đường núi, lửa trại, cửa hang (~-3384,2485,0309).</li>
      <li><strong>Tìm trong hang:</strong> Nói chuyện Laissa. Dây gai → đốt (Fire Fruit). Phòng lớn có luồng khí nóng → lướt lên. Đốt lại lửa trại lạnh (đá lửa/mũi tên Fire Fruit). Thả Hylian Pine Cone → luồng khí nóng → lối đi trên. Gesane: Tulin đi đến cây tuyết tùng đơn độc trên Tolonto Peak.</li>
      <li><strong>Tìm Tulin trên Tolonto Peak:</strong> Ra khỏi hang, leo về phía bắc đến cây tuyết tùng đơn độc (~-3152,2688,0567). Dùng gió tự nhiên. Nói chuyện Tulin. Aerocuda đã cắp Swallow Bow. Tulin gia nhập, cho gust.</li>
      <li><strong>Lấy lại cung:</strong> Ra lệnh Tulin gust → lướt đến platform. Bắn Aerocuda → rơi cung. Thêm Aerocuda + Bokoblin đến; bắn từ platform. Harth & Gesane đuổi kịp → điều tra bão trên Hebra Peak.</li>
      <li><strong>Leo Hebra Peak:</strong> Theo marker leo núi (yellow stone ledges). Dùng gust vượt khe. Mở chest trên yellow structure đầu. Nói chuyện Huck ở summit. Tiếp tục lên floating islands.</li>
      <li><strong>Rising Island Chain:</strong> Lướt + gust. Ship sails = launch pads. Ascend qua pillars. Activate Mayaumekis Shrine (chest phía sau trên platform trái qua Ascend). Balloon platform: metal plate + Flame Emitter dưới Balloon qua Ultrahand. Activate Kahatanaum Shrine (checkpoint). Temp cực lạnh → kiểm tra kháng lạnh. Lặn vào tâm mây → cutscene → Stormwind Ark (Wind Temple).</li>
      <li><strong>Mở 5 khóa:</strong> Activate travel point trên deck, examine terminal gần central hatch. Locks 1-5 (xem Wind Temple): (1) gắn icicle vào broken lever nâng gate, gust turbine; (2) lướt updraft lên roof tall structure phía bắc, mở metal doors, drop qua lasers, paraglider đến side opening, gust; (3) phá icicles, Recall spinning platform, gắn icicle giữa gears, gust; (4) lướt left side hull, lower passage, rơi xuống underside, đánh bại Construct, gust; (5) gust cross gap, Ascend, gắn stone slab vào cog, xoay cho đến khi door opens, Recall cog, leo qua nhanh, gust turbine cuối. Quay về terminal → mở hatch.</li>
      <li><strong>Đánh bại Colgera:</strong> 3 large ice plates. Lặn qua exposed plates to shatter; hoặc arrows. Phase 2 adds tornadoes → steer around. Phá all 3 plates again. ~10 min, high damage. Mang healing meals không ghi đè cold resistance.</li>
      <li><strong>Quay về Rito Village:</strong> Nhận Heart Container, nói chuyện Tulin. Teba gives Great Eagle Bow, Tulin = Sage of Wind (Secret Stone). Mayaumekis & Kahatanaum Shrines remain fast travel. Tính vào Regional Phenomena.</li>
    </ol>
    <figure><img src="images/zelda-tears-of-the-kingdom-tulin-of-rito-village-colgera-dive-p45-00-39-40-1024x576.webp" alt="Colgera dive"><figcaption>Lặn qua phiến băng của Colgera</figcaption></figure>
  </details></div>

  <div class="quest" id="q6"><div class="title">6. Yunobo of Goron City</div><div class="meta">Eldin – Fire Temple</div>
  <details><summary>Chi tiết</summary>
    <ol>
      <li><strong>Nói chuyện Bludo:</strong> Goron City, Eldin. Bludo near Marbled Rock Roast pile. Points to YunoboCo HQ phía bắc. Activate Marakuguc Shrine.</li>
      <li><strong>Đi đến HQ:</strong> NE exit, minecart tracks. Fan on cart, left rail, ride. Hoặc đi bộ. Cave entrance: nói chuyện Offrak & Slergo (first option) → inside. Cần Flame Guard (Flamebreaker/fireproof elixir).</li>
      <li><strong>Phá mặt nạ:</strong> Yunobo masked, rolls. Dodge, he crashes wall → stunned → strike mask. Lặp 3 lần. Yunobo joins, gains charge attack. Aim at red boulders blocking exit (2 charges).</li>
      <li><strong>Cưỡi tracks đến Death Mountain:</strong> West side tracks. Fan on cart, ride uphill, Yunobo charge break rocks/enemies. At junctions use green switch targets. Sitsum Shrine near upper tracks. Nói chuyện Yunobo at summit → Moragia.</li>
      <li><strong>Đánh bại Moragia:</strong> Fanplane at crater edge. Position with Ultrahand, climb aboard, activate fans. Hold control stick (roll Yunobo away first). Steer toward each head, command Yunobo charge. 1 hit/head. Keep level.</li>
      <li><strong>Đến Fire Temple qua Depths:</strong> Dive crater, steer to dark ground. Activate Mustis Lightroot. Follow marker west, Brightbloom Seeds light, avoid gloom, Yunobo break red boulders. Send Yunobo into red rock sealing entrance. Inside: examine green pedestal (5 gongs). Bring non-wooden gear (wood burns).</li>
      <li><strong>Rung 5 gong:</strong> Gong1 southern (Hydrant slabs bridge, Yunobo charge barrier). Gong2 western (rails, Recall slab). Gong3 southwestern (rocket cart, repair bridge, Recall block up). Gong4 northern. Gong5 northern 1F.</li>
      <li><strong>Đánh bại Marbled Gohma:</strong> Fuse stone to arrows hit eyes when open; when down, attack legs; dodge rocks. Reward Heart Container + Vow of Yunobo (Fire). Clear Eldin hazard.</li>
      <li><strong>Quay về Goron City:</strong> Report Bludo. Yunobo becomes Sage of Fire (Secret Stone).</li>
    </ol>
    <figure><img src="images/zelda-tears-of-the-kingdom-yunobo-goron-city-moragia-defeated-p87-00-38-10-1024x576.webp" alt="Moragia defeated"><figcaption>Moragia bị đánh bại</figcaption></figure>
  </details></div>

  <div class="quest" id="q7"><div class="title">7. The Sludge-Covered Statue</div><div class="meta">Lanayru – Zora</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Đến Zora's Domain (bị sludge).</li><li>Rửa tượng bằng Splash Fruit.</li><li>Nói Yona.</li><li>Đến Mipha Court gặp Sidon.</li></ol>
  </details></div>

  <div class="quest" id="q8"><div class="title">8. The Broken Slate</div><div class="meta">Zora's Domain</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Rửa bùn ở mảnh phiến của Jiahto tại Toto Lake.</li><li>Ghép vào tường → đọc manh mối về bầu trời.</li></ol>
  </details></div>

  <div class="quest" id="q9"><div class="title">9. Restoring the Zora Armor</div><div class="meta">Zora's Domain</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Mang Ancient Arowana cho Yona ở Zora's Domain.</li><li>Nhận Zora Armor (bơi ngược thác).</li></ol>
    <p><strong>Mẹo:</strong> Ancient Arowana ở Lulu Lake / Zora River.</p>
  </details></div>

  <div class="quest" id="q10"><div class="title">10. Clues to the Sky</div><div class="meta">Lanayru</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Nhận King's Scale từ Dorephan ở Pristine Sanctum (dưới Zora's Domain).</li><li>Bắn một King's Scale qua stone tear trên Floating Scales Island (sky).</li></ol>
  </details></div>

  <div class="quest" id="q11"><div class="title">11. Sidon of the Zora</div><div class="meta">Lanayru – Water Temple</div>
  <details><summary>Chi tiết</summary>
    <ol>
      <li><strong>Sludge-Covered Statue:</strong> Đến Zora's Domain (bị sludge). Rửa tượng bằng Splash Fruit. Nói Yona. Đến Mipha Court gặp Sidon.</li>
      <li><strong>Broken Slate:</strong> Rửa bùn ở mảnh phiến của Jiahto tại Toto Lake. Ghép vào tường → đọc manh mối về bầu trời.</li>
      <li><strong>Restoring Zora Armor:</strong> Mang Ancient Arowana cho Yona → nhận Zora Armor (bơi ngược thác). Ancient Arowana ở Lulu Lake/Zora River.</li>
      <li><strong>Clues to the Sky:</strong> Nhận King's Scale từ Dorephan ở Pristine Sanctum. Bắn qua stone tear trên Floating Scales Island.</li>
      <li><strong>Đến Water Temple:</strong> Follow trail: Yona, Jiahto, Sidon → King Dorephan, Floating Scales Island, Ancient Zora Waterworks → raise water → waterfall opens route to Wellspring Island. Wellspring Island low gravity; use water bubbles (Recall). Climb waterfalls, use Wing + Zonai devices cross to Sidon. Defeat Construct, swim up waterfall, activate travel point.</li>
      <li><strong>4 Faucets:</strong> Faucet1 B1 behind flames (Sidon shield, Hover Stone ball socket). Faucet2 left bubble lift (gate+Hover Stone). Faucet3 lower-right spinning tower (water-fused arrow clean switch). Faucet4 upper-right repair wheel (stone slab paddle + bubble current).</li>
      <li><strong>Đánh bại Mucktorok:</strong> Rửa sludge shark with Sidon's water wave / Splash Fruit / water-fused arrow. May need multiple hits. Exposed: stun with arrow before it dives back. Attack while stunned. At half health spread sludge → clear with wave. Keese Eyeball arrow when out of reach. Hydrants around platform clear sludge. Reward Heart Container + Vow of Sidon (Water). Clear sludge Zora's Domain.</li>
    </ol>
    <figure><img src="images/zelda-tears-of-the-kingdom-water-temple-mucktorok-exposed-p150-00-43-50-1024x576.webp" alt="Mucktorok exposed"><figcaption>Mucktorok bị lộ</figcaption></figure>
  </details></div>

  <div class="quest" id="q12"><div class="title">12. Riju of Gerudo Town</div><div class="meta">Gerudo – Lightning Temple</div>
  <details><summary>Chi tiết</summary>
    <ol>
      <li><strong>Đến Gerudo Town:</strong> Gerudo Town bị cát bão. Luyện Riju (lightning training).</li>
      <li><strong>Phòng thủ Kara Kara Bazaar & Gerudo Town:</strong> Phòng thủ các đợt Gibdo.</li>
      <li><strong>Giải 3-pillar light puzzle:</strong> Pillar1 climb top break cracked floor → light; mirror send beam. Pillar2 smaller tower turn wheel counterclockwise. Pillar3 break floor, repair wheel with sticks+platforms, turn → triangle forms → altar reveals → raise Lightning Temple.</li>
      <li><strong>Đuổi Queen Gibdo khỏi entrance:</strong> Riju lightning on purple hive above doors. Queen emerges. Keep moving (charge, sand tornadoes). When Riju's field ready, draw power, fire arrow at Queen inside field → strips armor. Attack, retreat, repeat. She retreats. Riju lightning on hive blocking entrance → break → enter.</li>
      <li><strong>Đến Room of Ascension:</strong> Entry room Korok-Frond Guster blow sand from floor switch. B1: collapsing floor, flame jets, rolling fireballs (Ascend if fall, Recall fireball). Mirror angle beam to yellow switch → door. Climb to Room of Ascension, activate terminal → travel point + 4 batteries.</li>
      <li><strong>Charge 4 batteries:</strong> Battery1 hidden room behind terminal (Ultrahand sandstone blocks). Room of Natural Light (stone upright in beam + mirror, slide pillars). Room of Offered Light (grate+balloon platform mirror). Cross flame shaft (glide between flames). Room of Light and Shade (rotating discs, mirror target, Stake).</li>
      <li><strong>Activate lift & Boss Queen Gibdo:</strong> Return to Room of Ascension, terminal → lift to 7F. Prepare healing, strong weapons, arrows with Bomb Flowers/elemental. Vulnerable after elemental hit (Riju lightning). Keep moving. When pale, attack. At half health: 5 tornadoes + 4 hives summon Gibdos → destroy hives with Riju lightning/Bomb Flower arrows → sunlight strips Gibdo armor. Finish Queen. Reward Heart Container + Vow of Riju (Lightning). Clear sandstorm Gerudo.</li>
    </ol>
    <figure><img src="images/zelda-tears-of-the-kingdom-lightning-temple-queen-gibdo-exposed-p186-00-30-50-1024x576.webp" alt="Queen Gibdo exposed"><figcaption>Queen Gibdo bị lộ</figcaption></figure>
  </details></div>

  <div class="quest" id="q13"><div class="title">13. Secret of the Ring Ruins</div><div class="meta">Necluda / Sky</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Chụp ảnh Ring Ruin tablet (Kakariko).</li><li>Tìm Charged armor (Thunderhead Isles).</li><li>Dâng Zonai Charge.</li><li>Đến Dragonhead Island.</li></ol>
  </details></div>

  <div class="quest" id="q14"><div class="title">14. Guidance from Ages Past</div><div class="meta">Depths / Sky</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Theo beam của mask xuống Depths.</li><li>Rebuild Mineru's Construct (thu thập parts).</li><li>Đánh Seized Construct.</li></ol>
    <p><strong>Mẹo:</strong> Xem phần Spirit Temple cho chi tiết boss.</p>
  </details></div>

  <div class="quest" id="q15"><div class="title">15. Find the Fifth Sage</div><div class="meta">Lookout Landing / Dragonhead Island</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Nói Purah, Paya, Tauro.</li><li>Theo Zonai relic trên Dragonhead Island.</li><li>Gặp Mineru (Sage of Spirit).</li></ol>
  </details></div>

  <div class="quest" id="q16"><div class="title">16. Camera Work in the Depths</div><div class="meta">Depths</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Nhảy vào Hyrule Field Chasm.</li><li>Thắp 2 Lightroots.</li><li>Chụp ảnh statue.</li><li>Nhận Zonaite x5 từ Josha.</li></ol>
  </details></div>

  <div class="quest" id="q17"><div class="title">17. A Mystery in the Depths</div><div class="meta">Depths</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Theo trail tượng từ Iayusus Lightroot.</li><li>Đến Great Abandoned Central Mine.</li><li>Học Autobuild.</li></ol>
  </details></div>

  <div class="quest" id="q18"><div class="title">18. Crisis at Hyrule Castle</div><div class="meta">Hyrule Castle / Lookout Landing</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Tìm Captain Hoz tại First Gatehouse.</li><li>Báo cáo Purah.</li><li>Nhận Paraglider.</li><li>Kích hoạt Lookout Landing Skyview Tower.</li></ol>
  </details></div>

  <div class="quest" id="q19"><div class="title">19. Trail of the Master Sword</div><div class="meta">Great Hyrule Forest / Depths</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Vào Korok Forest qua Depths (Lost Woods).</li><li>Đánh Phantom Ganon.</li><li>Nói Great Deku Tree.</li></ol>
  </details></div>

  <div class="quest" id="q20"><div class="title">20. Recovering the Hero's Sword</div><div class="meta">Sky</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Theo marker Light Dragon.</li><li>Phóng từ Skyview Tower.</li><li>Kéo Master Sword từ đầu rồng.</li></ol>
    <p><strong>Mẹo:</strong> Cần đủ stamina/heart để kéo; làm quest sau khi có đủ.</p>
  </details></div>

  <div class="quest" id="q21"><div class="title">21. Impa and the Geoglyphs</div><div class="meta">Tabantha</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Gặp Impa gần New Serenne Stable.</li><li>Sửa balloon bằng Ultrahand.</li><li>Bay lên glide đến Dragon's Tear → memory.</li></ol>
  </details></div>

  <div class="quest" id="q22"><div class="title">22. The Dragon's Tears</div><div class="meta">Map</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Tìm geoglyphs trên map (Impa quest).</li><li>Mỗi Dragon's Tear cho memory.</li><li>Có 12 tears + 1 hidden (13 total).</li></ol>
  </details></div>

  <div class="quest" id="q23"><div class="title">23. Destroy Ganondorf</div><div class="meta">Hyrule Castle Depths – Final</div>
  <details><summary>Chi tiết</summary>
    <ol><li>Xuống dưới Hyrule Castle (chasm).</li><li>Đánh quân đội Phantom Ganon.</li><li>Đánh Ganondorf (pha 1).</li><li>Đánh Demon Dragon (pha 2): bay paraglider, Fuse light vào tên, bắn mắt/corn.</li><li>Skydive bắt Zelda.</li></ol>
    <p><strong>Mẹo:</strong> Xem phần Endgame cho chi tiết boss.</p>
  </details></div>
</section>
'''

# Replace main-story section
html = re.sub(r'<section id="main-story".*?</section>\s*(?=<section id="temples")', main_story + "\n\n", html, flags=re.S, count=1)

# New Temples section (clean Vietnamese)
temples = '''<section id="temples" class="content">
  <h2><span class="num">08</span> Temple & Boss (chi tiết)</h2>
  <p>Mỗi temple có walkthrough granular + ảnh minh họa.</p>

  <div class="card">
    <h3 id="wind">🌬️ Wind Temple (Rito) – Boss: Colgera</h3>
    <p><strong>Vùng:</strong> Hebra. <strong>Quest:</strong> Tulin of Rito Village. Cần 2 cấp kháng lạnh (Snowquill set).</p>
    <h4>Đường đến</h4>
    <ul><li>Giúp Tulin lấy cung ở Hebra South Summit Cave → Tulin gia nhập, mở Wind ability.</li><li>Dùng Tulin's gust khi lướt để vượt khe giữa floating islands.</li><li>Fabric sails trên ships bounce Link lên cao; dùng Ascend khi có trần rắn.</li><li>Kahatanaum Shrine gần đỉnh: activate trước (fast travel).</li><li>Rơi qua opening ở tâm bão → Stormwind Ark.</li></ul>
    <figure><img src="images/zelda-tears-of-the-kingdom-wind-temple-stormwind-ark-below-p44-00-59-02-1024x576.webp" alt="Stormwind Ark"><figcaption>Stormwind Ark trong tâm bão</figcaption></figure>
    <h4>Activate terminal</h4>
    <ul><li>Activate green terminal ở main deck → fast travel + đánh dấu 5 turbine trên map. Map tabs: 1F, B1, B2.</li></ul>
    <h4>5 Turbine</h4>
    <details open><summary>Turbine 1: Repair lever (1F bow)</summary><p>Pick icicle bằng Ultrahand → attach vào broken lever → turn để raise gate. Vào trong, stand near turbine, dùng Tulin's gust. Room bên cạnh: lever tương tự → chest Opal.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-wind-temple-icicle-on-lever-p45-00-03-50-1024x576.webp" alt="Icicle on lever"></figure></details>
    <details><summary>Turbine 2: Drop through tower (1F→B1)</summary><p>Glide từ updraft trung tâm lên roof tall structure phía bắc. Mở metal doors bằng Ultrahand, drop vào shaft. Tránh red lasers. Paraglider near bottom → turbine alcove. Chest Soldier Blade trên ledge.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-wind-temple-tower-laser-shaft-p45-00-06-35-1024x576.webp" alt="Laser shaft"></figure></details>
    <details><summary>Turbine 3: Spinning wheel (B1)</summary><p>Break icicles blocking opening (fire). Inside: large spinning wheel over gap. Dùng Recall trên wheel → reverse spin → ride across. Room tiếp: lever Ultrahand mở bars; wall 2 gears thiếu connector → shoot down large icicle, attach between gears → gear turn → gate opens → activate turbine. Chest Sapphire trong cell (pull through bars bằng Ultrahand).</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-wind-temple-wheel-recall-start-p45-00-28-30-1024x576.webp" alt="Recall wheel"></figure></details>
    <details><summary>Turbine 4: Underside (B2)</summary><p>Ladder từ B1 xuống B2, follow icy corridor past Construct (ice blocks hide Time Bomb/Portable Pot). Leave window, glide beneath hull, dùng Tulin's gust cross to underside deck. Defeat Construct, activate turbine. Có thể dive thẳng từ main deck.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-wind-temple-underside-glide-p45-00-12-13-1024x576.webp" alt="Underside glide"></figure></details>
    <details><summary>Turbine 5: Pole spin (B1→1F)</summary><p>Corridor có red lasers + broken gap. Pass lasers (Ruby chest beyond), cross gap bằng Tulin's gust, defeat Construct, Ascend lên floor above. Pole treo trần: attach stone slab làm fin, dùng Tulin's gust spin pole → door opens. Climb ladder nhanh (door không giữ lâu). Lên 1F, activate turbine cuối.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-wind-temple-pole-slab-fin-p45-00-15-58-1024x576.webp" alt="Pole spin"></figure></details>
    <h4>Boss: Colgera</h4>
    <ul><li>Weak points = purple sections trên body, covered by ice.</li><li>Bắn tên từ dưới (khó) hoặc dive từ trên (đóng paraglider khi Colgera expose ice trên upper side sau khi fire spikes).</li><li>Fire Fruit/Bomb Flower phá ice + damage 1 shot; Keese Eyeball giúp track.</li><li>Pha 2: Colgera thêm tornadoes. Dùng Tulin's gust dodge/reposition; updrafts regain height.</li><li>Reward: Heart Container + Vow of Tulin (Wind ability khi lướt). Clear blizzard Hebra.</li></ul>
    <figure><img src="images/zelda-tears-of-the-kingdom-wind-temple-colgera-purple-core-p45-00-41-05-1024x576.webp" alt="Colgera weak point"></figure>
  </div>

  <div class="card">
    <h3 id="fire">🔥 Fire Temple (Goron) – Boss: Marbled Gohma</h3>
    <p><strong>Vùng:</strong> Eldin/Death Mountain. <strong>Quest:</strong> Yunobo of Goron City. Cần Flame Guard (Flamebreaker armor / Fireproof Elixir).</p>
    <h4>Defeat Moragia & Reach temple</h4>
    <ul><li>Moragia: dùng Zonai wing (có steering stick), activate Yunobo's charge khi approach mỗi head. 1 hit/head.</li><li>Dive qua crater → Death Mountain Chasm. Activate Mustis Lightroot. Follow mine-cart rails west. Brightbloom Seeds light route. Yunobo break red rock barrier at entrance. Chest 10 Arrows trong side room đầu.</li></ul>
    <figure><img src="images/zelda-tears-of-the-kingdom-fire-temple-moragia-zonai-wing-approach-p87-00-36-52-1024x576.webp" alt="Moragia"></figure>
    <h4>Activate terminal</h4>
    <ul><li>Activate green terminal ở central chamber → opens map + marks 5 gongs (1F, 2F, 3F hub, 4F, 5F).</li></ul>
    <h4>5 Gongs</h4>
    <details open><summary>Gong 1: Southern room (1F)</summary><p>Cross lava: hop stone slabs; wider pool dùng Hydrant tạo stone slabs. Minecart + fan; bell-shaped switch redirect route bằng Yunobo. Bridge lava: Hydrant make slabs, join with Ultrahand → bridge. Send Yunobo qua Marbled Rock barrier → gong. Defeat Fire Like (chest Zonaite Shield). Diamond chest trên raised platform.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-fire-temple-gong1-slab-bridge-ultrahand-p88-00-46-52-1024x576.webp" alt="Slab bridge"></figure></details>
    <details><summary>Gong 2: Western room (2F)</summary><p>Ride rails north to 2F (bell turn cart, Yunobo break rock). Turn cart around, arrow-shaped switch redirect. Cross lava room: place minecart trên lowered rail, ride into western room. Break Marbled Rock boulder trong lava pool → Hydrant water make slabs. Step onto moving slab + Recall → ride across. Defeat Construct, hit gong Yunobo. Chests: Zonaite x3 (Ascend through grate), 10 Arrows.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-fire-temple-gong2-recall-slab-target-p88-00-56-52-1024x576.webp" alt="Recall slab"></figure></details>
    <details><summary>Gong 3: Southwestern room (5F)</summary><p>3F hub → broken tracks southwest. Attach Zonai Rocket to minecart → ride across gap to 4F. Repair bridge (Ultrahand join planks). Check behind bridge for Ruby chest. Aim Yunobo up bridge at Marbled Rock boulder → opens hole + drops stone block. Recall block → ride up to 5F. Gong in southern room → hit Yunobo.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-fire-temple-gong4-bridge-planks-ultrahand-p89-00-05-42-1024x576.webp" alt="Bridge repair"></figure></details>
    <details><summary>Gong 4: Northern room (4F)</summary><p>Return to 3F hub. Use broken tracks northeast. Ride cart, shoot bell arrow to raise track → up to central room on 3F (hub). From hub, routes to upper floors. Gong 4 ở northern room 4F.</p></details>
    <details><summary>Gong 5: Northern room (1F)</summary><p>Route từ hub xuống 1F northern room; hit gong Yunobo.</p></details>
    <h4>Boss: Marbled Gohma</h4>
    <ul><li>Fuse đá vào tên bắn mắt khi mở.</li><li>Khi hạ xuống, đánh chân (legs).</li><li>Né đá rơi.</li><li>Reward: Heart Container + Vow of Yunobo (Fire). Clear hazard Eldin.</li></ul>
    <figure><img src="images/zelda-tears-of-the-kingdom-fire-temple-hub-minecart-left-track-p88-00-55-12-1024x576.webp" alt="Fire Temple hub"></figure>
  </div>

  <div class="card">
    <h3 id="water">💧 Water Temple (Zora) – Boss: Mucktorok</h3>
    <p><strong>Vùng:</strong> Lanayru. <strong>Quest:</strong> Sidon of the Zora. Zora Armor chest piece hữu ích (bơi ngược thác).</p>
    <h4>Reach temple</h4>
    <ul><li>Follow trail: Yona, Jiahto, Sidon → King Dorephan, Floating Scales Island, Ancient Zora Waterworks → raise water → waterfall opens route to Wellspring Island.</li><li>Wellspring Island low gravity: jump cao, fall chậm; dùng water bubbles làm lift; Recall bubble để ride back up.</li><li>Follow path across Wellspring Island, climb waterfalls. Use Wing + Zonai devices to cross to Sidon. Defeat Construct, swim up waterfall, activate travel point.</li></ul>
    <figure><img src="images/zelda-tears-of-the-kingdom-water-temple-entrance-ring-p150-00-09-20-1024x576.webp" alt="Water Temple entrance"></figure>
    <h4>4 Faucets</h4>
    <details open><summary>Faucet 1: B1 behind flames</summary><p>Glide down to basement entrance. Sidon's shield pass flame jets. Nếu Sidon kẹt ngoài, dùng Hover Stone giữ floor switch → tắt flames → Sidon follow. Glide across spike pit to stone ball. Attach ball to Hover Stone, carry across gap. Set into socket on far wall, activate Hover Stone → ball stays. Door opens → Sidon's water wave on faucet.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-water-temple-ball-socket-p150-00-14-00-1024x576.webp" alt="Ball socket"></figure></details>
    <details><summary>Faucet 2: left side bubble lift</summary><p>Cross floating platforms to lower-left island. Clear sludge from bubble emitter. Place stone ball in bubble → ride second bubble up. Lift gate with Ultrahand, pin open with Hover Stone → water drains, ball drops into socket → door opens → Sidon water wave.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-water-temple-gate-lifted-p150-00-25-00-1024x576.webp" alt="Gate lifted"></figure></details>
    <details><summary>Faucet 3: lower-right spinning tower</summary><p>Clear sludge from waterfall, swim up. Defeat Fire Like (chest). Switch inside rotating tower covered in sludge: fire water-fused arrow through opening to clean, then shoot exposed switch. Go through gate → activate faucet Sidon.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-water-temple-tower-switch-aim-p150-00-32-40-1024x576.webp" alt="Tower switch"></figure></details>
    <details><summary>Faucet 4: upper-right repair wheel</summary><p>Water bubble + Recall reach upper-right island. Water wheel missing paddle → attach stone slab to extend. Move water bubble into gap between electrical contacts → carries current → gate opens. Activate final faucet Sidon → return central platform.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-water-temple-paddle-repair-p150-00-36-30-1024x576.webp" alt="Paddle repair"></figure></details>
    <h4>Boss: Mucktorok</h4>
    <ul><li>Rửa sludge shark with Sidon's water wave / Splash Fruit / water-fused arrow. May need multiple hits.</li><li>Exposed: stun with arrow before it dives back.</li><li>Attack with strongest weapon while stunned; back away when moving.</li><li>At half health spread sludge → clear with wave. Keese Eyeball arrow when out of reach. Hydrants around platform clear sludge.</li><li>Reward: Heart Container + Vow of Sidon (Water). Clear sludge Zora's Domain.</li></ul>
    <figure><img src="images/zelda-tears-of-the-kingdom-water-temple-mucktorok-exposed-p150-00-43-50-1024x576.webp" alt="Mucktorok exposed"><figcaption>Mucktorok bị lộ</figcaption></figure>
  </div>

  <div class="card">
    <h3 id="lightning">⚡ Lightning Temple (Gerudo) – Boss: Queen Gibdo</h3>
    <p><strong>Vùng:</strong> Gerudo. <strong>Quest:</strong> Riju of Gerudo Town. Cần heat resistance ban ngày + electric resistance (Rubber armor).</p>
    <h4>Solve 3-pillar light puzzle</h4>
    <ul><li>Pillar1 climb top break cracked floor → light; mirror send beam.</li><li>Pillar2 smaller tower turn wheel counterclockwise.</li><li>Pillar3 break floor, repair wheel with sticks+platforms, turn → triangle forms → altar reveals → raise Lightning Temple.</li></ul>
    <figure><img src="images/zelda-tears-of-the-kingdom-lightning-temple-triangle-of-light-p185-00-26-40-1024x576.webp" alt="Triangle of light"></figure>
    <h4>Drive Queen Gibdo from entrance</h4>
    <ul><li>Use Riju's lightning on purple hive above doors. Queen emerges. Keep moving (charge, sand tornadoes). When Riju's field ready, draw power, fire arrow at Queen inside field → strips armor. Attack, retreat, repeat. She retreats. Use Riju lightning on hive blocking entrance → break → enter.</li></ul>
    <figure><img src="images/zelda-tears-of-the-kingdom-lightning-temple-queen-gibdo-lightning-strike-p185-00-32-10-1024x576.webp" alt="Queen Gibdo lightning"></figure>
    <h4>Reach Room of Ascension</h4>
    <ul><li>Entry room Korok-Frond Guster blow sand from floor switch.</li><li>B1: collapsing floor, flame jets, rolling fireballs (Ascend if fall, Recall fireball).</li><li>Mirror angle beam to yellow switch → door. Climb to Room of Ascension, activate terminal → travel point + 4 batteries.</li></ul>
    <h4>Charge 4 batteries</h4>
    <details open><summary>Battery 1: hidden room beside terminal</summary><p>Behind terminal: 2 loose sandstone blocks in wall. Move with Ultrahand, go through. Riju lightning + arrow charge battery.</p></details>
    <details><summary>Open Room of Natural Light</summary><p>Corner of 1F: lift stone blocking updraft. Ride wind to 5F, enter opening where beam shines down. Stand stone upright in beam, place mirror on top, angle light through opening into central chamber. On 5F move sliding mirror pillars until beam points NE then down to lower floors → opens 3F passage.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-lightning-temple-mirror-on-pillar-p186-00-07-00-1024x576.webp" alt="Mirror on pillar"></figure></details>
    <details><summary>Room of Offered Light</summary><p>Glide down to 3F door, step switch. Defeat Gibdos/Constructs. Build platform from grate + hot-air balloon. Attach mirror facing blocked wall. Place platform over beam. Light torch/wooden weapon, hold under balloon → platform rises, mirror reflects light to high switch → door opens. Drop down, charge battery.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-lightning-temple-platform-mirror-high-switch-p186-00-16-40-1024x576.webp" alt="Platform mirror"></figure></details>
    <details><summary>Cross flame shaft</summary><p>Return to 5F mirror pillars. Redirect beam to far pillar, clear sand, slide into position. Adjust next mirror send beam up to 6F. Ride updraft to switch → open room. Glide down shaft steering between flames. Bottom: floor switch opens door. Defeat 2 Constructs, let Riju in, charge battery.</p></details>
    <details><summary>Room of Light and Shade</summary><p>Ride updraft to 4F. Opening north side central chamber. Defeat Construct, pass 2 rotating stone discs. Move blocks from light source. Recall disc until gaps line up → light passes through to switch across central chamber. Glide, step switch → open route. Spike traps: use stone blocks hold traps open; step floor switch so Riju follow. In Room of Light and Shade: defeat Construct, uncover mirror in sand. Drop through opening to rotating room below. Use mirror direct light to green target; room spins → drive Stake into wall to stop rotation. Beam hits target → return upstairs, follow route to last battery, charge with Riju.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-lightning-temple-mirror-in-sand-p186-00-22-10-1024x576.webp" alt="Mirror in sand"></figure></details>
    <h4>Activate lift & Boss: Queen Gibdo</h4>
    <ul><li>Return to Room of Ascension, use terminal. Ride lift to 7F. Prepare healing, strong weapons, arrows with Bomb Flowers/elemental.</li><li>Vulnerable only after elemental hit strips armor (Riju lightning reliable; elemental arrows also work). Keep moving (charge, sand tornadoes).</li><li>When pale, attack with strongest weapon/arrows. At half health: 5 tornadoes + 4 hives summon Gibdos → destroy hives with Riju lightning/Bomb Flower arrows → sunlight strips Gibdo armor. Finish Queen. Reward Heart Container + Vow of Riju (Lightning). Clear sandstorm Gerudo.</li></ul>
    <figure><img src="images/zelda-tears-of-the-kingdom-lightning-temple-queen-gibdo-exposed-p186-00-30-50-1024x576.webp" alt="Queen Gibdo exposed"><figcaption>Queen Gibdo bị lộ</figcaption></figure>
  </div>

  <div class="card">
    <h3 id="spirit">🤖 Spirit Temple (Thunderhead Isles) – Boss: Seized Construct</h3>
    <p><strong>Quest:</strong> Guidance from Ages Past / Find the Fifth Sage. Finish Find the Fifth Sage first. Bring spare Zonai Charges/Energy Cells.</p>
    <h4>Ride Construct to temple</h4>
    <ul><li>After all 4 parts fitted at Construct Factory, climb aboard, follow yellow waypoint SE. Activate Sitoju Lightroot. Break rock walls with punches. Pause when battery low (refill). Near temple steep ledge: use Rockets from armory, attach to back, fire boost up.</li></ul>
    <figure><img src="images/zelda-tears-of-the-kingdom-spirit-temple-construct-jet-ledge-p227-00-46-43-1024x576.webp" alt="Construct jet"></figure>
    <h4>Wake owl statue & descend</h4>
    <ul><li>Interact owl statue while riding Construct → mask activates elevator. Ride down, cross gloom floor to boss arena. Activating statue unlocks travel point.</li></ul>
    <h4>Boss: Seized Construct</h4>
    <ul><li>Phase 1: Block (ZL) telegraphed punches. Counter with short punches → throws it back. Spiked Balls around arena; Cannon/Shock Emitter on arm stuns. Aim cannon shot at chest (hold ~1s). Push into electrified ropes for heavy damage + stun.</li><li>Phase 2 (~half health): grows 2 extra arms, rocket, flies. Cannon shot knocks down; dodge charge → stuck on floor briefly. Block/counter on return. Drive into ropes. Devices drop from capsules; fuse for reach.</li><li>Reward: Heart Container + Mineru's Secret Stone → Vow of Mineru (Spirit). Trail of Master Sword begins.</li></ul>
    <figure><img src="images/zelda-tears-of-the-kingdom-spirit-temple-seized-final-blow-p227-00-55-38-1024x576.webp" alt="Seized Construct final"></figure>
  </div>

  <div class="card">
    <h3 id="hyrule">🏰 Hyrule Castle – Phantom Ganon</h3>
    <p><strong>Quest:</strong> Trail of the Master Sword.</p>
    <ul><li>Vào Korok Forest qua Depths (Lost Woods).</li><li>Đánh Phantom Ganon.</li><li>Parry đòn; dùng light arrow.</li><li>Nhận Heart Container.</li></ul>
  </div>
</section>
'''

# Replace temples section
html = re.sub(r'<section id="temples".*?</section>\s*(?=<section id="endgame")', temples + "\n\n", html, flags=re.S, count=1)

open(r"E:\GameGuide\index.html","w",encoding="utf-8").write(html)
print("done")
PY