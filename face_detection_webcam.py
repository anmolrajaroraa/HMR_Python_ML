import cv2
capture = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    ret, image = capture.read()
    if ret:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray)
        for x,y,w,h in faces:
            cv2.rectangle(gray, (x,y),
                          (x+w,y+h), (255,0,0), 5)
        cv2.imshow('image.jpg',gray)
        if cv2.waitKey(1) & 0xff == 27:
            break
capture.release()
cv2.destroyAllWindows()
        
    
