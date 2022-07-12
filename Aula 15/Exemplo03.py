# coding=utf-8
import numpy as np
import cv2

img1 = cv2.imread('cristo-orig.jpg',0)
img2 = cv2.imread('cristo-scene.jpg',0)

orb = cv2.ORB_create(nfeatures=10000)

# extrai keypoints e descritores
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

res1 = cv2.drawKeypoints(img1, kp1, None)
res2 = cv2.drawKeypoints(img2, kp2, None)

# cria o BFMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)

# Ordena matches pela distancia
matches = sorted(matches, key = lambda x:x.distance)

# Seleciona os melhores matches (menor distância)
best=matches[:500]

if len(best)>10: #Define uma quantidade mínima de matches para calcular
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in best ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in best ]).reshape(-1,1,2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()

    h,w = img1.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)

    res2 = cv2.polylines(res2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

else:
    print("Matches insuficientes")
    matchesMask = None

draw_params = dict(matchColor = (0,255,0), singlePointColor = None, matchesMask = matchesMask, flags = 2)

img_match = cv2.drawMatches(res1,kp1,res2,kp2,best,None,**draw_params)

cv2.imshow("Matches", img_match)
cv2.waitKey(0)
