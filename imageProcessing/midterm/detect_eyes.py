import cv2

#haar cascade link from folder
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

# Load the video file
video_capture = cv2.VideoCapture('week5/video/Video.mp4')

while True:
    ret, frame = video_capture.read()

    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(
        #ปรับค่าให้เหมาะสมกับภาพ
        gray_frame, scaleFactor=1.3, minNeighbors=4, minSize=(15, 15))

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()


# 'haarcascade_frontalface_default.xml': Frontal face detection.
# 'haarcascade_frontalface_alt.xml': Alternative frontal face detection.
# 'haarcascade_frontalface_alt2.xml': Another alternative frontal face detection.
# 'haarcascade_profileface.xml': Profile (side) face detection.
# Haar Cascade for Eye Detection:

# 'haarcascade_eye.xml': Eye detection.
# 'haarcascade_eye_tree_eyeglasses.xml': Eye detection designed for eyeglasses.
# Haar Cascade for Upper Body Detection:

# 'haarcascade_upperbody.xml': Upper body detection (including shoulders and upper chest).
# Haar Cascade for Lower Body Detection:

# 'haarcascade_lowerbody.xml': Lower body detection (including hips and legs).
# Haar Cascade for Full Body Detection:

# 'haarcascade_fullbody.xml': Full body detection.
# Haar Cascade for Smile Detection:

# 'haarcascade_smile.xml': Smile detection (typically used in conjunction with face detection).
# Haar Cascade for Cat Face Detection:

# 'haarcascade_frontalcatface.xml': Frontal cat face detection.
# Haar Cascade for License Plate Detection:

# 'haarcascade_russian_plate_number.xml': Russian license plate number 