<<<<<<< HEAD
import base64
import io
from fastapi import FastAPI, HTTPException
from PIL import Image
import cv2
import numpy as np
from ultralytics import YOLO
from ImageResponse import ImageResponse
from ImageRequest import ImageRequest

app = FastAPI()

model = YOLO("mnist.pt")

def base64_to_image(base64_str):
    try:
        image_data = base64.b64decode(base64_str)
        image = Image.open(io.BytesIO(image_data))
        return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid image data")

def image_to_base64(image):
    _, buffer = cv2.imencode('.png', image)
    return base64.b64encode(buffer).decode('utf-8')

@app.post("/process-image", response_model=ImageResponse)
async def process_image(request: ImageRequest):
    image = base64_to_image(request.image_base64)

    results = model.predict(source=image)

    if results[0].boxes:
        annotated_image = results[0].plot()
    else:
        annotated_image = image

    processed_image_base64 = image_to_base64(annotated_image)
    
    return ImageResponse(image_base64=processed_image_base64)
=======
import base64
import io
from fastapi import FastAPI, HTTPException
from PIL import Image
import cv2
import numpy as np
from ultralytics import YOLO
from ImageResponse import ImageResponse
from ImageRequest import ImageRequest

app = FastAPI()

model = YOLO("mnist.pt")

def base64_to_image(base64_str):
    try:
        image_data = base64.b64decode(base64_str)
        image = Image.open(io.BytesIO(image_data))
        return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid image data")

def image_to_base64(image):
    _, buffer = cv2.imencode('.png', image)
    return base64.b64encode(buffer).decode('utf-8')

@app.post("/process-image", response_model=ImageResponse)
async def process_image(request: ImageRequest):
    image = base64_to_image(request.image_base64)

    results = model.predict(source=image)

    if results[0].boxes:
        annotated_image = results[0].plot()
    else:
        annotated_image = image

    processed_image_base64 = image_to_base64(annotated_image)
    
    return ImageResponse(image_base64=processed_image_base64)
>>>>>>> 80b95a30ea8f0c6c02fea26d8fe49a1eded98fc4
