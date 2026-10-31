p=r"E:\GameGuide\index.html"
s=open(p,encoding="utf-8").read()
# Fix broken image filenames (revert to on-disk English names)
s=s.replace("images/zelda-tears-of-the-kingdom-wind-temple-icicle-on-cần gạt-p45-00-03-50-1024x576.webp","images/zelda-tears-of-the-kingdom-wind-temple-icicle-on-lever-p45-00-03-50-1024x576.webp")
s=s.replace("images/zelda-tears-of-the-kingdom-wind-temple-tower-laser-giếng-p45-00-06-35-1024x576.webp","images/zelda-tears-of-the-kingdom-wind-temple-tower-laser-shaft-p45-00-06-35-1024x576.webp")
s=s.replace("images/zelda-tears-of-the-kingdom-water-temple-cổng-lifted-p150-00-25-00-1024x576.webp","images/zelda-tears-of-the-kingdom-water-temple-gate-lifted-p150-00-25-00-1024x576.webp")
s=s.replace("images/zelda-tears-of-the-kingdom-lightning-temple-bệ-mirror-high-switch-p186-00-16-40-1024x576.webp","images/zelda-tears-of-the-kingdom-lightning-temple-platform-mirror-high-switch-p186-00-16-40-1024x576.webp")
# Fix alt text for those
s=s.replace('alt="Icicle on cần gạt"','alt="Icicle on lever"')
s=s.replace('alt="Laser giếng"','alt="Laser shaft"')
s=s.replace('alt="Cổng lifted"','alt="Gate lifted"')
s=s.replace('alt="Bệ mirror high switch"','alt="Platform mirror high switch"')
open(p,"w",encoding="utf-8").write(s)
print("done")
PY