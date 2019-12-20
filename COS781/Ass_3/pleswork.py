from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
import numpy as np
from minisom import MiniSom
import sys
sys.path.insert(0, '../')


def onehot_encode(data, excluded=[], label):
    test = []
    transposed = np.transpose(data)

    encoded = []
    encoder = OneHotEncoder(sparse=False)

    for i in range(len(transposed)):
        if not(i in excluded) and i != label:
            onehot_primer = np.reshape(transposed[i], (-1, 1))

            onehot_encoded = encoder.fit_transform(onehot_primer)
            onehot_encoded_transposed = np.transpose(onehot_encoded)

            for col in onehot_encoded_transposed:
                encoded.append(col)
        elif i != label:
            encoded.append(transposed[i])

    encoded.append(transposed[label])
    output = np.transpose(encoded)

    return output

def euclid_distance(point1, point2):
    return np.linalg.norm(point1 - point2)


def BME(weight_vector, data):
    result = None
    smallest = 1.0e20

    for i in range(len(data)):
        test_val = euclid_distance(weight_vector, data[i])
        if test_val < smallest:
            smallest = test_val
            result = i

    return result


def weight_centric_labeling(SOM, data, classes):
    weight_set = []

    for i in range(len(SOM)):
        row = []
        for j in range(len(SOM[i])):

            index = BME(SOM[i][j], data)
            map_object = {
                "neuron": SOM[i][j],
                "label": classes[index]
            }
            row.append(map_object)

        weight_set.append(row)

    return weight_set


def print_labeled_som(labeled_set, x_lim, y_lim):

    print_set = []

    fig, ax = plt.subplots()

    for i in range(len(labeled_set)):
        row = []
        for j in range(len(labeled_set[i])):
            if(labeled_set[i][j]['label'] == None):
                row.append(-1)
                text = ax.text(j, i, "", ha="center", va="center", color="w")
            else:
                row.append(labeled_set[i][j]['label'])
                text = ax.text(j + 0.5, i + 0.5, labeled_set[i][j]['label'], ha="center", va="center", color="k")

        print_set.append(row)

    im = plt.imshow(print_set, cmap='Set3', origin='lower', extent=[0, x_lim, 0, y_lim])
    rows = len(labeled_set)
    cols = len(labeled_set[0])

    plt.yticks(np.arange(0, cols, step=1))
    plt.xticks(np.arange(0, rows, step=1))
    ax.set_xlim(0, x_lim)
    ax.set_ylim(0, y_lim)

    plt.grid()
    plt.show()


data = np.genfromtxt('mydata.csv', delimiter=',', usecols=(1, 2, 3, 4, 5), skip_header=(1))
data_2 = np.genfromtxt('mydata_short.csv', delimiter=',', usecols=(1, 2, 3, 4, 5), skip_header=(1))

data_row_len = len(data[0]) - 1
x = data[:, 0:data_row_len]
y = data[:, data_row_len]

data = onehot_encode('mydata.csv')
# data normalization
# data = np.apply_along_axis(lambda x: x / np.linalg.norm(x), 1, data)

# Initialization and training
som = MiniSom(25, 25, 5, sigma=3, learning_rate=0.5)

som.pca_weights_init(data)
print("Training...")
som.train_batch(data, 1000, verbose=False)  # random training
som_weights = som.get_weights()
weight_labeled = weight_centric_labeling(som_weights, data, y)
print("\n...ready!")
