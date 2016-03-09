import re
bool1 = re.match(r'^\d{3}\-\d{3,8}$','010-1234')
print("bool = " , bool1.pos)
bool2 = re.match(r'^\d{3}\-\d{3,8}$','010-122222234')
print("bool2 = ",bool2)

# match spilt string
result = re.split(r'\s+','a b   c')
print(result)

#cut string
m = re.match(r'^(\d{3})-(\d{3,8})$','010-1231212')
print(m.group(1))
print(m.group(2))

print(m.groups())

print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# compile
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')


print(re_telephone.match('010-12312').groups())

print(re_telephone.match("010-8982").groups())

myEail = r'[\w\.]+@\w+\.\w+'
val = "someone@gmail.com"
val2 = 'bill@gates@microsoft.com'
eail = re.match(myEail,val2)
print(eail)
print(len(val2))