import pytest
from ml.model import train_model, compute_model_metrics, inference
# TODO: add necessary import
import numpy as np
import xgboost as xgb

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    Test that train_model returns an XGBClassifier instance.
    """
    X = np.array([[0, 1], [1, 0]])
    y = np.array([0, 1])

    model = train_model(X, y)

    assert isinstance(model, xgb.XGBClassifier), "train_model should return an XGBClassifier instance."

    pass


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    Test that compute_model_metrics returns correct precision, recall, and f1.
    """
    y_true = np.array([0, 1, 1, 0])
    preds   = np.array([0, 1, 0, 0])

    precision, recall, fbeta = compute_model_metrics(y_true, preds)

    # Expected:
    # TP = 1, FP = 0, FN = 1 → precision = 1.0, recall = 0.5, f1 = 0.666...
    assert precision == 1.0
    assert recall == 0.5
    assert fbeta == pytest.approx(0.666, rel=1e-2)
    
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    Test that inference returns predictions with correct size.
    """
    X = np.array([[0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1])

    model = train_model(X, y)
    preds = inference(model, X)

    assert preds.shape == (3,), "Inference output must match number of input samples."
    assert preds.dtype == np.int64 or preds.dtype == int, "Predictions should be integer labels."
    
    pass