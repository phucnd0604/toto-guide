p=r"E:\GameGuide\pages\main-story.html"
s=open(p,encoding="utf-8").read()

# Replace quest 7
old7='''    <div class="quest" id="q7"><div class="title">7. The Sludge-Covered Statue</div><div class="meta">Lanayru – Zora</div>
    <details><summary>Chi tiết</summary>
      <ol>
        <li>Đến Zora's Domain (bị sludge).</li>
        <li>Rửa tượng bằng Splash Fruit.</li>
        <li>Nói Yona.</li>
        <li>Đến Mipha Court gặp Sidon.</li>
      </ol>
    </details></div>'''
new7='''    <div class="quest" id="q7"><div class="title">7. The Sludge-Covered Statue</div><div class="meta">Lanayru – Zora</div>
    <details><summary>Chi tiết</summary>
      <ol>
        <li>Đến Zora's Domain (bị sludge phủ khắp nơi).</li>
        <li>Rửa tượng bằng Splash Fruit (ném vào tượng).</li>
        <li>Nói chuyện Yona (Yona đang chăm sóc statue).</li>
        <li>Đến Mipha Court gặp Sidon (Sidon đang chờ).</li>
        <li>Nhận nhiệm vụ tìm Sidon và giải cứu Zora's Domain.</li>
      </ol>
      <p><strong>Mẹo:</strong> Mang Splash Fruit nhiều; sludge làm giảm máu tối đa tạm thời.</p>
    </details></div>'''
s=s.replace(old7,new7)

# Replace quest 8
old8='''    <div class="quest" id="q8"><div class="title">8. The Broken Slate</div><div class="meta">Zora's Domain</div>
    <details><summary>Chi tiết</summary>
      <ol>
        <li>Rửa bùn ở mảnh phiến của Jiahto tại Toto Lake.</li>
        <li>Ghép vào tường → đọc manh mối về bầu trời.</li>
      </ol>
    </details></div>'''
new8='''    <div class="quest" id="q8"><div class="title">8. The Broken Slate</div><div class="meta">Zora's Domain</div>
    <details><summary>Chi tiết</summary>
      <ol>
        <li>Đến Toto Lake (phía bắc Zora's Domain).</li>
        <li>Rửa bùn ở mảnh phiến của Jiahto bằng Splash Fruit.</li>
        <li>Ghép mảnh phiến vào tường.</li>
        <li>Đọc manh mối về bầu trời (clue về Floating Scales Island).</li>
      </ol>
      <p><strong>Mẹo:</strong> Toto Lake có sludge; dùng Splash Fruit để rửa.</p>
    </details></div>'''
s=s.replace(old8,new8)

# Replace quest 9
old9='''    <div class="quest" id="q9"><div class="title">9. Restoring the Zora Armor</div><div class="meta">Zora's Domain</div>
    <details><summary>Chi tiết</summary>
      <ol>
        <li>Mang Ancient Arowana cho Yona ở Zora's Domain.</li>
        <li>Nhận Zora Armor (bơi ngược thác).</li>
      </ol>
      <p><strong>Mẹo:</strong> Ancient Arowana ở Lulu Lake / Zora River.</p>
    </details></div>'''
new9='''    <div class="quest" id="q9"><div class="title">9. Restoring the Zora Armor</div><div class="meta">Zora's Domain</div>
    <details><summary>Chi tiết</summary>
      <ol>
        <li>Tìm Ancient Arowana (ở Lulu Lake hoặc Zora River).</li>
        <li>Mang Ancient Arowana cho Yona ở Zora's Domain.</li>
        <li>Nhận Zora Armor (cho phép bơi ngược thác).</li>
        <li>Dùng Zora Armor để bơi ngược thác lên Mipha Court.</li>
      </ol>
      <p><strong>Mẹo:</strong> Ancient Arowana là cá hiếm; tìm ở Lulu Lake.</p>
    </details></div>'''
s=s.replace(old9,new9)

# Replace quest 10
old10='''    <div class="quest" id="q10"><div class="title">10. Clues đến the Sky</div><div class="meta">Lanayru</div>
    <details><summary>Chi tiết</summary>
      <ol>
        <li>Nhận King's Scale từ Dorephan ở Pristine Sanctum (dưới Zora's Domain).</li>
        <li>Bắn một King's Scale qua stone tear trên Floating Scales Island (sky).</li>
      </ol>
    </details></div>'''
new10='''    <div class="quest" id="q10"><div class="title">10. Clues đến the Sky</div><div class="meta">Lanayru</div>
    <details><summary>Chi tiết</summary>
      <ol>
        <li>Đến Pristine Sanctum (dưới Zora's Domain, qua secret passage).</li>
        <li>Nói chuyện King Dorephan → nhận King's Scale.</li>
        <li>Đến Floating Scales Island (sky) bằng Zora Armor + bơi ngược thác.</li>
        <li>Bắn một King's Scale qua stone tear trên Floating Scales Island.</li>
        <li>Stone tear mở → clue về sky.</li>
      </ol>
      <p><strong>Mẹo:</strong> King Dorephan bị thương; Pristine Sanctum là nơi ông ẩn náu.</p>
    </details></div>'''
s=s.replace(old10,new10)

# Remove duplicate quest steps in quest 11 (steps 1-4 are duplicated from q7-10)
old_dup='''      <ol>
        <li><strong>Sludge-Covered Statue:</strong> Đến Zora's Domain (bị sludge). Rửa tượng bằng Splash Fruit. Nói Yona. Đến Mipha Court gặp Sidon.</li>
        <li><strong>Broken Slate:</strong> Rửa bùn ở mảnh phiến của Jiahto tại Toto Lake. Ghép vào tường → đọc manh mối về bầu trời.</li>
        <li><strong>Restoring Zora Armor:</strong> Mang Ancient Arowana cho Yona → nhận Zora Armor (bơi ngược thác). Ancient Arowana ở Lulu Lake/Zora River.</li>
        <li><strong>Clues to the Sky:</strong> Nhận King's Scale từ Dorephan ở Pristine Sanctum. Bắn qua stone tear trên Floating Scales Island.</li>
        <li><strong>Đến Water Temple:</strong> Follow trail: Yona, Jiahto, Sidon → King Dorephan, Floating Scales Island, Ancient Zora Waterworks → raise water → waterfall opens route to Wellspring Island. Wellspring Island low gravity; use water bubbles (Recall). Climb waterfalls, use Wing + Zonai devices cross to Sidon. Defeat Construct, swim up waterfall, activate travel point.</li>'''
new_dup='''      <ol>
        <li><strong>Đến Water Temple:</strong> Follow trail: Yona, Jiahto, Sidon → King Dorephan, Floating Scales Island, Ancient Zora Waterworks → raise water → waterfall opens route to Wellspring Island. Wellspring Island low gravity; use water bubbles (Recall). Climb waterfalls, use Wing + Zonai devices cross to Sidon. Defeat Construct, swim up waterfall, activate travel point.</li>'''
s=s.replace(old_dup,new_dup)

open(p,"w",encoding="utf-8").write(s)
print("done")
PY