Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> fred = turtle.Pen()
>>> for i in range(20):
	fred.forward(10)
	fred.left(45)

	
>>> 
>>> for i in range(20):
	fred.forward(25)
	fred.left(45)

	
>>> for i in range(20):
	fred.forward(5 * i)
	fred.left(45)

	
>>> for i in range(20):
	fred.forward(3 * i)
	fred.left(45)

	
>>> fred.reset()
>>> fred.shape('turtle')
>>> for i in range(20):
	fred.circle(3 * i)
	fred.left(45)

	
>>> fred.reset()
>>> for i in range(20):
	fred.circle(3 * i)
	fred.left(45)

	
>>> t.position
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    t.position
NameError: name 't' is not defined
>>> fred.position
<bound method TNavigator.pos of <turtle.Turtle object at 0x109f1a588>>
>>> fred.position()
(0.00,0.00)
>>> fred.down()
>>> fred.down(100)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    fred.down(100)
TypeError: pendown() takes 1 positional argument but 2 were given
>>> fred.reset()
>>> for i in range(20):
	fred.circle(3 * i)
	fred.left(45)

	
>>> colors = ['red', 'yellow', 'green', 'blue', 'red', 'yellow', 'green', 'blue', 'red', 'yellow', 'green', 'blue', 'red', 'yellow', 'green', 'blue', 'red', 'yellow', 'green', 'blue']
>>> for i in range(20):
	fred.setposition(400,400)
	fred.color(colors[i]
	fred.circle(3 * i)
	fred.left(45)
		   
SyntaxError: invalid syntax
>>> 
>>> for i in range(20):
	fred.setposition(400,400)
	fred.color(colors[i])
	fred.circle(3 * i)
	fred.left(45)

	
>>> for i in range(20):
	fred.setpos(400,400)
	fred.color(colors[i])
	fred.circle(3 * i)
	fred.left(45)

	
>>> fred.reset()
>>> colors = ['red', 'yellow', 'green', 'blue', 'red', 'yellow', 'green', 'blue', 'red', 'yellow']
>>> for i in range(20):
	fred.setpos(400,400)
	fred.color(colors[i])
	fred.circle(6 * i)
	fred.left(45)

	
Traceback (most recent call last):
  File "<pyshell#38>", line 3, in <module>
    fred.color(colors[i])
IndexError: list index out of range
>>> fred.reset()
>>> for i in range(10):
	fred.color(colors[i])
	fred.circle(6 * i)
	fred.left(45)

	
>>> 
