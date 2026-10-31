lines=open('index.html',encoding='utf-8').read().splitlines()
nums=[94,95,96,97,100,109,110,112,113,114,126,128,130,134,178,202,209,210,220,223,260,262,272,273,274,275,276,349,352,354,356,358,360,362,365,373,376,378,380,382,384,395,398,400,402,404]
out=[]
for n in nums:
    out.append(f"{n} :: {lines[n-1]}")
open('showlines_out.txt','w',encoding='utf-8').write("\n".join(out))
print("done")
PY