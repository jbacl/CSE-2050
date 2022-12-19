class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return Point.dist_from_origin(self) == Point.dist_from_origin(other)
    
    def __lt__(self, other):
        return Point.dist_from_origin(self) < Point.dist_from_origin(other)

    def __gt__(self, other):
        return Point.dist_from_origin(self) > Point.dist_from_origin(other)
    
    def __str__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    def dist_from_origin(self):
        return (self.x**2 + self.y**2) ** (1/2)