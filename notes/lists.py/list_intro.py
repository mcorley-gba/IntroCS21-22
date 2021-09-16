#list_intro.py

#What is a list?
#   A collection of items in a particular order.
#   Ex: The alphabet, digits 0-9, names of family
#   Typically we will plural nouns for list names

star_treks = ['TOS', 'TNG', 'Voyager', 'DS9']
#print(star_treks)

#Accessing Elements
#Because lists are ordered, each element has an index value
#we can use the index value to get elements out.
#REMEMBER: Python starts counting 0
#print(star_treks[0])
#print(star_treks[2])

#If you keep getting off-by-one indexing problems, check 
# to make sure you are counting from zero.

#The individual elements act like variables in their own right,
#    we can operate on them like variables.

print(star_treks[0].title())

#We need to check the last item of a list, but we dont
#   know how many elements are in the list.
print(star_treks[-1])
print(star_treks[-3])

message = f"The first star trek I \
watched was {star_treks[0].title()}."

print(message)