import numpy as np
import pandas as pd

def generate_glucose_data(n_steps=1000, seed=42):
    """Generates synthetic glucose continuous monitoring telemetry."""
    np.random.seed(seed)
    time = np.arange(n_steps)
    
    # Baseline blood glucose dynamics (mg/dL)
    base_glucose = 100
    diurnal_cycle = 15 * np.sin(2 * np.pi * time / 24)
    meal_spikes = 30 * np.maximum(0, np.sin(2 * np.pi * time / 8))
    noise = np.random.normal(0, 3, size=n_steps)
    
    glucose = base_glucose + diurnal_cycle + meal_spikes + noise
    
    df = pd.DataFrame({
        'timestamp': pd.date_range(start='2026-01-01', periods=n_steps, freq='H'),
        'glucose': glucose
    })
    return df

if __name__ == "__main__":
    df = generate_glucose_data()
    print(f"Generated {len(df)} synthetic telemetry samples.")
