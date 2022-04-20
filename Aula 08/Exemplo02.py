# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('logo-if.jpg',0)

laplacian = cv2.Laplacian(img,cv2.CV_8U)
sobelx = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)

cv2.imshow('Img',img)
cv2.imshow('Laplacian',laplacian)
cv2.imshow('SobelX',sobelx)
cv2.imshow('SobelY',sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()
