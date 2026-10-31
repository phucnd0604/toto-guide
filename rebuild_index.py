import re
pages = ['mechanics','abilities','tutorial','early-game','main-story','temples','endgame','shrines','tips','faq']
# Read clean page content
sections_map = {
 'mechanics': ('co-che', 'Cơ chế cốt lõi'),
 'abilities': ('nang-luc', 'Năng lực'),
 'tutorial': ('tutorial', 'Hướng dẫn: Great Sky Island'),
 'early-game': ('early', 'Đầu game'),
 'main-story': ('main-story', 'Cốt truyện chính'),
 'temples': ('temples', 'Đền thờ & Boss'),
 'endgame': ('endgame', 'Cuối game'),
 'shrines': ('shrines', 'Đền thờ nhỏ'),
 'tips': ('tips', 'Mẹo'),
 'faq': ('faq', 'Câu hỏi thường gặp'),
}
# Build body content by extracting <main class="content">...</main> from each page
body_parts = []
for pg in pages:
    src = open(r"E:\GameGuide\pages\%s.html"%pg, encoding="utf-8").read()
    m = re.search(r'<main class="content">(.*?)</main>', src, re.S)
    content = m.group(1).strip() if m else ''
    # fix paths
    content = content.replace('../images/', 'images/').replace('../assets/', 'assets/')
    # strip external links
    content = re.sub(r'<a href="(https?://[^"]*|pages/[^"]*)"[^>]*>(.*?)</a>', r'\2', content, flags=re.S)
    sid, title = sections_map[pg]
    body_parts.append('<section id="%s" class="content">\n<h2><span class="num">%s</span> %s</h2>\n%s\n</section>' % (sid, '•', title, content))

# Intro section
intro = '''<section id="gioi-thieu" class="content">
  <h1>Hướng dẫn chơi Zelda: Tears of the Kingdom từ A đến Z</h1>
  <div class="card">
    <p><strong>Tears of the Kingdom (TOTK)</strong> là phần tiếp theo của Breath of the Wild. Link và Zelda khám phá tàn tích Hyrule. Sau sự kiện Tears, Zelda mất tích, Link bị mất sức mạnh và có cánh tay Zonai của Rauru. Mục tiêu: tìm Zelda, ngăn Ganondorf.</p>
    <div class="grid grid-3">
      <div class="card"><h3>Nền tảng</h3><p>Nintendo Switch (vật lý/kỹ thuật số).</p></div>
      <div class="card"><h3>Thời lượng</h3><p>Cốt truyện chính ~40-60 giờ. 100% ~120-150 giờ.</p></div>
      <div class="card"><h3>Tiên quyết</h3><p>Không cần chơi BOTW trước.</p></div>
    </div>
    <h3>Điểm mới so với BOTW</h3>
    <ul>
      <li><strong>Ultrahand</strong> – ghép vật thể (cầu, thuyền, xe, máy bay).</li>
      <li><strong>Fuse</strong> – ghép vật liệu vào vũ khí/cung/khiên.</li>
      <li><strong>Ascend</strong> – xuyên trần lên cao.</li>
      <li><strong>Recall</strong> – đảo ngược chuyển động vật thể.</li>
      <li><strong>Autobuild</strong> – ghép theo bản vẽ (mở sau).</li>
      <li><strong>Depths</strong> (Vực thẳm), <strong>Sky Islands</strong> (Đảo trên trời), Zonai devices.</li>
    </ul>
    <h3>Lời khuyên cho người mới</h3>
    <ul>
      <li><strong>Đừng vội.</strong> Game khuyến khích khám phá.</li>
      <li><strong>Lưu thường xuyên:</strong> auto-save có, save thủ công trước boss.</li>
      <li><strong>Chết không mất đồ</strong> (chỉ mất tiến độ từ checkpoint).</li>
      <li><strong>Vũ khí gãy là bình thường</strong> – Fuse mới là cách mạnh.</li>
      <li><strong>Nhặt mọi thứ:</strong> nguyên liệu, quặng, Zonai device.</li>
      <li><strong>Nấu ăn quan trọng:</strong> hồi máu + buff.</li>
    </ul>
    <figure><img src="images/logo.svg" alt="Logo TOTK"><figcaption>The Legend of Zelda: Tears of the Kingdom</figcaption></figure>
  </div>
</section>
'''

# Combine
body = intro + "\n" + "\n".join(body_parts)

# Assemble full HTML
nav = '''<header class="navbar">
  <span class="brand">Hướng dẫn TOTK</span>
  <button class="theme-toggle" aria-label="Đổi giao diện sáng/tối">🌙 Tối</button>
  <button class="nav-toggle" aria-label="Menu">☰</button>
  <nav>
    <a href="#gioi-thieu">Giới thiệu</a>
    <a href="#dieu-khien">Điều khiển</a>
    <a href="#co-che">Cơ chế</a>
    <a href="#nang-luc">Năng lực</a>
    <a href="#tutorial">Hướng dẫn</a>
    <a href="#early">Đầu game</a>
    <a href="#main-story">Cốt truyện chính</a>
    <a href="#temples">Đền thờ</a>
    <a href="#endgame">Cuối game</a>
    <a href="#shrines">Đền thờ nhỏ</a>
    <a href="#tips">Mẹo</a>
    <a href="#faq">Câu hỏi thường gặp</a>
  </nav>
</header>'''

# Need to include điều khiển section (from mechanics page it's included). But mechanics page has controls table. Good.

html = '''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hướng dẫn Zelda: Tears of the Kingdom từ A đến Z</title>
<meta name="description" content="Hướng dẫn chơi đầy đủ từ A đến Z: điều khiển, cơ chế, hướng dẫn nhập môn, cốt truyện chính 23 nhiệm vụ, 5 đền thờ, boss, đền thờ nhỏ, mẹo, 100%.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
''' + nav + '''
<main class="container">
''' + body + '''
</main>
<footer><p>Hướng dẫn tổng hợp từ IGN Walkthrough, Nintendo Life, Zelda Central, Polygon, GameSpot, The Guardian.</p></footer>
<script src="assets/app.js"></script>
</body>
</html>'''

open(r"E:\GameGuide\index.html","w",encoding="utf-8").write(html)
print("done")
PY