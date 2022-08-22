# coding=utf-8
import numpy as np
import cv2,sys

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erro ao abrir a camera")
    sys.exit(0)

face_cascade = cv2.CascadeClassifier('classificadores/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('classificadores/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('classificadores/haarcascade_mcs_mouth.xml')

cv2.namedWindow('Cam')
while True:
    ret, frame = cap.read()
    img = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1,10)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        mouth = mouth_cascade.detectMultiScale(roi_gray, 2.0, 20)
        for (mx,my,mw,mh) in mouth:
            cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(0,0,255),2)

    cv2.imshow('Webcam', img)
    c = cv2.waitKey(1)
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()
