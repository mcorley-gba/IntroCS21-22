#Classes - Intro to Object Oriented Programming.
#OOP - paradigm about software creation
#       opposed to imperative or procedural
#       We will write "classes" to represent real-world
#       things, then create "objects" within these classes

#Making an object from a class is called "instantiation"
#We work with "instances" of a class

class Dog:
    """A simple model of a dog that will sit and roll over."""

    def __init__(self, name, age): #These are functions
        #But functions that belong to classes are methods.
        """Initialize name and age attributes."""
        #"self" is a reference to the instance itself
        self.name = name
        self.age = age
        #Any variable prefixed with "self." is available to all
        #instances of this class.

        #When we create an instance of a dog, we will only give
        #values to name and age.

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

        #When we call sit and roll_over, we won't pass any arguments
        #The "self" parameter is carried by the class/object itself

#Make an instance of the Dog class:
my_dog = Dog("Pepper", 2)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

#When we run this program we will be accessing the name
# and age attributes of the OBJECT my_dog

my_dog.sit() #NOT: sit(my_dog)!
my_dog.roll_over()

your_dog = Dog("Lewie", 7) #Create another instance of "Dog"

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()