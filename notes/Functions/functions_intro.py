#function_intro.py
#functions are blocks of code designed to accomplish a particular task
#functions are 'callable' from other code/functions
#               --other code (not just the user) can make the function run

#Benefit:
#If we need to accomplish the same task repeatedly in a program,
#we only need to 'call' the function several times, not write several
#sections of identical code

#Function to say 'Hello':
def hello_user(username): #general syntax is familiar
    #def keyword - begins a function definition
    #hello_user - name of the function
    #() - to hold information, parameters, the function needs to do its job
    #   - In this case, the function needs one parameter
    #   - len(list)
    '''Display a greeting'''
    #docstring - describes what the function does.
    #          - Python can generate documentation for programs
    #            and it looks for docstrings when it does that.
    print(f"Hello, {username}!")
    #Instructions for the function to accomplish
    #docstring + instructions = body of the function

#Calling code
#Three ways to call with parameters:
#1: directly type the parameter into the function
hello_user('mcorley') #this will run the function

#2: define a variable with the parameter stored in it, 
#   then use the variable when calling the function.
name = 'mcorley'
hello_user(name)

#3: specifically define the parameter within the function call
hello_user(username='mcorley') #You must use the same parameter name as is in the def

def num_int(xmin, xmax, ymin, ymax, delta_x):
    print('stuff')

num_int(xmin=4,xmax=3,ymin=-8,ymax=9,delta_x=5)
#This makes debugging much easier in functions with several parameters.

print('\n\n\n\n\n\n\n\n')

def pet_description(pet_name, animal_type='dog'):
    #Now the user MUST provide a pet_name, but they don't have to give an animal type
    '''Displays info about a pet'''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

pet_description('pepper')
#since we didn't give a specific argument for the animal_type,
#python defaulted to 'dog'

pet_description('tuna', 'cat')
#By providing a specific animal_type argument
#we override the default value of 'dog'

""" pet_description('dog','pepper')

pet_description(pet_name='pepper', animal_type='dog')
#pet_name and animal_type are parameters
#'pepper' and 'dog' are arguments

pet_description('cat', 'tuna')
pet_description('dog', 'london')
pet_description(pet_name='smokey', animal_type='dog')

#It is possible to give functions a default value """