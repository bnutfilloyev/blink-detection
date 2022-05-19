from lib2to3.pytree import Base
from pydantic import BaseModel
from typing import Optional


class MachineLearningResponse(BaseModel):
    prediction: float


class HealthResponse(BaseModel):
    status: bool

class Detection(BaseModel):
    status: bool