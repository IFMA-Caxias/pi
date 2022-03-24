import cv2
import numpy as np

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

import cv2
img = cv2.imread('logo-if.jpg')

cv2.line(img,(0,0),(150,150),BLUE,2)
# cv2.line(img,(200,100),(200,250),BLACK,7)

# cv2.rectangle(img,(250,150),(300,250),RED,3)

# cv2.circle(img,(350,200),50,GREEN,-1)

# pts = np.array([(400,270),(370,234),(450,85),(380,10)], np.int32)
# cv2.polylines(img,[pts],True,GRAY,3)


# cv2.putText(img, 'Txt1', (510, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, RED, 2,
#             cv2.LINE_4)
# cv2.putText(img, 'Txt2', (510, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, GREEN, 2,
#             cv2.LINE_8)
# cv2.putText(img, 'Txt3', (510, 110), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.9, BLUE, 2,
#             cv2.LINE_AA)

cv2.imshow('Logo IF',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

