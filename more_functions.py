# defining a function that can take n arguments
# tuple packing
def mysum(*values):
    sum = 0
    for ele in values:
        sum += ele
    return sum

'''print(mysum())
print(mysum(4))
print(mysum(5,6,3))
print(mysum(5,6,7,3,4,5))'''

def perimeter(length, breadth):
    return 2 * (length + breadth)

stats = [5, 3]
# print(perimeter(stats[0], stats[1]))
# print(perimeter(*stats)) # function argument unpacking

def area(**rectstats):
    return rectstats['length'] * rectstats['breadth']

# print(area(6, 3)) # should fail

#print(area(length=6, breadth=3)) # key word argument packing
#print(area(breadth=4, length=10))

statsmap = {'length': 11, 'breadth': 2}
# print(perimeter(statsmap['length'], statsmap['breadth']))
print(perimeter(**statsmap)) # unpacking
