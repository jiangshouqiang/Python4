import itertools

# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

# ns = itertools.repeat('Ab',8)
# for n in ns:
#     print

natuals = itertools.count(3)
ns = itertools.takewhile(lambda x:x <= 100 , natuals)
print(list(ns))

for c in itertools.chain(['bx','we','cw'],['auth','author','gethor']):
    print(c)

for key,group in itertools.groupby(['aab','abcd','aab','bbc','cnn','cnn','wei']):
    print(key,list(group))

for key , group in itertools.groupby(['aab','abcd','aab','bbc','cnn','cnn','wei'],lambda c:c.upper()):
    print(key,'=',list(group))