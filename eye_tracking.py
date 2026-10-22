import cv2

cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

face_detector = cv2.CascadeClassifier(cascade_path)

if face_detector.empty():
    raise Exception(f"Could not load Haar Cascade from: {cascade_path}")


def eye_contact(frame):

    if frame is None:
        return 0

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(80, 80)
    )

    if len(faces) == 0:
        return 0

    h, w = frame.shape[:2]

    x, y, fw, fh = faces[0]

    face_center_x = x + fw // 2
    face_center_y = y + fh // 2

    frame_center_x = w // 2
    frame_center_y = h // 2

    dx = abs(face_center_x - frame_center_x)
    dy = abs(face_center_y - frame_center_y)

    if dx < 60 and dy < 60:
        return 100
    elif dx < 120 and dy < 120:
        return 85
    elif dx < 180 and dy < 180:
        return 70
    else:
        return 40