Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #why function?
>>> #reusable code
>>> #block of code that can be called anytime from anywhere
>>> #DRY - Don't Repeat Yourself
>>> #SRP - Single Responsibility Principle
>>> 
>>> 
>>> def first():
	print('Function one..')

	
>>> def fn_name(params):
	'''
	A new function
	'''
	abc
	return

>>> first()
Function one..
>>> first
<function first at 0x102fffc80>
>>> def second():
	print('Function second')
	first()

	
>>> second()
Function second
Function one..
>>> x = 10
>>> y = 20
>>> print('Result is ' , x + y)
Result is  30
>>> def add():
	print('Result is ' , x + y)

	
>>> add()
Result is  30
>>> def add(x,y):
	print('Result is ' , x + y)

	
>>> add(12,24)
Result is  36
>>> add(12)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    add(12)
TypeError: add() missing 1 required positional argument: 'y'
>>> def add(x=0,y=0):
	print('Result is ' , x + y)

	
>>> add()
Result is  0
>>> add(1)
Result is  1
>>> add(1,1)
Result is  2
>>> a = 10
>>> b = 20
>>> add(a,b)
Result is  30
>>> add(a)
Result is  10
>>> add(x=10)
Result is  10
>>> add(y=10)
Result is  10
>>> def add(x=10,y=20):
	print('Result is ' , x + y)

	
>>> add(x=10)
Result is  30
>>> add(y)
Result is  40
>>> add(y=10)
Result is  20
>>> z = 30
>>> add(z)
Result is  50
>>> add(z=30)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    add(z=30)
TypeError: add() got an unexpected keyword argument 'z'
>>> def student(name='', college='', age=0):
	print(f'Name = {name}, college = {college}, age = {age}')

	
>>> student()
Name = , college = , age = 0
>>> student('Ram
	
SyntaxError: EOL while scanning string literal
>>> student('Ram')
Name = Ram, college = , age = 0
>>> student('hmr')
Name = hmr, college = , age = 0
>>> student(college='hmr')
Name = , college = hmr, age = 0
>>> student(college='hmr',age=20, name="ram")
Name = ram, college = hmr, age = 20
>>> def calc(x,y):
	return x+y

>>> calc(10,20)
30
>>> def calc(x,y):
	return x+y,x-y

>>> calc(10,20)
(30, -10)
>>> #tuple - (), list - []
>>> a = 10
>>> a
10
>>> a =10,20
>>> a
(10, 20)
>>> def calc(x,y):
	result = [x+y, x-y]
	return result

>>> calc(10,20)
[30, -10]
>>> def calc(x,y):
	return x+y,x-y

>>> a = calc(10,20)
>>> a
(30, -10)
>>> *a
SyntaxError: can't use starred expression here
>>> a*
SyntaxError: invalid syntax
>>> *a = calc(10,20)
SyntaxError: starred assignment target must be in a list or tuple
>>> a* = calc(10,20)
SyntaxError: invalid syntax
>>> def calc(x,y):
	return x+y,x-y

>>> *a, = calc(10,20)
>>> a
[30, -10]
>>> def calc(x,y):
	return x+y,x-y,x*y,x/y

>>> a,*b = calc(10,20)
>>> a
30
>>> b
[-10, 200, 0.5]
>>> a,b,*c = calc(10,20)
>>> a,b,c
(30, -10, [200, 0.5])
>>> a,*b,c = calc(10,20)
>>> a
30
>>> b
[-10, 200]
>>> c
0.5
>>> a,b,c,d = calc(x,y)
>>> 
>>> a
30
>>> b
-10
>>> c
200
>>> d
0.5
>>> a,b,c = calc(x,y)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    a,b,c = calc(x,y)
ValueError: too many values to unpack (expected 3)
>>> a,b,c,d,e = calc(x,y)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    a,b,c,d,e = calc(x,y)
ValueError: not enough values to unpack (expected 5, got 4)
>>> a,b,*c = calc(x,y)
>>> a
30
>>> b
-10
>>> c
[200, 0.5]
>>> 
