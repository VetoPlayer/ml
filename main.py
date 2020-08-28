import os
import sys
import pandas as pd
import numpy as np 


from load_data import load_housing_data
from split_test import split_train_test_stratified
from transform import CombinedAttributesAdder

from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

## Numeric Pipeline
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy="median")), ## Imputer replacing missing values with their median
    ('attribs_adder', CombinedAttributesAdder()), ## Our Custom Transformer
    ('std_scaler', StandardScaler()), ## Standardize all the numerical attributes 
])


def main():
    housing_whole = load_housing_data()
    ## Add a new, discretized numerical attribute for performing stratified sampling
    housing_whole["income_cat"] = pd.cut(housing_whole["median_income"],
                                        bins=[0.,1.5,3.0,4.5,6.,np.inf], 
                                        labels=[1,2,3,4,5])
    ## Split the training and test sets.
    train_set, test_set = split_train_test_stratified(housing_whole, "income_cat")

    # Let's now remove the extra attribute we added since it doesn't provide extra value
    for set_ in (train_set, test_set):
        set_.drop("income_cat", axis=1, inplace=True)

    ## It is important to fit the Scalers to the Training Data only!
    ## The test set should be excluded, Let's also separate predictors attributes and labels:
    housing = train_set.drop("median_house_value", axis=1)
    housing_labels = train_set["median_house_value"].copy()

    ## Transformation happens differently according on whether
    ## the attributes are numerical or categorical:

    housing_num = housing.drop("ocean_proximity", axis=1)

    num_attribs = list(housing_num)
    cat_attribs = ["ocean_proximity"] 

    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", OneHotEncoder(), cat_attribs),
    ])


    housing_prepared = full_pipeline.fit_transform(housing)


if __name__ == '__main__':
    sys.exit(main())
