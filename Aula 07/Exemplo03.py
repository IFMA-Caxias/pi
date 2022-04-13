# coding=utf-8
import cv2

img = cv2.imread('logo-if.jpg')

#Redimensiona imagem
img = cv2.resize(img,(200,100),interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, mask_inv = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
mask = cv2.bitwise_not(mask_inv)

cv2.imshow('Original',img)
cv2.imshow('Grayscale',gray)
cv2.imshow('Threshold',mask)
cv2.imshow('Mask Inv',mask_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()
