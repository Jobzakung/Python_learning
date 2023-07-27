import cv2 as cv
import numpy as np

image_path = r'ex4.png'
original_image = cv.imread(image_path)

# Convert the image to grayscale
gray_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)

# Apply thresholding using Otsu's method
thresh = cv.threshold(gray_image, 70, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

# Display the original and thresholded images side by side
cv.imshow('thresh', np.hstack([gray_image, thresh]))
cv.waitKey(0)
cv.destroyAllWindows()
