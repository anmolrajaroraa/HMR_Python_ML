Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def student(name,age,college):
	print("In student function")

	
>>> student(a,b,c,d)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    student(a,b,c,d)
NameError: name 'a' is not defined
>>> def student(name,age,college,*otherDetails):
	print("In student function",name,age,college,otherDetails)

	
>>> student(a,b,c,d,e,f)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    student(a,b,c,d,e,f)
NameError: name 'a' is not defined
>>> student(a','b','c','d','e','f')
	
SyntaxError: invalid syntax
>>> 
>>> student('a','b','c','d','e','f')
In student function a b c ('d', 'e', 'f')
>>> def student(name,age,*otherDetails,college):
	print(f'name={name},age={age},college={college},otherdetails={otherDetails}')

	
>>> student('a','b','c','d','e','f')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    student('a','b','c','d','e','f')
TypeError: student() missing 1 required keyword-only argument: 'college'
>>> student(college='a','b','c','d','e','f')
SyntaxError: positional argument follows keyword argument
>>> student('a','b','c','d','e',college='f')
name=a,age=b,college=f,otherdetails=('c', 'd', 'e')
>>> student(name='a',age='b','c','d','e',college='f')
SyntaxError: positional argument follows keyword argument
>>> student('a','b','c',name='d',age='e',college='f')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    student('a','b','c',name='d',age='e',college='f')
TypeError: student() got multiple values for argument 'name'
>>> student('a','b','c','d','e',college='f')
name=a,age=b,college=f,otherdetails=('c', 'd', 'e')
>>> student(name='a','b','c','d','e',college='f')
SyntaxError: positional argument follows keyword argument
>>> 
