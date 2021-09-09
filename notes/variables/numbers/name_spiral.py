import turtle
t = turtle.Pen()

turtle.Screen().bgcolor("black")
colors = ["red", "blue", "yellow", "green"]

#Ask for the user's name using turtle graphics
your_name = turtle.Screen().textinput("Enter your name", "What is your name?")

#Draw a spiral of the user's name on the screen 100 times:
for x in range(100): #range(100) --> [0, 1, 2, ... , 99]
    t.pencolor(colors[x%4])
        # colors[1]? --> Get the element at position 1
                            #Python starts counting at 0
        # x%4? What is the '%' operator? --> takes the remainder of x/4
    t.penup() # telling the turtle to pick up his pen -- do not write
    t.forward(x*4)
    t.pendown()
    t.write(your_name, font = ("Ariel", 24, "bold"))
    t.left(91)

turtle.done()
