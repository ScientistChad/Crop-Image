import cv2, json
import numpy as np
from PIL import Image


def getMasked(img_data,data,region='inside'):
    coords = []
    maskset = []
    mask_data = np.zeros((768,1024,4), dtype = "uint8")

    for mask in data:
        for coord in mask:
            coords.append([coord['x'],coord['y']])
        
        pts = np.array(coords,'int32')
        cv2.fillPoly(mask_data,[pts],(255,255,255,0))
        coords = []

    inside = cv2.bitwise_and(img_data,mask_data)
    flip = cv2.bitwise_not(mask_data)
    outside = cv2.bitwise_and(img_data,flip)

    if(region == 'inside'):
        return inside
    else:
        return outside



img_data = np.random.randint(255, size=(768,1024,4),dtype=np.uint8)

with open('mask_debug_data.json') as json_file:
    data = json.load(json_file)
    

cropped_img = getMasked(img_data,data)


cv2.imshow('cropped img',cropped_img)

cv2.waitKey(0)
