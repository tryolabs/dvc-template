import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from src.train_model import DATASETS_PATH
from utils import get_features

DATASETS_PATH = Path("assets/datasets")
METRICS_PATH = Path("assets/metrics")
METRICS_PATH.mkdir(exist_ok=True, parents = True)


def main():
    # Load features, targets and model
    features_train = get_features("train")
    features_test = get_features("test")
    y_train = pd.read_csv(DATASETS_PATH / "y_train.csv")
    y_test = pd.read_csv(DATASETS_PATH / "y_test.csv")
    model: RandomForestClassifier = joblib.load("assets/models/model.pkl")

    # Predict!
    y_pred_train = model.predict(features_train)
    y_pred_test = model.predict(features_test)

    # Compute and print accuracies
    train_acc = (y_pred_train == y_train["Survived"]).sum() / len(y_train) * 100
    test_acc = (y_pred_test == y_test["Survived"]).sum() / len(y_test) * 100
    print("Train accuracy:", train_acc)
    print("Test accuracy:", test_acc)

    # Save metrics
    metrics = {"train": train_acc, "test": test_acc}
    with open(METRICS_PATH / "metrics.json", "w") as f:
        json.dump(metrics, f)


if __name__ == "__main__":
    main()
