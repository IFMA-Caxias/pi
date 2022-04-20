# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('ifma-caxias.jpg')

rows,cols = img.shape[:2]

angle=0
center_x=0
center_y=0

T = np.float32([[1,0,cols*(-0.5)],[0,1,rows*(-0.5)]])

T_Inv = np.float32([[1,0,cols*(0.5)],[0,1,rows*(0.5)]])

def define_center(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global center_x,center_y
        center_x=x
        center_y=y

cv2.namedWindow('Tarefa')
cv2.setMouseCallback('Tarefa',define_center)

while(1):

    if(angle>360): angle=0

    R = cv2.getRotationMatrix2D((center_x,center_y),angle,1)
    
    res = cv2.warpAffine(img,R,(cols,rows))
    
    cv2.circle(res,(center_x,center_y),5,(0,0,255),-1)
    
    cv2.imshow('Tarefa',res)

    k=cv2.waitKey(20)
    if k == 27:
        break
    elif k == ord('r'):
        angle+=5
    
cv2.destroyAllWindows()