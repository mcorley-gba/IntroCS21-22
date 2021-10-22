#Conditional Tests HW - Due Monday
# 13 Tests --> 1 True and 1 False for each

#If Statements

#Simplest structure of an if statement:
#   if conditional_test:
#       do something <-- Instructions/commands

#my_age = 13
#if my_age >= 18:
#    print("You are old enough to vote.")
#    print("Are you registered to vote?")

#Unindent!

#Indentation plays the same role for if-statements
#as it did for 'for' loops. Anything indented will be
#executed whenever the conditional test is true. Anything
#indented will be skipped whenever the conditional test is
#false.

#USE CAUTION - Don't forget to un-indent when you are finished
#with your if-block.

#Often we want one action if the conditional test is True,
#But make another action whenever it is false. 
my_age = 33
if my_age >= 18:
    print("You are old enough to vote.")
    print("Are you registered to vote?")
else: #Catches any instances when the above test fails
    print("You are not old enough to vote.")
    print("Please register to vote when you turn 18.")

#The if-else structure works very well in situations in which python
#needs to always execute one of two possible actions. 
#in a simple if-else block, one of the two will always be evaluated.

#if-elif-else Chain
#Python will only execute one block in an if-elif-else chain. 
#As soon as one test passes, python execute that block
#and skips the rest (even if they might be true).

#Example: Admission to a theme park:
#Three price-levels: 
#Under 4 --> Free
#between 4 and 18 --> $25
#18 to 65 --> $40
#65 and older--> $20


age = 66

if age < 4:
    price = 0
elif age < 18: #elif = else+if --> if the above test(s) is(are) false, 
                #try this test next
    price = 25
elif age < 65:
    price = 40
    #We can have more than one elif statement
elif age >= 65:
    price = 20
#The catch-all 'else' statement is no longer needed.

#If you have a definite condition for the last block of an if-elif-else 
#Use an elif statement with a definite conditional test. If you don't have a
#definite condition in mind for the last layer of an if-elif-else block,
#else works fine (unless you don't really need it).

print(f"Your admission cost is ${price}")
#Think about the structure of your if-elif-else blocks.
#Especially when the tests overlap

#The purpose of the above code was to determine the cost for the user

#Multiple conditions.
requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("Finished making pizza!")


