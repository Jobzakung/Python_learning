import cv2
import numpy as np

# image path 
path = r'Fig0338.tif'

# using imread()  
img = cv2.imread(path)
dst = cv2.Laplacian(img, -1, ksize=3)
im2=img+dst
cv2.imshow('Laplacian', np.hstack((img, dst,im2)))
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.waitKey(1)  
