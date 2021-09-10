#Add and/or delete lines from the program below
#so that the turtle will draw circular spirals with any number of sides between
#1 and 8. When you have finished, save your code as 
#[yourname]_circle_spiral_input.py and upload to Google Classroom.

import turtle
t = turtle.Pen()
turtle.Screen().bgcolor("black")
colors = ["red", "yellow", "blue", "green","orange","purple","white","gray"]
sides = int(turtle.Screen().numinput("Number of sides", "How many sides do you want (1-8)?", 4,1,8))

for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)

turtle.done()