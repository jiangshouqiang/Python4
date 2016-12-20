from enum import Enum,unique
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wen = 3
    Thu = 4

print(Weekday(1))


def fn(self,name='world'):
    print("Hello , %s " % name)

Hello = type('Hello',(object,),dict(hello=fn))
h = Hello()
h.hello('jiang')