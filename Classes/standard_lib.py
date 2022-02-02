#standard_lib.py
#Python Standard Library
#set of modules (Classes and stand-alone functions) that are included
#with the python interpreter.

#WE can use any function or class from the library by including
#the right import at the top of the file.

#For example: random numbers
from random import randint, choice
#randint is a random integer generator
my_rand_number = randint(1,6) #Generates a random integer between 1 and 6
#randint is inclusive on the bounds
print(my_rand_number)

cakes = ['Chocolate', 'Vanilla', 'Ice Cream', 'Cookie', 'Birthday']
my_cake = choice(cakes)
print(my_cake)

#DO NOT USE THE RANDOM MODULE for any security-related applications

#Revisit your 'User' Class
#Store the 'User', 'Admin', and 'Privileges' classes in a separate
#  module. Then create a new file with instances of 'User', and 'Admin'
#   Call show_privileges at least once to demonstrate successful import

