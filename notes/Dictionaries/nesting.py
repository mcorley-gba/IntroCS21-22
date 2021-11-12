#nesting.py

#Nesting is when we have one programming structure inside of another
#In particular today we will look at lists and dictionaries.

alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

#See nesting three dictionaries inside of a list:

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#Above is a bit unrealistic
#Let's use a for loop to create 30 aliens (dictionaries) and 
#store them in a list. 

print("\n\n\n\n\n\n\n\n\n\n")

#Make empty list for new aliens:
aliens = []

#Make 30 aliens
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#Modify the first 3 aliens:
for alien in aliens[:3]:
    if alien['color'] == 'green': #If the alien has not already been changed
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow': #If the color has already changed, change it further
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#Print first 5:
for alien in aliens[0:5]:
    print(alien)
print("...")

#See how many are there in total
print(f"There are {len(aliens)} in total.")

#It is very common to have dictionaries in lists when each dictionary
#contains many pieces of information about a single object or type of object.


print("\n\n\n\n\n\n\n")

#Lists within Dictionaries

#Store information about the burger being ordered:
burger = {
    'bun': 'Sesame Seed',
    'toppings':['mayo', 'pickles', 'lettuce', 'mustard', 'tomato']
}

#Echo back to customer to make sure it's correct:
print(f"You ordered a burger with a {burger['bun']} bun and \
the following toppings: ")
for topping in burger['toppings']: #This will loop through the list of toppings.
    print(f"\t{topping}")

print("\n\n\n\n\n\n")

favorite_courses = {
    'Ty':['Science', 'English'],
    'Noah':['English','PE', 'Math'],
    'Ryder':['Math','English'],
    'Doug':['CS','Math'],
    'Kameron':['History', 'CS'],
    'Collin':['Math','Spanish'],
    'Logan':['Bible','History']
}

#Loop through the dictionary and loop through each list:
for name, courses in favorite_courses.items():
    print(f"\n{name.title()}'s favorite courses are: ")
    for course in courses:
        print(f"\t{course}")

for name, courses in favorite_courses.items():
    print(f"\n{name.title()}'s favorite courses are {course for course in courses}")