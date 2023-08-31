import cv2
import numpy as np

# Load the image
image = cv2.imread('midterm/coin2.jpeg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise and improve circle detection
blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# Detect circles using Hough Circle Transform
circles = cv2.HoughCircles(
    blurred,
    cv2.HOUGH_GRADIENT,
    #ปรับค่าให้เหมาะสมกับภาพ
    dp=1,  # Inverse ratio of the accumulator resolution
    minDist=100,  # Minimum distance between the centers of the detected circles
    param1=100,  # Upper threshold for the internal Canny edge detector
    param2=30,   # Threshold for circle center detection
    minRadius=20,  # Minimum radius of circles to be detected
    maxRadius=100   # Maximum radius of circles to be detected
)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        center = (circle[0], circle[1])
        radius = circle[2]
        
        # Draw the circle and center
        cv2.circle(image, center, radius, (0, 255, 0), 2)
        cv2.circle(image, center, 2, (0, 0, 255), 3)

# Display the result
cv2.imshow('Detected Circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
