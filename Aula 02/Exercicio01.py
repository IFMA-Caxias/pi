import cv2
import numpy
img = cv2.imread('logo-if.jpg')

print(img.shape)
(row, col) = img.shape[0:2]

for i in range(row):
	for j in range(col):
		img[i, j] = sum(img[i, j]) * 0.33


cv2.imshow('GRAY',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
