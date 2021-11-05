#Looping through a dictionary

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

print(user_0) #Prints the whole dictionary at once. Sometimes useful, I don't want now.

#Want to print each entry on its own line.
#Use For Loops!

for key,value in user_0.items(): #creates dummy variables to store both data points in the dictionary
                                #.items() is a method which returns a list of key-value pairs
    print(f"Key: {key}")        #Printing the key for each iteration of the loop.
    print(f"Value: {value} \n")

favorite_classes = {
    'Ty'        : 'Computer Science',
    'Noah J'    :'PE',
    'Ryder'     :'Math',
    'Kameron'   :'Spanish',
    'Collin'    :'Chemistry',
    'Ramsey'    :'Strength and Fitness',
    'Doug'      :'Math',
    'Noah L'    :'Computer Science',
    'Logan'     :'Bible',
    'MaKenna'   :'Biology'
}
#   keys    values
for name, course in favorite_classes.items():
    print(f"{name}'s favorite class is {course}.")

print("\n\n\n\n\n\n\n\n")

#Loop only through the keys in a dictionary
for name in favorite_classes.keys(): #.keys() -- creates a list of the keys from the dictionary.
    print(name)

""" for dummy_var in favorite_classes: #Looping through keys is the default behavior 
#                               when looping through a dictionary
    print(dummy_var) """

#Accessing/Looping through the values in a dictionary
for name in favorite_classes.keys():
    print(favorite_classes[name])

for course in favorite_classes.values():
    print(course)

print("\n\n\n\n\n\n\n\n\n")

#Looping through specific/subset of keys in a dictionary:
#Create a list of the keys that we want:
state_xc = ['Ty', 'Noah J', 'Collin']

#2 Ways:
#1: Loop through all keys, use conditionals to filter:
for name in favorite_classes.keys():
    if name in state_xc:
        print(f'{name} once said, "My favorite class is {favorite_classes[name]}"')

print("\n\n\n\n\n")

#2: Loop through the list and use .get()
for name in state_xc:
    favorite_course = favorite_classes[name]           #.get(name, f"{name} not in list")
    print(favorite_course)


print("\n\n\n\n\n\n")

for course in favorite_classes.values():
    print(course)

print("\n\n\n\n\n\n")
#A set in python is a collection of values in which each item is/must be unique

#2 ways to make a set:
#1: Call the set function around a list:
for course in set(favorite_classes.values()):
    print(course)

#2: define a brand-new set:
courses = {'Biology', 'Chem', 'Math', 'CS', 'Chem', 'Bible', 'PE', 'Math'}
print(courses)