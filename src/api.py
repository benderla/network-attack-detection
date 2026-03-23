from fastapi import FastAPI
import pandas as pd
from sklearn.ensemble import IsolationForest

app = FastAPI()

df = pd.read_csv("data/raw.csv")
df.columns = df.columns.str.strip()

features = df[["Flow Duration", "Flow Packets/s"]]

model = IsolationForest(random_state=42)
model.fit(features)

@app.get("/")
def root():
    return {"service": "network anomaly detection API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(duration: float, packet_rate: float):

    input_df = pd.DataFrame(
        [[duration, packet_rate]],
        columns=["Flow Duration", "Flow Packets/s"]
    )

    score = model.decision_function(input_df)[0]

    return {"anomaly_score": float(score)}