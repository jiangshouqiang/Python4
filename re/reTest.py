import re

m = re.search('(?<=abc)def','abcdefg')
print(len(m))
print(m.group(0))