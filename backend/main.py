import joblib
from pathlib import Path
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Breast Cancer ML API",
    description="API for the Breast Cancer prediction model",
    version="1.0.0"
)
# Locate the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Locate the saved ML model
MODEL_PATH = BASE_DIR / "models" / "random_forest_pipeline.joblib"

# Load the trained pipeline
model = joblib.load(MODEL_PATH)


@app.get("/")
def home():
    return {"message": "Breast Cancer ML API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/model-info")
def model_info():
    return {
        "model": "Random Forest",
        "status": "loaded",
        "features_required": 9,
        "model_file": MODEL_PATH.name
    }

class PredictionInput(BaseModel):

    Clump_Thickness: int = Field(ge=1, le=10)
    Uniformity_Cell_Size: int = Field(ge=1, le=10)
    Uniformity_Cell_Shape: int = Field(ge=1, le=10)
    Marginal_Adhesion: int = Field(ge=1, le=10)
    Single_Epithelial_Cell_Size: int = Field(ge=1, le=10)
    Bare_Nuclei: int = Field(ge=1, le=10)
    Bland_Chromatin: int = Field(ge=1, le=10)
    Normal_Nucleoli: int = Field(ge=1, le=10)
    Mitoses: int = Field(ge=1, le=10)

@app.post("/predict")
def predict(data: PredictionInput):

    input_data = pd.DataFrame([data.model_dump()])

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    result = "Malignant" if prediction == 1 else "Benign"

    return {
        "prediction": result,
        "benign_probability": round(float(probabilities[0]), 4),
        "malignant_probability": round(float(probabilities[1]), 4)
    }
