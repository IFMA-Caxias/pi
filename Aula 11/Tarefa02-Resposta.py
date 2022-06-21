# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('atividade_aula11.png', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,(200,200), interpolation = cv2.INTER_CUBIC)

#Img 1

# k_erosion = np.ones((21,21), dtype = np.uint8)
k_erosion = np.ones((3,3), dtype = np.uint8)

# eroded = cv2.erode(img, k_erosion, anchor=(20,20))
eroded = cv2.erode(img, k_erosion, anchor=(2,2), iterations=9)



#Img 2

k_erosion = np.ones((51,41), dtype = np.uint8)
# k_erosion = np.ones((11,9), dtype = np.uint8)

eroded_tmp = cv2.erode(img, k_erosion)
# eroded_tmp = cv2.erode(img, k_erosion,iterations=5)

k_dilation = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(31,31))

dilated = cv2.dilate(eroded_tmp, k_dilation)



#Img 3

k_dilation = np.ones((9,9), dtype = np.uint8)

dilated_tmpx = cv2.dilate(img, k_dilation, iterations=5)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9))

eroded_tmpx = cv2.erode(dilated_tmpx, kernel, iterations=5)

rounded = cv2.dilate(eroded_tmpx, kernel, iterations=3)


plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Imagem')
plt.subplot(222), plt.imshow(cv2.cvtColor(dilated_tmpx, cv2.COLOR_BGR2RGB))
plt.title('Dilation')
plt.subplot(223), plt.imshow(cv2.cvtColor(eroded_tmpx, cv2.COLOR_BGR2RGB))
plt.title('Erosion')
plt.subplot(224), plt.imshow(cv2.cvtColor(rounded, cv2.COLOR_BGR2RGB))
plt.title('Rounded')

plt.tight_layout()
plt.show()
