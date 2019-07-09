import cv2
image = cv2.imread('img_42.jpg')
#print(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray)
#cv2.imshow('image',gray)
#image = cv2.resize(image,None,fx=0.5,fy=0.5)
#image  (x,y)    (height,width)  (bgr)  width of border 
#cv2.rectangle(image, (20,20), (100,100), (255,0,0), 5)
#cv2.imshow('image',image)
