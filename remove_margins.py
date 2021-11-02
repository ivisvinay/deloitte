# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:58:47 2020

@author: admin
"""
import cv2
import numpy as np
from dilating import dilating

def remove_margins(img1):
    img_dilation,imagem,otsu=dilating(img1)
    #counting verticle white pixels
    count=0
    counter_ver=list()
    c_v=list()
    c_h=list()
    for i in range(len(img_dilation[1])):
        for j in range(len(img_dilation)):
             if imagem[j][i].all()==1:
                 count=count+1
        counter_ver.append(count)
        count=0
        
    for k in range(len(counter_ver)):
        if int(counter_ver[k])>0:
            counter_ver[k]=1
    
    #left verticle margin  
    for k in range(len(counter_ver)):
        if int(counter_ver[k])>counter_ver[k-1]:
            break
    x1=k-1
    
    #right verticle margin  
    for k in range(len(counter_ver)-1,-1,-1):
        if int(counter_ver[k])<counter_ver[k-1]:
            break
    x2=k+1
    
    #counting horizontal white pixels
    count=0
    counter_hor=list()
    for i in range(len(img_dilation)):
        for j in range(len(img_dilation[1])):
            if imagem[i][j].all()==1:
                count=count+1
        counter_hor.append(count)
        count=0    
        
    #projecting horizontal lines for document   
    for a in range(len(counter_hor)):
        if int(counter_hor[a])>0:
            counter_hor[a]=1
    
    #top horizontal margin
    for a in range(len(counter_hor)):
        if int(counter_hor[a])>counter_hor[a-1]:
            c_h.append(a)  
            break
    y1=a-1
                
    #bottom horizontal margin
    for a in range(len(counter_hor)-1,-1,-1):
        if int(counter_hor[a])<counter_hor[a-1]:
            break
    y2=a+1
    
    cropped_image=img_dilation[y1:y2,x1:x2]
    ots=otsu[y1:y2,x1:x2]
    return ots,cropped_image