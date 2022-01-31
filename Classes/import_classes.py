#import_classes.py
#Class files can become very big/long!
#Python philosophy -- files should be as uncluttered as possible.
# -- This means storing classes in one file, then importing them
#   into another.
from car_class import ElectricCar
#from filename import Class
#This tells python to open the car_class.py file and import the Car
#class. Now we can use the class as though we had written it in this file
"""
new_car = Car('audi', 'a4', 2019)
new_car.get_descriptive_name()
new_car.update_odometer(23)
new_car.read_odometer()
"""

new_electric_car = ElectricCar('tesla', 'model z', 2021)
new_electric_car.get_descriptive_name()
new_electric_car.battery.describe_battery()
new_electric_car.battery.get_range()


#We can store multiple classes in one module and import as many or as few as we want.
#However, also in keeping with the philosophy of python, the classe in one module
#SHOULD all be related.

#We can import more than one class from a module:
from car_class import Car, ElectricCar
my_vw_bug = Car('vw', 'bettle', 2005)
my_vw_bug.get_descriptive_name()

my_leaf = ElectricCar('nissan', 'leaf', 2010)
my_leaf.get_descriptive_name()

#We can import a whole module of classes:
import car_class
#Tradeoff - we have to prefix each class we use with 'car_class.'
my_truck = car_class.Car('ford', 'F150', 2018)
my_truck.get_descriptive_name()

#Finally, we can avoid the 'car_class.' notation by using
from car_class import *
#SHOULD BE AVOIDED IF AT ALL POSSIBLE 
