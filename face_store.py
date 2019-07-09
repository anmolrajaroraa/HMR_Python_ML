import cv2
import numpy as np
capture = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
data = []
while True:
    ret, image = capture.read()
    if ret:
        faces = cascade.detectMultiScale(image,1.5)
        for x,y,w,h in faces:
            cv2.rectangle(image, (x,y),
                          (x+w,y+h), (255,0,0), 5)
            myFace = image[y:y+h,x:x+w,:]
            myFace = cv2.resize(myFace,(50,50))
            if len(data) < 100:
                print(len(data))
                data.append(myFace)
        cv2.imshow('image.jpg',image)
        if cv2.waitKey(1) & 0xff == 27 or len(data) >= 100:
            break
arr = np.array(data)
np.save('name2.npy',arr)
capture.release()
cv2.destroyAllWindows()
        
    
