import pandas as pd
import numpy as np

train_raw = pd.read_csv('Raw_datasets/train.csv')
test_raw = pd.read_csv('Raw_datasets/test.csv')

print(train_raw.head(3))


def split_names(raw_dataset: pd.DataFrame):
    print(raw_dataset.head(3))
    name = raw_dataset.iloc[:,[3]]
    print(name.iloc[1])
    return

split_names(train_raw)