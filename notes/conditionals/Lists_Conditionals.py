#Conditionals and Lists:
requested_toppings = []
#Loop through each list item
#print a message saying "adding {topping}"
if requested_toppings: #Test if requested toppings is NOT empty:
    for requested_topping in requested_toppings:
        if requested_topping == "green peppers":
            print("Sorry, we are out of green peppers.")
        else: #Catches everything else other than green peppers
            print(f"Adding {requested_topping}")
        #print("Adding ", requested_topping)
else: #What if the list IS empty?
    print("Are you sure you don't want any toppings?")

print("Finished making pizza!") #Outside the if-statement AND the loop
print("\n\n\n\n\n")

#Mutliple Lists:


requested_toppings = []
""" num_toppings = eval(input("How many toppings do you want on your pizza?\n"))
if num_toppings > 0:
    for topping in range(num_toppings):
        requested_topping = input("What topping would you like?\n")
        requested_toppings.append(requested_topping)
else: 
    requested_toppings = []
 """
available_toppings = ["mushrooms", "olives", "pepperoni", \
    "3-meat", "pineapple", "extra cheese"]

requested_toppings = ["mushrooms", "sausage", "pepperoni", "extra cheese"]

if requested_toppings: #If requested_toppings is NOT empty
    for requested_topping in requested_toppings: #for item in list:
        if requested_topping in available_toppings: #Checks to see if 
                                            #the requested topping is in th
                                            #list of available toppings
            print(f"Adding {requested_topping}")
        else:
            print(f"Sorry, we don't have {requested_topping}.")
else:  #Catches if there's nothing in the list of requested toppings
    print("Are you sure you want no toppings?")

print("Finished making your pizza!")

#Conditional Tests
#==, Are two things equal?
#!=, Are two things not equal?
#<, <=
#>. >=