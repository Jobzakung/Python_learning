import cv2
import numpy as np

A = np.array([[25, 43, 0, 50, 45], [23, 35, 33, 47, 0], [31, 28, 30, 0, 20], [
             42, 37, 29, 39, 41], [108, 5, 31, 104, 48]], dtype=np.float64)
print(A)
kernel = (1.0/9.0)*np.ones((3, 3))
dst = cv2.filter2D(A, -1, kernel)
print(dst)
