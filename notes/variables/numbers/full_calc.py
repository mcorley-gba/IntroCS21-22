#Get the operation from the user
operation = input("Choose an operation: \
                    \n\t1: +\
                    \n\t2: -\
                    \n\t3: *\
                    \n\t4: /\
                    \n\t5: //\
                    \n\t6: **")

#Get 2 numbers from user
number_1 = eval(input("Please enter a number: "))
number_2 = eval(input("Please enter another number: "))

#Make python do the correct operation
#and tell user the result
#We will use 'conditional statements' AKA 'if ... then' statements
if (operation == "1"):
    print(number_1 + number_2)