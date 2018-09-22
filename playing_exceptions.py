print('Program started')
n = input('Enter n: ')

# exception handling
try:
    a = int(n)
except ValueError as e:
    # ValueError is a built in exception class in python whose object is thrown (raised)
    # ValueError -> Exception
    # to the caller when string passed cannot be converted to an int
    print(e)
    print('Please enter integer values')
else:
    # this will execute if there is no exception thrown in the corresponding try block
    print('odd') if a % 2 else print('even')

print('Program ended')
