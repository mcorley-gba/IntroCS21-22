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
    'MaKenna'   :'Biology'}

for name, course in favorite_classes.items():
    print(f"{name.title()}'s favorite class is {course.title()}.")