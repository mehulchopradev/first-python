# take n from the user
n = int(input('enter n : '))

# logic that will print even nos till n (including n)
# i = 0 # loop variable

# loops

'''while i <= n:
	if not i % 2:
		print(i)
	i = i + 1'''

# for loop
'''for i in range(0, n+1, 2):
	print(i)'''

# end index is exclusive
for i in range(0, n + 1):
	if not i % 2:
		print(i)