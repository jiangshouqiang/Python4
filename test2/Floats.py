import sys
def equal_float(a,b):
    return abs(a-b) <= sys.float_info.epsilon

print(equal_float(1,2))
print(sys.float_info.epsilon)

print(int(3.12312))
print(10/3)