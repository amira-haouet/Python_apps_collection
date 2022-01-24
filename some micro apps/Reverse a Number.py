
print(" ")
print("************Example 1: Reverse a Number using a while loop*****************")
print(" ")
num = int(input("Enter a number: "))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))


print(" ")
print("************Example 2: Using String slicing*****************")
print(" ")
num = int(input("Enter a number: "))
print(str(num)[::-1])