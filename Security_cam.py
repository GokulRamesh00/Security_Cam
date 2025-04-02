import cv2
import os
import time
from datetime import datetime

# Setup
output_dir = "F:\\computer_vision\\"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Configuration
Id = "pic"
sampleNum = 0
max_samples = 10           # Number of images to save
capture_duration = 30      # Total capture time in seconds

print(f"Starting face capture for {capture_duration} seconds or until {max_samples} samples are collected...")
start_time = time.time()

while True:
    ret, img = cam.read()
    if not ret:
        print("Failed to grab frame.")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Put timestamp on image
    cv2.putText(img, timestamp, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # Show the live video with rectangle and timestamp
    cv2.imshow('Face Capture', img)

    # Save image with rectangle and timestamp
    sampleNum += 1
    filename = os.path.join(output_dir, f"{Id}.{sampleNum}.jpg")
    cv2.imwrite(filename, img)
    print(f"[{sampleNum}] Image saved: {filename}")

    # Exit conditions
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Capture interrupted by user.")
        break

    if sampleNum >= max_samples or (time.time() - start_time) > capture_duration:
        print("Capture complete.")
        break

# Cleanup
cam.release()
cv2.destroyAllWindows()
