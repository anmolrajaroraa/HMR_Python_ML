Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list_1 = [1,2,3,4,5]
>>> tuple_1 = (1,2,3,4,5)
>>> set_1 = {1,2,3,4,5,5}
>>> set_1
{1, 2, 3, 4, 5}
>>> set_2 = {2,4,6,7,8}
>>> set_1 - set_2
{1, 3, 5}
>>> set_1.union(set_2)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> set_1.intersection(set_2)
{2, 4}
>>> list_1[1] = 1
>>> tuple_1[1] = 1
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    tuple_1[1] = 1
TypeError: 'tuple' object does not support item assignment
>>> del tuple_1[1]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    del tuple_1[1]
TypeError: 'tuple' object doesn't support item deletion
>>> tuple_1[1]
2
>>> set_1
{1, 2, 3, 4, 5}
>>> set_1
{1, 2, 3, 4, 5}
>>> set_1
{1, 2, 3, 4, 5}
>>> set_1
{1, 2, 3, 4, 5}
>>> set_1.add(6)
>>> set_1
{1, 2, 3, 4, 5, 6}
>>> set_2
{2, 4, 6, 7, 8}
>>> set_2
{2, 4, 6, 7, 8}
>>> set_3 = {}
>>> set_3.add(1)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    set_3.add(1)
AttributeError: 'dict' object has no attribute 'add'
>>> set_1
{1, 2, 3, 4, 5, 6}
>>> set_1.add(1)
>>> set_1
{1, 2, 3, 4, 5, 6}
>>> set_1[1]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    set_1[1]
TypeError: 'set' object is not subscriptable
>>> set_1.remove(5)
>>> set_1
{1, 2, 3, 4, 6}
>>> type(set_1)
<class 'set'>
>>> set_1 = set([1,2,3,4,5])
>>> set_1
{1, 2, 3, 4, 5}
>>> set_1
{1, 2, 3, 4, 5}
>>> set_1
{1, 2, 3, 4, 5}
>>> set_1 = {'a', 'hello', None, True, 100, 200}
>>> set_2 = {}
>>> type(set_2)
<class 'dict'>
>>> set_2 = set()
>>> set_1
{True, 100, 'hello', None, 200, 'a'}
>>> set_!
SyntaxError: invalid syntax
>>> set_1
{True, 100, 'hello', None, 200, 'a'}
>>> set_1
{True, 100, 'hello', None, 200, 'a'}
>>> set_1
{True, 100, 'hello', None, 200, 'a'}
>>> set_1
{True, 100, 'hello', None, 200, 'a'}
>>> set_1
{True, 100, 'hello', None, 200, 'a'}
>>> set_1 = {'a', 'hello', None, True, 100, 200}
>>> set_1
{True, 100, 'hello', None, 200, 'a'}
>>> set_1.add(False)
>>> set_1
{False, True, 100, 'hello', None, 200, 'a'}
>>> 
