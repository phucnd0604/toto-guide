import re, pathlib

allow=set("""totk guide shrine temple boss quest main story early game endgame faq tips mechanics abilities tutorial index html css js vercel ign nintendo life zelda central polygon gamespot guardian wikimedia commons svg webp jpg png ultrahand fuse ascend recall zonai zora gerudo rito goron hyrule hebra eldin lanayru necluda tabantha depths sky korok deku ganon ganondorf master sword hero paraglider purah pad goddess blessing heart container energy cell light of blessing aerocuda bokoblin keese eyeball bomb flower keese korok-frond guster construct mineru secret stone vow sage spirit water fire wind lightning thunderhead isles charged armor marbled rock roast flamebreaker fireproof elixir snowquill like hylian pine cone great eagle bow opal sapphire ruby diamond zonaite shield soldier blade time bomb portable pot brightbloom seeds hover stone ball socket hydrant hydrants sludge splash fruit ancient arowana king scale stone tear floating scales island wellspring wing rocket stake grates gatehouse chasm lightroot lightroots light dragon skyview tower lookout landing first gatehouse new serenne stable dragon tear geoglyph memory tab map total hidden demon dragon phantom ganon ganon's whisker whiskers whisker bazaar kara kara bazaar thunderhead isles charged armor thunderhead korok-forest lost woods room ascension natural offered shade stake stake stake stake stake stake stake stake stake stake stake stake""".split())

for p in ['pages/main-story.html','pages/temples.html']:
    t=pathlib.Path(p).read_text(encoding='utf-8')
    print('====',p)
    for m in re.finditer(r'<li>(.*?)</li>', t, re.S):
        txt=re.sub(r'<[^>]+>',' ',m.group(1)).strip()
        toks=re.findall(r"[A-Za-z][A-Za-z'-]*", txt)
        susp=[]
        for w in toks:
            lw=w.lower()
            if lw in allow: continue
            if len(w)<4: continue
            # also skip if part of multiword allow? simple
            susp.append(lw)
        if susp:
            print(repr(txt[:150]))
            print('   suspicious:', sorted(set(susp)))
"""