import os
import cv2
import torch

# Define base path and use forward slashes
base_path = ''
yolov5_path = f'{base_path}/yolov5'
dataset_path = f'{base_path}/dataset'
data_yaml_path = 'data.yaml'


# Print paths for debugging
print(f"YOLOv5 Path: {yolov5_path}")
print(f"Data YAML Path: {data_yaml_path}")
print(f"Training Command Path: {yolov5_path}/train.py")
print(f"Model Config Path: {yolov5_path}/models/yolov5s.yaml")
print(f"Pretrained Weights Path: {yolov5_path}/yolov5s-seg.pt")

# Train the model
train_command = f"python {yolov5_path}/train.py --img 640 --batch 16 --epochs 50 --data {data_yaml_path} --cfg {yolov5_path}/models/yolov5s.yaml --weights {yolov5_path}/yolov5s-seg.pt --name my_yolov5_model"
print(f"Running training command: {train_command}")
os.system(train_command)

# Verify the directory structure
runs_dir = f'{yolov5_path}/runs'
print(f"Checking if 'runs' directory exists: {runs_dir}")
if not os.path.exists(runs_dir):
    print(f"'runs' directory not found. Check if training started successfully.")

train_dir = f'{yolov5_path}/runs/train/my_yolov5_model/weights'
print(f"Checking if weights directory exists: {train_dir}")
if not os.path.exists(train_dir):
    print(f"Weights directory not found: {train_dir}")
else:
    weights_path = f'{train_dir}/best.pt'
    print(f"Checking if weights file exists: {weights_path}")
    if not os.path.exists(weights_path):
        print(f"Weights file not found: {weights_path}")
    else:
        print(f"Weights file found at: {weights_path}")

        # Validate the model
        val_command = f"python {yolov5_path}/val.py --data {data_yaml_path} --weights {weights_path} --img 640"
        print(f"Running validation command: {val_command}")
        os.system(val_command)

        # Test the model
        test_command = f"python {yolov5_path}/detect.py --weights {weights_path} --img 640 --source {dataset_path}/test"
        print(f"Running test command: {test_command}")
        os.system(test_command)

        # Real-Time Object Detection with Camera
        print(f"Loading model with weights: {weights_path}")
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path, force_reload=True)

        # Open the webcam
        print("Opening webcam...")
        cap = cv2.VideoCapture(0)  # 0 is the default camera

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Perform object detection
            results = model(frame)

            # Render the results
            frame = results.render()[0]

            # Display the frame
            cv2.imshow('YOLOv5 Live', frame)

            # Exit on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the webcam and close windows
        cap.release()
        cv2.destroyAllWindows()
