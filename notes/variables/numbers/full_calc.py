problem = input("Do you have a problem you want to calculate? (y or n): ")
    #   n       != n
while (problem != "n"):     # != is a "not-equals" comparison
    #Get the operation from the user
    operation = input("Choose an operation: \
                        \n\t1: +\
                        \n\t2: -\
                        \n\t3: *\
                        \n\t4: /\
                        \n\t5: //\
                        \n\t6: ** \
                        \n\t-------- \
                        \n\t")

    #Get 2 numbers from user
    number_1 = eval(input("Please enter a number: "))
    number_2 = eval(input("Please enter another number: "))

    #Make python do the correct operation
    #and tell user the result
    #We will use 'conditional statements' AKA 'if ... then' statements
    if (operation == "1"):  # == is comparing two values
                            # = is assigning values
        print(number_1 + number_2)
    if (operation == "2"):
        print(number_1 - number_2)
    if (operation == "3"):
        print(number_1 * number_2)
    if (operation == "4"):
        print(number_1 / number_2)
    if (operation == "5"):
        print(number_1 // number_2)
    if (operation == "6"):
        print(number_1**number_2)
    
    #Give user option to stop
    problem = input("Do you have another problem? (y or n): ")
