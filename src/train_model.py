from pathlib import Path

import joblib
import pandas as pd
import yaml
from sklearn.ensemble import RandomForestClassifier

from utils import get_features

DATASETS_PATH = Path("assets/datasets")
MODELS_PATH = Path("assets/models")
MODELS_PATH.mkdir(exist_ok=True, parents=True)

def main():
    # Get train features and targets
    features_train = get_features("train")
    y_train = pd.read_csv(DATASETS_PATH / "y_train.csv")

    # Load params
    with open("params.yaml", "r") as f:
        params = yaml.full_load(f)

    # Train model
    model = RandomForestClassifier(**params["model"]).fit(
        features_train, y_train["Survived"]
    )

    # Save model

    joblib.dump(model, MODELS_PATH / "model.pkl")


if __name__ == "__main__":
    main()
