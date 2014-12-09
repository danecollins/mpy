from __future__ import print_function
from __future__ import unicode_literals
from collections import defaultdict,Counter
 
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point {},{}".format(self.x,self.y)

    def __repr__(self):
        return "Point(x=%r,y=%r)" % (self.x,self.y)

class PointList(list):
    def sum_of_x(self):
        x=0
        for item in self:
            x+= item.x
        return x


if __name__ == '__main__':
    mylist = PointList()
    mylist.append(Point(1,2))
    mylist.append(Point(2,3))
    print(mylist)
    print(mylist.sum_of_x())