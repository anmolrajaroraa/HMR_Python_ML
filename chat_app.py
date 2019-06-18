print("Welcome".center(100))
#flag = True
'''
This is a multi-line comment
'''

hello_intent = ['hi', 'hello', 'hi there', 'hola']

while True:
    userMessage = input("Enter your message : ")
    userMessage = userMessage.lower()
    #if userMessage == "hello" or userMessage == "hi" or userMessage == "hola" or userMessage == "hi there":
    if userMessage in hello_intent:
        print("Hi")
    elif userMessage == "bye":
        print("See you later")
        #flag = False
        break
        #exit(0)
        #quit()
    else:
        print("I don't understand")
print('Program terminated')
