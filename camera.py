import cv2
capture=cv2.VideoCapture(0)
if capture.isOpened():
	print("READY!!!!!!!!!!!!!!!!!!!CHEESEEEEE")
	#current camera data,after frame take camera status
	frame,status=capture.read() 
	cv2.imshow("frame1",frame)
	cv2.imwrite("You.jpeg",frame)
	cv2.waitKey(0)
	capture.release()
else:
	print("you are ugly")
