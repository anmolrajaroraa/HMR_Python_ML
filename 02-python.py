Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b = 20
>>> a,b = b,a
>>> a
20
>>> b
10
>>> a,b = 10,20
>>> a = 10,20
>>> a
(10, 20)
>>> 10 ** 2
100
>>> 10 ** 3
1000
>>> 2**10
1024
>>> a = a + b
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a = a + b
TypeError: can only concatenate tuple (not "int") to tuple
>>> a = 10
>>> b = 20
>>> a = a+b
>>> a += b
>>> a = a+ b
>>> a++
SyntaxError: invalid syntax
>>> a+=1
>>> a//=b
>>> a
3
>>> a = 10
>>> b = 20
>>> a**=4
>>> a
10000
>>> a**4
10000000000000000
>>> a
10000
>>> a = [4,5,6]
>>> b = [4,5,6]
>>> a is b
False
>>> x = 10
>>> y = 10
>>> a = a ** 4
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a = a ** 4
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
>>> x is y
True
>>> str1 = 'python'
>>> str2 = 'python
SyntaxError: EOL while scanning string literal
>>> str2 = 'python'
>>> str1 is str2
True
>>> str2 = 'r programming'
>>> str1 is str2
False
>>> str1 is not str2
True
>>> a = 10
>>> b = 10
>>> a == b
True
>>> True == True
True
>>> x = True
>>> y = True
>>> x == y
True
>>> x != y
False
>>> a > b
False
>>> a >= b
True
>>> string = 'hello python
SyntaxError: EOL while scanning string literal
>>> 
>>> string = 'hello python'
>>> 'a'.in(string)
SyntaxError: invalid syntax
>>> 'a' in string
False
>>> 'a' not in string
True
>>> if True:
	print('hello')

	
hello
>>> if False:
	print('hello')

	
>>> if False:
	print('hello')

	
>>> if False:
	print('hello')
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> 
============== RESTART: /Users/anmolrajarora/Documents/demo.py ==============
true
>>> 
============== RESTART: /Users/anmolrajarora/Documents/demo.py ==============
not greater
>>> 
============== RESTART: /Users/anmolrajarora/Documents/demo.py ==============
equal
>>> 
