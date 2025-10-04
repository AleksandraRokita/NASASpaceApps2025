import pandas as pd
from sklearn.model_selection import train_test_split
import os

# 1. Ścieżki do plików (dzięki temu nie trzeba wpisywać ręcznie)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "raw_data.csv")

# 2. Wczytanie danych (ignorujemy linie zaczynające się od #)
df = pd.read_csv(DATA_PATH, comment="#")

# 3. Definiujemy etykiety i cechy
label_col = "koi_disposition"

feature_cols = [
    "koi_steff",
    "koi_slogg",
    "koi_srad",
    "ra",
    "dec",
    "koi_kepmag",
    "koi_period",
    "koi_time0bk",
    "koi_duration",
    "koi_impact",
    "koi_depth",
    "koi_model_snr",
    "koi_prad",
    "koi_teq",
    "koi_insol",
]

# Usuwamy brakujące kolumny (czasem nie wszystkie są w pliku)
feature_cols = [c for c in feature_cols if c in df.columns]

X = df[feature_cols].copy()
y = df[label_col].copy()

# 4. Usuwamy wiersze z brakami
mask = X.notna().all(axis=1) & y.notna()
X = X[mask]
y = y[mask]

# 5. Podział na dane uczące i testowe
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 6. Informacyjnie wypisujemy
print("Cechy wejściowe:", feature_cols)
print("Cechy wyjściowe:", label_col)
print("Rozmiar X_train:", X_train.shape, "X_test:", X_test.shape)
print("Rozkład klas w y_train:", y_train.value_counts())

# 7. Zapisujemy podzielone dane do plików CSV
output_dir = os.path.join(BASE_DIR, "data", "processed")
os.makedirs(output_dir, exist_ok=True)
X_train.to_csv(os.path.join(output_dir, "X_train.csv"), index=False)
X_test.to_csv(os.path.join(output_dir, "X_test.csv"), index=False)
y_train.to_csv(os.path.join(output_dir, "y_train.csv"), index=False)
y_test.to_csv(os.path.join(output_dir, "y_test.csv"), index=False)
print(f"Dane zapisane w katalogu: {output_dir}")
