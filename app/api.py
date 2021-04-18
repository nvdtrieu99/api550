from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder
from tensorflow.keras.models import load_model
# import numpy as np
# from PIL import Image, ExifTags
# import cv2

app = FastAPI()

@app.get("/", tags=["Root"])
async def get_root() -> dict:
    return {
        "message": "Welcome to your Okteto app."
    }
