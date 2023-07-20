import cv2
import numpy as np

# image path 
path = r'Fig0333.tif'

# using imread()  
img = cv2.imread(path)
path = r'Fig0335.tif'
img2 = cv2.imread(path)
im1 = cv2.blur(img,(5,5))
im2 = cv2.boxFilter(img, -1, (15, 15), normalize=True)  
im3 = cv2.medianBlur(img2,5)
cv2.imshow('blur filter', np.hstack((img,im1, im2)))
cv2.imshow('median filter', np.hstack((img2,im3)))
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.waitKey(1)  
