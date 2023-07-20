import cv2
import numpy as np
path = r'j.png'

# using imread()  
img=cv2.imread(path)
kernel = np.ones((5,5),np.uint8)
kernel7 = np.ones((7,7),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
erosion7 = cv2.erode(img,kernel7,iterations = 1)
cv2.imshow('Laplacian', np.hstack((img, erosion, erosion7)))
cv2.waitKey(0);
cv2.destroyAllWindows();
