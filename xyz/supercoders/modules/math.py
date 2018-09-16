# math.py -> math
def isEvenOrOdd(n):
	'''take in n and return a string "even" or "odd"'''
	return "Odd" if n % 2 else "Even"

# testing the functions in the module
# magic variable
print(__name__)
# when running this module separately __name__ = '__main__'
# when running this module as part of an import __name__ = 'math_ops'

if __name__ == '__main__':
	n = int(input('enter n : '))
	print(isEvenOrOdd(n))