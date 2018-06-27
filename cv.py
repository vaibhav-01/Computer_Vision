#opening an image using opencv

import cv2
img=cv2.imread('car1.jpeg')

cv2.circle(img,(162,100),100,(204,140,114),2)
font=cv2.FONT_HERSHEY_PLAIN
cv2.putText(img,'CAAAAR',(162,100),font,1,(162,247,246),cv2.LINE_AA)
cv2.imshow("Lamborghini",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
