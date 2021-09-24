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
for number in range(1,11):
    square = number**2
    squares.append(square)

print(squares)