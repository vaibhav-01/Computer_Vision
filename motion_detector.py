 #program for detecting motion through webcam
import cv2
import random
import numpy
import os
#defining a function that will return the difference between three conseutive images,taken from webcam.......threearguments represents three consecutive takes of the webcam.
def imgdiff(x,y,z):
	img1=cv2.absdiff(x,y)
	img2=cv2.absdiff(y,z)	
	comm_diff=cv2.bitwise_and(img1,img2)
	return(comm_diff)

#using webcam
cap=cv2.VideoCapture(0)

#taking three takes.
frame1=cap.read()[1]
frame2=cap.read()[1]
frame3=cap.read()[1]

#converting to grey scale...it will ease the process of finding out difference between consecutive takes.
gray1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(frame3,cv2.COLOR_BGR2GRAY)

while cap.isOpened():
	img_diff=imgdiff(gray1,gray2,gray3)
	cv2.imshow('Motion Detector',img_diff)
	status,frame4=cap.read()
	gray1=gray2
	gray2=gray3
	gray3=cv2.cvtColor(frame4,cv2.COLOR_BGR2GRAY)
	

	for i in range(0,480):
		for j in range(0,640):

			if img_diff[i][j]==0:
				print("coming zero")
			else:
				print("not coming zero")
	
	if cv2.waitKey(1) & 0xFF==ord("q"):
		break
cv2.destroyAllWindows()
cap.releaase()
