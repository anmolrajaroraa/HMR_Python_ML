import cv2
image = cv2.imread('img_42.jpg')
#cv2.imshow('img',image)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = cascade.detectMultiScale(image,1.3)
#print(faces)
for x,y,w,h in faces:
    #print(x,y,w,h)
    cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 5)
cv2.imshow('result',image)
