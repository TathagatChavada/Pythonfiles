import cv2

img = cv2.imread('E:\/Road.jpg')
print(img.shape)

width, height = 400, 400
Img_Resize = cv2.resize(img,(width,height))
print(Img_Resize)

imgCropped = img[150:402,0:591]

cv2.imshow('Road',img)
cv2.imshow('Road Resize',Img_Resize)
cv2.imshow('RoadCropped',imgCropped)
cv2.waitKey(0)
cv2.destroyWindow()