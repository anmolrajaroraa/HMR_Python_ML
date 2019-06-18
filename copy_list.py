Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======= RESTART: /Users/anmolrajarora/Documents/hmr_python_ml/calc.py =======

    1. Add
    2. Subtract
    3. Multiply
    4. Divide

Enter first number: 1
Enter second number: 1
Result is  2
>>> list_1 = [1,2,3,4,5]
>>> list_1.remove(3)
>>> list_1
[1, 2, 4, 5]
>>> list_2 = list_1
>>> list_1 is list_2
True
>>> import copy
>>> list_3 = copy.deepcopy(list_1)
>>> list_3 is list_1
False
>>> list_1
[1, 2, 4, 5]
>>> list_3
[1, 2, 4, 5]
>>> list_1.pop()
5
>>> list_1
[1, 2, 4]
>>> list_2
[1, 2, 4]
>>> list_3
[1, 2, 4, 5]
>>> import random
>>> choices = ['stone', 'paper', 'scissors']
>>> random.choice(choices)
'stone'
>>> random.choice(choices)
'stone'
>>> random.choice(choices)
'paper'
>>> random.choice(choices)
'paper'
>>> random.choice(choices)
'stone'
>>> random.choice(choices)
'stone'
>>> random.choice(choices)
'scissors'
>>> random.choices(choices)
['stone']
>>> random.choices(choices)
['scissors']
>>> random.choices(choices)
['paper']
>>> random.choices(choices)
['paper']
>>> 
