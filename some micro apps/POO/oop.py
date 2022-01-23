
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


class Person:

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def meth1(self, song):
        return "{} feel {}".format(self.name, song)

    def meth2(self):
        return "{} is now dancing".format(self.name)


# instantiate the object
amira = Person("Amira", 23)

# call our instance methods
print(amira.meth1(" Happy "))
print(amira.meth2())


print(" ")
print(" ")
print(" ******** Example 3: Use of Inheritance in Python *******")
print(" ")


# parent class
class Vehicle:

    def __init__(self):
        print("Vehicle is ready")

    def whoisThis(self):
        print("Vehicle")

    def roll(self):
        print("rolled faster")

# child class


class Car(Vehicle):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Car is ready")

    def whoisThis(self):
        print("Car !")

    def run(self):
        print("Run faster")


bmw = Car()
bmw.whoisThis()
bmw.roll()
bmw.run()

print(" ")
print(" ")
print(" ******** Example 4: Data Encapsulation in Python *******")
print(" ")

class Computer:
    
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

print(" ")
print(" ")
print(" ******** Example 5: Using Polymorphism in Python *******")
print(" ")

class Parrot:
    
    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)