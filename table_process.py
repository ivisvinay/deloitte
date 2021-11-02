# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:07:39 2020

@author: admin
"""

import cv2

from remove_margins import remove_margins
from counting_verticle_white_spaces import counting_verticle_white_spaces
#from counting_horizontal_white_spaces import counting_horizontal_white_spaces

def table_process(img1):
    exception=0
    ots, cropped_image = remove_margins(img1)
    cv2.imshow('cropped_image',cropped_image)          
    cv2.waitKey()
    segment_left,segment_right,ver = counting_verticle_white_spaces(ots,cropped_image)
    cv2.imshow("segment_left",segment_left)
    cv2.waitKey()
    try:
        
        cv2.destroyAllWindows()
        if ver!=0:
            table_process(segment_right)
        else:
            return
        
        
    except:
        exception=exception+1