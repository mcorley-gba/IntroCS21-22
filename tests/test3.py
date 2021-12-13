#Test 3 - Final Test -- Fall 2021
#For your final exam you should work each of the three problems below:

#PROBLEM 1 - Animal Encyclopedia
#   a.) Make three dictionaries. Each dictionary should represent a 
#   different animal. In each dictionary, include the name of the animal, 
#   the continent it is native to, and at least one other fact.  
#   b.) Store your dictionaries in a list. Loop through your list and
#   print what you know about each animal.
#YOUR CODE GOES BELOW:


#PROBLEM 2 - No More Pastrami!
#   Below is a completed version of the finished/unfinished sandwiches
#   classwork. Notice that the 'pastrami' sandwich appears several times.
#   a.) Near the beginning of the code, add code that will print a message to 
#   customers saying the restaurant is out of pastrami.
#   b.) Use a loop to remove all occurences of 'pastrami' from the 
#   'unfinished' list before the sandwiches are "made".

unfinished = ['turkey','pastrami', 'meatball sub', 'ham and cheese', \
    'pastrami', 'veggie', 'italian sub']
finished_sandwiches = []

while unfinished:
    current_sandwich = unfinished.pop()
    print(f"We are making your {current_sandwich} sandwich.\
\nIt will be ready momentarily.")
    finished_sandwiches.append(current_sandwich)

print("We have finished making the following sandwiches.")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)


#PROBLEM 3 - Custom Sandwich Creator:
#   a.) Write a function that takes the following parameters
#       (1) The customer's name
#       (2) The sandwich they want (e.g., ham, turkey, meatball, etc.),
#       (3) The bread they want, and
#       (4) A toppings parameter that takes as many toppings as the
#       customer provides when he/she calls the function.
#   b.) The function should print a well-formatted summary of the sandwich 
#   being ordered.
