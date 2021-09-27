#Making numerical lists:
for x in range(1,6):
    #Notation range(start, end+1)
    print(x)

#That's using it in a loop
#What if we want an actual list of numbers?
numbers = list(range(1,6))
print(numbers)

#What if I only want even numbers?
evens = list(range(2,10,2))
#               range(start, stop+1, increment)
print(evens)

squares = []
for number in range(1,11): #range(start, stop+1, increment)
    square = number**2
    squares.append(square)

print(squares)


#Simple stats:
digits = list(range(1,11))
print(min(digits)) #should be 1 - the least
print(max(digits)) #should be 10 - the max
print(sum(digits)) #shoudl be 55 - the sum of 1 through 10

#List Comprehension
squares = []
for number in range(1,11): #range(start, stop+1, increment)
    square = number**2
    squares.append(square)

print(squares)

squares_2 = [number**2 for number in range(1,11)]
#            start with an expression for the values we want in the list
#            next write the 'for' statement of a for loop
#                      which generates the numbers to use in the expression
print(squares_2)

plus_two = [value+2 for value in range(1,16)]
print(plus_two)

even_cubes = [value**3 for value in range(2,21,2)]
print(even_cubes)
