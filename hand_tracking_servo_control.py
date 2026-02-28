import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import serial
import time
import os

# -------------------------
# Serial setup
# -------------------------
SERIAL_PORT = 'COM3'
BAUD_RATE = 115200
print(f"Connecting to {SERIAL_PORT}...")
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)

# -------------------------
# MediaPipe HandLandmarker
# -------------------------
MODEL_PATH = "hand_landmarker.task"
if not os.path.exists(MODEL_PATH):
    print("Model not found!")
    exit()

base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.HandLandmarkerOptions(base_options=base_options)
landmarker = vision.HandLandmarker.create_from_options(options)

# -------------------------
# Finger tips and PIP mapping
# -------------------------
FINGERTIPS = [16, 4, 8, 12, 20]
PIP_JOINTS = [15, 3, 7, 11, 19]

THUMB_THRESHOLD = 0.01  # adjust threshold if thumb is too sensitive

print("Running... Press ESC to quit")

# -------------------------
# Webcam loop
# -------------------------
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    result = landmarker.detect(mp_image)

    if result.hand_landmarks:
        hand = result.hand_landmarks[0]

        # generate binary open/closed for each finger
        binary_list = []
        for i, (tip, pip) in enumerate(zip(FINGERTIPS, PIP_JOINTS)):
            y_diff = hand[pip].y - hand[tip].y
            # channel 1 uses threshold
            if i == 1:
                if y_diff > THUMB_THRESHOLD:
                    binary_list.append("0")  # closed
                else:
                    binary_list.append("1")  # open
            else:
                if hand[tip].y < hand[pip].y:
                    binary_list.append("1")
                else:
                    binary_list.append("0")

        # -------------------------
        # Fix thumb sweep (channel 0) mirrors thumb up/down
        # -------------------------
        binary_list[0] = binary_list[1]

        # combine ring+pinky (channel 4)
        if binary_list[4] == "1" or binary_list[4] == "1":
            binary_list[4] = "1"
        else:
            binary_list[4] = "0"

        # send packet
        final_packet = "".join(binary_list) + "\n"
        ser.write(final_packet.encode())
        print("Sent:", final_packet.strip())

        # show on screen
        cv2.putText(frame, final_packet.strip(), (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Hand Tracking", frame)
    if cv2.waitKey(1) == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
ser.close()