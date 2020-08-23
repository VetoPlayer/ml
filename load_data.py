import sys
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

HOUSING_PATH=os.path.join('dataset','housing')

os.path.join('dataset','housing')


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

def main():
    housing = load_housing_data()
    

if __name__ == '__main__':
    sys.exit(main())
