def perimeterRectangle(length, breadth):
	return 2 * (length + breadth)

def areaRectangle(length, breadth):
	return length * breadth

l1 = input('Enter the length : ') # str
b1 = input('Enter the breadth : ') # str

# str -> int
# '7' -> 7
# '3' -> 3
# 'Good morning' -> ???
li = int(l1)
bi = int(b1)

# float(), str(), bool(), int()

# function call
# per = perimeterRectangle(l1, b1)

# built in functions in python
print(perimeterRectangle(li, bi))

# area = areaRectangle(l1, b1)
print(areaRectangle(li, bi))