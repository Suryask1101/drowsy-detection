import cv2
import os
import time
import winsound  # For Windows alert sound

# Get the absolute path of the current directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load Haar cascade models with correct paths
face_cascade_path = os.path.join(base_dir, "models", "haarcascade_frontalface_default.xml")
eye_cascade_path = os.path.join(base_dir, "models", "haarcascade_eye.xml")

# Check if Haar cascade files exist
if not os.path.exists(face_cascade_path) or not os.path.exists(eye_cascade_path):
    print("❌ Error: Haar cascade XML files not found in 'models/' directory.")
    exit(1)

# Load the cascade classifiers
face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

# Check if classifiers loaded correctly
if face_cascade.empty() or eye_cascade.empty():
    print("❌ Error loading Haar cascades. Check file paths!")
    exit(1)

# Create screenshots directory if not exists
screenshot_dir = os.path.join(base_dir, "screenshots")
os.makedirs(screenshot_dir, exist_ok=True)

# Open webcam
cap = cv2.VideoCapture(0)

sleep_frame_count = 0  # Track consecutive frames without eyes

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Error: Could not read frame from webcam.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)

        if len(eyes) == 0:
            sleep_frame_count += 1
        else:
            sleep_frame_count = 0  # Reset if eyes are detected

        # If eyes are closed for a certain number of frames, play alert sound and take screenshot
        if sleep_frame_count >= 10:
            print("⚠️ Sleep detected! Playing alert sound and taking screenshot.")

            # Play beep sound
            winsound.Beep(1000, 500)  # Frequency: 1000 Hz, Duration: 500 ms

            # Save screenshot
            screenshot_path = os.path.join(screenshot_dir, f"screenshot_{int(time.time())}.png")
            cv2.imwrite(screenshot_path, frame)
            print(f"📸 Screenshot saved: {screenshot_path}")

            sleep_frame_count = 0  # Reset counter after alert

        # Draw rectangles around faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Sleep Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
