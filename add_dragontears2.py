p=r"E:\GameGuide\pages\endgame.html"
s=open(p,encoding="utf-8").read()
# find the Dragon's Tears section by searching for "geoglyphs"
idx=s.find("geoglyphs")
# find the <ul> containing it
start=s.rfind("<ul>",0,idx)
end=s.find("</ul>",idx)+len("</ul>")
print("found ul:", start, end)
# replace with table
old_block=s[start:end]
new_block='''<p>Tìm geoglyphs trên map (Impa quest). Mỗi Dragon's Tear cho memory. Có 12 tears + 1 hidden (13 total).</p>
    <div class="card">
      <table>
        <tr><th>#</th><th>Vùng</th><th>Ghi chú</th></tr>
        <tr><td>1</td><td>Tabantha Frontier</td><td>Gần New Serenne Stable, Impa quest bắt đầu.</td></tr>
        <tr><td>2</td><td>Hyrule Field</td><td>Gần Lookout Landing.</td></tr>
        <tr><td>3</td><td>Hebra Mountains</td><td>Gần Rito Village.</td></tr>
        <tr><td>4</td><td>Eldin</td><td>Gần Goron City.</td></tr>
        <tr><td>5</td><td>Lanayru</td><td>Gần Zora's Domain.</td></tr>
        <tr><td>6</td><td>Gerudo</td><td>Gần Gerudo Town.</td></tr>
        <tr><td>7</td><td>Necluda</td><td>Gần Kakariko Village.</td></tr>
        <tr><td>8</td><td>Faron</td><td>Gần Lake Hylia.</td></tr>
        <tr><td>9</td><td>Akkala</td><td>Gần Tarrey Town.</td></tr>
        <tr><td>10</td><td>Great Hyrule Forest</td><td>Gần Korok Forest.</td></tr>
        <tr><td>11</td><td>Hyrule Ridge</td><td>Gần Lindor's Brow.</td></tr>
        <tr><td>12</td><td>Tabantha Tundra</td><td>Gần Snowfield Stable.</td></tr>
        <tr><td>13 (hidden)</td><td>Sky</td><td>Trên Light Dragon, cần phóng từ Skyview Tower.</td></tr>
      </table>
      <p><strong>Mẹo:</strong> Dùng Shrine Sensor hoặc Impa's balloon để tìm geoglyphs. Mỗi tear cho 1 memory (cắt cảnh).</p>
    </div>'''
s=s.replace(old_block,new_block)
open(p,"w",encoding="utf-8").write(s)
print("done")
PY