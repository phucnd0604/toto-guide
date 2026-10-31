import re,glob
req=['<!DOCTYPE html>','<html lang="vi">','<meta charset="UTF-8">','<meta name="viewport"','<title>','<meta name="description"']
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    miss=[r for r in req if r not in s]
    if miss: print(f,'MISSING:',miss)
print('checked')
# check canonical/og
for f in ['index.html']+glob.glob('pages/*.html'):
    s=open(f,encoding='utf-8').read()
    if 'og:title' not in s: print('NO OG TITLE',f)
print('og check done')
