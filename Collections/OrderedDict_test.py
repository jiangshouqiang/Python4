from collections import OrderedDict

d = dict([('a',1),('b',2),('c',3)])
print(d)

od = OrderedDict([('a',1),('b',3),('c',4)])
print(od)

odd = OrderedDict()
odd['z'] = 1
odd['y'] = 2
odd['x'] = 3
dlist_key = list(odd.keys())
dlist_val = list(odd.values())
print(dlist_key)
print(dlist_val)
