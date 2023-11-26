import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from lib import preprocessing, visualization, statistic
from model import fixed_set_of_features, random_set_of_features


def main():
    df = pd.read_csv('WineDataset.csv')
    pd.set_option('display.max_columns', None)

    statistic(df)
    preprocessing(df)
    visualization(df)
    fixed_set_of_features(df)
    random_set_of_features(df)


if __name__ == '__main__':
    main()
