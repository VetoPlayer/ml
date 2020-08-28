import sys
import os
import pandas as pd
import numpy as np
from load_data import load_housing_data
from split_test import split_train_test_stratified

def main():
    housing_whole = load_housing_data()
    ## Add a new, discretized numerical attribute for performing stratified sampling
    housing_whole["income_cat"] = pd.cut(housing_whole["median_income"], bins=[0.,1.5,3.0,4.5,6.,np.inf], labels=[1,2,3,4,5])
    ## Split the training and test sets.
    train_set, test_set = split_train_test_stratified(housing_whole, "income_cat")
    housing = train_set

    attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
    housing_extra_attribs = attr_adder.transform(housing.values)


    


from sklearn.base import BaseEstimator, TransformerMixin

rooms_ix, bedrooms_ix, population_ix, households_ix = 3,4,5,6


class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]



if __name__ == '__main__':
    sys.exit(main())
