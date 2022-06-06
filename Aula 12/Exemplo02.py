# coding=utf-8
import cv2
import numpy as np

orig = cv2.imread('logo-if.jpg')

gray = cv2.cvtColor(orig,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
res=orig.copy()

lines = cv2.HoughLines(edges,1,np.pi/180,100)
for line in lines:
    for rho,theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(res,(x1,y1),(x2,y2),(255,0,0),2)
cv2.imshow('HoughLines',res)

lines = cv2.HoughLinesP(edges,1,np.pi/180,50,minLineLength=0,maxLineGap=10)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(res,(x1,y1),(x2,y2),(255,0,255),2)
cv2.imshow('HoughLinesP',res)

img_blur = cv2.medianBlur(orig,5)
img_blur = cv2.cvtColor(img_blur,cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(img_blur,cv2.HOUGH_GRADIENT,1,150,param1=200,param2=50,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(res,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(res,(i[0],i[1]),2,(255,0,0),3)
cv2.imshow('HoughCircles',res)

cv2.waitKey(0)
cv2.destroyAllWindows()
