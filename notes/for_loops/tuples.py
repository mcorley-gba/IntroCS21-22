#Tuples - Like lists, but different
#Lists store data with entries that can be changed independently. 
#Tuples store data with entries that cannot be changed independently.
#       We must either leave the whole tuple alone, or change the whole thing.

#Example: A rectangle's dimensions. We want them fixed.
dimensions = (200,50) #This is a tuple with 2 entries. 
#we can access them like lists:
print(dimensions[1])
print(dimensions[0])

#dimensions[0] = 150 
#print(dimensions[0])
#Error: "tuple does not suppor ITEM assignment" - we can't change individual pieces.

dimensions = (150,50)
print(dimensions[0])

#The individual items in a tuple are 'immutable'. They cannot be changed 
#without changing the entire thing. 

#It is possible to have a tuple of 1 entry. This won't done much (if at all)
example_tuple = (44,) #<-- This is a tuple of 1. The key syntax is the ,. 

#We can loop through tuples the same as through lists. 
for dimension in dimensions:
    print(dimension) 