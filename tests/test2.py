#INTRODUCTION to COMPUTER SCIENCE
#TEST 2: LISTS AND 'FOR' LOOPS

#1. Define a list with ten names in it. 


#2. Create a 'for' loop that will loop through each name in your list
#   Each iteration should print a message saying that the person 
#   is a good student.
#   Example output: Joe is a good student. 



#3. In your list of names, do the following:
#   a. Delete the name at index 2
#   b. Insert a new name at index 5
#   c. Append a new name to the list. 
#   d. Sort your list in alphabetical order.
#   e. Print your modified, sorted list.


#4. MULTIPLE CHOICE: Un-Comment the line of code below that will 
#   create a list of numbers from 1 to 20:
#numbers = range(1,21)          #OPTION A
#numbers = list(1,20)           #OPTION B
#numbers = int(1,20)            #OPTION C
#numbers = list(range(1,21))    #OPTION D


#5. With your list of numbers from above, use a for loop to 
#   find the average of the numbers. 


#6. The code below has errors, please fix it. 
#   It should output the letters of the alphabet (one per line)
#   and the number of letters in the alphabet (without just printing the number 26).
#   It should print the number of letters ONLY ONCE.
my_abcs = ['a','b','c','d','e','f','g','h','i','j','k','l','m',n,'o','p','q','r','s','t','u','v','w','x','y','z']
for letter in my_abcs
    print(letter)
    print(len(my_abcs))

#BONUS: Below are two lists, each ten items long. Use a 'for' loop to create a list of tuples
#       in which the first item in each tuple is from list1 and the second in each tuple is
#       from list2. 

list1 = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'Ruth', 'I Samuel', 'II Samuel']
list2 = ['Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', 'I Corinthians', 'II Corinthians', 'Galatians', 'Ephesians']