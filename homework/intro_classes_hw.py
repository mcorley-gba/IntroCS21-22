#Make a class called Restaurant. The initialization method for Restaurant
#should store two attributes: restaurant_name and cuisine_type. Make a method
#within the class called describe_restaurant() that prints these pieces of
#information. Make a second method called open_restaurant() that prints a message
#stating that the restaurant is open.
#YOUR CODE GOES BELOW:

class Restaurant:
    """Class to simulate a restaurant. Methods to describe and open the restaurant."""

    def __init__(self,restaurant_name, cuisine_type):
        """Initialization for Restaurant. Stores name and type of cuisine."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints a statement about the restaurant"""
        print(f"\nThe name of my restaurant is {self.restaurant_name.title()}.")
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} food.")

    def open_restaurant(self):
        """Simulating opening the restaurant by printing a message saying the restaurant is open."""
        print(f"{self.restaurant_name.title()} is open!")



#After making your class, create three different instances of the class.
#Call describe_restaurant() for each instance.
the_olive_garden = Restaurant("The Olive Garden", "italian")

restaurant_1 = Restaurant("The Cheesecake Factory", "American")
restaurant_1.describe_restaurant()

amigos = Restaurant("Amigo's", "mexican")
amigos.describe_restaurant()

mcdonalds = Restaurant("McDonald's", "American")
mcdonalds.describe_restaurant()
mcdonalds.open_restaurant()