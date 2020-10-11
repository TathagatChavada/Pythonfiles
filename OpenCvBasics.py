import cv2
import numpy as np

kernel = np.ones((2,2), np.uint8)
print(kernel)

img = cv2.imread('E:\/John.jpg')
Grey_Scale = cv2.imread('E:\/John.jpg', 0)
Blur = cv2.GaussianBlur(Grey_Scale, (11, 11), 0)
Image_Canny = cv2.Canny(img, 200, 200)
Img_Dilation = cv2.dilate(Image_Canny, kernel, iterations=1)

cv2.imshow('John', img)
cv2.imshow('Grey_Scale', Grey_Scale)
cv2.imshow('Blur', Blur)
cv2.imshow('Image_Canny', Image_Canny)
cv2.imshow('Img_Dilation', Img_Dilation)

cv2.waitKey(0)
cv2.destroyWindow()

