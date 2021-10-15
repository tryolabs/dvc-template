from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

DATASETS_PATH = Path("assets/datasets")


def main():
    # Load the raw data
    data = pd.read_csv("assets/raw_data/train.csv")

    # Split features and target
    X = data.drop(columns=["Survived"])
    y = data["Survived"]

    # Split train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=42, stratify=data["Pclass"]
    )

    # Save
    X_train.to_csv(DATASETS_PATH / "X_train.csv", index=False)
    X_test.to_csv(DATASETS_PATH / "X_test.csv", index=False)
    y_train.to_csv(DATASETS_PATH / "y_train.csv", index=False)
    y_test.to_csv(DATASETS_PATH / "y_test.csv", index=False)


if __name__ == "__main__":
    DATASETS_PATH.mkdir(exist_ok=True, parents=True)
    main()
