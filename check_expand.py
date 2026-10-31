s=open(r"E:\GameGuide/pages/main-story.html",encoding="utf-8").read()
print("quest count:", s.count('class="quest"'))
print("q7 has Lulu Lake:", 'Lulu Lake' in s)
print("q11 has Sludge-Covered Statue dup:", 'Sludge-Covered Statue:' in s)
PY