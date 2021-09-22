#List of car makes
cars = ['ford', 'tesla', 'vw', 'cooper', 'fiat']
cars.sort()
print(cars)
#sort() permanently changes the order of the list
#sort() will also order in reverse
cars.sort(reverse=True)
#           'reverse' is an argument for the sort() method.
print(cars)

#What if we don't want permanently change the list order?
cars = ['ford', 'tesla', 'vw', 'cooper', 'fiat'] #Redefine unsorted list
#To keep the original order, but still print a sorted list, use the
#   sorted function.

print('Original List: ', cars)

print('\nSorted List: ', sorted(cars))

print('\nOriginal List (again): ', cars)

#Don't want to alphabetize the list in reverse (.sort(reverse=True)), but just
#want to have the list in reverse original order.

#Use the .reverse() method.
cars.reverse() #permanent reversal (until redefinition)
print(cars) #called for cars. It was already reversed
cars.reverse() #reverse the reversed list -> back to original order
print(cars)

#.sort() --> permanent change alphabetical or numerical least to greatest
#.sort(reverse=True) --> permanent change to reverse alphabetical or
#                           reverse numerical order (great to least)
#sorted() --> non-permanent change to alphabetical order 
#.reverse() --> permanent reversal of list order (not necessarily alphabetical)

#How long is a list
print(len(cars))
