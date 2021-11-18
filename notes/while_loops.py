#While loops
#A for loop will run from a start point to a stop point
#A while loop will run until some *condition* is met

#Basic example:

#Starting point (not always needed)
current_number=1
while current_number <= 5: #while conditional_test:
    print(current_number)
    #Exit Condition:
    current_number += 1 #Adds 1 to current_number

#As long as the conditional test is True, the loop will keep repeating
#We must provide an exit-condition to stop the loop
#A counter is one type of exit condition

#A for loop is really a special case of a while loop.
for current_number in range(1,6):
    print(current_number)

print('\n\n\n\n\n\n\n\n')

#Getting user involvement:
prompt = "\nEnter text, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. " #Using + with strings concatenates two or more strings.

message = "" #Starting variable (empty string)
""" while message.lower() != 'quit': #As long as the message is not 'quit', do the following
    message = input(prompt+"\n")

    if message.lower() != 'quit':
        print(message) #Now it will only print if the message is not 'quit'.  """

#User input controlling exit condition is a second way to have an exit condition.


#If a program needs to run as long as many conditions are true, we want to use a 
#single variable that tells us when or if the loop should quit. 
#We call this variable a 'flag'. A flag is typically a Boolean variable.
#So we will structure our loop to run as long as the flag is True.
#As soon as one exit condition is met, the flag is set to False and the loop exits.

print('\n\n\n\n\n\n\n')

#Set flag to True before loop starts.
active_loop = True
message_count = 0
""" while active_loop: #while active_loop=True.
    message = input(prompt)
    message_count += 1
    
    if (message.lower() == 'quit') or (message_count >= 10): #Is lower case message 'quit'?
        active_loop = False #If yes, change flag to False (loop will stop)
    else:
        print(message) #If no, print message and restart (active_loop is still True) """

#Using the break statement

prompt2 = "\nEnter a city you would like to visit: "
prompt2 += "\n(Enter 'quit' when you are finished.) "

""" while True: #This loop will run forever.
    city = input(prompt2) #Get city name from user.

    if city.lower() == 'quit': #If the user wants to quit
        break #break jumps out of a loop and returns to the next level up of indentation
    else:
        print(f"I hear {city.title()} is nice to visit.")
 """
#'break' can be used in ANY python loop. (Even for loops.)

print('\n\n\n\n\n\n\n')

#Tomorrow: using 'continue', then classwork
#Sometimes we don't want to totally break out of a loop.
#Sometimes we just want to skip one or a few iterations
#'continue' command helps do this:

current_number = 0
#Make a while loop that will print only the odd numbers:
while current_number < 10:
    current_number += 1 #exit condition -- counter
    if current_number%2 == 0: #Check if the current_number is even (0 remainder)
        continue #terminates the current loop-cycle and restarts the loop.

    print(current_number)

#Beware of infinite loops! Especially loops with little to no output.
while current_number > 1:
    #print(current_number)
    current_number += 1

print(current_number)