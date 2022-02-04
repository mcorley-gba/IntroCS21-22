#car_class.py
class Car:
    """A class to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes"""
        #Everything defined in the __init__ is an attribute
        #We can differentiate between:
        #   1. User-Provided: The attributes in the __init__ parameter list (e.g., make model year)
        #   2. Pre-defined/default attributes: Attributes defined in __init__ by the developer
        #       e.g., odometer_reading
        #Takeaway - Not every attribute must be listed in the __init__ parameter list.
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Print a long-form name of the car"""
        long_name = f"{self.year} {self.make} {self.model}"
        print(long_name)

    def read_odometer(self):
        """Print a statement of the odometer reading"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        set the odometer reading to 'mileage'
        reject if mileage is less than current 
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer! That's illegal!") 

    def increment_odometer(self, miles):
        """
        adds given miles to odometer
        reject if miles is negative
        """   
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer! That's illegal!") 


class Battery:
    """A simple model of a batter"""
    def __init__(self, battery_size=75):
        """Initialize battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement of the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print the range of the battery in the electric car"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go {range} miles on a full charge.")

class ElectricCar(Car): #Makes electriccar a child of car.
    """Models aspects of an electric car. Inherits from Car."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of child class by calling parent class
        Then initialize particular electic car attributes
        """
        super().__init__(make, model, year)
        self.battery = Battery() #This makes an instance of the battery class as an attributes
                                #of the electric car class.
