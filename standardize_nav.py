import re
pages=['mechanics','abilities','tutorial','early-game','main-story','temples','endgame','shrines','tips','faq']

# Standard navbar for pages (relative paths)
page_nav = '''<header class="navbar">
  <span class="brand">Hướng dẫn TOTK</span>
  <button class="theme-toggle" aria-label="Đổi giao diện sáng/tối">🌙 Tối</button>
  <button class="nav-toggle" aria-label="Menu">☰</button>
  <nav>
    <a href="../index.html">Trang chủ</a>
    <a href="mechanics.html">Cơ chế</a>
    <a href="abilities.html">Năng lực</a>
    <a href="tutorial.html">Hướng dẫn</a>
    <a href="early-game.html">Đầu game</a>
    <a href="main-story.html">Cốt truyện chính</a>
    <a href="temples.html">Đền thờ</a>
    <a href="endgame.html">Cuối game</a>
    <a href="shrines.html">Đền thờ nhỏ</a>
    <a href="tips.html">Mẹo</a>
    <a href="faq.html">Câu hỏi thường gặp</a>
  </nav>
</header>'''

index_nav = '''<header class="navbar">
  <span class="brand">Hướng dẫn TOTK</span>
  <button class="theme-toggle" aria-label="Đổi giao diện sáng/tối">🌙 Tối</button>
  <button class="nav-toggle" aria-label="Menu">☰</button>
  <nav>
    <a href="index.html">Trang chủ</a>
    <a href="pages/mechanics.html">Cơ chế</a>
    <a href="pages/abilities.html">Năng lực</a>
    <a href="pages/tutorial.html">Hướng dẫn</a>
    <a href="pages/early-game.html">Đầu game</a>
    <a href="pages/main-story.html">Cốt truyện chính</a>
    <a href="pages/temples.html">Đền thờ</a>
    <a href="pages/endgame.html">Cuối game</a>
    <a href="pages/shrines.html">Đền thờ nhỏ</a>
    <a href="pages/tips.html">Mẹo</a>
    <a href="pages/faq.html">Câu hỏi thường gặp</a>
  </nav>
</header>'''

# Standardize page navbars
for pg in pages:
    path=r"E:\GameGuide\pages\%s.html"%pg
    s=open(path,encoding="utf-8").read()
    s=re.sub(r'<header class="navbar">.*?</header>', page_nav, s, count=1, flags=re.S)
    # Remove cross-page links from content (keep text)
    s=re.sub(r'<a href="(https?://[^"]*|pages/[^"]*|\.\./pages/[^"]*|temples\.html[^"]*|endgame\.html[^"]*|main-story\.html[^"]*|shrines\.html[^"]*|tips\.html[^"]*|faq\.html[^"]*|early-game\.html[^"]*|tutorial\.html[^"]*|abilities\.html[^"]*|mechanics\.html[^"]*)"[^>]*>(.*?)</a>', r'\2', s, flags=re.S)
    open(path,"w",encoding="utf-8").write(s)

# Standardize index navbar
s=open(r"E:\GameGuide\index.html",encoding="utf-8").read()
s=re.sub(r'<header class="navbar">.*?</header>', index_nav, s, count=1, flags=re.S)
# Remove cross-page links from index content (keep text) - but keep navbar anchors
s=re.sub(r'<a href="(https?://[^"]*|pages/[^"]*)"[^>]*>(.*?)</a>', r'\2', s, flags=re.S)
open(r"E:\GameGuide\index.html","w",encoding="utf-8").write(s)
print("done")
PY