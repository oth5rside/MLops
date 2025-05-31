from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib

app = FastAPI()

# Загрузка модели
try:
    model = joblib.load("model.pkl")
except Exception as e:
    raise Exception(f"Failed to load model: {str(e)}")

# Определение структуры данных для запроса
class PredictionRequest(BaseModel):
    feature1: float = Field(..., ge=0.0)  # Пример: feature1 должен быть неотрицательным

# Определение структуры данных для ответа
class PredictionResponse(BaseModel):
    prediction: float

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    try:
        data = [[request.feature1]]
        prediction = model.predict(data)
        return PredictionResponse(prediction=float(prediction[0]))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

# Запуск приложения
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)