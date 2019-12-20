import copy
import numpy as np
from numpy import loadtxt


def cross_sampling(windows, nn, epoch=30):
    total_acc = np.array([])
    total_loss = np.array([])
    for i in range(10):
        temp_data = copy.deepcopy(windows)

        test_set = temp_data.pop(i)
        test_set = np.array(test_set)

        train_set = np.array(temp_data)
        dimension_1 = train_set.shape[0]
        dimension_2 = train_set.shape[1]
        train_set = train_set.reshape(dimension_1 * dimension_2, 9)

        test_x = test_set[:, 0:8]
        test_y = test_set[:, 8]
        train_x = train_set[:, 0:8]
        train_y = train_set[:, 8]

        nn.fit(train_x, train_y, epochs=epoch, batch_size=15)
        loss, accuracy = nn.evaluate(test_x, test_y)
        total_acc = np.append(total_acc, accuracy)
        total_loss = np.append(total_loss, loss)

    mean_acc = np.mean(total_acc)
    std_acc = np.std(total_acc)
    mean_loss = np.mean(total_loss)
    std_loss = np.std(total_loss)

    return ({
        "mean_acc": mean_acc,
        "std_acc": std_acc,
    })


def split_data_windows(data, N=10):
    window_size = len(data) / N
    window_size = int(window_size)

    windowed_data = []

    temp_data = copy.deepcopy(data)
    np.random.shuffle(temp_data)
    temp_data = temp_data.tolist()

    for i in range(N):
        new_window = []
        for j in range(window_size):
            new_window.append(temp_data.pop(0))

        windowed_data.append(new_window)

    # test_data = []

    # if(len(temp_data) > 0):
    #     for i in range(len(temp_data)):
    #         test_data.append(temp_data.pop(0))

    # return (windowed_data, test_data)
    return windowed_data


def value_min_max_normalisation(Rmin, Rmax, Tmin, Tmax, value):
    """Scale a value to be within a range.

    Parameters
    ----------
    Rmin :
        Minimum value of the current range
    Rmax :
        Maximum value of the current range
    Tmin :
        Minimum value of the desired range
    Tmax :
        Maximum value of the desired range
    value :
        The value to be scaled

    Returns
    -------
    The scaled value as a float
"""

    scaled = (value - Rmin) / (Rmax - Rmin) * (Tmax - Tmin) + Tmin

    return scaled


def sobol_test(num_rows, num_params, Tmin, Tmax):
    sobol_set = loadtxt('master_Sobol_numbers.csv', delimiter='\t')
    sobol_set = sobol_set[:num_rows, 0:num_params]

    param_values = []
    for vals in sobol_set:
        res = []
        for sobol_val in vals:
            converted_val = value_min_max_normalisation(0, 1, Tmin, Tmax, sobol_val)
            res.append(converted_val)
        param_values.append(res)

    return param_values
        # stuff param_values/ converted_val into cross_sampling test and hopefully nice shit happens



# print(sobol_test(32, 3, 0, 1))
