import pytest
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from data_generator import generate_glucose_data
from model import create_lag_features, run_experiment

def test_data_generator():
    df = generate_glucose_data(n_steps=100)
    assert len(df) == 100
    assert 'glucose' in df.columns

def test_lag_features():
    df = generate_glucose_data(n_steps=20)
    X, y = create_lag_features(df, lag=5)
    assert X.shape == (15, 5)
    assert len(y) == 15

def test_model_experiment():
    model, results = run_experiment()
    assert results['ml_mae'] < results['
