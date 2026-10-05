import cv2
imagestore=cv2.imread(r'C:\Python\Python\open cv\flower.jpg')
cv2.imshow('original.image',imagestore)
cv2.waitKey(0)
grayimage=cv2.imread(r'C:\Python\Python\open cv\flower.jpg',0)
cv2.imshow('gray ',grayimage)
cv2.waitKey(0)