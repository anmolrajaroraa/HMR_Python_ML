Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> a
10
>>> type(a)
<class 'int'>
>>> a = 12.0
>>> type(a)
<class 'float'>
>>> a = True
>>> type(a)
<class 'bool'>
>>> a = 10
>>> b = 5
>>> a + b
15
>>> a - b
5
>>> a / b
2.0
>>> a = 12
>>> b = 5
>>> a / b
2.4
>>> a.floor(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.floor(a)
AttributeError: 'int' object has no attribute 'floor'
>>> a // b
2
>>> a % b
2
>>> input("Enter your name")
Enter your nameram
'ram'
>>> name = input("Enter your name: ")
Enter your name: Ram
>>> name
'Ram'
>>> type(name)
<class 'str'>
>>> a = 10
>>> True = 10
SyntaxError: can't assign to keyword
>>> print(name)
Ram
>>> print('hello','world')
hello world
>>> print('hello','world', sep='---')
hello---world
>>> a = 'hello'
>>> a = 'hi'
>>> a
'hi'
>>> list1 = [1,2,3]
>>> list1[0] = 4
>>> list1
[4, 2, 3]
>>> list1 = [4,5,6]
>>> list2 = [4,5,6]
>>> list1 is list2
False
>>> str1 = 'hello'
>>> str1[0]
'h'
>>> str1[0] = 'a
SyntaxError: EOL while scanning string literal
>>> str1[0] = 'a'
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    str1[0] = 'a'
TypeError: 'str' object does not support item assignment
>>> str1 = 'this is python programming'
>>> str1[0]
't'
>>> str1[:]
'this is python programming'
>>> str1[:5]
'this '
>>> str1[:10]
'this is py'
>>> str1[2:10]
'is is py'
>>> str1[2:]
'is is python programming'
>>> str1[2::2]
'i spto rgamn'
>>> str1[2::3]
'iiph oai'
>>> str1[::3]
'tssyopgmn'
>>> str1 = str1[2:10]
>>> str1
'is is py'
>>> len(str1)
8
>>> str1[8:1:-1]
'yp si '
>>> str1[8:0:-1]
'yp si s'
>>> str1[8:0]
''
>>> str1[8:-1:-1]
''
>>> str1[-1]
'y'
>>> str[-1:]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    str[-1:]
TypeError: 'type' object is not subscriptable
>>> str1[-1:]
'y'
>>> str1[-1:0:-1]
'yp si s'
>>> str1[-1::-1]
'yp si si'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> str1.__doc__
"str(object='') -> str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'."
>>> str1.count('p')
1
>>> str1
'is is py'
>>> str1.count('i')
2
>>> str1.count('is')
2
>>> str1.capitalize()
'Is is py'
>>> str1.upper()
'IS IS PY'
>>> a = 'hello'
>>> a = "hello"
>>> a = "i don't understand python"
>>> a = 'i don\'t understand python.\nthis is python'
>>> a
"i don't understand python.\nthis is python"
>>> print(a)
i don't understand python.
this is python
>>> str1.__doc
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    str1.__doc
AttributeError: 'str' object has no attribute '__doc'
>>> str1.__doc__
"str(object='') -> str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'."
>>> print(str1.__doc__)
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
>>> str1.lower()
'is is py'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> str1.swapcase()
'IS IS PY'
>>> str1
'is is py'
>>> str1 = "Hello python"
>>> str1.swapcase()
'hELLO PYTHON'
>>> str1.find('o')
4
>>> str1.count('o')
2
>>> str1.rfind('o')
10
>>> str1.find('a')
-1
>>> str1 = 'hello python hello"
SyntaxError: EOL while scanning string literal
>>> str1 = 'hello python hello'
>>> str1.find('o')
4
>>> str1.rfind('o')
17
>>> str2 = str1[6:]
>>> str2
'python hello'
>>> str1[6:].find('o')
4
>>> str2.find('o')
4
>>> str1.find('o', 5)
10
>>> '''
lnlskvsvlksklvm
sbbbebdbdbd
'''
'\nlnlskvsvlksklvm\nsbbbebdbdbd\n'
>>> #comment
>>> a = 10
>>> b = 20
>>> c = 30
>>> print('a = ',a)
a =  10
>>> c = a + b
>>> c
30
>>> print('Sum of ', a, ' and ', b, ' is ', c)
Sum of  10  and  20  is  30
>>> print('a = %d'%a)
a = 10
>>> print('a = %d'a)
SyntaxError: invalid syntax
>>> print('Sum of %d and %d is %d'%(c))
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    print('Sum of %d and %d is %d'%(c))
TypeError: not enough arguments for format string
>>> print('Sum of %d and %d is %d'%(a,b,c))
Sum of 10 and 20 is 30
>>> print('Sum of {} and {} is {}'.format(a,b,c))
Sum of 10 and 20 is 30
>>> print('Sum of {a} and {b} is {c}')
Sum of {a} and {b} is {c}
>>> print(f'Sum of {a} and {b} is {c}')
Sum of 10 and 20 is 30
>>> import turtle
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    import turtle
  File "/Users/anmolrajarora/Documents/turtle.py", line 2, in <module>
    t = turtle.Pen()
AttributeError: module 'turtle' has no attribute 'Pen'
>>> import turtle
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    import turtle
  File "/Users/anmolrajarora/Documents/turtle.py", line 2, in <module>
    t = turtle.Pen()
AttributeError: module 'turtle' has no attribute 'Pen'
>>> 
