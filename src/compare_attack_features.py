import pandas as pd
import numpy as np

df = pd.read_csv("data/raw.csv", low_memory=False)
df.columns = df.columns.str.strip()

# separate attack vs normal
benign = df[df["Label"] == "BENIGN"]
attack = df[df["Label"] != "BENIGN"]

features = [
    "Flow Duration",
    "Flow Bytes/s",
    "Flow Packets/s",
    "Average Packet Size"
]

print("\nAverage feature values\n")

for f in features:
    b = benign[f].replace([np.inf, -np.inf], np.nan).mean()
    a = attack[f].replace([np.inf, -np.inf], np.nan).mean()

    print(f)
    print("  BENIGN :", round(b,2))
    print("  ATTACK :", round(a,2))
    print()