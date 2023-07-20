import cv2
import numpy as np
path = r'j.png'

# using imread()  
img=cv2.imread(path)
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow('Laplacian', np.hstack((img,dilation)))
cv2.waitKey(0);
cv2.destroyAllWindows();
