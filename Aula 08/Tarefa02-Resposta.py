from email.mime import base
import cv2
import numpy as np

img = cv2.imread('cars.png', 3)
mask = np.ones(img.shape, np.uint8)
cv2.circle(mask, (mask.shape[1] - 480, mask.shape[0] -
           300), 270, (255, 255, 255), -1)
mask = cv2.GaussianBlur(mask, (51,51), 51)

maskInv = cv2.bitwise_not(mask)
imgBlur = cv2.blur(img, (50, 50))


imageMaskedBack = imgBlur * (maskInv / 255)
imageMaskedBack=imageMaskedBack.astype(np.uint8)

imageMaskedFocus = img * (mask / 255)
imageMaskedFocus=imageMaskedFocus.astype(np.uint8)

res = cv2.add(imageMaskedBack, imageMaskedFocus,  dtype=cv2.CV_8U)

cv2.imshow('noBlur', img)
cv2.imshow('blur', imgBlur)
cv2.imshow('mask', maskInv)
cv2.imshow('imageMaskedBack', imageMaskedBack)
cv2.imshow('imageMaskedFocus', imageMaskedFocus)
cv2.imshow('res', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
