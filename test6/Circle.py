from Point import Point
class Circle(Point):
    def __init__(self,radius,x=0,y=0):
        super().__init__(x,y)
        self.radius = radius
    @property
    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin()-self.radius)
    def __eq__(self, other):
        return self.radius == other.radius  and super().__eq__(other)
    def __str__(self):
        return repr(self)

def main():
    c = Circle(10,1,3)
    print(c.edge_distance_from_origin)

if __name__ == "__main__":
    main()