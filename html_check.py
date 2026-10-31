from html.parser import HTMLParser
class P(HTMLParser):
    def error(self,msg): print("ERROR",msg)
p=P()
data=open('index.html',encoding='utf-8').read()
p.feed(data)
print("parsed ok")
PY