import cv2
import numpy as np

# image path
path = r'Fig0334.tif'

# using imread()
imgage = cv2.imread(path)
# path = r'Fig0334.tif'
# img2 = cv2.imread(path)
image_2 = cv2.blur(imgage, (15, 15))
ret, thresh = cv2.threshold(image_2, 70, 255, cv2.THRESH_BINARY)
# im2 = cv2.boxFilter(img, -1, (15, 15), normalize=True)
# im3 = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("testing", np.hstack((imgage, image_2, thresh)))
# cv2.imshow('blur filter', np.hstack((img, image_2, im2)))
# cv2.imshow('median filter', np.hstack((img2, im3)))
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
