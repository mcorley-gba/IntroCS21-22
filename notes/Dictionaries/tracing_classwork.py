#In this assignment you will trace 2 pieces of code. Recall: tracing code is 
#running through the code in your mind or on paper to see what the final output
#will be without evaluating it on a computer.


#CODE 1:
number = 10
print(number)
for n in range(10000):
    if number % 2 == 0:  #This will test if the number is even
        number = number/2 
        print(number)
    elif (number % 2 == 1) and (number != 1): #The first test here will check if the number is odd. I'll let you tell what the second test checks.
        number = 3*number + 1
        print(number)
    elif number == 1:
        break #I'll give you this for free: the keyword 'break' terminates a loop, even if the loop is not properly finished yet.

#Questions:
#   1. What will print from the above code with starting number 10? (HINT: There should be seven lines of output)
#   2. Hopefully you saw that eventually the above code will set number equal to 1 and stop. Can you think of a number for which that won't happen?






#CODE 2:
#Tomorrow in class, we will talk about nesting. It is not a hard concept. IN FACT, one simple appication of nesting is 
#having a list inside a dictionary as you will see below:

customer_pizza = { #imagine this dictionary is built from customer input (perhaps on an app?)
    'requested_crust': 'hand-tossed',
    'requested_toppings': ['pepperoni', 'extra cheese' 'jalepenos', 'mushrooms'] #Here is an example of nesting: A list inside a dictionary
} 

#Let's repeat the customer order back to them so they can verify it is correct:
print(f"You ordered a {customer_pizza['requested_crust']} crust pizza with the following toppings: ")

for topping in customer_pizza['requested_toppings']: #This will loop through the list that is nested as a value inside the dictionary
    print(f"\t{topping}") #Do you remember what the \t key-combo does in a string?

#What will be printed when this code is run? 


#Write your answers on paper or in a google doc and submit them on google classroom.
