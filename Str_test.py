import locale
locale.setlocale(locale.LC_ALL,"")
treatises = ['jiang','shou','qiang']
treatises2 = ['姜','守','qiang']
print(" ".join(treatises))
print("jiangja".count("a",2))

print("jiang/wang/shou/qiang".rpartition("/"))
print("jiang/wang/shou/qiang".split("/"))
print(int("20"))
print('''{0} , world {1}'''.format("Hello",200))
print('''{who} , world {age}'''.format(who="Hello",age=20))
print("your name {1[1]}".format(treatises,treatises2))
print("{} {} {}".format("Python","can","count"))
print("{0:<4}".format("jiangshouqiang"))

s = "The word of truth"
print(len(s))
print("{0}".format(s))
print("{0:20}".format(s))
print("{0:>20}".format(s))
print("{0:^20}".format(s))
# print("{0.10}".format(s))
# print("{0.10}".format("jiangshouqiang"))

x,y=(123456790,1234.06)
locale.setlocale(locale.LC_ALL,"C")
c = "{0:n} {1:n}".format(x,y)
print("c = "+c)

import math
amount=(10**3)*math.pi
print("[{0:12.2e}] [{0:12.2f}]".format(amount))
import decimal
print("{:,.5f}".format(decimal.Decimal("123988777723.23232321023")))

print(locals())
import sys
import unicodedata

def print_unicode_table(word):
    print("decimal     hex   chr  {0:^40}".format("name"))
    print("------   ----------- {0:-<40}".format("") )
    code = ord(" ")
    end = sys.maxunicode

    while code < end :
        c = chr(code)
        name = unicodedata.name(c,"*** unknown ***")
        if word is None or word in name.lower():
            print("{0:7} {0:5X} {0:^3c} {1}".format(code,name.title()))
        code += 1

