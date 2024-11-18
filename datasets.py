import pandas as pd
import numpy as np
import os

def find_dataset_files():
    datasets = {}
    # Create relative file path (comment/uncomment relevant path)
    base_path = os.path.join(os.getcwd(), 'Raw_datasets')
    # base_path = '/kaggle/input'

    for dirname, _, filenames in os.walk(base_path):
        for filename in filenames:
            if filename.endswith('.csv'):  # Only add if the file is a CSV
                file_path = os.path.join(dirname, filename)
                file_key = filename.split('.')[0]
                datasets[file_key] = file_path
    return datasets

def load_dataset_df(dataset_file):
    dataset_dataframe =pd.read_csv(dataset_file)
    return dataset_dataframe


# Create dictionary of dataset paths
datasets = find_dataset_files()

# Load datasets into dataframes
train_df = load_dataset_df(datasets.get('train'))
test_df = load_dataset_df(datasets.get('test'))

# Preview datasets
print(train_df.head(10))
print(test_df.head(3))


def clean_dataset(dataset_df: pd.DataFrame):
    
    def split_name(dataset_df):
        return " ".join([i.strip('\'\" ().,') for i in dataset_df.split(" ")])
    
    dataset_df["Name"] = dataset_df["Name"].apply(split_name)
    

    return dataset_df

df = clean_dataset(train_df)

print(df)

