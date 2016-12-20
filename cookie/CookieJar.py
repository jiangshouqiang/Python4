import urllib
import string
from http import cookiejar
from urllib import request
from urllib import parse

fileName = 'cookie.txt'
# cookie = cookiejar.MozillaCookieJar(fileName)
# opener = request.urlopen('http://www.jd.com')
# cookie.save(ignore_discard=True,ignore_expires=True)

cj = cookiejar.LWPCookieJar()
cookie_support = request.HTTPCookieProcessor(cj)
opener = request.build_opener(cookie_support,request.HTTPHandler)
request.install_opener(opener)

handler = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}

postData = { '_xsrf': '45bcba43a5d007f7b0453e9e2e49434f',
                            'captcha_type':'cn',
                            'remember_me':'true',
                            'phone_num': '15974156301',
                            'password': 'jsq1998'
            }
posturl = 'https://www.zhihu.com/login/phone_num'
postData = parse.urlencode(postData).encode('utf-8')
requests = request.Request(posturl,postData,headers=handler)
print(requests)
response = request.urlopen(requests)
# print(dir(response))
print(response.headers)
text = response.read()
print(text)
f_obj = open(fileName,'wb')
f_obj.write(text)
