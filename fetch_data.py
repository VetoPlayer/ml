#!/usr/bin/python3.7

import sys
import os 
import tarfile
import urllib.request

DOWNLOAD_URL='https://github.com/ageron/handson-ml2/raw/master/datasets/housing/housing.tgz'
HOUSING_PATH=os.path.join('dataset','housing')

def fetch_housing_data(housing_url=DOWNLOAD_URL, housing_path=HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def main():
    "Fetch the housing data"
    fetch_housing_data()


if __name__ == '__main__':
    sys.exit(main())
