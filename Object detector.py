from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("yolov8n.pt")   

print("YOLO Model Loaded Successfully!")

# ----- IMAGE DETECTION -----
image_path = "test.jpg"   

# Read image
image = cv2.imread(image_path)

# Run YOLO on image
results = model(image, show=True)

# Print detected objects
for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])          # class ID
        confidence = float(box.conf[0]) # confidence score
        label = model.names[cls]        # class name
        print(f"Detected: {label} ({confidence:.2f})")

# Wait so the window stays open
cv2.waitKey(0)
cv2.destroyAllWindows()
