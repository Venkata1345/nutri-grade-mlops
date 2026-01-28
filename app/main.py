import mlflow.pyfunc
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

class FoodItem(BaseModel):
    total_fat:float
    carbs:float
    protein:float
    sugar:float 

app = FastAPI(title="Nutri-Grade Predictor")

# CHANGED: Now loading from the local folder we just created
model = mlflow.pyfunc.load_model("./models/production_model")
print("✅ Model loaded successfully!")

@app.post("/predict")
def predict(item:FoodItem):
    data=pd.DataFrame([item.dict()])
    prediction=model.predict(data)
    return {"predicted_calories": float(prediction[0])}