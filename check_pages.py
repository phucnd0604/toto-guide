for fn in ['main-story','temples','shrines','tips','faq','mechanics','abilities','tutorial','early-game']:
    s=open(r"E:\GameGuide/pages/%s.html"%fn,encoding="utf-8").read()
    print(fn, "mojibake:", s.count("\ufffd"), "quests:", s.count('class="quest"'), "shrines:", s.count("<tr><td>"))
PY