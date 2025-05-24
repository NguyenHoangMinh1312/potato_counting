# Potato Counter

A computer vision system that counts potatoes on a conveyor belt using YOLOv11 object detection and tracking.

## Description

This project implements a YOLOv11-based model to automatically detect and count potatoes moving on a conveyor belt. The system uses polygon zone tracking to monitor a specific region and provides real-time counting functionality.

**Reference:** [Ultralytics Object Counting](https://docs.ultralytics.com/guides/object-counting/#what-is-object-counting)

## Getting Started

### Prerequisites

**Operating System:**
- Linux 22.04.5 LTS or higher

**Software Requirements:**
- Python 3.10.12 or higher
- PyTorch 2.6.0 or higher
- TensorFlow 2.19.0 or higher
- OpenCV 4.11.0.86 or higher
- Ultralytics 8.3.111 or higher

### Dataset Setup

1. Download the dataset from [Google Drive](https://drive.google.com/drive/folders/1WJXPd1Pl0kCMWYbJE4h-M6vEEe0S1Fxr)
2. Extract all files to your project directory

### Installation

Install the required dependencies:

```bash
# Install PyTorch
pip install torch

# Install TensorFlow
pip install tensorflow

# Install OpenCV
pip install opencv-python

# Install Ultralytics
pip install ultralytics
```

## Training the Model

1. **Prepare the dataset:**
   ```bash
   python dataset.py
   ```
   *Note: Review and adjust parameters in `dataset.py` before running*

2. **Train the model:**
   ```bash
   python train.py
   ```
   *Note: Review and adjust parameters in `train.py` before running*

## Running the Application

### Important Notes
- This model is designed for **static camera angles only**
- Ensure your camera setup remains fixed during operation

### Setup Steps

1. **Define the tracking region:**
   - Extract a representative frame from your video
   - Visit [Roboflow PolygonZone](https://polygonzone.roboflow.com/)
   - Upload your frame
   - Select `Polygon` mode
   - Draw the tracking region boundary
   - Copy the coordinate list (not the NumPy array)
   - Paste the coordinates into the `region_points` variable in `main.py`

2. **Configure the model path:**
   - Update the model path in `main.py` to point to your trained model
   - Verify the path is correct before execution

3. **Run the application:**
   ```bash
   python main.py
   ```

## Project Structure

```
potato-counter/
├── dataset.py          # Dataset preparation script
├── train.py           # Model training script
├── main.py            # Main application
├── requirements.txt   # Dependencies (if available)
└── README.md         # This file
```

## Troubleshooting

- Ensure all file paths are correctly configured
- Verify your camera feed is stable and properly positioned
- Check that the polygon region covers the desired tracking area
- Confirm model weights are accessible at the specified path

## Demo
[Demo video](./object_counting_output.avi)