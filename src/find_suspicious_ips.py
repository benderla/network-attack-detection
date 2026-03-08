import pandas as pd
import numpy as np
from joblib import load

print("Loading dataset")

# Load the CIC-IDS dataset.
# Each row represents a network flow with statistical features
# such as packet counts, byte rates, and connection duration.
df = pd.read_csv("data/raw.csv", low_memory=False)
df.columns = df.columns.str.strip()

print("Loading model")

model = load("artifacts/anomaly_model.joblib")

X = df.drop(columns=["Label"])
X = X.select_dtypes(include="number")
X = X.replace([np.inf, -np.inf], np.nan)

scores = model.decision_function(X)

df["anomaly_score"] = scores

print("Finding suspicious IPs")

ip_scores = (
    df.groupby("Source IP")["anomaly_score"]
    .mean()
    .sort_values()
)

print(ip_scores.head(10))
