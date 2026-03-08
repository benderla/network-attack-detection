import pandas as pd

# Load the CIC-IDS dataset.
# Each row represents a network flow with statistical features
# such as packet counts, byte rates, and connection duration.
df = pd.read_csv("data/raw.csv", low_memory=False)
df.columns = df.columns.str.strip()

print(df["Label"].value_counts())
