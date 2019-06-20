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

#Movie recommendation system
            Movies dataset
            Dictionary -> category
            user1 watched movies
            user2 watched movies
            Find similar movies of both users
            Find category of most watched movies by both users

movies = {
    'action':[],
    'thriller':[]
    }


common_movies = []
common_movies_categories = []
for movie in common_movies:
    for key in movies:
        if movie in movies[key]:
            common_movies_categories.append(key)

count = []
categories = list(movies.keys())

for key in movies:
    count.append(common_movies_categories.count(key))

indexOfMostWatchedCategory = count.index(max(count))
print("Most watched category is", categories[indexOfMostWatchedCategory])
