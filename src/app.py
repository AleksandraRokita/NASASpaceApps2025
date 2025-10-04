from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import pandas as pd
import joblib
import os
from fastapi.staticfiles import StaticFiles

# --------- ŚCIEŻKI ----------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
PROC_DIR = os.path.join(DATA_DIR, "processed")

MODEL_PATH = os.path.join(DATA_DIR, "rf_koi_model.joblib")
ENC_PATH = os.path.join(DATA_DIR, "label_encoder.joblib")
XTRAIN_PATH = os.path.join(PROC_DIR, "X_train.csv")

# --------- ŁADOWANIE ARTEFAKTÓW ----------
if not (
    os.path.exists(MODEL_PATH)
    and os.path.exists(ENC_PATH)
    and os.path.exists(XTRAIN_PATH)
):
    raise RuntimeError(
        "Brakuje plików: rf_koi_model.joblib / label_encoder.joblib / processed/X_train.csv"
    )

rf = joblib.load(MODEL_PATH)
le = joblib.load(ENC_PATH)

X_train = pd.read_csv(XTRAIN_PATH)
FEATURE_ORDER = X_train.columns.tolist()
MEDIANS = X_train.median(numeric_only=True).to_dict()
CLASS_NAMES = le.classes_.tolist()

# --------- FASTAPI ----------
app = FastAPI(title="Exoplanet KOI Classifier", version="0.1.0")

# pozwól na testy z pliku index.html / localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # w produkcji zawęź do swojej domeny
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PredictIn(BaseModel):
    data: dict = Field(..., description="Słownik: nazwa_cechy -> wartość (float)")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/metadata")
def metadata():
    return {
        "feature_order": FEATURE_ORDER,
        "class_names": CLASS_NAMES,
        "medians": MEDIANS,  # <-- DODAJ TO
    }


@app.post("/predict")
def predict(payload: PredictIn):
    # zbuduj wiersz w tej samej kolejności kolumn; braki -> mediany
    row = {}
    for col in FEATURE_ORDER:
        v = payload.data.get(col, None)
        if v is None or (isinstance(v, str) and v.strip() == ""):
            v = MEDIANS.get(col, None)
        try:
            row[col] = float(v)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail=f"Zła wartość w '{col}': {payload.data.get(col)}",
            )

    X = pd.DataFrame([row])[FEATURE_ORDER]

    try:
        pred_enc = rf.predict(X)[0]
        probs = rf.predict_proba(X)[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Błąd predykcji: {e}")

    label = le.inverse_transform([pred_enc])[0]
    prob_map = {CLASS_NAMES[i]: float(probs[i]) for i in range(len(CLASS_NAMES))}

    return {"prediction": label, "probabilities": prob_map}


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app.mount(
    "/", StaticFiles(directory=os.path.join(BASE_DIR, "web"), html=True), name="static"
)
