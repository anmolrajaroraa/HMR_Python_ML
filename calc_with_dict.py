def add(x,y):
    print("add called")
    return x+y
def subtract(x,y):
    print("subtract called")
    return x-y
'''def multiply(x,y):
    print("x*y = ",x*y)
def divide(x,y):
    print("x/y = ",x/y)'''
def errorHandler(*args):
    return "Wrong choice.."

print('''
1. Add
2. Subtract
3. Multiply
4. Divide
''')
choice  = input("Enter your choice : ")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
options = {
    "1" : add,
    "2" : subtract
    #"3" : multiply(num1,num2),
    #"4" : divide(num1,num2)
}
result = options.get(choice,errorHandler)(num1,num2)
print(result)
