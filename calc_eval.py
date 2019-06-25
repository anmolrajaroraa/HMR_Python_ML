def calc(x,y,op):
    print(eval(x+op+y))
#eval() accepts everything as string

print('''
    1. +
    2. -
''')

options = {
    "1":'+',
    "2":'-'
}
op = options['1']
calc('10','12',op)
