import joblib
import pytest
import numpy as np
from pathlib import Path

def test_model_compatibility():
    model_path = Path(__file__).parent.parent / "model.pkl"  
    model = joblib.load(model_path)
    test_input = np.array([[1.0]])
    prediction = model.predict(test_input)
    assert isinstance(prediction, np.ndarray), "Prediction is not a numpy array"
    assert prediction.shape == (1,), "Unexpected prediction shape"