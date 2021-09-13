Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle as t


>>> def turn_right():
	t.setheading(0)
	t.forward(50)

	
>>> def turn_up():
	t.setheading(90)
	t.forward(50)

	
>>> def turn_left():
	t.setheading(180)
	t.forward(50)

	
>>> def turn_down():
	t.setheading(270)
	t.forward(50)

	
>>> def blank():
	t.clear()

	
>>> t.shape("turtle")
>>> t.speed(0)
>>> t.onkeypress(turn_right,"d")
>>> t.onkeypress(turn_up,"w")
>>> t.onkeppress(turn_left,"a")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    t.onkeppress(turn_left,"a")
AttributeError: module 'turtle' has no attribute 'onkeppress'
>>> t.onkeypress(turn_left,"a")
>>> t.onkeypress(turn_down,"s")
>>> t.onkeypress(blank,"Escape")
>>> t.listen()
>>> 