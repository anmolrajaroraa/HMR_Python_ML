import cv2
capture = cv2.VideoCapture('video_1.mp4')
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_COMPLEX
while True:
    ret, image = capture.read()
    if ret:
        faces = cascade.detectMultiScale(image,1.3)
        for x,y,w,h in faces:
            cv2.rectangle(image, (x,y),
                          (x+w,y+h), (255,0,0), 5)
            #image   text   coordinates
            #fontFamily  fontScale color fontWeight
            cv2.putText(image, 'Person',
                        (x,y), font, 1, (0,255,0), 2)
        cv2.imshow('image.jpg',image)
        if cv2.waitKey(1) & 0xff == 27:
            break
capture.release()
cv2.destroyAllWindows()
        
    
