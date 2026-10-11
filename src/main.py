from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from model import run_experiment

app = FastAPI(title="GlucoTwin AI API", version="1.0.0")

# Pre-train model on startup
model, metrics = run_experiment()

class GlucoseInput(BaseModel):
    past_readings: list[float]  # Expects 5 recent readings

@app.get("/")
def read_root():
    return {"message": "GlucoTwin AI Digital Twin Engine active", "metrics": metrics}

@app.post("/predict")
def predict_glucose(input_data: GlucoseInput):
    if len(input_data.past_readings) != 5:
        return {"error": "Requires exactly 5 past sequential readings."}
    
    features = np.array(input_data.past_readings).reshape(1, -1)
    prediction = model.predict(features)[0]
    
    status = "Normal"
    if prediction > 140:
        status = "Hyperglycemia Alert"
    elif prediction < 70:
        status = "Hypoglycemia Alert"
        
    return {
        "predicted_glucose": round(float(prediction), 2),
        "status": status
    }
