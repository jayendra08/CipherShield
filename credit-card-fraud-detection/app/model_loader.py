from functools import lru_cache
from pathlib import Path

import joblib


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "credit_card_fraud_xgboost.pkl"


@lru_cache(maxsize=1)
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

    if MODEL_PATH.stat().st_size == 0:
        raise ValueError("Model file is empty")

    try:
        model = joblib.load(MODEL_PATH)
        return model

    except Exception as e:
        raise RuntimeError(f"Failed to load model: {e}")