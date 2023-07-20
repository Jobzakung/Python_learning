import cv2
import numpy as np
path = r'Fig0907.tif'

# using imread()  
img=cv2.imread(path)
# kernel = np.ones((3,3),np.uint8)
kernel = np.array([[0,1,0],[1,0,1],[0,1,0]],dtype=np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow('dilate', np.hstack((img,dilation)))
cv2.waitKey(0);
cv2.destroyAllWindows();
