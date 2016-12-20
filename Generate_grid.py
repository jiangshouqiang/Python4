def get_int(msg,minimum,default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print("must be >=",minimum)
            else:
                return i
        except ValueError as err:
            print(err)

print(10/4)
print(10//4)
rows = get_int("rows:",1,None)
columns = get_int("columns:",1,None)
minimum = get_int("minimum(or Enter for 0):",-10000,0)
default = 1000
if default < minimum:
    default = 2*minimum
maximum = get_int("maximum(or Entor for"+str(default)+"):",minimum,default)