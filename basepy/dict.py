
d1 = dict(a=1, b=2, c=3)
print(len(d1))  # use len to get count

del d1['a']  # to delete

# get name value pair
print(d1.pop('b'))  # return value of b and removes it
while d1:
    print(d1.popitem())  # returns k,v tuples

d2 = {}

d2.setdefault('a', 3)  # get value of a or set to 3 and return

def x():
    assert True

d2.setdefault('a', x())  # x never gets called if a is set

d3 = dict(three=3, four=4, five=5)
d3.update([('three',4), ('five',4)])  # list of updates
print(d3)


