import pandas as pd
from src.utils import create_feature


def fare(data: pd.DataFrame):
    return data[["PassengerId", "Fare"]]


if __name__ == "__main__":
    create_feature(fare, "fare")
