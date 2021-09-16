#Monday - In-class about lists
#Tuesday - No class
#Wednesday-Friday - More lists
#Another test - Probably 2 weeks

#Changing lists
#   Changing elements
#   Adding elements
#   Removing elements

characters = ['Luke', 'leia', 'Han', 'C3PO', 'R2D2']
print(characters[0])

#Change 1st element:
characters[0] = 'Darth Vader'
print(characters)

#Add Elements
#   Add to the end using .append() method
characters.append('Luke')
print(characters)

characters = [] #Make characters an empty list
characters.append('Darth Vader')
characters.append('Han Solo')
characters.append('Luke')
characters.append('Leia')
print(characters)

characters.insert(0, 'Yoda')
print(characters)

characters.insert(3, 'Obi-wan')
print(characters)

#Removing Elements
#   Delete function statement
#   You must know the index of what you want to remove.

#del characters[0]
del characters[1]
print(characters)

# Remove item using the .pop() method
#.pop() removes the last item in a list
#   but we can still use it after we remove it 

#popped_character = characters.pop()
#print(characters)
#print(popped_character)

#Jedi = characters.pop()
#print(f"The best Jedi is {Jedi.title()}.")
#print(characters)

#scoundrel = characters.pop(1)
#print(characters)
#print(scoundrel)

#Removing items if we don't know the index.
#As long as you know *what* it is, the .remove() method works

not_jedi = 'Han Solo'
characters.remove(not_jedi)
print(characters)
print(not_jedi)

#.remove() only takes the first instance that it finds:
characters.insert(1, not_jedi)
characters.insert(3, not_jedi)
print(characters)

characters.remove(not_jedi)
print(characters)

characters.remove(not_jedi)
print(characters)

characters[1] = "Chewie"
characters.append('Anakin')
characters.insert(2, 'Uncle Owen')
del characters[1]
removed_char = characters.pop()
removed_char2 = characters.pop(2)

removed_char3 = 'Yoda'
characters.remove(removed_char3)
print(characters)

#Monday - In-class assignment working with lists
#Wed-Friday - More lists (another assignment Friday)
#Approx 2 weeks - next test (lists and for loops)