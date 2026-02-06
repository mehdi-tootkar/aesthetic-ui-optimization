from pydantic import BaseModel
from typing import List

class StepRequest(BaseModel):
    image: List[int]  # image bytes as list of ints

class StepResponse(BaseModel):
    score: float
