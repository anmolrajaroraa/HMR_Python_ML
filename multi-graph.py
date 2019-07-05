import matplotlib.pyplot as plot
x = [8,9,8,9]
y = [2,3,2,3]
m = [4,3,5,6]
z = [1,2,3,4]
bottom = []
for i in range(len(x)):
    bottom.append(x[i]+y[i])


#plot.plot(x, label='x')
plot.bar(z, x, label='x', color='blue')
#plot.plot(y, label='y')
plot.bar(z, y, label='y', bottom=x, color='orange')
plot.bar(z, m, label='m', bottom=bottom, color='yellow')
plot.legend()
plot.show()
