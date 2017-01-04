import numpy as np
import cv2  #add OpenCV Library
import rawpy
import os
import sys

# Add sub directory /Images
fileDir = os.path.dirname(os.path.realpath('__file__')) #curent file directory
imagesDir = fileDir + '\Images'
flowersDir = imagesDir + '\Flowers'
landscapeDir = imagesDir + '\Petroglyphs' 

#change directory for landscape
os.chdir(flowersDir)

UV_THRESHOLD = 40
BLUE_GREEN_RED_THRESHOLD = 100

UVraw = rawpy.imread('bouquet_uvAndreaU2_sun_20160914wf_50784.nef')	#Creates RAWPY Object
VLraw = rawpy.imread('bouquet_visRef_sun_20160914wf_50701.nef')  #Creates RAWPY Object

UVrgb = UVraw.postprocess()
VLrgb = VLraw.postprocess()

VLr,VLg,VLb = cv2.split(VLrgb)
UVr,UVg,UVb = cv2.split(UVrgb)

#openCV style image
VLbgr = cv2.merge((VLb,VLg,VLr))
UVbgr = cv2.merge((UVb,UVg,UVr))
UVbw = cv2.cvtColor(UVbgr, cv2.COLOR_RGB2GRAY )

#only blue part of the image
VLblue 	= VLbgr.copy()
VLblue[:,:,1] = 0
VLblue[:,:,2] = 0

VLgreen = VLbgr.copy()
VLgreen[:,:,0] = 0
VLgreen[:,:,2] = 0

VLred = VLbgr.copy()
VLred[:,:,0] = 0
VLred[:,:,1] = 0

VLblue_green_red = VLbgr.copy()

VLbgr_sum = VLr + VLb + VLg

ret, VLbgr_mask = cv2.threshold(VLbgr_sum,BLUE_GREEN_RED_THRESHOLD,512,cv2.THRESH_BINARY)
ret, UV_mask = cv2.threshold(UVbw,UV_THRESHOLD,255,cv2.THRESH_BINARY)

UV_mask_inv = cv2.bitwise_not(UV_mask)
VLbgr_mask_inv = cv2.bitwise_not(VLbgr_mask)

UV_only = cv2.bitwise_and(VLbgr_mask,UV_mask_inv) #no blue or green or black

VLblue_green_red_UV_AR = VLblue_green_red.copy()
VLblue_green_red_UV_AR[:,:,0] += UV_only*50
VLblue_green_red_UV_AR[:,:,2] += UV_only*50
#cv2.imshow('red_blue_green_UV_AR',VLred_blue_green_UV_AR)
VLbgr_AR_UV_S 	= cv2.resize(VLblue_green_red_UV_AR, (960, 540))  
UV_onlyS     = cv2.resize(UV_only, (960, 540))
UV_maskS 	= cv2.resize(UV_mask, (960, 540))
VLbgr_maskS 	= cv2.resize(VLbgr_mask, (960, 540))

cv2.imshow('VLbgr_AR_UV_S',VLbgr_AR_UV_S)
cv2.imshow('UV_onlyS',UV_onlyS)
cv2.imshow('UV_maskS',UV_maskS)
cv2.imshow('VLbgr_maskS',VLbgr_maskS)

#small (resized images)
VLbgrS 	= cv2.resize(VLbgr, (960, 540))  
UVbgrS 	= cv2.resize(UVbgr, (960, 540))  
UVbwS 	= cv2.resize(UVbw, (960, 540))  

cv2.imshow('UVbwS',UVbwS)

cv2.waitKey(0)
cv2.destroyAllWindows()