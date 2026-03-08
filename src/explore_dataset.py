import pandas as pd

df = pd.read_csv("data/raw.csv", low_memory=False)
df.columns = df.columns.str.strip()

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nLabel distribution:")
print(df["Label"].value_counts())

print("\nTop destination ports:")
print(df["Destination Port"].value_counts().head(10))

print("\nAverage Flow Duration by Label:")
print((df.groupby("Label")["Flow Duration"].mean()/1_000_000).round(2))

print("\nAverage Flow Bytes/s by Label:")
clean_bytes = df["Flow Bytes/s"].replace([float("inf"), -float("inf")], None)

df["Flow Bytes/s"] = clean_bytes

print((df.groupby("Label")["Flow Bytes/s"].mean()).round(2))