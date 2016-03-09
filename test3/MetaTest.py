t = "jiang",-24,'shou',"2.0",18.6
print(type(t[1]))
print(t.count("shou"))
MAX1,MAX2,MAX3=(1,2,4)
VAL1,VAL2=1,2
print(MAX1)
print("VAL1,VAL2=",VAL1,VAL2)
print("Hello world"[1:-1])
import collections
Aircratft = collections.namedtuple("Aircraft","manufacter model seating")
Seating = collections.namedtuple("Seating","minimum maximum model")

aircraft = Aircratft("Airbus","A320-200",Seating(100,200,150))
print("aircraft.seating.model=" ,aircraft.seating.model)
print("aircraft.manufacter=",aircraft.manufacter)
print("aircraft.model=",aircraft.model)
print("_asdict=",aircraft._asdict())
print("model manufacter == {model} {manufacter}".format(**aircraft._asdict()))

My_nametuple = collections.namedtuple("my_nametuple","key val")
test = My_nametuple("jiang","27")
print("key = ",test.key)


first,*rest = [9,2,3,4,5,1-2]
print(first,*rest)
print(rest[1])

woods=['jiang','shou','qiang']
print(woods[::2])
woods[2:2] = ["insert"]
print(woods)

x = [1,2,3,4,5,6,7,8,9,10]
print(type(x))
xx = {1,2,3,4,5,6,7,8,9,10}
print(type(xx))
y = {1,2,3,4,5,6}
print("x[1::2]=",x[3::3])
print("len(x[1::2])=",len(x[1::2]))
print(xx.difference(y))

z = {"1":1,"2":4,"3":3}
sorted("z = ",z)
print(type(z))
for (k,v) in z.items():
    print("key , val = ",k,v)
print(z.get("2"))