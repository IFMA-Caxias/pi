# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread('logo-if.jpg')

def ajuste_brilho(img,br):
    brilho=[br,br,br]
    res=np.zeros(img.shape, np.uint8)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            res[y, x] = np.maximum(np.minimum(img[y,x]+brilho,[255,255,255]),[0,0,0])
    return res

def ajuste_contraste(img,contraste):
    res=np.zeros(img.shape, np.uint8)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            res[y, x] = np.maximum(np.minimum(img[y,x]*contraste,[255,255,255]),[0,0,0])
    return res

def ajuste_negativo(img):
    res=np.zeros(img.shape, np.uint8)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            res[y, x] = np.maximum([255,255,255]-img[y,x],[0,0,0])
    return res

cv2.namedWindow('Brilho-Contraste-Negativo')
brilho=0
contraste=1
negativo=False
result=imagem
cv2.imshow('Brilho-Contraste-Negativo',result)

while(True): 

    k=cv2.waitKey(20)
    if k == 27:
        break
    elif k == ord('a'):
        brilho=min(brilho+50,255)
        result=ajuste_brilho(imagem,brilho)
        cv2.imshow('Brilho-Contraste-Negativo',result)
    elif k == ord('z'):
        brilho=max(brilho-50,-255)
        result=ajuste_brilho(imagem,brilho)
        cv2.imshow('Brilho-Contraste-Negativo',result)
    elif k == ord('s'):
        contraste=min(contraste+0.25,2.0)
        result=ajuste_contraste(imagem,contraste)
        cv2.imshow('Brilho-Contraste-Negativo',result)
    elif k == ord('x'):
        contraste=max(contraste-0.25,0)
        result=ajuste_contraste(imagem,contraste)
        cv2.imshow('Brilho-Contraste-Negativo',result)
    elif k == ord('n'):
        result=ajuste_negativo(result)
        cv2.imshow('Brilho-Contraste-Negativo',result)

cv2.destroyAllWindows()
