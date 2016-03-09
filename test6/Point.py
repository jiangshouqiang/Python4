import math

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x,self.y)

    def __eq__(self,other):
        print("self = ",self)
        print("other = ",other)
        return self.x == other.x and self.y == other.y
    def __ne__(self,other):
        return self.x != other.x or self.y != other.y

    def __repr__(self):
        return "Point({0.x!r},{0.y!r})".format(self)

    def __str__(self):
        return "({0.x!r},{0.y!r})".format(self)

def main():
    a = Point(3,5)
    b = Point(4,5)
    print(a != b)
    print(a == b)

if __name__ == "__main__":
    main()