Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(1,11,2):
	print(i)

	
1
3
5
7
9
>>> for i in range(1,11,-1):
	print(i)

	
>>> for i in range(11,1,-1):
	print(i)

	
11
10
9
8
7
6
5
4
3
2
>>> for i in range(1,11,2):
	print(11-i)

	
10
8
6
4
2
>>> for i in reversed(range(1,11,2)):
	print(i)

	
9
7
5
3
1
>>> for i in reversed(range(11,1)):
	print(i)

	
>>> for i in range(10):
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> for i in range(10):
	print (i)

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(1,11):
	print (i)

	
1
2
3
4
5
6
7
8
9
10
>>> for i in range(1,11,2):
	print (i)

	
1
3
5
7
9
>>> for i in range(1,11,-1):
	print (i)

	
>>> for i in range(11,1,-1):
	print (i)

	
11
10
9
8
7
6
5
4
3
2
>>> for i in reversed(range(1,11)):
	print(i)

	
10
9
8
7
6
5
4
3
2
1
>>> for i in reversed(range(1,11)):
	print(i, end='')

	
10987654321
>>> print('Hello','Python',sep='---')
Hello---Python
>>> for i in reversed(range(1,11)):
	print(i, end='  ')

	
10  9  8  7  6  5  4  3  2  1  
>>> for i in reversed(range(1,11)):
	print(i, end=' | ')

	
10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 
>>> list_1 = [1,2,3,4,5]
>>> list_2 = ['Ram', 'Shyam', 'Mohan']
>>> for i in list_2:
	print(i)

	
Ram
Shyam
Mohan
>>> for i in len(list_2):
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    for i in len(list_2):
TypeError: 'int' object is not iterable
>>> for i in range(len(list_2)):
	print(i)

	
0
1
2
>>> for i in range(len(list_2)):
	print(list_2[i])

	
Ram
Shyam
Mohan
>>> list_1.append(list_2)
>>> list_1
[1, 2, 3, 4, 5, ['Ram', 'Shyam', 'Mohan']]
>>> for i in list_1:
	print(i)

	
1
2
3
4
5
['Ram', 'Shyam', 'Mohan']
>>> newList = [[1,2,3],['Ram','Mohan','Shyam']]
>>> for i in newList:
	print(i)

	
[1, 2, 3]
['Ram', 'Mohan', 'Shyam']
>>> for i in newList:
	print(newList[0][i])

	
Traceback (most recent call last):
  File "<pyshell#55>", line 2, in <module>
    print(newList[0][i])
TypeError: list indices must be integers or slices, not list
>>> for i in newList:
	print(i)

	
[1, 2, 3]
['Ram', 'Mohan', 'Shyam']
>>> for lst in newList:
	print(lst)

	
[1, 2, 3]
['Ram', 'Mohan', 'Shyam']
>>> for lst in newList:
	print(lst[0], lst[1], lst[2])

	
1 2 3
Ram Mohan Shyam
>>> for lst in newList:
	for j in lst:
		print(j)

		
1
2
3
Ram
Mohan
Shyam
>>> newList
[[1, 2, 3], ['Ram', 'Mohan', 'Shyam']]
>>> len(newList)
2
>>> for i in [0,1]:
	print(i)

	
0
1
>>> for i in [0,1]:
	print(newList[i])

	
[1, 2, 3]
['Ram', 'Mohan', 'Shyam']
>>> for i in [0,1]:
	for j in [1,2,3,4,5]
	
SyntaxError: invalid syntax
>>> for i in [0,1]:
	for j in [1,2,3,4,5]:
		print(j)

		
1
2
3
4
5
1
2
3
4
5
>>> for i in [0,1]:
	for j in [1,2,3,4,5]:
		print(newList[i][j])

		
2
3
Traceback (most recent call last):
  File "<pyshell#78>", line 3, in <module>
    print(newList[i][j])
IndexError: list index out of range
>>> for i in range(len(newList)):
	for j in range(len(newList[i])):
		print(newList[i][j])

		
1
2
3
Ram
Mohan
Shyam
>>> newList.append([1,2,3,4,5,6,7,8])
>>> newList
[[1, 2, 3], ['Ram', 'Mohan', 'Shyam'], [1, 2, 3, 4, 5, 6, 7, 8]]
>>> for i in range(len(newList)):
	for j in range(len(newList[i])):
		print(newList[i][j])

		
1
2
3
Ram
Mohan
Shyam
1
2
3
4
5
6
7
8
>>> newList.append(1)
>>> newList
[[1, 2, 3], ['Ram', 'Mohan', 'Shyam'], [1, 2, 3, 4, 5, 6, 7, 8], 1]
>>> for i in range(len(newList)):
	for j in range(len(newList[i])):
		print(newList[i][j])

		
1
2
3
Ram
Mohan
Shyam
1
2
3
4
5
6
7
8
Traceback (most recent call last):
  File "<pyshell#88>", line 2, in <module>
    for j in range(len(newList[i])):
TypeError: object of type 'int' has no len()
>>> for i in range(len(newList)):
	if type(newList[i]) == int:
		print(newList[i])
	else:
		for j in range(len(newList[i])):
			print(newList[i][j])

			
1
2
3
Ram
Mohan
Shyam
1
2
3
4
5
6
7
8
1
>>> newList.append('hello')
>>> for i in range(len(newList)):
	if type(newList[i]) == int:
		print(newList[i])
	else:
		for j in range(len(newList[i])):
			print(newList[i][j])

			
1
2
3
Ram
Mohan
Shyam
1
2
3
4
5
6
7
8
1
h
e
l
l
o
>>> newList
[[1, 2, 3], ['Ram', 'Mohan', 'Shyam'], [1, 2, 3, 4, 5, 6, 7, 8], 1, 'hello']
>>> 
