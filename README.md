# New-AI-and-ML-Project-Vityarthi
Project Overview
This project uses the YOLOv8 deep learning model to detect objects in a given image. It processes the entire image in one pass, making detection extremely fast.

 Project Title
AI Object Detection Using YOLOv8

 Overview of the Project
This project demonstrates how an AI model (YOLOv8) can detect multiple objects in an image with high speed and accuracy. It loads a pre-trained YOLO model and performs inference on any input image. The output shows bounding boxes, object labels, and confidence scores.

 Features
•	High speed object detection
•	Detects multiple objects in one image
•	Uses YOLOv8 (latest YOLO model)
•	Easy to run and modify
•	Beginner friendly code
•	Prints detected object names with confidence scores
•	Works with any image format (JPG, PNG, etc.)

Technologies / Tools Used
•	Python
•	Ultralytics YOLOv8 (deep learning model)
•	OpenCV (for image processing)
•	NumPy (internally used by OpenCV)
•	Pretrained YOLO weights (yolov8n.pt)

 Steps to Install & Run the Project
1. Install Dependencies
pip install ultralytics
pip install opencv-python
2. Download YOLOv8 Model
This is automatic — the model downloads the first time the script runs.
3. Place Your Image
Add your test image to the project folder. Example:
test.jpg
4. Run the Script
python object_detect.py

 Instructions for Testing
1.	Use a clear image containing objects like people, cars, animals, etc.
2.	Update image_path in the script:
image_path = "test.jpg"
3.	Run the code — a new window will pop up showing:
o	Bounding boxes
o	Object labels
o	Detection confidence
4.	Check the terminal — it prints all detected objects.
5.	Try with different images to see accuracy.
6.	For best results, use high quality images with clear lighting.

 Existing Content 
This project demonstrates object detection using YOLOv8 (You Only Look Once), one of the fastest and most accurate object detection algorithms. It identifies multiple objects in an image and displays bounding boxes with labels.
This version performs image-only detection 

 What is YOLO?
YOLO (You Only Look Once) is a deep learning algorithm used to detect objects in images and videos. It processes the entire image in a single pass, making it extremely fast and ideal for real-time applications.
YOLO can detect objects like:
•	Person
•	Car
•	Dog
•	Bicycle
•	Bottle
•	Many more...

Technologies Used
•	Python
•	Ultralytics YOLOv8
•	OpenCV
•	Deep Learning (CNN-based)


Installation
Run the following commands:
pip install ultralytics
pip install opencv-python

How to Run the Program
1.	Place your image in the project folder (example name: test.jpg).
2.	Run the script:
python object_detect.py
3.	A window will open showing:
•	Detected objects
•	Labels (e.g., person, car)
•	Confidence scores

Code (Image-Only Object Detection)
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

print("YOLO Model Loaded Successfully!")

image_path = "test.jpg”

image = cv2.imread(image_path)

results = model(image, show=True)

for r in results:
for box in r.boxes:
cls = int(box.cls[0]) 
confidence = float(box.conf[0]) 
label = model.names[cls] 
print(f"Detected: {label} ({confidence:.2f})")

cv2.waitKey(0)
cv2.destroyAllWindows()

 Output Example
•	Bounding boxes drawn around detected objects
•	Labels such as person, car, dog, etc.
•	Confidence score for each detection
Applications
•	Self-driving cars
•	CCTV surveillance
•	Robotics
•	Traffic analysis
•	Smart security systems
________________________________________
