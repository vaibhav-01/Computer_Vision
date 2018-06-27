 #program for using webcam
import cv2
import random
import numpy 
#starting webcam
cap=cv2.VideoCapture(0)

while cap.isOpened():
	status,frame=cap.read()
	cv2.imshow('webcam',frame)
	#cv2.imwrite("img",frame)
	x=random.random()
	y=str(x)[2:4]
	bwimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('webcam1',bwimg)	

	if cv2.waitKey(1) & 0xFF==ord("q"):
		break

cv2.destroyAllWindows()
cap.release()	
