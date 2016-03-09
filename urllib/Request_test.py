from urllib import request
import json
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print("status :",f.status,f.reason)
    for k,v in f.getheaders():
        print('%s : %s' % (k,v))

    datas = data.decode('utf-8')
    json_data = json.loads(datas)
    print(json_data['summary'])
    print(json_data['tags'])
    # print(type(datas))