import numpy as np
import cv2  #add OpenCV Library
#from . import * #add access to subdirectory files 


cam = cv2.VideoCapture(0)
RED_THRESHOLD = 50
BLUE_GREEN_THRESHOLD = 100

while(True):
	s, img = cam.read() # captures image
	cv2.imshow("Test Picture", img) # displays captured image
	#cv2.imwrite("test.bmp",im) # writes image test.bmp to disk


	b,g,r 	= cv2.split(img)

	#only blue part of the image
	blue 	= img.copy()
	blue[:,:,1] = 0
	blue[:,:,2] = 0

	green = img.copy()
	green[:,:,0] = 0
	green[:,:,2] = 0

	red = img.copy()
	red[:,:,0] = 0
	red[:,:,1] = 0

	blue_green = img.copy()
	blue_green[:,:,2] = 0

	red_threshold_image = img.copy()
	red_threshold_image[:,:,0] = 0
	red_threshold_image[:,:,1] = 0
	red_threshold_image[:,:,2] = RED_THRESHOLD

	bg = b + g

	ret, bg_mask = cv2.threshold(bg,BLUE_GREEN_THRESHOLD,512,cv2.THRESH_BINARY)
	ret, r_mask = cv2.threshold(r,RED_THRESHOLD,255,cv2.THRESH_BINARY)
	bg_mask_inv = cv2.bitwise_not(bg_mask)

	red_only = cv2.bitwise_and(bg_mask_inv,r_mask) #no blue or green or black

	#red only AR
	blue_green_r_AR = blue_green.copy()
	blue_green_r_AR[:,:,1] += red_only*100
	cv2.imshow('blue_green_r_AR',blue_green_r_AR)
	cv2.imshow('bg_mask_inv',bg_mask_inv)

	#red anywhere AR
	blue_green_r2_AR = blue_green.copy()
	blue_green_r2_AR[:,:,1] += r_mask*100
	cv2.imshow('blue_green_r2_AR',blue_green_r2_AR)


	cv2.imshow('bg_mask_inv',bg_mask_inv)
	#cv2.imshow('red_only', red_only)
	#cv2.imshow('bg_mask', bg_mask)
	#cv2.imshow('r_mask', r_mask)
	cv2.imshow('RED_THRESHOLD',red_threshold_image)
	#cv2.imshow('red_only', red_only)
	#cv2.imshow('bg',bg)
	#cv2.imshow('r',r)

	cv2.imshow('image',img)
	#cv2.imshow('blue',blue)
	#cv2.imshow('green',green)
	#cv2.imshow('red',red)
	cv2.imshow('blue_green',blue_green)

	#cv2.waitKey(0)

	if cv2.waitKey(1) & 0xFF == ord('w') and RED_THRESHOLD <255:
    		RED_THRESHOLD += 1
	if cv2.waitKey(1) & 0xFF == ord('s') and RED_THRESHOLD > 1:
    		RED_THRESHOLD -= 1

	if cv2.waitKey(1) & 0xFF == ord('d') and BLUE_GREEN_THRESHOLD <510:
    		BLUE_GREEN_THRESHOLD += 1
	if cv2.waitKey(1) & 0xFF == ord('a') and BLUE_GREEN_THRESHOLD > 1:
    		BLUE_GREEN_THRESHOLD -= 1


    		

#	if cv2.waitKey(1) & 0xFF == ord('a'):
 #   		break
    		
#	if cv2.waitKey(1) & 0xFF == ord('d'):
#    		break




	if cv2.waitKey(1) & 0xFF == ord('q'):
    		break

cap.release()
cv2.destroyAllWindows()
