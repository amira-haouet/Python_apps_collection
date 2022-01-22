# Program to find the sum of all numbers stored in a list ;)

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val

print("The sum is", sum)
print("  ")

print(" ******************* ")
# The range() function

print(range(10))
print("  ")

print(" ******************* ")
print(list(range(10)))
print("  ")

print(" ******************* ")
print(list(range(2, 8)))
print("  ")

print(" ******************* ")
print(list(range(2, 20, 3)))


print("  ")

print(" ******************* ")
# Program to iterate through a list using indexing

sports = ['foot', 'tennis', 'xxxx']

# iterate over the list using index
for i in range(len(sports)):
    print("I like", sports[i])
