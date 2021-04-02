import turtle
wn = turtle.Screen()
wn.bgcolor("yellow")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("circle")

dist = 5
tess.up()                       # this is new
for _ in range(30):             # start with size = 5 and grow by 2
    if _ == 15:
        tess.down()
        tess.shape("square")
    elif _ < 15:
        tess.stamp()            # leave an impression on the canvas
        tess.forward(dist)      # move tess along
        tess.right(24)          # and turn
        dist = dist + 2
    elif _ < 20:
        tess.down()
        tess.forward(dist)      # move tess along
        tess.right(24)          # and turn
        dist = dist + 2
    else:
        tess.forward(dist)      # move tess along
        tess.stamp()            # leave an impression on the canvas
        tess.right(24)          # and turn
        dist = dist + 2
wn.exitonclick()
