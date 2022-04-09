# coding=utf-8
import cv2
import numpy as np

imagem1 = cv2.imread('bandeira_cxs.jpg')
imagem2 = cv2.imread('bandeira_ma.jpg')

def addImg(img1,img2):
    res=np.zeros(img1.shape, np.uint8)
    for y in range(0, img1.shape[0]):
        for x in range(0, img1.shape[1]):
            pixel1=img1[y,x].astype(np.int32)
            pixel2=img2[y,x].astype(np.int32)
            res[y, x] = np.maximum(np.minimum(pixel1-pixel2,(255,255,255)),(0,0,0))
    return res

cv2.namedWindow('Operacoes')
alpha=0.5
while(1):
    result=cv2.add(imagem1,imagem2)
    # result=cv2.subtract(imagem1,imagem2)
    # result=cv2.addWeighted(imagem1,alpha,imagem2,(1.0-alpha),0)
    # result=addImg(imagem1,imagem2)

    cv2.imshow('Operacoes',result)
    k=cv2.waitKey(20)
    if k == 27:
        break
    elif k == ord('a'):
        alpha=min(alpha+0.1,1.0)
    elif k == ord('z'):
        alpha=max(alpha-0.1,0.0)
cv2.destroyAllWindows()
