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

print_models(unprinted, completed_models)
show_completed_models(completed_models)
#completed_models continued to exist with the modifications made by
#print_models because the list existed outside the function.
#It was created before the function was called.