import glob
files=glob.glob(r"E:\GameGuide/pages/*.html")
n=0
for f in files:
    s=open(f,encoding="utf-8").read()
    if 'name="description"' in s:
        n+=1
print("pages with meta description:", n, "of", len(files))
PY