import cv2
import numpy as np
path = r'jc.png'

# using imread()  
img=cv2.imread(path)
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Laplacian', np.hstack((img,closing)))
cv2.waitKey(0);
cv2.destroyAllWindows();