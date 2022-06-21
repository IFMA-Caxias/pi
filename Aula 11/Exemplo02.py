# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

kernel = np.ones((5,5),np.uint8)

img_open = cv2.imread('j_opening.png',0)

kernel = np.ones((5,5),np.uint)
erosion = cv2.erode(img_open,kernel,iterations = 1)
opening = cv2.dilate(erosion,kernel,iterations = 1)

# opening = cv2.morphologyEx(img_open, cv2.MORPH_OPEN, kernel)

img_close = cv2.imread('j_closing.png',0)
closing = cv2.morphologyEx(img_close, cv2.MORPH_CLOSE, kernel)

plt.subplot(221), plt.imshow(img_open)
plt.title('Imagem 1')
plt.subplot(222), plt.imshow(opening)
plt.title('Opening')
plt.subplot(223), plt.imshow(img_close)
plt.title('Imagem 2')
plt.subplot(224), plt.imshow(closing)
plt.title('Closing')

plt.tight_layout()
plt.show()