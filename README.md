# 🎥 Real-Time Attendance Automation using Computer Vision

## Overview
This project is a real-time employee attendance monitoring system that uses computer vision to automatically detect and record employee entry and exit times. The system processes live video feeds and compares detected faces with preloaded employee images stored in the backend.

By automating attendance tracking, the system reduces manual intervention and improves efficiency in employee monitoring.

---

## Problem Statement
Traditional attendance systems rely on manual entry or biometric systems, which can be time-consuming and prone to misuse. This project aims to automate attendance tracking using computer vision to ensure reliable and accurate employee monitoring.

---

## Key Features
- Real-time face detection and recognition using live video feeds
- Image similarity comparison with stored employee images
- Automated entry and exit time recording
- Daily consolidated attendance report generation
- Scheduled execution for continuous system operation
- Reduced manual attendance processing by **75%**

---

## System Performance
- Achieved **~90% accuracy** in image similarity checks
- Real-time monitoring and detection
- Reliable tracking of employee entry and exit between **00:00 – 23:55**

---

## Technologies Used
- **Python**
- **OpenCV**
- **Convolutional Neural Networks (CNN)**
- **NumPy**
- **Windows Task Scheduler**

---

## Project Workflow
1. Live video feed captures employee images.
2. Captured images are compared with **preloaded supervised images** stored in the backend.
3. Image similarity checks determine employee identity.
4. Entry and exit times are recorded automatically.
5. At the end of the day, the system generates a **consolidated attendance report**.

---

## Running the Project

### Step 1: Install Dependencies
```bash
pip install opencv-python numpy
```

### Step 2: Run Attendance Monitoring
```bash
python attendance.py
```

This script runs continuously and tracks employee attendance throughout the day.

---

## Scheduling Automation

To automate execution, use **Windows Task Scheduler**.

### Schedule Configuration

| Script | Time |
|------|------|
| `attendance.py` | 00:00 – 23:55 |
| `consolidated_attendance.py` | 23:55 |

This ensures:
- Continuous monitoring throughout the day
- Automatic generation of daily attendance reports

---

## Applications
- Office employee attendance systems
- Secure workplace monitoring
- Automated workforce management
- Smart workplace solutions

---

## Future Improvements
- Deploy the system as a web-based application
- Integrate cloud storage for attendance records
- Improve facial recognition accuracy using larger datasets
- Add real-time dashboard for attendance monitoring

---

## Author

**Abhishek Singaravel**  
Backend Developer | AI Enthusiast

- LinkedIn: https://linkedin.com/in/abhishek-singaravel-698b35250
- GitHub: https://github.com/AbhishekSingaravel
