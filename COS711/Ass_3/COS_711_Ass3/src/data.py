from pandas import read_csv
from matplotlib import pyplot
import pandas as pd
import numpy as np
import os
from scipy.stats import zscore


def read_csv(filename):

    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + "/data/"

    filepath = os.path.normpath(my_path + filename)

    # ingest = pd.read_csv(filepath, sep=',')
    ingest = pd.read_csv(filepath, parse_dates=[0], index_col=0)
    ingest.index.name = 'timestamp'
    return ingest


def zscore_normalisation(df, col):
    df = df.apply(lambda x: zscore(x) if x.name == col else x)

    return df


def zscore_df_normalisation(df, columns):
    df = df.apply(lambda x: zscore(x) if x.name in columns else x)

    return df


def remove_df_row(df, index):
    df.drop([df.index[index]], inplace=True)


def remove_df_cols(df, field_num):
    if field_num == 1:
        df.drop(df.columns[[2, 3, 4, 5, 6, 7]], axis=1, inplace=True)
    if field_num == 2:
        df.drop(df.columns[[0, 1, 4, 5, 6, 7]], axis=1, inplace=True)
    if field_num == 3:
        df.drop(df.columns[[0, 1, 2, 3, 6, 7]], axis=1, inplace=True)
    if field_num == 4:
        df.drop(df.columns[[0, 1, 2, 3, 4, 5]], axis=1, inplace=True)

    # return df


def visualize_data(df):
    values = df.values
    # specify columns to plot
    groups = [0, 1, 2, 3, 5, 6, 7]
    i = 1
    # plot each column
    pyplot.figure()
    for group in groups:
        pyplot.subplot(len(groups), 1, i)
        pyplot.plot(values[:, group])
        pyplot.title(df.columns[group], y=0.5, loc='right')
        i += 1
    pyplot.show()
