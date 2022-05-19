from services.eye_detector import eye_blink_detection
from models.prediction import Detection

from fastapi import APIRouter, HTTPException, UploadFile, File
from loguru import logger
import numpy as np
import cv2


router = APIRouter()


@router.post("/detect", response_model=Detection, name="image:get-data")
async def image(file: UploadFile = File(...)):
    try:
        # Load image
        contents = await file.read()

        # Decode image to numpy array
        nparr = np.fromstring(contents, np.uint8)

        # Convert numpy array to image
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Detect eye blinks
        result, pred_l, pred_r = eye_blink_detection(frame)

        # Return result
        # TODO: you can return more than one result
        if result is not None:
            if result == 'Blink':
                return Detection(status=False)
            
            if result == 'No blink':
                return Detection(status=True)
        else:
            return Detection(status=False)

    # Catch errors
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Exception: {e}")
