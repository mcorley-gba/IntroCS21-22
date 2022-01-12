#function_style.py

#Not rules that you must follow, but these are conventions
# that many/most developers will use

#1. Every function should have it's own docstring. 
#   Doesn't have to be long. Just long enough to give a 
#   short description of the functions (desired) behavior

#2. If a module has several related functions/data
#   then give a docstring or comment at the beginning of the module

#3. If a parameter in a function has a default value, 
#   then no spaces should be left between the parameter name
#   and the default value in the function def.
#   EX: def example_func(param0, param1="default_value"):

#3b. When you call a function with a keyword argument, the same
#    'no-space' rule should be followed.
#     EX: Using the example_func
#       example_func(value_0, param1="value_1")

#4. By convention, try to keep function definitions to 79 char's
#   or less. If you have a function def with more than that,
#   break the parameter list onto multiple lines, all indented
#   equally:
#   EX: def examle_2(
#                    param0, param1, param2, param3
#                    param4, param5, param6):
#           <function_body>...

#5. All imports should be at the beginning of the file in the first
#   several non-comment lines.

#For more guidelines, see the official unofficial Python style guide:
#   PEP 8 (on python.org)

#Create a module with at least 1 function.
#In a separate file, import using all of the methods we've discussed.