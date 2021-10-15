from pathlib import Path
from typing import Callable

import pandas as pd

DATASETS_PATH = Path("assets/datasets")
FEATURES_PATH = Path("assets/features")
TRAIN = "train"
TEST = "test"


def create_feature(creator: Callable[[pd.DataFrame], pd.DataFrame], name: str) -> None:
    train_data = pd.read_csv(DATASETS_PATH / f"X_{TRAIN}.csv")
    test_data = pd.read_csv(DATASETS_PATH / f"X_{TEST}.csv")

    train_feature = creator(train_data)
    test_feature = creator(test_data)

    train_path = FEATURES_PATH / TRAIN / f"{name}.csv"
    train_path.parent.mkdir(exist_ok=True, parents=True)
    test_path = FEATURES_PATH / TEST / f"{name}.csv"
    test_path.parent.mkdir(exist_ok=True, parents=True)
    train_feature.to_csv(train_path, index=False)
    test_feature.to_csv(test_path, index=False)


def get_features(dataset_name: str):
    features_dir = FEATURES_PATH / dataset_name
    features = []
    for path in features_dir.glob(f"*.csv"):
        feature_df = pd.read_csv(path).set_index("PassengerId")
        features.append(feature_df)
    return pd.concat(features, join="outer", axis=1)
