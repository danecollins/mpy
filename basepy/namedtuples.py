from collections import namedtuple

# define a named tuple with x, y and z members
PointA = namedtuple('PointA', ['x', 'y', 'z'])
PointB = namedtuple('PointB', 'x y z')  # or can do it with a string

# creation
p1 = PointA(1.0, 2.0, 3.0)  # positional
t1 = (2, 3, 4)
p2 = PointA._make(t1)  # or from a tuple
p3 = PointA(*t1)  # another way from tuple

# accessing
p1.x  # access by name
p1[1]  # or by position
field = 'z'
getattr(p1, field)

# changing value
new_p = p1._replace(y=4)  # replaces the y value with 4
new_p = p1._replace(**{field: 5})  # define kwargs as z=5 and replace



print(p1)
print(p2.y)
print(p3[1])
print(getattr(p1, field))


