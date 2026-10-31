p=r"E:\GameGuide\index.html"
s=open(p,encoding="utf-8").read()
reps=[
 ("Wind Temple","Đền thờ Gió"),
 ("Fire Temple","Đền thờ Lửa"),
 ("Water Temple","Đền thờ Nước"),
 ("Lightning Temple","Đền thờ Sấm"),
 ("Spirit Temple","Đền thờ Siêu Linh"),
 ("Wind Đền thờ","Đền thờ Gió"),
 ("Fire Đền thờ","Đền thờ Lửa"),
 ("Water Đền thờ","Đền thờ Nước"),
 ("Lightning Đền thờ","Đền thờ Sấm"),
 ("Spirit Đền thờ","Đền thờ Siêu Linh"),
]
for a,b in reps:
    if a in s:
        s=s.replace(a,b)
open(p,"w",encoding="utf-8").write(s)
print("done")
PY