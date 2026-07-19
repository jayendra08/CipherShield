from pathlib import Path
from time import perf_counter

import joblib
import pandas as pd

from .model_loader import load_model


BASE_DIR = Path(__file__).resolve().parent.parent
SCALER_PATH = BASE_DIR / "model" / "scaler.pkl"
FEATURES = ["Time"] + [f"V{i}" for i in range(1, 29)] + ["Amount"]


def _load_artifact(path):
	if not path.exists() or path.stat().st_size == 0:
		return None
	try:
		return joblib.load(path)
	except EOFError:
		return None


def _build_frame(form_data):
	data = {}
	for feature in FEATURES:
		value = form_data.get(feature, 0)
		data[feature] = float(value) if value not in (None, "") else 0.0
	return pd.DataFrame([data], columns=FEATURES)


def _apply_preprocessing(frame):
	scaler = _load_artifact(SCALER_PATH)
	if scaler is not None:
		frame[["Time", "Amount"]] = scaler.transform(frame[["Time", "Amount"]])
	return frame


def predict_transaction(form_data):
	started_at = perf_counter()
	model = load_model()
	if model is None:
		return {"error": "Model file is empty or unavailable."}

	frame = _apply_preprocessing(_build_frame(form_data))
	prediction = int(model.predict(frame)[0])
	probability = float(model.predict_proba(frame)[0][1]) if hasattr(model, "predict_proba") else None
	duration_ms = round((perf_counter() - started_at) * 1000, 2)
	fraud_probability_pct = round((probability or 0.0) * 100, 2) if probability is not None else None
	confidence_pct = round(max((probability or 0.0), 1 - (probability or 0.0)) * 100, 2) if probability is not None else None

	return {
		"prediction": prediction,
		"label": "Fraud" if prediction == 1 else "Legitimate",
		"probability": probability,
		"fraud_probability_pct": fraud_probability_pct,
		"confidence_pct": confidence_pct,
		"duration_ms": duration_ms,
	}
