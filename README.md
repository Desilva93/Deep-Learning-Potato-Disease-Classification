# 🥔 Deep Learning Potato Disease Classification

A Deep Learning based Potato Disease Classification system that identifies potato leaf diseases from images.

The model classifies potato leaves into:

- Healthy
- Early Blight
- Late Blight

This project includes model training, REST API deployment, React frontend, TensorFlow Lite conversion, mobile application support, and Google Cloud deployment.

---

# Project Architecture

Image → Deep Learning Model → Prediction → API → Frontend / Mobile App

---

# Project Structure

```text
Deep-Learning-Potato-Disease-Classification
│
├── Dataset/
│   └── Potato leaf image dataset
│
├── api/
│   └── FastAPI backend
│
├── frontend/
│   └── ReactJS web application
│
├── gcp/
│   └── Google Cloud deployment scripts
│
├── mobile-app/
│   └── React Native mobile application
│
├── models/
│   └── TensorFlow SavedModel
│
├── tf-lite-models/
│   └── TensorFlow Lite models
│
├── test_images_from_internet/
│   └── Sample test images
│
├── Training.ipynb
│   └── Model training notebook
│
├── export_model.py
│   └── SavedModel export script
│
├── model_potatoes.h5
│   └── Trained CNN model
│
├── requirements.txt
│
└── README.md
```

---

# Dataset

The model is trained on potato leaf images containing:

- Healthy
- Early Blight
- Late Blight

Dataset images are stored inside the `Dataset` folder.

---

# Technologies Used

- Python
- TensorFlow
- Keras
- FastAPI
- ReactJS
- React Native
- Google Cloud Platform (GCP)
- TensorFlow Lite
- Docker

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Desilva93/Deep-Learning-Potato-Disease-Classification.git

cd Deep-Learning-Potato-Disease-Classification
```

---

## Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Model Training

Open Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
Training.ipynb
```

Run all notebook cells sequentially to:

- Load Dataset
- Preprocess Images
- Train CNN Model
- Evaluate Performance
- Save Trained Model

---

# Export Model

Run:

```bash
python export_model.py
```

This exports the trained model to the `models` folder.

---

# Run FastAPI Backend

Navigate to API folder:

```bash
cd api
```

Start server:

```bash
uvicorn main:app --reload
```

Backend will run at:

```text
http://localhost:8000
```

---

# Run Frontend

Open new terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run application:

```bash
npm start
```

Frontend will run at:

```text
http://localhost:3000
```

---

# Run Mobile Application

Navigate to:

```bash
cd mobile-app
```

Install dependencies:

```bash
yarn install
```

For macOS:

```bash
cd ios
pod install
cd ..
```

Run application:

```bash
npm run ios
```

or

```bash
npm run android
```

---

# TensorFlow Lite Conversion

TensorFlow Lite models are stored inside:

```text
tf-lite-models/
```

These models can be used on mobile and edge devices.

---

# Testing

Sample images are available in:

```text
test_images_from_internet/
```

Use these images to test predictions.

---

# Google Cloud Deployment

Deployment related scripts are available in:

```text
gcp/
```

Steps:

1. Create GCP Project
2. Create Storage Bucket
3. Upload Model
4. Deploy Cloud Function
5. Test API Endpoint

---

# Model Performance

The CNN model achieves high accuracy on potato disease classification and successfully distinguishes:

- Healthy Leaves
- Early Blight
- Late Blight

---

# Future Improvements

- Improve model accuracy using transfer learning
- Deploy on Kubernetes
- Add disease treatment recommendations
- Real-time camera prediction
- Multi-crop disease detection

---

# Author

**Desilva Roy**

M.Tech, Indian Institute of Science (IISc)

Deep Learning | NLP | Computer Vision | Generative AI

GitHub:
https://github.com/Desilva93
