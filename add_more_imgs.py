# Add images to pages with few images
edits = {
 'shrines': ('<h1 class="page-title">Đền thờ nhỏ (152 đền thờ nhỏ)</h1>',
             '<h1 class="page-title">Đền thờ nhỏ (152 đền thờ nhỏ)</h1>\n    <figure><img src="../images/logo.svg" alt="Logo TOTK"><figcaption>The Legend of Zelda: Tears of the Kingdom</figcaption></figure>'),
}
# shrines.html h1 might be different
p=r"E:\GameGuide\pages\shrines.html"
s=open(p,encoding="utf-8").read()
if 'page-title' in s:
    # insert figure after first h1
    import re
    s=re.sub(r'(<h1[^>]*>.*?</h1>)', r'\1\n    <figure><img src="../images/great-sky-island-map.svg" alt="Bản đồ Great Sky Island"><figcaption>Bản đồ Great Sky Island</figcaption></figure>', s, count=1)
    open(p,"w",encoding="utf-8").write(s)
    print("shrines done")

# early-game: add logo
p=r"E:\GameGuide\pages\early-game.html"
s=open(p,encoding="utf-8").read()
s=re.sub(r'(<h1[^>]*>.*?</h1>)', r'\1\n    <figure><img src="../images/logo.svg" alt="Logo TOTK"><figcaption>The Legend of Zelda: Tears of the Kingdom</figcaption></figure>', s, count=1)
open(p,"w",encoding="utf-8").write(s)
print("early-game done")

# faq: add logo
p=r"E:\GameGuide\pages\faq.html"
s=open(p,encoding="utf-8").read()
s=re.sub(r'(<h1[^>]*>.*?</h1>)', r'\1\n    <figure><img src="../images/logo.svg" alt="Logo TOTK"><figcaption>The Legend of Zelda: Tears of the Kingdom</figcaption></figure>', s, count=1)
open(p,"w",encoding="utf-8").write(s)
print("faq done")

# mechanics: add logo
p=r"E:\GameGuide\pages\mechanics.html"
s=open(p,encoding="utf-8").read()
s=re.sub(r'(<h1[^>]*>.*?</h1>)', r'\1\n    <figure><img src="../images/logo.svg" alt="Logo TOTK"><figcaption>The Legend of Zelda: Tears of the Kingdom</figcaption></figure>', s, count=1)
open(p,"w",encoding="utf-8").write(s)
print("mechanics done")

# abilities: add logo
p=r"E:\GameGuide\pages\abilities.html"
s=open(p,encoding="utf-8").read()
s=re.sub(r'(<h1[^>]*>.*?</h1>)', r'\1\n    <figure><img src="../images/zonai-devices.svg" alt="Thiết bị Zonai"><figcaption>Thiết bị Zonai</figcaption></figure>', s, count=1)
open(p,"w",encoding="utf-8").write(s)
print("abilities done")

# tutorial: add logo
p=r"E:\GameGuide\pages\tutorial.html"
s=open(p,encoding="utf-8").read()
s=re.sub(r'(<h1[^>]*>.*?</h1>)', r'\1\n    <figure><img src="../images/great-sky-island-map.svg" alt="Bản đồ Great Sky Island"><figcaption>Bản đồ Great Sky Island</figcaption></figure>', s, count=1)
open(p,"w",encoding="utf-8").write(s)
print("tutorial done")

# endgame: add logo (already has ganondorf)
p=r"E:\GameGuide\pages\endgame.html"
s=open(p,encoding="utf-8").read()
# already has images, skip
print("endgame skip")

# tips: add zonai-parts (already has 2 images)
print("tips skip")
PY