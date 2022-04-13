# coding=utf-8
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('ifma-caxias.jpg', cv2.IMREAD_GRAYSCALE)

eq_img = cv2.equalizeHist(img)

cv2.imshow('Original',img)
cv2.imshow('Equalizada', eq_img)

hist = cv2.calcHist([img],[0],None,[256],[0,256])
eq_hist = cv2.calcHist([eq_img],[0],None,[256],[0,256])

plt.plot(eq_hist,color = 'r')
plt.plot(hist, color = 'b')
plt.xlim([0,256])
plt.show()

cv2.waitKey(0)

cv2.destroyAllWindows()
