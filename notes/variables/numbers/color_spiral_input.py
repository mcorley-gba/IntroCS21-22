import turtle
t = turtle.Pen()
t.speed(8)

turtle.Screen().bgcolor("black")

colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]

sides = int(turtle.Screen().numinput("Number of Sides", \
                                    "How many sides do you want (1-8)?", \
                                        4, 1, 8))
                                        #Default = 4
                                        #Min Value = 1
                                        #Max Value = 8
for x in range(360):
    t.pencolor(colors[x%sides]) #Will only use as many colors as sides
    t.forward(x*3/sides + x)
    t.left(360/sides + 1) #Making the "sides"-sided figure
    t.width(x*sides/200) #Width will get bigger (200 is just scaling)

turtle.done()