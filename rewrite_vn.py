import re
html=open(r"E:\GameGuide\index.html",encoding="utf-8").read()

# Clean Vietnamese temple section
temples = '''<section id="temples" class="content">
  <h2><span class="num">08</span> Đền thờ & Boss (chi tiết)</h2>
  <p>Mỗi đền thờ có walkthrough chi tiết + ảnh minh họa.</p>

  <div class="card">
    <h3 id="wind">🌬️ Đền thờ Gió (Rito) – Boss: Colgera</h3>
    <p><strong>Vùng:</strong> Hebra. <strong>Quest:</strong> Tulin of Rito Village. Cần 2 cấp kháng lạnh (Snowquill set).</p>
    <h4>Đường đến</h4>
    <ul><li>Giúp Tulin lấy cung ở Hebra South Summit Cave → Tulin gia nhập, mở Wind ability.</li><li>Dùng Tulin's gust khi lướt để vượt khe giữa các floating islands.</li><li>Fabric sails trên ships bounce Link lên cao; dùng Ascend khi có trần rắn.</li><li>Kahatanaum Shrine gần đỉnh: kích hoạt trước (fast travel).</li><li>Rơi qua opening ở tâm bão → Stormwind Ark.</li></ul>
    <figure><img src="images/zelda-tears-of-the-kingdom-wind-temple-stormwind-ark-below-p44-00-59-02-1024x576.webp" alt="Stormwind Ark"><figcaption>Stormwind Ark trong tâm bão</figcaption></figure>
    <h4>Kích hoạt terminal</h4>
    <ul><li>Kích hoạt green terminal ở main deck → fast travel + đánh dấu 5 turbine trên map. Map tabs: 1F, B1, B2.</li></ul>
    <h4>5 Turbine</h4>
    <details open><summary>Turbine 1: Sửa cần gạt (1F bow)</summary><p>Nhặt icicle bằng Ultrahand → gắn vào cần gạt bị gãy → xoay để nâng cổng. Vào trong, đứng gần turbine, dùng Tulin's gust. Room bên cạnh: lever tương tự → rương Opal.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-wind-temple-icicle-on-lever-p45-00-03-50-1024x576.webp" alt="Icicle on lever"></figure></details>
    <details><summary>Turbine 2: Rơi qua tháp (1F→B1)</summary><p>Lướt từ updraft trung tâm lên roof tall structure phía bắc. Mở metal doors bằng Ultrahand, rơi vào shaft. Tránh red lasers. Paraglider near bottom → turbine alcove. Rương Soldier Blade trên ledge.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-wind-temple-tower-laser-shaft-p45-00-06-35-1024x576.webp" alt="Laser shaft"></figure></details>
    <details><summary>Turbine 3: Bánh xe xoay (B1)</summary><p>Phá icicles blocking opening (fire). Inside: large spinning wheel over gap. Dùng Recall trên wheel → reverse spin → ride across. Room tiếp: lever Ultrahand mở bars; wall 2 gears thiếu connector → shoot down large icicle, gắn between gears → gear turn → gate opens → activate turbine. Rương Sapphire trong cell (pull through bars bằng Ultrahand).</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-wind-temple-wheel-recall-start-p45-00-28-30-1024x576.webp" alt="Recall wheel"></figure></details>
    <details><summary>Turbine 4: Underside (B2)</summary><p>Ladder từ B1 xuống B2, follow icy corridor past Construct (ice blocks hide Time Bomb/Portable Pot). Leave window, glide beneath hull, dùng Tulin's gust cross to underside deck. Defeat Construct, activate turbine. Có thể dive thẳng từ main deck.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-wind-temple-underside-glide-p45-00-12-13-1024x576.webp" alt="Underside glide"></figure></details>
    <details><summary>Turbine 5: Pole spin (B1→1F)</summary><p>Corridor có red lasers + broken gap. Pass lasers (Ruby rương beyond), cross gap bằng Tulin's gust, defeat Construct, Ascend lên floor above. Pole treo trần: attach stone slab làm fin, dùng Tulin's gust spin pole → door opens. Climb ladder nhanh (door không giữ lâu). Lên 1F, activate turbine cuối.</p>
      <figure><img src="images/zelda-tears-of-the-kingdom-wind-temple-pole-slab-fin-p45-00-15-58-1024x576.webp" alt="Pole spin"></figure></details>
    <h4>Boss: Colgera</h4>
    <ul><li>Weak points = purple sections trên body, covered by ice.</li><li>Bắn tên từ dưới (khó) hoặc dive từ trên (đóng paraglider khi Colgera expose ice trên upper side sau khi fire spikes).</li><li>Fire Fruit/Bomb Flower phá ice + damage 1 shot; Keese Eyeball giúp track.</li><li>Pha 2: Colgera thêm tornadoes. Dùng Tulin's gust dodge/reposition; updrafts regain height.</li><li>Reward: Heart Container + Vow of Tulin (Wind ability khi lướt). Clear blizzard Hebra.</li></ul>
    <figure><img src="images/zelda-tears-of-the-kingdom-wind-temple-colgera-purple-core-p45-00-41-05-1024x576.webp" alt="Colgera weak point"></figure>
  </div>

  <div class="card">
    <h3 id="fire">🔥 Đền thờ Lửa (Goron) – Boss: Marbled Gohma</h3>
    <p><strong>Vùng:</strong> Eldin/Death Mountain. <strong>Quest:</strong> Yunobo of Goron City. Cần Flame Guard (Flamebreaker armor / Fireproof Elixir).</p>
    <h4>Đánh bại Moragia & Đến temple</h4>
    <ul><li>Moragia: dùng Zonai wing (có steering stick), activate Yunobo's charge khi approach mỗi head. 1 hit/head.</li><li>Dive qua crater → Death Mountain Chasm. Activate Mustis Lightroot. Follow mine-cart rails west. Brightbloom Seeds light route. Yunobo break red rock barrier at entrance. Chest 10 Arrows trong side room đầu.</li></ul>
    <figure><img src="images/zelda-tears-of-the-kingdom-fire-temple-moragia-zonai-wing-approach-p87-00-36-52-1024x576.webp" alt="Moragia"></figure>
    <h4>Kích hoạt terminal</h4>
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
    <h3 id="water">💧 Đền thờ Nước (Zora) – Boss: Mucktorok</h3>
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
    <h3 id="lightning">⚡ Đền thờ Sấm (Gerudo) – Boss: Queen Gibdo</h3>
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
    <h3 id="spirit">🤖 Đền thờ Siêu Linh (Thunderhead Isles) – Boss: Seized Construct</h3>
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