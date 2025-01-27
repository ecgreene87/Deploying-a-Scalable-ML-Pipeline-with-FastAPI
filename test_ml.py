import pytest
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from ml.model import train_model, inference, compute_model_metrics
from sklearn.metrics import precision_score, recall_score, fbeta_score
from train_model import X_train, y_train

# TODO: add necessary import


# TODO: implement the first test. Change the function name and input as needed
def test_load_data():
    """
    verify that the data is loaded correctly and has the expected shape.
    """
    X, y = make_classification(n_samples=50, n_features=5, random_state=42)
    assert X.shape == (50, 5), f"Unexpected shape for X: {X.shape}"
    assert y.shape == (50,), f"Unexpected shape for y: {y.shape}"


# TODO: implement the second test. Change the function name and input as needed
def test_inference_model():
    """
    Tests that 3 metrics are returned and each of the ranges are between 0 and 1
    """
    model = train_model(X_train, y_train)
    preds = inference(model, X_train)
    metrics = compute_model_metrics(y_train, preds)
    assert len(metrics) == 3, f"Unexpected number of metrics: {len(metrics)}"
    assert type(metrics) == tuple, f"Unexpected type of metrics: {type(metrics)}"
    for metric in metrics:
        assert metric >= 0 and metric <= 1, f"Unexpected value of metric: {metric}"


# TODO: implement the third test. Change the function name and input as needed
def test_model():
    """
    Test that this function will return a trained RandomForestClassifier
    """
    model = train_model(X_train, y_train)
    assert type(model) == RandomForestClassifier, f"Unexpected type of model: {type(model)}"
