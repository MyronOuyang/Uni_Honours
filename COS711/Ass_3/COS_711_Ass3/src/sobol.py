import copy
import numpy as np
from numpy import loadtxt
import nn
import data


def value_min_max_normalisation(Rmin, Rmax, Tmin, Tmax, value):
    scaled = (value - Rmin) / (Rmax - Rmin) * (Tmax - Tmin) + Tmin
    return int(scaled)


def sobol_params(num_rows, num_params, Tmin, Tmax):
    sobol_set = loadtxt('data/master_Sobol_numbers.csv', delimiter='\t')
    sobol_set = sobol_set[:num_rows, 0:num_params]
    param_values = []
    for vals in sobol_set:
        res = []
        for index, sobol_val in enumerate(vals):
            converted_val = value_min_max_normalisation(0, 1, Tmin[index], Tmax[index], sobol_val)
            res.append(converted_val)
        param_values.append(res)
    return param_values


def sobol_test(params, df):
    # df = data.read_csv("Train_imputed_short.csv")
    # data.remove_df_cols(df, 1)
    best_scores = []
    for param in params:
        res = nn.generate_nn(df, param[0], param[1], param[2])
        best_scores.append(res)

    print("Params: {}".format(params))
    print("Best Scores: {}".format(best_scores))
    print("Best score: {} Best params: {}".format(min(best_scores), params[best_scores.index(min(best_scores))]))
    return params.index(min(best_scores))
