Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.reset()
>>> count=6
>>> while(count>0):
	turtle.forward(500)
	turtle.penup()
	turtle.back(500)
	turtle.left(90)
	turtle.forward(100)
	turtle.pendown()
	turtle.right(90)
	count=count-1

	
>>> turtle.goto(0,0)
>>> count
01
>>> turtle.undo()
>>> turtle.penup()
>>> turtle.goto(0,0)
>>> turtle.left(90)
>>> cnt=6
>>> while(cnt>0):
	turtle.forward(500)
	turtle.penup()
	turtle.back(500)
	turtle.right(90)
	turtle.pendown()
	turtle.forward(100)
	turtle.left(90)
	cnt=cnt-1

	
>>> turtle.undo()
>>> turtle.undo()
>>> turtle.goto(0,0)
>>> turtle.left(90)
]
>>> turtle.forward(500)
>>> turtle.exitonclick()
