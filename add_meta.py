import re
pages=['mechanics','abilities','tutorial','early-game','main-story','temples','endgame','shrines','tips','faq']
descs={
 'mechanics':'Cơ chế cốt lõi: máu, stamina, nhiệt độ, pin Zonai, Gloom, Depths, thời tiết, điều khiển.',
 'abilities':'Năng lực: Ultrahand, Fuse, Ascend, Recall, Autobuild và các năng lực khác.',
 'tutorial':'Hướng dẫn Great Sky Island từng bước: 4 shrine, 4 năng lực, Temple of Time.',
 'early-game':'Bước đầu trên mặt đất: Lookout Landing, Paraglider, ngựa, tower, vùng.',
 'main-story':'Main Story 23 nhiệm vụ chính từ A đến Z.',
 'temples':'6 Temple + Boss: Wind, Fire, Water, Lightning, Spirit, Hyrule Castle.',
 'endgame':'Endgame: Master Sword, Dragon\'s Tears, Ganondorf, 100% completion.',
 'shrines':'152 Shrine theo vùng + 31 shrine quests.',
 'tips':'Mẹo: nấu ăn, Fuse recipes, giáp, Depths, Sky, Korok, 100%.',
 'faq':'Câu hỏi thường gặp về TOTK.',
}
for pg in pages:
    p=r"E:\GameGuide\pages\%s.html"%pg
    s=open(p,encoding="utf-8").read()
    if 'name="description"' not in s:
        meta='<meta name="description" content="%s">'%descs[pg]
        s=s.replace('<title>','<title>',1)  # no-op anchor
        # insert after charset meta
        s=s.replace('<meta charset="UTF-8">','<meta charset="UTF-8">\n'+meta,1)
        open(p,"w",encoding="utf-8").write(s)
print("done")
PY