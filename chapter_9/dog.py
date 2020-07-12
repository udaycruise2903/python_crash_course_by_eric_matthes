# Programmer: Uday Date: 22-apr-2020
class Dog():
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to the command."""
        print(self.name.title() + " is sitting.")
    
    def roll_over(self):
        """Simulate a dog rolling over in response to the command."""
        print(self.name.title() + " is rolled over.")

# Make an instance from a class with the attributes.
my_dog = Dog('jimmy', 3)

print("\n My dog's name is " + my_dog.name.title() + ".")
print("My dog 's age is " + str(my_dog.age) + ".")

# Calling methods 
my_dog = Dog('johnny',2)

my_dog.sit()
my_dog.roll_over()

# Creating Multiple Instances
my_dog = Dog('seena', 1)
your_dog = Dog('ramu', 6)

print("\n My dog's name is " + my_dog.name.title() + ".")
print("My dog 's age is " + str(my_dog.age) + ".")

print("\n My dog's name is " + your_dog.name.title() + ".")
print("My dog's age is " + str(your_dog.age) + ".")
