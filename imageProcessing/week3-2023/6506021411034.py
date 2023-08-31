import cv2
import numpy as np

image_path = r'week3-2023/note.png'
original_image = cv2.imread(image_path)

image = cv2.imread(image_path)
# cv2.imshow('source_image', image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 1))
detected_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN,
                                  horizontal_kernel, iterations=2)

cnts = cv2.findContours(
    detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

for c in cnts:
    cv2.drawContours(image, [c], -1, (255, 255, 255), 2)

repair_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 6))

result = 255 - cv2.morphologyEx(255 - image, cv2.MORPH_CLOSE, repair_kernel,
                                iterations=1)

cv2.imshow('resultant image', np.hstack([original_image, result]))
cv2.waitKey()
cv2.destroyAllWindows()
