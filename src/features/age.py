import pandas as pd
from src.utils import create_feature


def age(data: pd.DataFrame):
    age = data[["PassengerId", "Age"]]
    age = age.fillna(age["Age"].mean())
    return age


if __name__ == "__main__":
    create_feature(age, "age")
