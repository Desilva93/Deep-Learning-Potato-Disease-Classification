from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import requests

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TensorFlow Serving Endpoint
endpoint = "http://localhost:8501/v1/models/potatoes_model:predict"

# Update according to your dataset labels
CLASS_NAMES = [
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy"
]

IMAGE_SIZE = 256


@app.get("/ping")
async def ping():
    return "Hello, I am alive"


def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data))

    # Convert to RGB
    image = image.convert("RGB")

    # Resize according to model input shape
    image = image.resize((IMAGE_SIZE, IMAGE_SIZE))

    image = np.array(image)

    return image


@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())

    img_batch = np.expand_dims(image, 0)

    json_data = {
        "instances": img_batch.tolist()
    }

    response = requests.post(
        endpoint,
        json=json_data
    )

    prediction = np.array(
        response.json()["predictions"][0]
    )

    predicted_class = CLASS_NAMES[
        np.argmax(prediction)
    ]

    confidence = float(
        np.max(prediction)
    )

    return {
        "class": predicted_class,
        "confidence": confidence
    }


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=8000
    )