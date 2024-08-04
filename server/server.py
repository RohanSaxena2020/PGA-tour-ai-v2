from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
from util import load_model, predict_scoring_average
import numpy as np
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Add CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for Replit deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount your static files
app.mount("/UI", StaticFiles(directory="UI"), name="UI")


@app.get("/")
async def read_root():
    return FileResponse('UI/index.html')


model, scaler = load_model()


class PredictionInput(BaseModel):
    sg_ott: float
    sg_app: float
    sg_atg: float
    sg_putting: float
    birdie_avg: float
    driving_dist_yds: float
    gir_pct: float


@app.post("/predict/")
async def predict(input_data: PredictionInput):
    try:
        data = np.array([[
            input_data.sg_ott, input_data.sg_app, input_data.sg_atg,
            input_data.sg_putting, input_data.birdie_avg,
            input_data.driving_dist_yds, input_data.gir_pct
        ]])
        scaled_data = scaler.transform(data)
        result = predict_scoring_average(model, scaled_data)
        return {"scoring_average": result}
    except Exception as e:
        logging.error(f"Error during prediction: {e}", exc_info=True)
        raise HTTPException(status_code=500,
                            detail=f"Internal Server Error: {e}")


if __name__ == '__main__':
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
