import cv2
import numpy as np
def load_face_encoding(img_path):
    img = cv2.imread(img_path, 0)
    return cv2.resize(img, (100, 100)).flatten()
# Load reference face (grayscale)
ref_encoding = load_face_encoding("known_face.jpg")  # Provide a known face image
# Webcam
cap = cv2.VideoCapture(0)
print("Looking for a match... Press 'q' to quit.")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        face_resized = cv2.resize(face_roi, (100, 100)).flatten()
        # Simple comparison: Euclidean distance
        distance = np.linalg.norm(ref_encoding - face_resized)
        label = "Unknown"
        if distance < 2000:  # Threshold (tweak as needed)
            label = "Matched!"
        # Draw box and label
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, label, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
