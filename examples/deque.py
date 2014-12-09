from __future__ import print_function
from __future__ import unicode_literals
from collections import deque

## Build a queue that keeps the last 3 lines
d = deque("",3)

d.append("1")
d.append("2")
d.append("3")
d.append("4")
d.append("5")
print(d) # contains last 3 lines

## in addition you can extent (grow the list) or append/extend from the left
