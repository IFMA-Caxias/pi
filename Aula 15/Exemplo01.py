# coding=utf-8
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("logo-if.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
harris = cv2.cornerHarris(gray,2,3,0.05)
harris = cv2.cvtColor(harris,cv2.COLOR_BGR2RGB)

corners = cv2.goodFeaturesToTrack(gray,50,0.01,10)
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.subplot(211), plt.imshow(harris)
plt.title('Corners')
plt.subplot(212), plt.imshow(img)
plt.title('Features')

plt.tight_layout()
plt.show()