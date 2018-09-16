# series.py -> series
def getFiboSeries(n):
	'''take in n and returns a string fibo series for n numbers'''
	a = 0
	b = 1

	series = ''

	# inpython, only str data can be concatenated with str data
	series += str(a) + '\t' + str(b)

	for i in range(0, n - 2):
		c = a + b
		series += '\t' + str(c)
		a, b = b, c

	return series


def getEvenSeries(n):
	'''take in n and returns the even series till n'''
	series = ''
	for i in range(0, n + 1, 2):
		series += str(i) + '\t'

	return series

if __name__ == '__main__':
	# testing the functions in the module
	n = int(input('enter n : '))
	print(getFiboSeries(n))
	print(getEvenSeries(n))