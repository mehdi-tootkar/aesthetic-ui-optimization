from fastapi import FastAPI
from server.schemas import StepRequest, StepResponse
from server.evaluator.aesthetic import AestheticScorer

app = FastAPI(title="Aesthetic UI Optimization API")

# load scorer once
scorer = AestheticScorer()

@app.post("/score", response_model=StepResponse)
def score_image(req: StepRequest):
    image_bytes = bytes(req.image)
    score = scorer.score(image_bytes)
    return StepResponse(score=score)
