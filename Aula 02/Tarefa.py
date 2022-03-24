import cv2
img = cv2.imread('logo-if.jpg')

gray = cv2.imread('logo-if.jpg',cv2.IMREAD_GRAYSCALE)

(row, col) = img.shape[0:2]

for i in range(row):
	for j in range(col):
		img[i, j] = sum(img[i, j]) * 0.33

cv2.imshow('Media', img)
cv2.imshow('Gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
