#function_return.py

def get_formatted_name(first_name, last_name, middle_name=""):
    #scope - first_name is not a true variable. It is a parameter
    #it only exists for the duration of the function.
    #make middle_name optional by giving it an empty default value
    '''returns a full name, formatted in title case'''
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
    #the return keyword tells python what data should be
    #given back to the calling program

#Calling/Driver Code
name = get_formatted_name('logan', 'petty', 'joseph')
print('\n\n\n\n\n\n\n\n')


#returning dictionary
def create_person(first_name, last_name, age=None):
    #None is a special value which is used when a numerical (or other) data 
    # has no specific value
    #Age is now an optional parameter
    #None counts as 'False' in conditional tests
    '''creates and returns a dictionary of info about a person'''
    person = {'first':first_name, 'last':last_name}
    if age: #If age is any number, the test is true. If age is 'None', the test is false.
        person['age'] = age #new key: 'age', value = age
    return person #The dictionary we created will be given to the calling program

person = create_person('Evariste', 'Galois',age=21)
print(person)

print('\n\n\n\n\n\n\n\n\n')

#use a function within a loop:
#get_formatted_name is above

while True:
    print("\nPlease enter your name: ")
    print("\tEnter 'q' at any time to quit.")
    first = input("\tFirst name: ")
    if first.lower() == 'q': 
        break
    last = input("\tLast name: ")

    formatted_name = get_formatted_name(first, last)
    print(f"Hello, {formatted_name}!")
