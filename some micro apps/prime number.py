# Program to check if a number is prime or not

#num = 30
# or
'''Example 1: Using a flag variable
'''
# To take input from the user

print(" ")
print(" Example 1: Using a flag variable")
print(" ")

num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

print(" ")
print(" Using a for...else statement")
print(" ")