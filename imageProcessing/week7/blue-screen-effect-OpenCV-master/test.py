import cv2 as cv
import numpy as np

video = cv.VideoCapture(
    "imageProcessing/week7/blue-screen-effect-OpenCV-master/137986 (1080p).mp4")
image = cv.imread(
    "imageProcessing/week7/blue-screen-effect-OpenCV-master/severin-hoin-jkM4W3VnfHg-unsplash.jpg")

while True:
    ret, frame = video.read()

    if not ret:
        break

    frame = cv.resize(frame, (640, 480))
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_green = np.array([55, 165, 170])
    u_green = np.array([179, 255, 255])

    mask = cv.inRange(hsv, l_green, u_green)
    res = cv.bitwise_and(frame, frame, mask=mask)
    f = frame - res
    resized_image = cv.resize(image, (frame.shape[1], frame.shape[0]))

    green_screen = np.where(f == 0, resized_image, f)
    # Invert the mask to select the non-green regions
    mask_inverted = cv.bitwise_not(mask)

    # Create a black background image
    background_frame = np.zeros_like(frame)

    # Combine the filtered frame and the background
    combined_frame = cv.add(res, background_frame)
    cv.imshow("Frame", frame)
    cv.imshow("Mask", mask)
    cv.imshow("Green Screen Effect", combined_frame)
    cv.imshow("f", green_screen)

    # Exit if 'q' key is pressed
    k = cv.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv.destroyAllWindows()
