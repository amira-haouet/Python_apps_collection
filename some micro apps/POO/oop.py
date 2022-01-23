
print(" ")
print(" ******** Example 1: Creating Class and Object in Python *******")
print(" ")


class Person:

    # class attribute
    genre = "female"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


# instantiate the Person class
amira = Person("amira", 23)
mouh = Person("mouh", 24)

# access the class attributes
print("amira is a {}".format(amira.__class__.genre))
print("mouh is not a {}".format(mouh.__class__.genre))

# access the instance attributes
print("{} is {} years old".format(amira.name, amira.age))
print("{} is {} years old".format(mouh.name, mouh.age))

print(" ")
print(" ")
print(" ******** Example 2 : Creating Methods in Python *******")
print(" ")
