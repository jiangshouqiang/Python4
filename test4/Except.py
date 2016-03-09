class FoundException(Exception):
    pass

try:
    for i in range(10):
        if i == 90 :
            raise FoundException()
except FoundException:
    print("i = ",i)
else:print("not found")
