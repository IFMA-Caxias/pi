# coding=utf-8
import numpy as np
import cv2

img1 = cv2.imread('logo-if.jpg',0)
img2 = cv2.imread('logo-if-vertical.png',0)

orb = cv2.ORB_create(nfeatures=10000)

# extrai keypoints e descritores
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

res1 = cv2.drawKeypoints(img1, kp1, None)
res2 = cv2.drawKeypoints(img2, kp2, None)

cv2.imshow("Image1", res1)
cv2.imshow("Image2", res2)

# cria o BFMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)

# Ordena matches pela distancia
matches = sorted(matches, key = lambda x:x.distance)

#Seleciona os 100 melhores
matches=matches[:100]

#Desenha keypoints da imagem 1
img1 = cv2.drawKeypoints(img1, kp1, None)

img_match = cv2.drawMatches(img1,kp1,img2,kp2,matches,None, flags=2)

cv2.imshow("Matches", img_match)
cv2.waitKey(0)
