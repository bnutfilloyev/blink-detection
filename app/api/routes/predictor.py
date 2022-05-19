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
        contents = await file.read()
        nparr = np.fromstring(contents, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        print(frame.shape)

        result, pred_l, pred_r = eye_blink_detection(frame)

        if result is not None:
            if result == 'Blink':
                return Detection(status=False)
            
            if result == 'No blink':
                return Detection(status=True)
        else:
            return Detection(status=False)


    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Exception: {e}")
