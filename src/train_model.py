import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


def load_data(path):
    df = pd.read_csv(path, low_memory=False)
    df.columns = df.columns.str.strip()
    return df


def prepare_features(df):

    y = df["Label"].apply(lambda x: 1 if x != "BENIGN" else 0)

    X = df.select_dtypes(include=["float64","int64"])

    # Replace infinity values
    X = X.replace([float("inf"), float("-inf")], 0)

    # Replace NaN values
    X = X.fillna(0)

    # Scale features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return X, y


def train_model(X):

    model = IsolationForest(
        n_estimators=100,
        contamination=0.02,
        random_state=42
    )

    model.fit(X)
    return model


def main():

    df = load_data("data/raw.csv")

    X, y = prepare_features(df)

    model = train_model(X)

    print("Model training complete")

    print("Feature matrix shape:", X.shape)


if __name__ == "__main__":
    main()