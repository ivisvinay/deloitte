# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:55:08 2020

@author: admin
"""
import numpy as np
import cv2

def dilating(img1):
    ret, otsu = cv2.threshold(img1, 120, 255, cv2.THRESH_OTSU)
    kernel = np.ones((1,2), np.uint8)
    img_dilation = cv2.erode(otsu, kernel, iterations=5)
    imagem = cv2.bitwise_not(img_dilation)
    return img_dilation,imagem,otsu