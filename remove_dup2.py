p=r"E:\GameGuide\pages\main-story.html"
s=open(p,encoding="utf-8").read()
old='''        <li><strong>Sludge-Covered Statue:</strong> Đến Zora's Domain (bị sludge). Rửa tượng bằng Splash Fruit. Nói Yona. Đến Mipha Court gặp Sidon.</li>
        <li><strong>Broken Slate:</strong> Rửa bùn ở mảnh phiến của Jiahto tại Toto Lake. Ghép vào tường → đọc manh mối về bầu trời.</li>
        <li><strong>Restoring Zora Armor:</strong> Mang Ancient Arowana cho Yona → nhận Zora Armor (bơi ngược thác). Ancient Arowana ở Lulu Lake/Zora River.</li>
        <li><strong>Clues to the Sky:</strong> Nhận King's Scale từ Dorephan ở Pristine Sanctum. Bắn qua stone tear trên Floating Scales Island.</li>
        <li><strong>Đến Water Temple:</strong>'''
new='''        <li><strong>Đến Water Temple:</strong>'''
assert old in s, "pattern not found"
s=s.replace(old,new)
open(p,"w",encoding="utf-8").write(s)
print("done")
PY