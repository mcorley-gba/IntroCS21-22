#more_functions.py

#Passing a List into a Function:
def greet_users(names): 
    '''Print a simple greeting for each user in the list.'''
    #loop through and print a message to each:
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

#Driver code to test:
usernames = ["bob", "ross", "doug"]
greet_users(names=usernames)
            #Parameter = actual_data

print('\n\n\n\n\n\n\n\n\n\n\n\n')

#Modifying a list within a function:
def print_models(unprinted, completed):
    """
    Simulate printing 3d designs until all are completed.
    Each design will move from 'unprinted' to 'completed'
    as we simulate the printing.
    """
    while unprinted: #As long as we have unprinted designs, this will run.
        current_design = unprinted.pop()
        #simulate printing
        print(f"We are printing {current_design}.")
        completed.append(current_design)

def show_completed_models(completed):
    """Show the 3d models that were completed."""
    print('\nThe following 3d models have finished printing: ')
    for completed_model in completed:
        print(completed_model)

#Driver code to use the functions
unprinted = ['dodecahedron', 'pendant', 'phone case']
completed_models = []

#print_models(unprinted, completed_models)
#show_completed_models(completed_models)
#completed_models continued to exist with the modifications made by
#print_models because the list existed outside the function.
#It was created before the function was called.

#Prevent a function from modifying a list.
#If we wanted to keep the original list of unprinted models
#without deleting them, then we would need to pass the function
#a copy of the list rather than the original.

#Review: 2 Ways to copy a list:
#1 - Not a true copy. Two variable names pointing at the same internal
#data.
# list = [...data here...]
# list_copy = list

#2 - Make an entirely distinct copy
# list_copy = list[:]

print_models(unprinted[:], completed_models)
print(unprinted)

#Single Arguments, 
#Multiple distinct arguments
#List arguments
#Passing an indeterminant number of distinct arguments

print('\n\n\n\n\n\n\n\n\n\n')

def make_pizza(crust, size, *toppings):
    #the star tells python that we don't know how many 
    #arguments will be passed in.
    #We can mix distinct arguments and arbitrary arguments
    """Print the topings that have been requested."""
    print(f"\nMaking a {size}-inch pizza on {crust} crust with the following requested toppings: ")
    for topping in toppings:
        print(f" - {topping}")

#make_pizza('pepperoni')
#make_pizza('sausage', 'extra cheese', 'banana peppers')
make_pizza('thin', 12, 'bacon', 'peppers', 'sausage', 'pepperoni')
#You may often see placeholder arguments with names like
# *args

print('\n\n\n\n\n\n\n\n\n\n\n')

#What did we assume above about our arbitrary number of arguments?
#We assumed they would all be strings.

def build_user(first, last, **user_info):
    #The double star tells python to make an empty dictionary
    #so we can mix-and-match data types (e.g., string and int)
    """Build a dictionary containing user information"""
    user_info['first'] = first
    user_info['last'] = last
    return user_info

user_profile = build_user('albert',
                            'einstein',
                            location='princeton',
                            field='physics')

print(user_profile)

#You can mix positional, keyword, and arbitrary values in many different
#ways

#KEY IDEA: Use the simplest approach you can think of to get the job done


#CONGRATULATIONS - WE HAVE FINISHED OUR NOTES FOR FALL 2021!

#After Christmas - Modules and Classes 