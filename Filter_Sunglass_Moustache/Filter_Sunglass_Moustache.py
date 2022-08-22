# coding=utf-8
import numpy as np
import cv2,sys
from operator import itemgetter

sunglass = cv2.imread('sunglass.png', cv2.IMREAD_UNCHANGED)
moustache = cv2.imread('moustache.png', cv2.IMREAD_UNCHANGED)

face_cascade = cv2.CascadeClassifier('classificadores/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('classificadores/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('classificadores/haarcascade_mcs_mouth.xml')

sunglass_pos=(0,0)
sunglass_width=0
moustache_pos=(0,0)
moustache_width=0
moustache_increase=2.0
sunglass_increase=1.25

def smooth_value(current,new,rate=0.75):
    return int(current*rate+new*(1-rate))

def smooth_pos(current,new,rate=0.75):
    res_x=smooth_value(current[0],new[0],rate)
    res_y=smooth_value(current[1],new[1],rate)
    return (res_x,res_y)


def resizeImg(img, width):
    scale = width/img.shape[1]
    height = int(img.shape[0] * scale)
    size = (width, height)
    return cv2.resize(img, size, interpolation=cv2.INTER_AREA)

def drawElement(img, element, position, width):
    
    res = resizeImg(element, width)
    rows, cols = res.shape[:2]

    if(position[0]<cols/2) or (position[1]<rows/2): return

    x=position[0]-int(cols/2)
    y=position[1]-int(rows/2)

    if(rows>=img.shape[0]) or (cols>=img.shape[1]): return
    if(x+cols>=img.shape[1]) or (y+rows>=img.shape[0]): return

    roi = img[y:(y+rows), x:(x+cols)]
    
    (_,_,_,alpha)=cv2.split(res)
    roi[alpha>0] = res[alpha>0]

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erro ao abrir a camera")
    sys.exit(0)

cv2.namedWindow('Cam')
while True:
    ret, frame = cap.read()
    img = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
    for (x,y,w,h) in faces:
        # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        face_gray = gray[y:y+h, x:x+w]
        face_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(face_gray, 1.1,10)
        min_x,min_y=(x+w,y+h)
        max_x,max_y=(0,0)
        if(len(eyes)==2):
            for (ex,ey,ew,eh) in eyes:
                # cv2.rectangle(face_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                min_x=min(ex,min_x)
                min_y=min(ey,min_y)
                max_x=max(ex+ew,max_x)
                max_y=max(ey+eh,max_y)

            eyes_width=(max_x-min_x)
            eyes_height=(max_y-min_y)
            eyes_center=(min_x+int(eyes_width*0.5),min_y+int(eyes_height*0.5))
            sunglass_pos=smooth_pos(sunglass_pos, eyes_center)
            sunglass_width=smooth_value(sunglass_width, eyes_width)
            drawElement(face_color, sunglass, sunglass_pos, int(sunglass_width*sunglass_increase))
        else:
            drawElement(face_color, sunglass, sunglass_pos, int(sunglass_width*sunglass_increase))

        mouth = mouth_cascade.detectMultiScale(face_gray, 2.0, 10)
        if(len(mouth)>0):
            mouth_center=(0,0)
            mouth_width=0
            for (mx,my,mw,mh) in [max(mouth,key=itemgetter(1))]:
                #cv2.rectangle(face_color,(mx,my),(mx+mw,my+mh),(0,0,255),2)
                mouth_center=(int(mx+mw*0.5), int(my+mh*0.1))
                mouth_width=mw
            
            if(mouth_width>0):
                moustache_pos=smooth_pos(moustache_pos, mouth_center)
                moustache_width=smooth_value(moustache_width, mouth_width)
                drawElement(face_color, moustache, moustache_pos, int(moustache_width*moustache_increase))
        else:
            drawElement(face_color, moustache, moustache_pos, int(moustache_width*moustache_increase))

    cv2.imshow('Webcam', img)
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
c = cv2.waitKey(0)
cv2.destroyAllWindows()
