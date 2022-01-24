# Python code to count the number of occurrences
def countX(lst, x):
	count = 0
	for ele in lst:
		if (ele == x):
			count = count + 1
	return count

# Driver Code
lst = ["amira", "hello", "bye", "amira", "lina", "amira", "bye", "hello", "amira"]
x = input("enter the word : ")
print (" ")
print('{} has occurred {} times'.format(x, countX(lst, x)))
