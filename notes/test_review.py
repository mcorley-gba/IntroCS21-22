#What is a string in python?
# A sequence of characters which are enclosed in single
#   or double quotes .

#Does python see any difference between '1' and "1"?
#   No. Why Not? For python, single and double quotes both
#   denote strings.

#Is there a difference between 1 and '1' in Python?
#   Yes. The first is an integer
#        The second is a string

#What will be the output of this code:
str1 = "Time for class"
str2 = "time for \n class"
print(str1)
print(str2)
#Time for class
#time for
# class

#What will be the output:
str3 = "Test on Wednesday"
str4 = "Test \ton \n Wednesday"
print(str3)
print(str4)
#Test on Wednesday
#Test   on
# Wednesday

#For the variables below:
class_time = "2 O'Clock"
statement = "Class is at"
#How would you use these variables to print
#   Class is at 2 O'Clock
print(statement, class_time)

#What are the 6 basic arithmetic functions in python
# +, -, *, /, //, **
#Addition, subtraction, mult., division, integer division, exponentiation

#What will be the output?
print(5/2)
print(5//2)
#2.5
#2 -> Integer division gives the next lowest integer

#What is the output
print(-7/2)
print(-7//2)
#-3.5
#-4

#Which of these are good variable names?
num_questions = 26
average_of_all_scores_in_class_on_wednesday_test = 99.25
avg_test_scores = 99.25
n = 8.9 #TOO VAgue

#What's wrong with these?
computers in class = 10 #NO SPACES ALLOWED
one_1_computer_1  = "This one" #CAN't START WITH A NUMBER
I_LOVE_CS_CLASS! = "YAY!" #No Special characters
