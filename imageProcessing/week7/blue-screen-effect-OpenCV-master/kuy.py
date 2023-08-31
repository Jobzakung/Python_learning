import cv2
import numpy as np
import matplotlib.pyplot as plt


# Load the video
video = cv2.VideoCapture("imageProcessing/week7/blue-screen-effect-OpenCV-master/137986 (1080p).mp4")
background_image = cv2.imread("imageProcessing/week7/blue-screen-effect-OpenCV-master/severin-hoin-jkM4W3VnfHg-unsplash.jpg")

# Define the color to remove (RGB color [6, 247, 41])
color_to_remove = np.array([0, 133, 198])

# Define a tolerance for color matching (you can adjust this based on your needs)
color_tolerance = np.array([179, 255, 255])


while True:
    ret, frame = video.read()

    if not ret:
        break

    # Calculate the lower and upper bounds of the color with tolerance
    lower_bound = color_to_remove - color_tolerance
    upper_bound = color_to_remove + color_tolerance

    # Create a mask for the pixels within the specified color range
    mask = cv2.inRange(frame, lower_bound, upper_bound)

    # Invert the mask to identify pixels outside the specified color range
    mask_inverted = cv2.bitwise_not(mask)

    # Create a new frame where the specified color is removed
    removed_color_frame = cv2.bitwise_and(frame, frame, mask=mask_inverted)

    # Resize the background image to match the frame size
    resized_background = cv2.resize(background_image, (frame.shape[1], frame.shape[0]))


    # Combine the removed color frame and the background
    combined_frame = cv2.add(removed_color_frame, resized_background)

    # Display the resulting frame
    cv2.imshow("Green Screen Effect", combined_frame)

    # Exit if 'Esc' key is pressed
    if cv2.waitKey(25) == 27:
        break

video.release()
cv2.destroyAllWindows()
