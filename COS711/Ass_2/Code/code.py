import csv
import matplotlib.pyplot as plt
import numpy as np
import os.path
from scipy import stats
import sys


def main():
    data_list, data_dict = load_data('pulsar_stars.csv')
    data_list.pop(len(data_list) - 1)

    data_list = np.array(data_list).astype(np.float)

    plt.plot(data_list)
    plt.show()

    z_data_list = stats.zscore(data_list)

    plt.plot(z_data_list) 
    plt.show()

    print("Done")


def load_data(filename):
    filepath = filename
    path = filename

    columns = ["Mean of the integrated profile", "Standard deviation of the integrated profile", "Excess kurtosis of the integrated profile", "Skewness of the integrated profile",
               "Mean of the DM-SNR curve", "Standard deviation of the DM-SNR curve", "Excess kurtosis of the DM-SNR curve", "Skewness of the DM-SNR curve ,target_class"]
    data_list = [[], [], [], [], [], [], [], [], []]
    data_dict = {}

    try:
        with open(path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                for header, value in row.items():
                    try:
                        data_dict[header].append(value)
                    except KeyError:
                        data_dict[header] = [value]
    except OSError:
        sys.exit("Unable to locate file at: " + path)

    try:
        with open(path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            list_reader = list(reader)
            list_reader.pop(0)

            for i in range(len(list_reader)):
                for j in range(len(list_reader[i])):
                    temp = list_reader[i][j]
                    data_list[j].append(temp)
    except OSError:
        sys.exit("Unable to locate file at: " + path)

    return (data_list, data_dict)


main()
