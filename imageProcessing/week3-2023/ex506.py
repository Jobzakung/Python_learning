import cv2
import numpy as np
path = r'week3-2023/jn.png'

# using imread()  
img=cv2.imread(path)
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('Laplacian', np.hstack((img,opening)))
cv2.waitKey(0);
cv2.destroyAllWindows();