import re, pathlib
for p in ['pages/main-story.html','pages/temples.html']:
    lines=pathlib.Path(p).read_text(encoding='utf-8').splitlines()
    print('===',p)
    for i,line in enumerate(lines,1):
        # strip tags
        t=re.sub(r'<[^>]+>',' ',line)
        t=t.strip()
        if not t: continue
        # remove common html/entities
        # check if line has any Vietnamese diacritic
        has_vi = bool(re.search(r'[àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴĐ]', t))
        # ascii letters count
        ascii_letters = len(re.findall(r'[A-Za-z]', t))
        total_chars = len(re.sub(r'\s+','',t))
        if (not has_vi) and ascii_letters>15 and total_chars>20:
            with open('scan2_out.txt','a',encoding='utf-8') as f:
                f.write(f"{p}:{i} :: {t[:200]}\n")