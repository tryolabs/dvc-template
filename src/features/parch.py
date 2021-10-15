import pandas as pd
from src.utils import create_feature


def parch(data: pd.DataFrame):
    return data[["PassengerId", "Parch"]]


if __name__ == "__main__":
    create_feature(parch, "parch")
