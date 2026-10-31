import re, pathlib
for p in ['pages/main-story.html','pages/temples.html']:
    lines=pathlib.Path(p).read_text(encoding='utf-8').splitlines()
    print('===',p)
    for i,line in enumerate(lines,1):
        t=line.strip()
        if '<li' not in t and '<p' not in t: 
            continue
        # strip tags
        txt=re.sub(r'<[^>]+>',' ',t).strip()
        if not txt: continue
        has_vi = bool(re.search(r'[àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵđÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴĐ]', txt))
        if not has_vi:
            print(i, '::', txt[:160])