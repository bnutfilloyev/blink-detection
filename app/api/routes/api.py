from fastapi import APIRouter

from api.routes import predictor

# API TAGS and PREFIX
router = APIRouter()
router.include_router(predictor.router, tags=["predictor"], prefix="/v1")
