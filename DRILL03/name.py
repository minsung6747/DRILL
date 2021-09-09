Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.reset()
>>> turtle.forward(100)
>>> turtle.right(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.penup()
>>> turtle.forword(10)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    turtle.forword(10)
AttributeError: module 'turtle' has no attribute 'forword'
>>> turtle.goto(110,100)
>>> turtle.goto(110,-100)
>>> turtle.left(90)
>>> turtle.pendown()
>>> turtle.forward(100)
>>> turtle.penup()
>>> turtle.goto(50,-150)
>>> turtle.goto(70,-150)
>>> turtle.pendown()
>>> turtle.forward(20)
>>> turtle.back()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    turtle.back()
TypeError: back() missing 1 required positional argument: 'distance'
>>> title.undo()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    title.undo()
NameError: name 'title' is not defined
>>> turtle.undo()
>>> turtle.forward(30)
>>> turtle.left(90)
>>> turtle.undo()
>>> turtle.right(90)
>>> turtle.forward(30)
>>> turtle.right(90)
>>> turtle.forward(30)
>>> turtle.right(90)
>>> turtle.forward(30)
>>> turtle.goto(130,0)
>>> turtle.undo
<function undo at 0x000001EB8894F550>
>>> turtle.undo()
>>> turtle.penup()
>>> turtle.goto(130,0)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.undo()
t
>>> turtle.pendown()
>>> turtle.forward(100)
>>> tuetle.right(90)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
     tuetle.right(90) 
NameError: name 'tuetle' is not defined
>>> turtle.right(90)
>>> turtle.right(180)
>>> turtle.forward(100)
>>> turtle.right(180)
>>> turtle.right(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.penup()
>>> turtle.goto(250.0)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    turtle.goto(250.0)
  File "<string>", line 8, in goto
  File "C:\Python\lib\turtle.py", line 1775, in goto
    self._goto(Vec2D(*x))
TypeError: turtle.Vec2D() argument after * must be an iterable, not float
>>> turtle.goto(250,0)
>>> turtle.write('250,0')
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.undo()
>>> turtle.pendown()
>>> turtle.forward(100)
>>> turtle.penup()
>>> turtle.goto(190,-150)
>>> turtle.write('190,-150)
	     
SyntaxError: EOL while scanning string literal
>>> turtle.write('190,-150)
	     
SyntaxError: EOL while scanning string literal
>>> turtle.wirte('190,-150')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    turtle.wirte('190,-150')
AttributeError: module 'turtle' has no attribute 'wirte'
>>> turtle.write('190,-150')
>>> turtle.right(180)
>>> turtle.forward(30)
>>> turtle.undo()
>>> turtle.forward(30)
>>> turtle.right(90)
>>> turtle.right(90)
>>> turtle.pendown()
>>> turtle.forward(30)
>>> turtle.left(90)
>>> turtle.forward(30)
>>> turtle.penup()
>>> turtle.goto(300,0)
>>> turtle.goto(320,0)
>>> turtle.goto(330,0)
>>> turtle.pendown()
>>> turtle.right(120)
>>> turtle.forward(100
	       )
>>> turtle.penup()
>>> turtle.back(50)
>>> turtle.pendown()
>>> turtle.left(60)
>>> turtle.forward(50)
>>> turtle.penup()
>>> turtle.goto(350,0)
>>> tuetle.goto(360,0)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    tuetle.goto(360,0)
NameError: name 'tuetle' is not defined
>>> turtle.goto(360,0)
>>> turtle.right(30)
>>> turtle.pendown()
>>> tuetle.forward(100)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    tuetle.forward(100)
NameError: name 'tuetle' is not defined
>>> turtle.forward(100)
>>> turtle.penup()
>>> tuetle.bakc(50)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    tuetle.bakc(50)
NameError: name 'tuetle' is not defined
>>> turtle.back(50)
>>> turtle.right(90)
>>> turtle.pendown()
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    urtle.pendown()
NameError: name 'urtle' is not defined
>>> turtle.pendown()
>>> turtle.forward(30)
>>> turtle.penup()
>>> turtle.goto(330,-150)
>>> turtle.right(90)
>>> turtle.forward(20)
>>> turtle.pendown()
>>> turtle.circle()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    turtle.circle()
TypeError: circle() missing 1 required positional argument: 'radius'
>>> turtle.circle(20)
>>> turtle.undo
<function undo at 0x000001EB8894F550>
>>> turtle.undo()
>>> turtle.right(90
	     )
>>> turtle.penup()
>>> turtle.forward(20)
>>> turtle.pendown()
>>> turtle.circle(20)
>>> turtle.exitonclick()
                 
