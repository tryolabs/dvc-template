import pandas as pd
from src.utils import create_feature


def pclass(data: pd.DataFrame):
    return data[["PassengerId", "Pclass"]]


if __name__ == "__main__":
    create_feature(pclass, "pclass")
