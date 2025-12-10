from fastapi import FastAPI
from pydantic import BaseModel
import joblib


app = FastAPI()

# load model
model = joblib.load('model.pkl')


class InputData(BaseModel):
    X: float


@app.get("/")
def read_root():
    return {"message": "Helo world"}


@app.post("/predict")
def predict(data: InputData):
    prediction = model.predict([[data.X]])[0]
    return {"prediction": prediction}

