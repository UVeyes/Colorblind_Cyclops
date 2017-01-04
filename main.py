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
os.chdir(landscapeDir)

RED_THRESHOLD = 100
BLUE_GREEN_THRESHOLD = 50

UVraw = rawpy.imread('petroglyphs_uvBaader_20160225valleyOfFireStateParkNV_45180.nef')	#Creates RAWPY Object
VLraw = rawpy.imread('petroglyphs_visible_20160225valleyOfFireStateParkNV_45170.nef')  #Creates RAWPY Object

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

VLbS 		= cv2.resize(VLb, (960, 540))  
cv2.imshow('VLbS',VLbS)

VLbS 		= cv2.resize(VLb, (960, 540))  
cv2.imshow('VLbS',VLbS)

VLbS 		= cv2.resize(VLb, (960, 540))  
cv2.imshow('VLbS',VLbS)



cv2.waitKey(0)
cv2.destroyAllWindows()

VLblue_green = VLbgr.copy()
VLblue_green[:,:,2] = 0

VLred_threshold_image = VLbgr.copy()
VLred_threshold_image[:,:,0] = 0
VLred_threshold_image[:,:,1] = 0
VLred_threshold_image[:,:,2] = RED_THRESHOLD

VLbg = VLb + VLg

ret, VLbg_mask = cv2.threshold(VLbg,BLUE_GREEN_THRESHOLD,512,cv2.THRESH_BINARY)
ret, VLr_mask = cv2.threshold(VLr,RED_THRESHOLD,255,cv2.THRESH_BINARY)
VLbg_mask_inv = cv2.bitwise_not(VLbg_mask)

VLred_only = cv2.bitwise_and(VLbg_mask_inv,VLr_mask) #no blue or green or black

VLblue_green_r_AR = VLblue_green.copy()
VLblue_green_r_AR[:,:,1] += VLred_only*20
#cv2.imshow('blue_green_r_AR',VLblue_green_r_AR)
#cv2.imshow('bg_mask_inv',VLbg_mask_inv)
#cv2.imshow('red_only', VLred_only)
#cv2.imshow('bg_mask', VLbg_mask)
#cv2.imshow('r_mask', VLr_mask)
#cv2.imshow('RED_THRESHOLD',VLred_threshold_image)
#cv2.imshow('red_only', red_only)
#cv2.imshow('bg',bg)
#cv2.imshow('r',r)

#cv2.imshow('image',VLbgr)
#cv2.imshow('blue',blue)
#cv2.imshow('green',green)
#cv2.imshow('red',VLred)
#cv2.imshow('blue_green',VLblue_green)


#small (resized images)
VLbgrS 	= cv2.resize(VLbgr, (960, 540))  
UVbgrS 	= cv2.resize(UVbgr, (960, 540))  
UVbwS 	= cv2.resize(UVbw, (960, 540))  

#VLrS 		= cv2.resize(VLr, (960, 540))  
#VLbS 		= cv2.resize(VLg, (960, 540))  
#VLgS 		= cv2.resize(VLb, (960, 540))  

UVrS 		= cv2.resize(UVr, (960, 540))  
UVbS 		= cv2.resize(UVg, (960, 540))  
UVgS 		= cv2.resize(UVb, (960, 540))  

cv2.imshow('VLbgrS',VLbgrS)
cv2.imshow('UVbgrS',UVbgrS)
cv2.imshow('UVbwS',UVbwS)

#cv2.imshow('VLrS', VLrS)
#cv2.imshow('VLbS', VLbS)
#cv2.imshow('VLgS', VLgS)
cv2.imshow('UVrS', UVrS)
cv2.imshow('UVbS', UVbS)
cv2.imshow('UVgS', UVgS)


cv2.waitKey(0)
cv2.destroyAllWindows()