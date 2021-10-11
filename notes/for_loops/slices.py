#Today: Slices of Lists
#Tomorrow: No Class :(
#Wednesday: In-Class assignment on Slices
#Thursday: Review for Test
#Friday: Test2

#Slices:
#A Slice is part of a list
students = ['collin', 'ramsey', 'doug', 'makenna', 'logan', 'noah']
#print only the first three:
print(students[0:3]) #this will print students[0], students[1], and students[2]
#really I wanted to print doug makenna and logan:
print(students[2:5]) #this will print students [2], [3], and [4]

#Back to students[0:3]
#If we want a slice that starts at the beginning, we don't have to use the 
#0 index:
print(students[:3]) #Special notation telling python to start at zero.

#There is a similar notation for slices that include the end index
print(students[4:]) #This tells python we want to go to the end of the list. 

#Suppose we want to print from makenna to the end of the list
print(students[3:])
#Suppose we want to print the last three:
print(students[3:])

students.append('ryder')
students.append('noah j')
students.append('ty')

print(students[3:]) #will this still give the last three?
#No. It gives the last six.

#If we want the last three entries in a list that can change:
print(students[-3:]) #This tells python to start three entries from the end
#                       and print to the end.


#Loop through slices:
print('Here are the students in the middle row:')
for student in students[:3]: #Uses the slice of students with the first three
    print(student)

#In a game, we can store scores in a list, then sort the list
#and print the slice of the last three to get the top three scores.

#Using data analysis: we can process data in chunks

#Copying Lists
#Two ways: 
#1. Create an entirely new list with a new variable. 
foods = ['mac n cheese', 'apple', 'sushi']
other_foods = foods[:] #This creates an entirely new list with the 
#                       variable name other_foods

print('Our class food is: \n', foods)
print('Some other foods are: \n', other_foods) #the lists are the same right now

other_foods.append('oranges')
other_foods[1] = 'pizza'

print('Our class food is: \n', foods)
print('Some other foods are: \n', other_foods) #Now they are different. 

places = ['beach', 'pool', 'disney world']
other_places = places #This time we leave off the [:]

print('Some places are: \n', places)
print('Some other places are: \n', other_places) #They are the same

#Make changes in 'other_places':
other_places.append('movies')
other_places[1] = 'disney land'

print('Some places are: \n', places)
print('Some other places are: \n', other_places) #BOTH LISTS CHANGED!

#Here's what happens when you copy a list without [:]
#Python sees this
#       places --> data/list <-- other_places
# When we change the data through one name, it changes the data for both

#When you copy a list with [:] python sees this
#       places --> data
#       other_places --> copy_of_data
#We can change the second data without affecting the first.

#Key takeaway: If you want to copy a list into an idependent copy, use [:]!!!!