'''
1. Print Fibonacci Series
2. Print Even Series
3. Find whether even or odd
4. Exit
Please enter your choice : 1
Enter n: 8
0 1 1 2 3 5 8 13

1. Print Fibonacci Series
2. Print Even Series
3. Find whether even or odd
4. Exit
Please enter your choice : 2
Enter n: 8
0 2 4 6 8

1. Print Fibonacci Series
2. Print Even Series
3. Find whether even or odd
4. Exit
Please enter your choice : 3
Enter n : 3
It is odd

1. Print Fibonacci Series
2. Print Even Series
3. Find whether even or odd
4. Exit
Please enter your choice : 4
'''

# imported only the module
# import series
import xyz.supercoders.modules.math as mymath # user defined module

# built in module in python 'math'
import math
# packages
# own logical directory structure and place ur modules in that directory structure
# google.com
# com.google.appspecific directory
# supercoders.xyz

# directly import functions from a module.
# FYI the module name is not imported
from xyz.supercoders.modules.series import getFiboSeries, getEvenSeries as evenSeries

print(math.pi)

def getEvenSeries(n):
	print('Dummy 0 - 100')
	# no return statement
	# python implicitly puts 'return None'

while True:
	print('1. Print Fibonacci Series\n2. Print Even Series\n3. Find whether even or odd\n4. Exit')

	choice = int(input('Please enter your choice : '))
	if choice != 4:
		n = int(input('Enter n : '))

	if choice == 1:
		# fibonacci series
		print(getFiboSeries(n))
	elif choice == 2:
		# Even Series
		print(evenSeries(n))
	elif choice == 3:
		# even or odd
		print(mymath.isEvenOrOdd(n))
	else:
		# exit out of the program
		break
