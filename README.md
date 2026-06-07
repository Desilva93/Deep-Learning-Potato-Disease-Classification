 # 🥔 Potato Disease Classification Using Deep Learning

## Overview

Potato diseases can significantly reduce crop yield and quality if not detected early. This project presents an end-to-end Deep Learning solution for automatic potato leaf disease detection using Convolutional Neural Networks (CNNs).

The model classifies potato leaf images into three categories:

* Healthy
* Early Blight
* Late Blight

The system enables farmers and agricultural professionals to quickly identify diseases from leaf images, allowing timely intervention and improved crop management.

---

## Problem Statement

Manual disease identification requires agricultural expertise and can be time-consuming. Misdiagnosis can lead to crop loss and reduced productivity.

This project automates disease detection using Computer Vision and Deep Learning techniques to provide fast and accurate predictions from leaf images.

---

## Dataset

The dataset consists of potato leaf images categorized into:

1. Healthy
2. Early Blight
3. Late Blight

Each image is preprocessed and resized before being used for model training.

---

## Project Architecture

```text
Potato Leaf Images
        │
        ▼
 Data Preprocessing
        │
        ▼
 Data Augmentation
        │
        ▼
 CNN Model Training
        │
        ▼
 Model Evaluation
        │
        ▼
 Saved TensorFlow Model
        │
        ▼
 TensorFlow Serving
        │
        ▼
 FastAPI Backend
        │
        ▼
 React Frontend
        │
        ▼
 Disease Prediction
```

---

## Features

✅ Automatic potato disease detection

✅ Deep Learning-based image classification

✅ REST API for model inference

✅ TensorFlow Serving deployment

✅ React-based user interface

✅ Real-time disease prediction

✅ End-to-end production-ready architecture

---

## Tech Stack

### Machine Learning

* Python
* TensorFlow
* Keras
* NumPy
* Matplotlib

### Backend

* FastAPI
* TensorFlow Serving
* Docker

### Frontend

* React.js

### Deployment

* Google Cloud Platform (GCP)
* Docker Containers

---

## Model Training Pipeline

### 1. Data Collection

Potato leaf images are collected and organized into disease categories.

### 2. Data Preprocessing

* Image resizing
* Normalization
* Dataset splitting
* Label encoding

### 3. Data Augmentation

To improve model generalization:

* Rotation
* Horizontal flipping
* Zooming
* Translation

### 4. CNN Model Training

A Convolutional Neural Network is trained to learn disease-specific visual patterns from leaf images.

### 5. Evaluation

Model performance is evaluated using validation and test datasets.

### 6. Deployment

The trained model is exported and served using TensorFlow Serving and FastAPI APIs.

---

## Folder Structure

```text
potato-disease-classification/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│
├── models/
│   ├── saved_model/
│
├── notebooks/
│   ├── training.ipynb
│
├── screenshots/
│
├── README.md
│
└── requirements.txt
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/potato-disease-classification.git

cd potato-disease-classification
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
uvicorn main:app --reload
```

Backend API will be available at:

```text
http://localhost:8000
```

---

## Run Frontend

```bash
cd frontend

npm install

npm start
```

Frontend will be available at:

```text
http://localhost:3000
```

---

## API Workflow

1. User uploads potato leaf image.
2. Frontend sends image to FastAPI server.
3. FastAPI forwards image to TensorFlow model.
4. Model predicts disease category.
5. Prediction is returned to frontend.
6. Result is displayed to user.

---

## Results

The CNN model successfully classifies potato leaf diseases into:

* Healthy
* Early Blight
* Late Blight

The trained model demonstrates strong performance and can be integrated into real-world agricultural monitoring systems.

---

## Screenshots

### Application Interface

Add screenshots here:

```text
screenshots/homepage.png
screenshots/prediction.png
screenshots/results.png
```

---

## Future Improvements

* Mobile application deployment
* Multi-crop disease detection
* Explainable AI visualizations (Grad-CAM)
* Cloud-based prediction service
* Real-time field monitoring

---

## Skills Demonstrated

* Deep Learning
* Computer Vision
* CNN Architecture Design
* TensorFlow & Keras
* FastAPI
* REST API Development
* TensorFlow Serving
* React.js
* Docker
* Cloud Deployment

---

## Learning Outcomes

Through this project, I gained hands-on experience in building an end-to-end Deep Learning application involving model training, API development, frontend integration, and deployment workflows.

---

## Author

Desilva Roy

M.Tech – Artificial Intelligence

Indian Institute of Science (IISc), Bangalore

