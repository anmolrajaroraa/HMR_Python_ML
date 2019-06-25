'''x = 10
y = 20
def fn():
    global x
    x = 20
    print(x+y)

fn()
x+=1
print(x)'''

def outer():
    print("Outer called")
    def inner1():
        print("Inner1 called")
    def inner2():
        print("Inner2 called")
    #inner1()
    #inner2()
    return inner1, inner2

result = outer()[0]()
print("Result is ", result)
#inner1()

