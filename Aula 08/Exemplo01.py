# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('logo-if.jpg')

ksize=7

kernel = np.ones((ksize,ksize),np.float32)/(ksize*ksize)

conv = cv2.filter2D(img,-1,kernel)

blur = cv2.blur(img,(ksize,ksize))

gauss = cv2.GaussianBlur(img,(ksize,ksize),0)

median = cv2.medianBlur(img,ksize)


cv2.imshow('Img',img)
cv2.imshow('Convolution',conv)
cv2.imshow('Blur',blur)
cv2.imshow('GaussianBlur',gauss)
cv2.imshow('Median',median)

cv2.waitKey(0)
cv2.destroyAllWindows()
