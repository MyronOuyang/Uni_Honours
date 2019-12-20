import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import loadtxt

import seaborn as sns
from pyod.models.pca import PCA
from pyod.utils.data import evaluate_print, generate_data, get_outliers_inliers
from pyod.utils.example import visualize


dataset = loadtxt('Data/test_shuf.csv', delimiter=',')
x = dataset[:, 0:8]
y = dataset[:, 8]
outliers, inliers = get_outliers_inliers(x, y)
