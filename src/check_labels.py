import pandas as pd

df = pd.read_csv("data/raw.csv", low_memory=False)
df.columns = df.columns.str.strip()

print(df["Label"].value_counts())