#PROBLEM 1:
#Make a class called Restaurant. This class should have the following features:
#    a)The __init__() method for this class should take in two parameters
#      (other than 'self') -- restaurant_name and cuisine_type -- and store
#      them as attributes.
#    b)The __init__() method should also create (NOT take-in from the user) an attribute called
#      number_served. This attribute should be initialized to zero.
#    c)Add a method to Restaurant called describe_restaurant() which takes no parameters prints
#      the restaurant name and the cuisine type.
#    d)Add a method called open_restaurant() that takes no parameters and prints a message stating
#      that the restaurant is open.
#    e)Add a method called set_number_served(...) that takes a number as a parameter
#      and sets that as the number_served attribute.
#    f)Add a method called increment_number_served() that takes no parameters and increments the
#      number_served attribute by 1 each time it is called.
#
#
#PROBLEM 2:
#Create a class called IceCreamStand that is a child of Restaurant.
#    a)Initialize IceCreamStand using the super().__init__() call.
#    b)Create a new class (separate from IceCreamStand) called IceCreamFlavors that has the following
#      features.
#        1)Stores a list of three available flavors as an attribute in the
#          __init__() method. NOTE: The list should be a python list and it 
#          SHOULD NOT be a parameter in the __init__ for IceCreamStand.
#        2)Has a method called flavors_today() that takes no parameters and prints a message reporting
#          the three flavors available.
#    c)Add an attribute to the IceCreamStand __init__() method called
#      available_flavors. This attribute should be an instance of the
#      IceCreamFlavors class.
#
#
#PROBLEM 3:
#Create a separate python script.
#    a)Import the three classes you have created.
#    b)Create a restaurant and call the describe_restaurant() method on it.
#    c)Create an ice cream stand and call the flavors_today() method.
#
#
#BONUS POINTS AVAILABLE:
#   a) Good programming practices (i.e., doc-strings, etc.)
#   b) Add a method to IceCreamStand called 'add_flavor(...)' 
#       that takes a flavor as a parameter and adds it to the 
#       available_flavors list.
#
#YOU MUST SUBMIT 2 PYTHON FILES FOR THIS TEST.