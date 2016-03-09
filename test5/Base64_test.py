import base64
import string
binary = open("/Users/jiang/Documents/learn/python/3.jpg","rb").read()
ascii_test = ""
for i,c in enumerate(base64.b64encode(binary)):
    if i and i % 68 == 0 :
        ascii_test += "\\\n"
    ascii_test += chr(c)

# print(ascii_test)
print(string.ascii_letters)
heads = [c +":"for c in string.ascii_letters]
print(heads)