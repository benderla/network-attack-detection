import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from joblib import dump

print("Loading dataset...")

# Load the CIC-IDS dataset.
# Each row represents a network flow with statistical features
# such as packet counts, byte rates, and connection duration.
df = pd.read_csv("data/raw.csv", low_memory=False)

# remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Separate labels
y = df["Label"]

# Keep only numeric columns
X = df.drop(columns=["Label"])
X = X.select_dtypes(include="number")

# Replace infinite values
X = X.replace([np.inf, -np.inf], np.nan)

# Train only on benign traffic
train_mask = y == "BENIGN"
X_train = X[train_mask]

print("Training rows:", X_train.shape)

# Isolation Forest is used for anomaly detection.
# The model learns the normal behavior of network traffic
# using only benign flows and identifies observations
# that deviate significantly from that baseline.

pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("model", IsolationForest(
        n_estimators=200,
        contamination=0.01,
        random_state=42,
        n_jobs=-1
    ))
])

print("Training model...")

pipeline.fit(X_train)

dump(pipeline, "artifacts/anomaly_model.joblib")

print("Model saved to artifacts/anomaly_model.joblib")
