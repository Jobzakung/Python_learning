import cv2

FACE_CASCADE_PATH = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
EYE_CASCADE_PATH = cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml'
VIDEO_PATH = 'week5/video/Video.mp4'

FACE_SCALE_FACTOR = 1.1
FACE_MIN_NEIGHBORS = 5
FACE_MIN_SIZE = (30, 30)
EYE_SCALE_FACTOR = 1.3
EYE_MIN_NEIGHBORS = 4
EYE_MIN_SIZE = (15, 15)

face_cascade = cv2.CascadeClassifier(FACE_CASCADE_PATH)
eye_cascade = cv2.CascadeClassifier(EYE_CASCADE_PATH)

video_capture = cv2.VideoCapture(VIDEO_PATH)

while True:
    ret, frame = video_capture.read()

    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray_frame, scaleFactor=FACE_SCALE_FACTOR,
        minNeighbors=FACE_MIN_NEIGHBORS, minSize=FACE_MIN_SIZE)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray_frame[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(
            roi_gray, scaleFactor=EYE_SCALE_FACTOR,
            minNeighbors=EYE_MIN_NEIGHBORS, minSize=EYE_MIN_SIZE)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
