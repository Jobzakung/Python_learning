import cv2

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
