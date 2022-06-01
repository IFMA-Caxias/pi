# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('logo-if.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,process = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(process, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,255), 2)

for cnt in contours:
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.circle(img,(cx,cy),3,(255,0,0),-1)

ids=[1,28,29]
for id in ids:
    area = cv2.contourArea(contours[id])
    perimeter = cv2.arcLength(contours[id],True)
    print('Id:%d\nArea:%d\nPerimetro:%d\n\n' % (id,area,perimeter))

    x,y,w,h = cv2.boundingRect(contours[id])
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    (x,y),radius = cv2.minEnclosingCircle(contours[id])
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(img,center,radius,(0,255,0),2)

cv2.imshow('Contours',img)

cv2.waitKey(0)
cv2.destroyAllWindows()