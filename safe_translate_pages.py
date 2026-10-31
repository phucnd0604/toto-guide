import re
pages=['mechanics','abilities','tutorial','early-game','main-story','temples','endgame','shrines','tips','faq']
trans = {
 "Follow":"Theo","Defeat":"Đánh bại","Activate":"Kích hoạt","Glide":"Lướt",
 "Cross":"Vượt","Ride":"Cưỡi","Turn":"Xoay","Attach":"Gắn","Break":"Phá",
 "Climb":"Leo","Return":"Quay về","Open":"Mở","Use":"Dùng","Set":"Đặt",
 "Place":"Đặt","Move":"Di chuyển","Lift":"Nâng","Push":"Đẩy","Raise":"Nâng",
 "Reach":"Đến","Shoot":"Bắn","Stand":"Đứng","Steer":"Lái","Step":"Bước",
 "Drop":"Rơi","Pass":"Vượt","Leave":"Rời","Pause":"Tạm dừng","Check":"Kiểm tra",
 "Aim":"Nhắm","Hold":"Giữ","Collect":"Nhận","Report":"Báo cáo","Pick":"Nhặt",
 "weak":"yếu","points":"điểm","sections":"phần","body":"thân","covered":"phủ",
 "ice":"băng","slabs":"phiến đá","wider":"rộng hơn","pool":"bể","minecart":"xe goòng",
 "cart":"xe","bell":"chuông","redirect":"chuyển hướng","lowered":"hạ","rail":"ray",
 "western":"phía tây","room":"phòng","rocks":"đá","broken":"bị gãy","tracks":"đường ray",
 "southwest":"tây nam","gap":"khe","platform":"bệ","slab":"phiến","gate":"cổng",
 "door":"cửa","opens":"mở","floor":"sàn","switch":"công tắc","wall":"tường",
 "chest":"rương","lever":"cần gạt","shaft":"giếng","updraft":"luồng khí",
 "roof":"mái","structure":"cấu trúc","north":"bắc","opening":"lối mở",
 "lasers":"lasers","avoid":"tránh","past":"qua","Construct":"Construct",
 "icy":"đá","corridor":"hành lang","hide":"ẩn","Time":"Time","Bomb":"Bomb",
 "Portable":"Portable","Pot":"Pot","window":"cửa sổ","beneath":"dưới","hull":"vỏ tàu",
 "cross":"vượt","to":"đến","underside":"underside","deck":"deck","Defeat":"Đánh bại",
 "Construct":"Construct","activate":"kích hoạt","turbine":"turbine","last":"cuối",
 "Corridor":"Hành lang","red":"đỏ","lasers":"lasers","avoid":"tránh","past":"qua",
 "Construct":"Construct","icy":"đá","corridor":"hành lang","hide":"ẩn","Time":"Time",
 "Bomb":"Bomb","Portable":"Portable","Pot":"Pot","Leave":"Rời","window":"cửa sổ",
 "beneath":"dưới","hull":"vỏ tàu","cross":"vượt","to":"đến","underside":"underside",
 "deck":"deck","Defeat":"Đánh bại","Construct":"Construct","activate":"kích hoạt",
 "turbine":"turbine","last":"cuối",
}
def replace_in_text(text):
    for en, vi in trans.items():
        text = re.sub(r'\b'+re.escape(en)+r'\b', vi, text)
    return text
for pg in pages:
    path=r"E:\GameGuide\pages\%s.html"%pg
    s=open(path,encoding="utf-8").read()
    result = re.sub(r'>([^<]+)<', lambda m: '>'+replace_in_text(m.group(1))+'<', s)
    open(path,"w",encoding="utf-8").write(result)
    print("done", pg)
PY