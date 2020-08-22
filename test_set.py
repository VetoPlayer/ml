import sys
import os
import pandas as pd
import numpy as np
from zlib import crc32

os.path.join('dataset','housing')

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

## Naive implementation!
def split_train_test(data, test_ratio=0.2):
    "Split the given dataset, returning tuple containing the training and test set"
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


## You do want to take into account a random split for your dataset, 
## but you do want to avoid for sure keep this split overtime.
## A Naive implementation for achieving this is to use: np.random.seed(42) 
## But it becomes a problem once you get new data
## The best implementation is to compute an hash on each instance's qualifier
## and put that instance in the test set if the hash is lower that or equal 20%
## of the maximum hash value

def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32
    
def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

def main():
    load_housing_data()
    

if __name__ == '__main__':
    sys.exit(main())
