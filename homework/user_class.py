#In this classwork, you will create a class for users of a computer
#and work with attributes and inheritance. There are problems.

#Problem 1: 
#   a) Create a class called 'User'. Create two attributes: 'first_name'
#   and 'last_name', Then create two other attributes that would also
#   typically be associated with user profiles. 
#   b) Create a method called 'describe_user()' that prints a summary
#   of the user information. 
#   c) Create a method called 'greet_user()' that prints a personalized
#   greeting to the user
#   d) Create an instance of the 'User' class and call both methods.
#YOUR CODE GOES HERE:









#Problem 2:
#   a) Add an attribute to you 'User' class called 'login_attempts'. 
#       The default value for this should be 0
#   b) Write a method called 'increment_login_attempts()' that will 
#       increment the value of 'login_attempts' by 1 each time.
#   c) Write another method in your 'User' class called
#       'reset_login_attempts()' that will reset the 'login_attempts'
#       attribute back to zero.
#   d) Make an instance of 'User' and call 'increment_login_attempts()'
#       several times. Print the 'login_attempts' data. Then call
#       'reset_login_attempts' once. Print the 'login_attempts'
#       data again to make sure it is zero.
#YOUR CODE GOES HERE.








#Problem 3: 
#   a) Write a class called 'Admin' that inherits from the 'User' class.
#   b) Add an attribute called privileges, that stores a list of 
#       strings describing what the admin user can do. For example:
#       "can add post", "can delete post", "can ban user", etc.
#   c) Write a method called 'show_privileges()' that will
#       print the list of administrator privileges.
#   d) Create an instance of 'Admin' anc call this method.
#YOUR CODE GOES HERE










#Problem 4:
#   a) Write a separate Privileges class. This class should have one attribute:
#       'privileges' which should store the same  list as in Problem 3.
#   b) Move the 'show_privileges()' method from 'Admin' to 'Privileges'.
#   c) Add a 'privileges' attribute to your 'Admin' class by 
#       creating an instance of the Privileges class.
#   d) Create an instance of 'Admin' and call the 'show_privileges()' method.
#YOUR CODE GOES HERE