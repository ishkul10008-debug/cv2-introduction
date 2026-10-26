import cv2
import os
imagestore1=cv2.imread(r'C:\Python\Python\open cv\vibrant image1.jpg')
cv2.imshow('original image1',imagestore1)
cv2.waitKey(0)
gaussian=cv2.GaussianBlur(imagestore1,(3,3),0)
cv2.imshow('gaussian blur image',gaussian)
# cv2.waitKey(0)
median=cv2.medianBlur(imagestore1,(3))
cv2.imshow('median blur image',median)
# cv2.waitKey(0)
bilateral=cv2.bilateralFilter(imagestore1,5,50,50)   
cv2.imshow('bilateral filter image',bilateral)
cv2.waitKey(0)  