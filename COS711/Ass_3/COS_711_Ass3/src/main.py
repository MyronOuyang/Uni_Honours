from copy import deepcopy
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.layers import (LSTM, Dense, Dropout, Embedding, GlobalMaxPooling1D,
                          SpatialDropout1D)
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

import data
import impute
import nn
import sobol

def main():

    df = data.read_csv("Train_imputed_short.csv")
    data.remove_df_cols(df, 1)

    # train_df = data.read_csv("train_data.csv")
    # data.remove_df_cols(train_df, 1)
    # test_df = data.read_csv("test_data.csv")
    # data.remove_df_cols(test_df, 1)
    # data.visualize_data(df)

    nn.calculate_future_values(df)
    # nn.generate_nn(df)
    # nn.cross_validate(df)

    # params = sobol.sobol_params(8, 3, [10, 50, 10], [100, 100, 120])
    # sobol.sobol_test(params, df)    

    # model = nn.generate_and_return_nn(df)
    # nn.cross_validate_generalisation(df, model)
    print("Done")


if __name__ == "__main__":
    main()
