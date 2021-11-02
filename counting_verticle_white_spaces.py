# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:48:37 2020

@author: admin
"""



import cv2

def counting_verticle_white_spaces(ots,cropped_image):
    ver=0
    count=0
    exception=0
    counter_ver2=list()
    counter_ver2.clear()
    img_dilation2=ots
    imagem2= cv2.bitwise_not(cropped_image) 
    for i in range(len(img_dilation2[1])):
        for j in range(len(img_dilation2)):
            if imagem2[j][i].all()==1:
                count=count+1
        counter_ver2.append(count)
        count=0
    
    for k in range(len(counter_ver2)):
        if int(counter_ver2[k])>0:
            counter_ver2[k]=1
            
    try:        
        for k in range(len(counter_ver2)): 
            if int(counter_ver2[k])==0 and int(counter_ver2[k+1])==1: 
                ver=ver+1
                break
        x1=k
        
        if ver == 0:
            segment_left = ots
        else:
            segment_left=img_dilation2[0:len(img_dilation2)-1,1:x1-1]   
        if ver == 0:
            segment_right = None
        else:
            segment_right=img_dilation2[0:len(img_dilation2)-1,x1+1:len(img_dilation2[1])]
        
        return segment_left,segment_right,ver
    except:
        exception=exception+1
        #object_repository.append(ots)