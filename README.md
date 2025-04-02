# Turn your PC into Security Cam

## Overview
This project implements a **face detection and capture system** using OpenCV. It uses a webcam to detect human faces in real-time, overlays a timestamp, and saves the captured images into a specified folder. This can be useful for dataset creation, attendance systems, and face recognition pipelines.

## Features
- Real-time face detection using Haar cascades.
- Saves face-detected images with a timestamp overlay.
- Automatically stops after a set number of captures or time duration.

## How It Works
1. The webcam is initialized using OpenCV.
2. A Haar Cascade Classifier detects faces in grayscale video frames.
3. If a face is detected:
   - A rectangle is drawn around the face.
   - A timestamp is overlaid on the image.
   - The frame is saved to the specified output directory.
4. The program stops when either:
   - A set number of images are captured (`max_samples`)
   - The capture duration exceeds a time limit (`capture_duration`)
   - The user presses **'q'** to quit.

## Usage
### Requirements
- Webcam-enabled device
- Haar cascade XML file: `haarcascade_frontalface_default.xml`

## Output
- Captured images are saved in the `F:\computer_vision\` directory.
- Each image includes the detected face and timestamp.

## Applications
- Face dataset creation
- Surveillance
- Attendance systems
- Preprocessing for face recognition
