#Whitespace - within strings: tabs, spaces, and end-of-line characters.
#Adding whitespace
# Tab: \t
print("Python")
print("\tPython")

# Line-breaks: \n
print("Computer Languages: \nPython\nFortran\nC\nC++")
print("Computer Languages: \n\tPython\n\tFortran\n\tC\n\tC++")
print("Computer Languages: \t\nPython\t\nFortran\t\nC\t\nC++")

#Stripping whitespace:
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
#rstrip() does not permanently change the variable string without 
# reassigning the variable
favorite_language = favorite_language.rstrip()
#similarly we have .lstrip() - takes whitespace off the left side
#                  .strip() - takes all whitespace