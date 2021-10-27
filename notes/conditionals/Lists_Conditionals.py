#Conditionals and Lists:
requested_toppings = ["Mushrooms", "green peppers", "extra cheese"]

#Loop through each list item
#print a message saying "adding {topping}"
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers.")
    else:
        print(f"Adding {requested_topping}")
    #print("Adding ", requested_topping)

print("Finished making pizza!")