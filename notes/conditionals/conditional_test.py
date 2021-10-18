countries = ['usA', 'England', 'canada', 'taiwan', 'indIa']
for country in countries:
    if country == 'usA':
        print(country.upper())
    else:
        print(country.title())

#Check for equality:
#== - checks if two quantities are equal.
#   for strings, this is case sensitive: usa DNE usA

#Check for Inequality:
# != - Checks if two quantities are NOT equal.
#       That is, it will return a value of 'True' if they are Not equal.

requested_topping = 'pineapple'

if requested_topping != 'pineapple':
    #The test doesn't care what requested topping is, it just cares
    #that it is NOT pineapple.
    print("No Pineapple!")

#Numerical Comparisons
#== - tests equality
# != - tests inequality
# <= - less than or equal to
# < - Less than
# >= - Greater than or equal to
# > - Greater than

answer = 42
if answer != 42:
    print('That is not the answer! Please try again.')

if answer == 42:
    print('Correct! Great Job!')

#Check more than one condition...
#Check if country = 'usa' and my_age >= driving_age
#Use the and operator

requested_toppings = ['mushrooms', 'onions', 'pineapple']
#check if 'mushrooms' is in the list?
#Check if a particular item is in a list:
print('mushrooms' in requested_toppings)
# item in list

del requested_toppings[0]

if 'mushrooms' in requested_toppings:
    print("Customer wants mushrooms")

#Conditional tests are also called Boolean expression
#Boolean values are either True or False
game_active = True
high_score = False