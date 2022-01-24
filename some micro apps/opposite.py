str1 = input('Enter first string:  ')
str2 =  input('Enter second string:  ')
#str1="hello"
 

# convert both the strings into lowercase
#str1 = str1.lower()
#str2 = str2.lower()
'''
print(" ")
print(" *** result ***")
print(" ")
print(str1[::-1])
print(" ")
print(str2[::-1])

'''

print(" ")
print(" *** result ***")
print(" ")
if(len(str1) == len(str2)):
    


    # if sorted char arrays are same
    if(str1[::-1]==str2[::-1]):
        print(str1 + " and " + str2 + " are opposite.")
    else:
        print(str1 + " and " + str2 + " are not opposite.")

else:
    print(str1 + " and " + str2 + " are not opposite.")
