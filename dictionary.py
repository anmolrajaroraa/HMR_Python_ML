students = {
	'names':['Ram', 'Shyam', 'Sohan', 'Sahil', 'Mohan'],
	'marks':[
            {
                'subject1':50,
                'subject2':60,
                'subject3':70,
                'subject4':80,
                'subject5':90
                },
            {
                'subject1':50,
                'subject2':60,
                'subject3':70,
                'subject4':80,
                'subject5':90
                },
            {
                'subject1':50,
                'subject2':60,
                'subject3':70,
                'subject4':80,
                'subject5':90
                },
            {
                'subject1':50,
                'subject2':60,
                'subject3':70,
                'subject4':80,
                'subject5':90
                },
            {
                'subject1':20,
                'subject2':20,
                'subject3':20,
                'subject4':20,
                'subject5':20
                }
            ],
        'college':['abc','abc','def','xyz','xyz'],
        'pass':[True, True, True, True]
        }

'''for key in students.keys():
    print(key)

for value in students.values():
    print(value)'''

'''for key in students.keys():
    print("Key is -> ", key)
    for value in students[key]:
        print(value)'''

print('----------------------')

for index in range(len(students['names'])):
    for key in students:
        if index<len(students[key]):
            print(students[key][index])
