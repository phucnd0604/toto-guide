import re
src=open(r"C:\Users\phucn\AppData\Local\Temp\opencode\shrines-zc.txt",encoding="utf-16").read()
sections=re.split(r'\n## ', src)
regions=[]
for sec in sections[1:]:
    first_line=sec.split('\n',1)[0].strip()
    m=re.match(r'(.+?)\s*\(\d+\)', first_line)
    region_name = m.group(1).strip() if m else first_line
    body=sec.split('\n',1)[1] if '\n' in sec else ''
    rows=[]
    buf=''
    for line in body.split('\n'):
        s=line.strip()
        if s.startswith('|'):
            if buf:
                buf+='\n'+s
            else:
                buf=s
            if s.endswith('|'):
                rows.append(buf)
                buf=''
        else:
            if buf:
                rows.append(buf)
                buf=''
    if buf:
        rows.append(buf)
    data_rows=[]
    for r in rows:
        if re.match(r'\|\s*Shrine\s*\|', r):
            continue
        if re.match(r'\|\s*---', r):
            continue
        if 'Shrine' not in r:
            continue
        data_rows.append(r)
    regions.append((region_name, data_rows))

def parse_row(r):
    r=r.replace('\n',' ')
    parts=[p.strip() for p in r.split('|')]
    if parts and parts[0]=='':
        parts=parts[1:]
    if parts and parts[-1]=='':
        parts=parts[:-1]
    shrine=parts[0] if len(parts)>0 else ''
    trial=parts[1] if len(parts)>1 else ''
    typ=parts[2] if len(parts)>2 else ''
    loc=parts[3] if len(parts)>3 else ''
    m=re.search(r'\[.*?\]\((https?://[^)]+)\)', shrine)
    link=m.group(1) if m else ''
    nm=re.search(r'\[(.*?)\]', shrine)
    name=(nm.group(1) if nm else shrine).replace('**','').strip()
    return name, trial, typ, loc, link

