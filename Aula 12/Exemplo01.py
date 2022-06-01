# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('logo-if.jpg', 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

sobelx = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)

canny = cv2.Canny(img,100,200)
canny = cv2.cvtColor(canny, cv2.COLOR_BGR2RGB)


plt.subplot(221), plt.imshow(img)
plt.title('Imagem')
plt.subplot(222), plt.imshow(sobelx)
plt.title('SobelX')
plt.subplot(223), plt.imshow(sobely)
plt.title('SobelY')
plt.subplot(224), plt.imshow(canny)
plt.title('Canny')

plt.tight_layout()
plt.show()