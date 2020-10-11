import cv2
import numpy as np

img = np.zeros((500,1100,3))
# img[10:100,60:500] = 0,0,300

cv2.line(img,(0,0),(500,500),(0,0,555),2)                              # Code for drawing line.
cv2.rectangle(img,(300,200),(400,100),(0,455,0),cv2.FILLED)            # Code for drawing rectangle.

cv2.circle(img,(150,400),50,(500,0,0),8)                               # Code for drawing circle.
cv2.circle(img,(150,400),40,(0,500,0),8)
cv2.circle(img,(150,400),30,(0,0,500),8)
cv2.circle(img,(150,400),20,(500,0,0),8)
cv2.circle(img,(150,400),10,(0,500,0),8)

cv2.putText(img,'Shapes',(500,50),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,500),2)         # Code for putting text into an image.


cv2.imwrite('E:\/Shapes.png', img)
cv2.imshow('Image', img)


cv2.waitKey(0)
cv2.destroyWindow()



