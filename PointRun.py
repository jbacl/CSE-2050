from Point import *

p1 = Point(3, 4) # dist_from_origin() - 5
p2 = Point(3, 4) # dist_from_origin() - 5
p3 = Point(4, 3) # dist_from_origin() - 5
p4 = Point(0, 1) # dist_from_origin() - 1

print(p1 > p4)

print(p4 > p1)

print(p1 > p3)

print(p1 == p3)

print(str(p1))