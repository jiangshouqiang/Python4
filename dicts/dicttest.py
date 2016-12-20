import unittest

from myDict import Dict

dicts = Dict(a='12',b='jiang')
print(dicts.a)

d = Dict()
d['test'] = 'testValue'
print(d.test)

d.ke = 'value'
print(d.ke)