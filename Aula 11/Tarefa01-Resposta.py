# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('ifma-caxias.jpg', 0)

rectKernel=cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
res=cv2.morphologyEx(img, cv2.MORPH_TOPHAT, rectKernel)

cv2.imshow('Result',res)

cv2.waitKey(0)
cv2.destroyAllWindows()
