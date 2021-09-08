#Get problem from user.
problem = input("Enter an arithmetic problem or enter 'q' to quit: ")

#Loop around asking for problems until user says to stop
#   We've seen 'for' loops ex: for x in range(100):
#   We need a loop that doesn't have a definite ending 
#   point: A 'while' loop

while (problem != "q"):
    #In the parentheses is a true/false statement. 
    #the loop is going to continue until the statement
    #is false

    #Give answer to user.
    print(problem, "=", eval(problem))

    #Ask for another problem
    problem = input("Enter another problem or enter 'q' to quit: ")

print("Thank you for using my calculator!")