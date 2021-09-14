import turtle

def turn_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def turn_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def turn_up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()


def turn_down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle') 
turtle.onkey(turn_right,'d')
turtle.onkey(turn_left,'a')
turtle.onkey(turn_down,'s')
turtle.onkey(turn_up,'w')
turtle.onkey(restart,'Escape')
turtle.listen()
