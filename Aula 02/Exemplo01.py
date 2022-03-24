import cv2

img = cv2.imread('logo-if.jpg')

b, g, r = cv2.split(img)

cv2.imshow('BGR',img)
cv2.imshow('Red',r)
cv2.imshow('Green',g)
cv2.imshow('Blue',b)

# res = cv2.merge([r,g,b])
# cv2.imshow('RGB',res)

cv2.waitKey(0)
cv2.destroyAllWindows()
