# # crowd_analysis.py
# import cv2

# def analyze_crowd(image_path):
#     image = cv2.imread(image_path)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Threshold to highlight dense areas
#     _, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)
#     white_pixels = cv2.countNonZero(thresh)
#     total_pixels = image.shape[0] * image.shape[1]

#     density_percentage = (white_pixels / total_pixels) * 100

#     if density_percentage > 20:  # tweak threshold based on your camera/view
#         alert = "High Crowd Density! Possible Risk!"
#     else:
#         alert = "Crowd is Normal."

#     return density_percentage, alert




# crowd_analysis.py
import cv2

def analyze_crowd(image_path):
    # Load image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Threshold to highlight potential people blobs
    _, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours (blobs)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Calculate total area covered by contours
    crowd_area = sum(cv2.contourArea(c) for c in contours)
    total_area = image.shape[0] * image.shape[1]
    
    # Crowd density as percentage of image area
    density = (crowd_area / total_area) * 100
    
    # Alert based on density
    if density > 15:  # Adjust threshold based on testing
        alert = "High Crowd Density! Possible Risk!"
    else:
        alert = "Crowd is Normal."
    
    return density, alert







#crowd_analysis_dl.py
# from ultralytics import YOLO
# import cv2
# import os

# # Load pre-trained YOLOv8 model (nano for speed)
# model = YOLO("yolov8n.pt")  # COCO pre-trained weights

# def analyze_crowd(image_path):
#     """
#     Input: path to image
#     Output: number of people detected, alert message
#     """
#     if not os.path.exists(image_path):
#         return 0, "File not found"

#     frame = cv2.imread(image_path)
#     results = model(frame)  # detect objects

#     count = 0
#     for r in results:
#         boxes = r.boxes
#         for box in boxes:
#             if int(box.cls) == 0:  # class 0 = person
#                 count += 1

#     # Generate alert
#     if count > 15:  # adjust threshold based on your scene
#         alert = "High Crowd Density! Possible Risk!"
#     else:
#         alert = "Crowd is Normal."
    
#     return count, alert

