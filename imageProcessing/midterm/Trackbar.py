import cv2 as cv
import numpy as np

video = cv.VideoCapture("imageProcessing/week7/blue-screen-effect-OpenCV-master/137986 (1080p).mp4")
image = cv.imread("imageProcessing/week7/blue-screen-effect-OpenCV-master/severin-hoin-jkM4W3VnfHg-unsplash.jpg")

cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars", 300, 300)

cv.createTrackbar(" L - H ", "Trackbars", 0, 255, lambda x: None)
cv.createTrackbar(" L - S ", "Trackbars", 0, 255, lambda x: None)
cv.createTrackbar(" L - V ", "Trackbars", 0, 255, lambda x: None)
cv.createTrackbar(" U - H ", "Trackbars", 220, 255, lambda x: None)
cv.createTrackbar(" U - S ", "Trackbars", 255, 255, lambda x: None)
cv.createTrackbar(" U - V ", "Trackbars", 255, 255, lambda x: None)

while True:
    ret, frame = video.read()

    if not ret:
        break

    frame = cv.resize(frame, (640, 480))
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    l_h = cv.getTrackbarPos(" L - H ", "Trackbars")
    l_s = cv.getTrackbarPos(" L - S ", "Trackbars")
    l_v = cv.getTrackbarPos(" L - V ", "Trackbars")
    u_h = cv.getTrackbarPos(" U - H ", "Trackbars")
    u_s = cv.getTrackbarPos(" U - S ", "Trackbars")
    u_v = cv.getTrackbarPos(" U - V ", "Trackbars")
    
    l_green = np.array([l_h, l_s, l_v])
    u_green = np.array([u_h, u_s, u_v])
    
    mask = cv.inRange(hsv, l_green, u_green)
    res = cv.bitwise_and(frame, frame, mask=mask)
    
    # Invert the mask to select the non-green regions
    mask_inverted = cv.bitwise_not(mask)
    
    # Create a black background image
    background_frame = np.zeros_like(frame)
    
    # Combine the filtered frame and the background
    combined_frame = cv.add(res, background_frame)
    
    cv.imshow("Green Screen Effect", combined_frame)
    
    # Exit if 'q' key is pressed
    k = cv.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv.destroyAllWindows()
