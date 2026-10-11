import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from data_generator import generate_glucose_data

def create_lag_features(df, lag=5):
    """Creates lagged features for chronological time-series evaluation."""
    X, y = [], []
    values = df['glucose'].values
    for i in range(lag, len(values)):
        X.append(values[i-lag:i])
        y.append(values[i])
    return np.array(X), np.array(y)

def run_experiment():
    df = generate_glucose_data()
    
    # Chronological Time-based split (80% train, 20% test)
    train_size = int(len(df) * 0.8)
    train_df = df.iloc[:train_size]
    test_df = df.iloc[train_size:]
    
    # 1. Baseline Model (Persistence / Rolling Mean)
    baseline_preds = test_df['glucose'].shift(1).rolling(window=5).mean().bfill()
    baseline_mae = mean_absolute_error(test_df['glucose'], baseline_preds)
    baseline_rmse = np.sqrt(mean_squared_error(test_df['glucose'], baseline_preds))
    
    # 2. Trained ML Model
    X_train, y_train = create_lag_features(train_df)
    X_test, y_test = create_lag_features(test_df)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    ml_preds = model.predict(X_test)
    ml_mae = mean_absolute_error(y_test, ml_preds)
    ml_rmse = np.sqrt(mean_squared_error(y_test, ml_preds))
    
    results = {
        "baseline_mae": round(baseline_mae, 2),
        "baseline_rmse": round(baseline_rmse, 2),
        "ml_mae": round(ml_mae, 2),
        "ml_rmse": round(ml_rmse, 2)
    }
    return model, results

if __name__ == "__main__":
    _, res = run_experiment()
    print("--- Empirical Evaluation Results ---")
    print(f"Baseline MAE: {res['baseline_mae']} | RMSE: {res['baseline_rmse']}")
    print(f"GlucoTwin Model MAE: {res['ml_mae']}
