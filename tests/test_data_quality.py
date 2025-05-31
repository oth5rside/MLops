import joblib
import pytest
import numpy as np

def test_model_compatibility():
    model = joblib.load("../model.pkl")
    test_input = np.array([[1.0]])
    prediction = model.predict(test_input)
    assert isinstance(prediction, np.ndarray), "Prediction is not a numpy array"
    assert prediction.shape == (1,), "Unexpected prediction shape"