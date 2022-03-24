import cv2
img = cv2.imread('logo-if.jpg',cv2.IMREAD_COLOR)
# img = cv2.imread('logo-if.jpg',cv2.IMREAD_GRAYSCALE)


print(img.shape)
print(img.size)

cv2.imshow('Logo IF',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
