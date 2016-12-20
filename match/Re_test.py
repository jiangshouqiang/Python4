import re
bool1 = re.match(r'^\d{3}\-\d{3,8}$','010-1234')
print("bool = " , bool1.pos)
bool2 = re.match(r'^\d{3}\-\d{3,8}$','010-122222233')
print("bool2 = ",bool2)

# match spilt string
result = re.split(r'\s+','a b   c')
print(result)

#cut string
m = re.match(r'^(\d{3})-(\d{3,8})$','010-1231212')
print(m.group(1))
print(m.group(2))
m2 = re.match(r'\D*(\d{1,4}\w)','\t\t\t\t\t86天')
print('m2 = = ' , m2.group(1))
print(m.groups())

print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# compile
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')


print(re_telephone.match('010-12312').groups())

print(re_telephone.match("010-8982").groups())

myEail = r'[\w\.]+@\w+\.\w+'
val = "someone@gmail.com"
val2 = 'bill@gates@microsoft.com'
eail = re.match(myEail,val)
print('eail = ',eail.pos)
print(len(val2))

url = r'http://news.ifeng.com/a/\d+/\d+_\d\.shtml'
val_url = 'http://news.ifeng.com/a/20160422/48556097_0.shtml'
print('length = ',len(val_url))
result = re.match(url,val_url)
print("result.pos = ",result.endpos)
print(re.match(url,val_url))

match_url = 'http://8.wacai.com/list/wenying/\w\d+$';
url = 'http://8.wacai.com/list/wenying/p3';
res = re.match(match_url,url)
print(res.endpos)

resp_url = "http://wacai.com/list/wenying"
ma   =  re.search(r'([http:\/\/|https:\/\/].*\.\w+)',resp_url)
print(ma.group(1))

rs = ".com.com"
rs2 = re.match(r'\..*',rs)
print('rs2 = ',rs2)

rss = ' 7.0% ' \
      '~ 9.8% '
rs_ma = re.search(r'(\d+\.\d+\%).+~.+(\d+\.\d+\%)',rss)
print('rs_ma = ',rs_ma.lastindex)

objs = ['8.00%', '11.50%']
print(type(objs[0]+'~'+objs[1]))