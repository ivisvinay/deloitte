# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:54:20 2020

@author: admin
"""
import cv2
from table_process import table_process

img1 = cv2.imread('thamer.png',0)
object_repository=list()
    
table_process(img1)

