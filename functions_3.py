Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 10
>>> y = 20
>>> 
==== RESTART: /Users/anmolrajarora/Documents/hmr_python_ml/functions_2.py ====
11
>>> 
==== RESTART: /Users/anmolrajarora/Documents/hmr_python_ml/functions_2.py ====
11
40
>>> 
==== RESTART: /Users/anmolrajarora/Documents/hmr_python_ml/functions_2.py ====
11
40
>>> 
==== RESTART: /Users/anmolrajarora/Documents/hmr_python_ml/functions_2.py ====
11
31
>>> 
==== RESTART: /Users/anmolrajarora/Documents/hmr_python_ml/functions_2.py ====
40
21
>>> 
==== RESTART: /Users/anmolrajarora/Documents/hmr_python_ml/functions_2.py ====
Outer called
Traceback (most recent call last):
  File "/Users/anmolrajarora/Documents/hmr_python_ml/functions_2.py", line 20, in <module>
    inner()
NameError: name 'inner' is not defined
>>> 
==== RESTART: /Users/anmolrajarora/Documents/hmr_python_ml/functions_2.py ====
Outer called
Traceback (most recent call last):
  File "/Users/anmolrajarora/Documents/hmr_python_ml/functions_2.py", line 20, in <module>
    inner1()
NameError: name 'inner1' is not defined
>>> 
==== RESTART: /Users/anmolrajarora/Documents/hmr_python_ml/functions_2.py ====
Outer called
>>> 
==== RESTART: /Users/anmolrajarora/Documents/hmr_python_ml/functions_2.py ====
Outer called
Inner1 called
Inner2 called
>>> 
==== RESTART: /Users/anmolrajarora/Documents/hmr_python_ml/functions_2.py ====
Outer called
Inner1 called
Result is  None
>>> 
==== RESTART: /Users/anmolrajarora/Documents/hmr_python_ml/functions_2.py ====
Outer called
Result is  (<function outer.<locals>.inner1 at 0x1102b8e18>, <function outer.<locals>.inner2 at 0x1102b8ea0>)
>>> result[0]()
Inner1 called
>>> outer()
Outer called
(<function outer.<locals>.inner1 at 0x1102b8f28>, <function outer.<locals>.inner2 at 0x1102c2048>)
>>> outer()[0]
Outer called
<function outer.<locals>.inner1 at 0x1102c20d0>
>>> outer()[0]()
Outer called
Inner1 called
>>> def main():
	return 1,2,3,4

>>> main()
(1, 2, 3, 4)
>>> *a, = main()
>>> 
>>> a
[1, 2, 3, 4]
>>> def main(*a):
	print(a)

	
>>> main(1,2,3,4)
(1, 2, 3, 4)
>>> def main(a,b,**c):
	print(a,b,c)

	
>>> main(a=1,b=2,c=3,d=4,e=5)
1 2 {'c': 3, 'd': 4, 'e': 5}
>>> def student(name,age,*otherDetails,college):
	print(name,age,otherDetails,college)

	
>>> student('Ram',20,'a','b','c')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    student('Ram',20,'a','b','c')
TypeError: student() missing 1 required keyword-only argument: 'college'
>>> student('Ram',20,'a','b',college='c')
Ram 20 ('a', 'b') c
>>> student('Ram',20,'a','b',college='c','course':'btech')
SyntaxError: invalid syntax
>>> student('Ram',20,'a','b',college='c','course'='btech')
SyntaxError: keyword can't be an expression
>>> student('Ram',20,'a','b',college='c',course='btech')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    student('Ram',20,'a','b',college='c',course='btech')
TypeError: student() got an unexpected keyword argument 'course'
>>> def student(name,age,**otherDetails,college):
	print(name,age,otherDetails,college)
	
SyntaxError: invalid syntax
>>> def student(name,age,college,**otherDetails):
	print(name,age,otherDetails,college)

	
>>> student(name="Ram", age=20, college='abc', course='btech', batch='2016-2020')
Ram 20 {'course': 'btech', 'batch': '2016-2020'} abc
>>> 
