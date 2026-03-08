import pandas as pd
import numpy as np
from joblib import load

print("Loading dataset...")

# Load the CIC-IDS dataset.
# Each row represents a network flow with statistical features
# such as packet counts, byte rates, and connection duration.
df = pd.read_csv("data/raw.csv", low_memory=False)

# clean column names
df.columns = df.columns.str.strip()

print("Rows:", df.shape[0])

# separate label
y = df["Label"]

# build features
X = df.drop(columns=["Label"])
X = X.select_dtypes(include="number")
X = X.replace([np.inf, -np.inf], np.nan)

print("Loading trained model...")

model = load("artifacts/anomaly_model.joblib")

print("Scoring network flows...")

scores = model.decision_function(X)
pred = model.predict(X)

df["anomaly_score"] = scores
df["is_anomaly"] = (pred == -1)

print("Anomaly rate:", df["is_anomaly"].mean())

print("Selecting most suspicious flows...")

top = df.sort_values("anomaly_score").head(50)

top.to_csv("outputs/top_anomalies.csv", index=False)

print("Top anomalies written to outputs/top_anomalies.csv")
