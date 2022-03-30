# coding=utf-8

import cv2
import numpy as np

img1 = cv2.imread("drawing_1.png")
img2 = cv2.imread("drawing_2.png")

bit_and = cv2.bitwise_and(img2, img1)
bit_or = cv2.bitwise_or(img2, img1)
bit_xor = cv2.bitwise_xor(img1, img2)
bit_not = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)


cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

cv2.imshow("bit_and", bit_and)
cv2.imshow("bit_or", bit_or)
cv2.imshow("bit_xor", bit_xor)
cv2.imshow("bit_not", bit_not)
cv2.imshow("bit_not2", bit_not2)


cv2.waitKey(0)
cv2.destroyAllWindows()
