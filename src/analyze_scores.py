import pandas as pd
import numpy as np
from joblib import load

print("Loading dataset")

df = pd.read_csv("data/raw.csv", low_memory=False)
df.columns = df.columns.str.strip()

y = df["Label"]

X = df.drop(columns=["Label"])
X = X.select_dtypes(include="number")
X = X.replace([np.inf, -np.inf], np.nan)

print("Loading model")

model = load("artifacts/anomaly_model.joblib")

scores = model.decision_function(X)

df["anomaly_score"] = scores

print("\nAverage anomaly score by label:\n")

print(df.groupby("Label")["anomaly_score"].mean().sort_values())