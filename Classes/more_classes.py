#more_classes.py
class Car:
    """A simple simulation of a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        #Store the intialization parameters
        #Not every attribute for a class needs to be an init parameter
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #This initializes the odometer_reading attribute
                                #to be zero without needing to come from the user
                                #when an instance is created.

    def get_descriptive_name(self):
        """Return a neatly formatted name of the car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement giving the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to mileage.
        Reject the change if the odometer is being rolled back.
        """ 
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer. That's illegal!")

    def increment_odometer(self, miles):
        """Add the given miles to current mileage"""
        if miles >= 0:
            self.odometer_reading += miles 
            #self.odometer_reading = self.odometer_reading+miles
        else:
            print("You cannot roll back an odometer. That's illegal!")
            

class ElectricCar(Car):
    #Tells python to have the electric cars inherits all the attributes and methods
    #in Car class.
    """Represents attributes specific to electric cars."""
    def __init__(self, make, model, year):
        """Initialize basic attributes from parent class"""
        super().__init__(make, model, year)
        #super() calls a method from the parent class (in this case, Car)


my_car = Car("Toyota", "FJ Cruiser", 2018)
print(my_car.get_descriptive_name())

my_electric_car = ElectricCar("tesla", "model s", 2019)
print(my_electric_car.get_descriptive_name())


#We need to modify the odometer_reading attribute for my_car
#Don't do that in the class itself. We can modify from the main body
#of our script
#Modify as we would any other variable:
my_car.odometer_reading = 23000
my_car.read_odometer()

#If we expect to modify an attribute repeatedly, direct modification (as above)
#Is probably not efficient.
#We can write a method in our class to modify attributes:
my_car.update_odometer(24000)
my_car.read_odometer()

my_car.update_odometer(12000)
my_car.read_odometer()

my_car.increment_odometer(150)
my_car.read_odometer()

my_car.increment_odometer(-1000)
my_car.read_odometer()