html=[]
html.append('<!DOCTYPE html>')
html.append('<html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">')
html.append('<title>Shrine – TOTK Guide</title>')
html.append('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
html.append('<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">')
html.append('<link rel="stylesheet" href="../assets/style.css"></head><body>')
html.append('<header class="navbar"><span class="brand">TOTK Guide</span><button class="nav-toggle" aria-label="Menu">☰</button><nav>')
for (lbl,href) in [("Trang chủ","../index.html"),("Cơ chế","mechanics.html"),("Năng lực","abilities.html"),("Tutorial","tutorial.html"),("Early Game","early-game.html"),("Main Story","main-story.html"),("Temple","temples.html"),("Endgame","endgame.html"),("Shrine","shrines.html"),("Mẹo","tips.html"),("FAQ","faq.html")]:
    html.append('<a href="%s">%s</a>' % (href, lbl))
html.append('</nav></header>')
html.append('<div class="container layout"><aside class="sidebar"><h4>Mục lục trang</h4><nav class="toc">')
for region,_ in regions:
    if region=='Shrine Quests':
        continue
    anchor=region.lower().replace(' ','-').replace('(','').replace(')','')
    html.append('<a href="#%s">%s</a>' % (anchor, region))
html.append('<a href="#shrine-quests">Shrine Quests</a>')
html.append('<a href="#patterns">Mẫu puzzle</a><a href="#links">Link đầy đủ</a>')
html.append('</nav></aside><main class="content"><h1 class="page-title">Shrine (152 shrines)</h1>')
html.append('<section id="intro"><h2><span class="num">ℹ️</span> Giới thiệu</h2><div class="card"><ul>')
html.append('<li>TOTK có <strong>152 shrines</strong> (120 mặt đất + 32 sky) + <strong>31 shrine quests</strong>. Mỗi shrine cho <strong>Light of Blessing</strong> → đổi tim/stamina.</li>')
html.append('<li><strong>Interact shrine</strong> (chạm vào) để mở fast travel, không cần giải ngay.</li>')
html.append('<li>Shrine Sensor (Purah Pad) tìm shrine gần nhất.</li>')
html.append('<li>Bảng dưới: tên shrine, trial, loại, vùng (Zelda Central).</li>')
html.append('</ul></div></section>')

total=0
shrine_regions=[(r,rows) for r,rows in regions if r!='Shrine Quests']
quest_regions=[(r,rows) for r,rows in regions if r=='Shrine Quests']

for region, rows in shrine_regions:
    anchor=region.lower().replace(' ','-').replace('(','').replace(')','')
    html.append('<section id="%s"><h2><span class="num">📍</span> %s (%d)</h2><div class="card"><table><tr><th>Shrine</th><th>Trial</th><th>Type</th><th>Location</th></tr>' % (anchor, region, len(rows)))
    for r in rows:
        name,trial,typ,loc,link=parse_row(r)
        total+=1
        html.append('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (name, trial, typ, loc))
    html.append('</table></div></section>')

for region, rows in quest_regions:
    anchor='shrine-quests'
    data_rows=[r for r in rows if not r.strip().startswith('| Quest')]
    html.append('<section id="%s"><h2><span class="num">📜</span> %s (%d)</h2><div class="card"><p>Các shrine mở bằng shrine quest (nhiệm vụ nhỏ). Mỗi shrine cho Light of Blessing.</p><table><tr><th>Quest</th><th>Shrine</th><th>Region</th></tr>' % (anchor, region, len(data_rows)))
    for r in data_rows:
        # format: Quest | Shrine (with link) | Region
        r2=r.replace('\n',' ')
        parts=[p.strip() for p in r2.split('|')]
        if parts and parts[0]=='': parts=parts[1:]
        if parts and parts[-1]=='': parts=parts[:-1]
        quest=parts[0] if len(parts)>0 else ''
        shrine_cell=parts[1] if len(parts)>1 else ''
        region_name=parts[2] if len(parts)>2 else ''
        nm=re.search(r'\[(.*?)\]', shrine_cell)
        shrine_name=(nm.group(1) if nm else shrine_cell).replace('**','').strip()
        html.append('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (quest, shrine_name, region_name))
    html.append('</table></div></section>')

html.append('<section id="patterns"><h2><span class="num">🧩</span> Mẫu puzzle shrine thường gặp</h2><div class="card"><ul>')
for p in [
 "Ultrahand cầu/thang: ghép ván gỗ qua khe; dán hook lên ván làm ski-lift.",
 "Fan/rocket: gắn fan vào thuyền/minecart để di chuyển nhanh.",
 "Recall clock: chỉnh kim đồng hồ chồng lên nhau cùng chiều.",
 "Ascend: tìm trần rắn phía trên để xuyên lên.",
 "Fuse: Fuse đá vào vũ khí phá đá; Fuse fire fruit vào tên.",
 "Ball/weight: đặt ball đúng vị trí để mở cửa.",
 "Wind: dùng fan để thổi vật nhẹ.",
 "Proving Grounds: đánh Constructs không vũ khí (nhặt từ môi trường).",
 "Rauru's Blessing: shrine không puzzle, chỉ lấy chest + blessing.",
]:
    html.append('<li>%s</li>' % p)
html.append('</ul></div></section>')
html.append('<section id="links"><h2><span class="num">🔗</span> Danh sách đầy đủ & hình ảnh</h2><div class="card"><ul>')
html.append('<li><a href="https://zeldacentral.com/games/tears-of-the-kingdom/shrines/" target="_blank" rel="noopener">Zelda Central – All 152 Shrines (tên + trial + tọa độ)</a></li>')
html.append('<li><a href="https://www.nintendolife.com/guides/zelda-tears-of-the-kingdom-all-shrine-locations-and-maps" target="_blank" rel="noopener">Nintendo Life – All Shrine Locations & Maps</a></li>')
html.append('<li><a href="https://www.zeldadungeon.net/wiki/Category:Tears_of_the_Kingdom_Shrine_Files" target="_blank" rel="noopener">Zelda Dungeon Wiki – Shrine Files (screenshot)</a></li>')
html.append('</ul><p><strong>Mẹo:</strong> Dùng Shrine Sensor trong game để tìm shrine gần nhất; interact để mở fast travel.</p></div></section>')
html.append('</main></div><footer><p>Hướng dẫn tổng hợp từ IGN (tương đương), Nintendo Life, Zelda Central.</p></footer>')
html.append('<script src="../assets/app.js"></script></body></html>')

open(r"E:\GameGuide\pages\shrines.html","w",encoding="utf-8").write("\n".join(html))
print("Total shrines written:", total)
print("Regions:", len(regions))
for region,rows in regions:
    print(region, len(rows))