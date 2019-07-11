import cv2
import numpy as np

capture = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_COMPLEX

name1 = np.load('name1.npy').reshape(100,50*50*3)
name2 = np.load('name2.npy').reshape(100,50*50*3)
users = {0:'name1', 1:'name2'}
labels = np.zeros((200,1))
labels[:100] = 0.0
labels[100:] = 1.0
data = np.concatenate([name1,name2])
#print(data.shape)

def distance(x1,x2):
    #print(np.sqrt(sum((x2-x1) ** 2)))
    return np.sqrt(sum((x2-x1) ** 2))

def knn(x,train,k=5):
    n = train.shape[0]
    #print(n)
    distances = []
    for i in range(n):
        #print(distances)
        #print(i)
        dist = distance(x,train[i])
        distances.append(dist)
    sortedIndex = np.argsort(distances)
    sortedIndex = sortedIndex[:k]
    nearestNeighbours = []
    for index in sortedIndex:
        nearestNeighbours.append(labels[index])
    count = np.unique(nearestNeighbours,
    return_counts=True)
    label = count[0][np.argmax(count[1])]
    #print(nearestNeighbours)
    return int(label)

while True:
    ret, image = capture.read()
    if ret:
        faces = cascade.detectMultiScale(image)
        for x,y,w,h in faces:
            cv2.rectangle(image, (x,y),
                          (x+w,y+h), (255,0,0), 5)
            myFace = image[y:y+h,x:x+w,:]
            myFace = cv2.resize(myFace,(50,50))
            label = knn(myFace.flatten(),data)
            userName = users[label]
            cv2.putText(image, userName,
                        (x,y), font, 1, (0,255,0), 2)
        cv2.imshow('image.jpg',image)
        if cv2.waitKey(1) & 0xff == 27:
            break
capture.release()
cv2.destroyAllWindows()
