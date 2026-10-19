import cv2
import os
import numpy as np
imagestore1=cv2.imread(r'C:\Python\Python\open cv\vibrant image1.jpg')
imagestore2=cv2.imread(r'C:\Python\Python\open cv\vibrant image2.jpg')
cv2.imshow('original image',imagestore1)
cv2.waitKey(0)
cv2.imshow('second original image',imagestore2) 
cv2.waitKey(0)
resize1=cv2.resize(imagestore1,(500,500))
cv2.imshow('rezised image of original image',resize1)
cv2.waitKey(0)
resize2=cv2.resize(imagestore2,(500,500))
cv2.imshow('resized image of second original image',resize2)
cv2.waitKey(0)
resultstore=cv2.subtract(resize1,resize2)
cv2.imshow('both images subtracted',resultstore)
cv2.waitKey(0)
storekernal=np.ones((3,3),np.uint8)
erodstore=cv2.erode(resize1,storekernal)
cv2.imshow('eroded version of first oreiginal image',erodstore)
cv2.waitKey(0)
#the eroding is used for bluring the picture