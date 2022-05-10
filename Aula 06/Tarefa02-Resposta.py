# coding=utf-8
from math import *
import cv2
import numpy as np

img = cv2.imread('ifma-caxias.jpg')

rows,cols = img.shape[:2]

angle=0
cosR = cos(radians(angle))
sinR = sin(radians(angle))
R = [[cosR,sinR],[-sinR,cosR]]

def rotacaoDireta():

    res=np.zeros(img.shape, np.uint8)

    for r in range(0,rows):
        for c in range(0, cols):
            (x,y)=(np.matmul([c,r],R)).astype(int)
            if (x>=0)and(x<cols) and (y>=0)and(y<rows):
                res[y,x]=img[r,c]
    return res

def rotacaoInversa():
    R_Inv=np.linalg.inv(R)
    
    res=np.zeros(img.shape, np.uint8)

    for r in range(0,rows):
        for c in range(0, cols):
            (x,y)=(np.matmul([c,r],R_Inv)).astype(int)
            if (x>=0)and(x<cols) and (y>=0)and(y<rows):
                res[r,c]=img[y,x]
                
    return res
    
resInv=rotacaoInversa()
resDir=rotacaoDireta()
while(1):

    if(angle>360): angle=0
    
    cv2.imshow('Direta',resDir)
    cv2.imshow('Inversa',resInv)

    k=cv2.waitKey(20)
    if k == 27:
        break
    elif k == ord('r'):
        angle+=5
        cosR = cos(radians(angle))
        sinR = sin(radians(angle))
        R = [[cosR,sinR],[-sinR,cosR]]

        resInv=rotacaoInversa()
        resDir=rotacaoDireta()

cv2.destroyAllWindows()