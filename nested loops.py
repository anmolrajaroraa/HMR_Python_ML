x = 1
while x < 10:
    print("X is ", x)
    for i in range(10):
        print("i is ", i)
        if i == 5:
            break
    if x == 5:
        break
    x+=1

print("Both loops terminated")
