import itertools

for c in itertools.chain('ABC','XYZ'):
    print(c)

for key,group in itertools.groupby('AAabBCCD@@@@',lambda x:x.upper()):
    print(key,list(group))
