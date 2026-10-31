import re,glob
# find <table> occurrences and check if preceded by <div class="card"> without close? simple: count tables and card
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    t=s.count('<table')
    c=s.count('class="card"')
    print(f,'tables=',t,'cards=',c)