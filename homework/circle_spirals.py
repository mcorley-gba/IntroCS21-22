#Modify the code below to make a python program that will draw circular spirals 
# with any number of sides between one and eight. 

import turtle
t = turtle.Pen()
turtle.Screen().bgcolor("black")
colors=["red", "yellow", "blue", "green"]
for x in range(100):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(91)