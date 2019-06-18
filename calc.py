import math
#Calculator

#print('1.Add\n2.Sub')
print('''
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
''')
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

result = num_1 + num_2 if num_1>=0 and num_2>=0 else print("Please enter positive integers")

'''if num_1 > num_2:
    result = num_1 - num_2
else:
    result = num_2 - num_1'''
#result = num_1 - num_2 if num_1>num_2 else num_2-num_1
print("Result is ", result)
#x>y ? num1-num2 : num2-num1
#math.log(10)
