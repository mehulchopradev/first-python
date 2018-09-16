# take n from the user (n represents the number of fibonacci numbers)
# n = 8
# 0 1 1 2 3 5 8 13

n = int(input('enter n : '))
a, b = 0, 1

print(a)
print(b)

for i in range(0, n - 2):
	c = a + b
	print(c)
	a, b = b, c
