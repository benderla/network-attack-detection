from fastapi import FastAPI
import pandas as pd
from sklearn.ensemble import IsolationForest

app = FastAPI()

# ------------------------------------------
# Load dataset
# ------------------------------------------

df = pd.read_csv("data/raw.csv")

# Fix whitespace in column names
df.columns = df.columns.str.strip()

# Select features
features = df[["Flow Duration", "Flow Packets/s"]]

# Train model
model = IsolationForest(random_state=42)
model.fit(features)

# ------------------------------------------
# Health endpoint
# ------------------------------------------

@app.get("/")
def health():
    return {"status": "anomaly detection service running"}

# ------------------------------------------
# Prediction endpoint
# ------------------------------------------

@app.post("/predict")
def predict(duration: float, packet_rate: float):

    input_df = pd.DataFrame(
        [[duration, packet_rate]],
        columns=["Flow Duration", "Flow Packets/s"]
    )

    score = model.decision_function(input_df)[0]

    return {
        "anomaly_score": float(score)
    }