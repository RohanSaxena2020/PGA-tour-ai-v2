from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
from util import load_model, predict_scoring_average
import numpy as np

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Add CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model, scaler = load_model()  # Assuming load_model now returns both the model and the scaler

class PredictionInput(BaseModel):
    sg_ott: float
    sg_app: float
    sg_atg: float
    sg_putting: float
    sg_ttg: float
    birdie_avg: float
    driving_dist_yds: float
    gir_pct: float

@app.post("/predict/")
async def predict(input_data: PredictionInput):
    try:
        # Convert input data to numpy array and scale
        data = np.array([[
            input_data.sg_ott,
            input_data.sg_app,
            input_data.sg_atg,
            input_data.sg_putting,
            input_data.sg_ttg,
            input_data.birdie_avg,
            input_data.driving_dist_yds,
            input_data.gir_pct
        ]])
        scaled_data = scaler.transform(data)
        
        # Predict the scoring average
        result = predict_scoring_average(model, scaled_data)
        return {"scoring_average": result}
    except Exception as e:
        logging.error(f"Error during prediction: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
