#Intro CS -- Test 3, Version 1 -- Fall 2021
#You must work two of the following three questions.
#If you correctly solve all three, I will replace 
#your lowest classwork score with a 100. If you don't
#have a classwork less than 100, I will give you
#bonus points on this test.

#PROBLEM 1 - Animal Encyclopedia
#   a.) Make three dictionaries. Each dictionary should represent a 
#   different animal. In each dictionary, include the name of the animal, 
#   the continent it is native to, and at least one other fact (for example,
#   'endangered' = 'Yes').  
#   b.) Store your dictionaries in a list. Loop through your list and
#   neatly print what you know about each animal.
#YOUR CODE GOES BELOW:


#PROBLEM 2 - No More Pastrami!
#   Below is a completed version of the finished/unfinished sandwiches
#   classwork. Notice that the 'pastrami' sandwich appears several times.
#   a.) Near the beginning of the code, add code that will print a message to 
#   customers apologizing and saying the restaurant is out of pastrami.
#   b.) Use a loop to remove all occurrences of 'pastrami' from the 
#   'unfinished' list before the sandwiches are "made".

unfinished = ['turkey','pastrami', 'meatball sub', 'ham and cheese', \
    'pastrami', 'veggie', 'italian sub', 'pastrami']
finished_sandwiches = []

while unfinished:
    current_sandwich = unfinished.pop()
    print(f"\nWe are making your {current_sandwich} sandwich.\
\n\tIt will be ready momentarily.")
    finished_sandwiches.append(current_sandwich)

print("\nWe have finished making the following sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(f"\t-{finished_sandwich}")


#PROBLEM 3 - Custom Sandwich Creator:
#   a.) Write a function that takes the following parameters
#       (1) The customer's name
#       (2) The sandwich they want (e.g., ham, turkey, meatball, etc.),
#       (3) The bread they want (e.g., white, wheat, herb and cheese, etc), and
#       (4) A toppings parameter that takes as many toppings as the
#       customer provides when he/she calls the function.
#   b.) The function should print a well-formatted summary of the sandwich 
#   being ordered.
