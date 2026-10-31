import re
def lum(hexcolor):
    h=hexcolor.lstrip('#')
    r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    def f(c): return c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
def contrast(c1,c2):
    l1=lum(c1); l2=lum(c2)
    hi,lo=max(l1,l2),min(l1,l2)
    return (hi+0.05)/(lo+0.05)
# dark
print('dark fg/bg',round(contrast('#E2E8F0','#0F0F23'),2))
print('dark muted/bg',round(contrast('#94A3B8','#0F0F23'),2))
print('dark primary/bg',round(contrast('#A78BFA','#0F0F23'),2))
print('dark accent/bg',round(contrast('#F43F5E','#0F0F23'),2))
# light
print('light fg/bg',round(contrast('#1E1B4B','#F5F3FF'),2))
print('light muted/bg',round(contrast('#6B7280','#F5F3FF'),2))
print('light primary/bg',round(contrast('#7C3AED','#F5F3FF'),2))
print('light accent/bg',round(contrast('#E11D48','#F5F3FF'),2))
# figcaption muted on card-bg
print('dark muted/cardbg',round(contrast('#94A3B8','#1E1C35'),2))
print('light muted/cardbg',round(contrast('#6B7280','#FFFFFF'),2))
