# ArUco Marker Detection and Distance Estimation

## Overview
This repository contains two Python scripts for real-time ArUco marker detection and distance estimation using OpenCV. These scripts utilize a webcam to identify ArUco markers, display their IDs, and estimate their position in 3D space relative to the camera.

### Files
1. **`markerDetection.py`**: Detects ArUco markers in real-time and displays their IDs and corner coordinates.
2. **`distance_estimation.py`**: Detects ArUco markers, estimates their 3D position (distance and orientation) using camera calibration data, and displays this information in real-time.

### Calibration Data
The file `MultiMatrix.npz` contains the camera calibration data:
- **`camMatrix`**: Camera matrix.
- **`distCoef`**: Distortion coefficients.
- **`rVector`**: Rotation vectors.
- **`tVector`**: Translation vectors.

## Installation

### Requirements
- Python 3.7+
- OpenCV (`cv2`)
- NumPy

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/PraharshG/aruco-detection.git
   cd aruco-detection
   ```
2. Install the required Python packages:
   ```bash
   pip install numpy opencv-python
   ```
3. Ensure the `MultiMatrix.npz` file and the scripts are in the same directory.

## Usage

### 1. ArUco Marker Detection
Run `markerDetection.py` to detect and identify ArUco markers in the webcam feed.

```bash
python markerDetection.py
```

- Press `q` to exit the video feed.
- The script will:
  - Detect ArUco markers.
  - Draw bounding boxes around detected markers.
  - Display the marker ID and corner coordinates in the console.

### 2. Distance Estimation
Run `distance_estimation.py` to estimate the distance and position of detected ArUco markers.

```bash
python distance_estimation.py
```

- Press `q` to exit the video feed.
- The script will:
  - Detect ArUco markers.
  - Estimate their 3D position relative to the camera.
  - Display the marker ID, distance, and x/y coordinates on the video feed.

## Example Outputs
### Marker Detection
```text
ID: [23]   [[100, 100], [200, 100], [200, 200], [100, 200]]
```
- A bounding box will be drawn around the marker with its ID displayed.

### Distance Estimation
```text
ID: [42] Dist: 50.3
x: 10.5 y: -5.2
```
- Displays the marker's distance and x/y coordinates on the video feed.

## Customization
### Marker Dictionary
You can change the marker dictionary by modifying this line:
```python
marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)
```
Refer to [OpenCV's ArUco documentation](https://docs.opencv.org/master/d9/d6a/group__aruco.html) for more options.

### Marker Size
Update the `marker_size` variable in `distance_estimation.py` to match the physical size of your markers (in centimeters):
```python
marker_size = 10 # centimeters
```

## Notes
- Ensure the camera is calibrated using OpenCV to generate the `MultiMatrix.npz` file. Use OpenCV's calibration tutorials if needed.
- Lighting conditions and marker quality may affect detection accuracy.


