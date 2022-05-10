# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('noise.jpg')

median = cv2.medianBlur(img,5)

cv2.imwrite('Img.jpg',img)
cv2.imwrite('Median.jpg',median)

cv2.waitKey(0)
cv2.destroyAllWindows()
