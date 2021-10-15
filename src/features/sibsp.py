import pandas as pd
from src.utils import create_feature


def sibsp(data: pd.DataFrame):
    return data[["PassengerId", "SibSp"]]


if __name__ == "__main__":
    create_feature(sibsp, "sibsp")
