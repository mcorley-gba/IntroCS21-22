#Monday - Quiz over conditionals
#Next topic - Dictionaries, another way to organize data
#While Loops - Loops that no definite ending. 

#Functions
#Classes *Vital for bigger, more involved games*


#Dictionaries allow programmers to link together related pieces of data. 
#So, we can model real-world situation with more accuracy and detail.


alien_0 = {'color': 'green', 'points': 5}
#A dictionary -- a collection of key-value pairs
#The 'keys' are the entries before the colons (ex: 'color', 'points')
#We use the keys to access the values
#Key-value pairs are sets of values associated with each other.

#Access the values:
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 0
print(alien_0)

print("\n\n\n\n")

alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10

print(f"You just earned {alien_1['color'].upper()} points!")
alien_1['points'] = 50
print(alien_1)


print("\n\n\n\n\n\n")
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_0['x_position']}.")

#Move to the right
#Determine how far to move in one move based on current speed
if alien_0['speed'] == 'slow':
    x_increment = 1 #How far it will move
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#Update position to show movement:
#alien_0['x_position'] = alien_['x_position'] + x_increment
alien_0['x_position'] += x_increment

print(f"New position: {alien_0['x_position']}")