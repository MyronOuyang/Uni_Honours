import datawig
import numpy as np
import os
import pandas as pd

def impute(input_cols, output_col, data):

    df_train, df_test = datawig.utils.random_split(data)

    imputer = datawig.SimpleImputer(
        input_columns = input_cols,
        output_column = output_col, 
        output_path = 'imputer_model' 
    )

    imputer.fit(train_df=df_train, test_df=df_test, num_epochs=100)

    imputed_df = imputer.predict(data)

    return imputed_df

def replace_with_imputed(data, col, imputed, imputed_col):

    for i in range(len(data[col])):

        if (data[col][i] == "") or (np.isnan(data[col][i])):
            data[col][i] = imputed[imputed_col][i]

    return data

def save_imputed_csv(imputed_df, filename):

    my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + "/data/"

    filepath = os.path.normpath(my_path + filename)

    imputed_df.to_csv(filepath)
