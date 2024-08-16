import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Load YOLOv5 small model
import cv2

cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the frame
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
    results = model(img)  # Run frame through the YOLO model

    # Draw bounding boxes and labels on the original frame
    results.render()  # YOLO's render method draws the detections on the frame

    # Display the frame with detections
    cv2.imshow('Object Detection', results.ims[0])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


