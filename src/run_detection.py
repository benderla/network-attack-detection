import pandas as pd
from sklearn.ensemble import IsolationForest

# Load data
df = pd.read_csv("data/raw.csv", low_memory=False)
df.columns = df.columns.str.strip()

# Create attack label
df["Attack"] = (df["Label"] != "BENIGN").astype(int)

# Use numeric features only
X = df.drop(columns=["Label", "Attack"])
X = X.select_dtypes(include="number")

# Train anomaly detection model
model = IsolationForest(
    n_estimators=100,
    contamination=0.01,
    random_state=42,
    n_jobs=-1
)

model.fit(X)

# Generate anomaly scores
df["anomaly_score"] = model.decision_function(X)

# Save suspicious flows
df.sort_values("anomaly_score").head(100).to_csv(
    "outputs/top_anomalies.csv",
    index=False
)

print("Detection complete. Results saved to outputs/top_anomalies.csv")