class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


# instantiate the Parrot class
amira = Parrot("amira", 23)
mouh = Parrot("mouh", 24)

# access the class attributes
print("amira is not a {}".format(amira.__class__.species))
print("mouh is also not a {}".format(mouh.__class__.species))

# access the instance attributes
print("{} is {} years old".format(amira.name, amira.age))
print("{} is {} years old".format(mouh.name, mouh.age))
