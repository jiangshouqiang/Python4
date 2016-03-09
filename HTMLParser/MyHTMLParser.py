from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print('%s' % tag)
    def handle_endtag(self,tag):
        print('%s' % tag)
    def handle_startendtag(self, tag, attrs):
        print('%s' % tag)
    def handle_data(self,data):
        print(type(data))
    def handle_comment(self, data):
        print('<!--',data,'-->')
    def handle_entityref(self, name):
        print('& %s;' %name)
    def handle_entityref(self,name):
        print('&%s;' % name)
    def handle_charref(self, name):
        print("&#%s;" % name)

html = r'''<html>
<head></head>
<p>someone to do something</p>
</html>
'''
f = request.urlopen('http://www.ifeng.com/')
htmls = f.read()
# print(htmls)
parser = MyHTMLParser()
parser.feed(str(htmls))
print(parser.get_starttag_text())
parser.close()