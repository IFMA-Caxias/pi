# coding=utf-8
import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('inpaint_opencv.png')
mask = cv2.imread('inpaint_mask.png',0)

telea = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
ns = cv2.inpaint(img,mask,3,cv2.INPAINT_NS)

plt.subplot(221), plt.imshow(img)
plt.title('Imagem')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.title('Máscara')
plt.subplot(223), plt.imshow(telea)
plt.title('TELEA')
plt.subplot(224), plt.imshow(ns)
plt.title('NS')

plt.tight_layout()
plt.show()