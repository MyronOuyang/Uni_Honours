import graphviz
import matplotlib.pyplot as plt
import numpy as np
# from labels import labels
from matplotlib.gridspec import GridSpec
from minisom import MiniSom
from sklearn import tree
from sklearn.preprocessing import OneHotEncoder


def main():

    MAP_WIDTH = 15
    MAP_HEIGHT = 15

    soms = []
    titles = ["Education Level", "Reading Ability", "Language In", "Language Out", "Eye", "Remembering Ability"]
    data_sets = []
    class_sets = []

    for i in range(6):
        data = np.genfromtxt('mydata.csv', delimiter=',', skip_header=1, dtype='i8')
        data = onehot_encode(data, [len(data[0])-1], i)
        # data = min_max_normalisation(data, len(data[0])-2, 0, 7111500)

        data_row_len = len(data[0]) - 1
        x = data[:, 0:data_row_len]
        y = data[:, data_row_len]

        data_sets.append(x)
        class_sets.append(y)

        data_row_len = len(x[0])

        som = MiniSom(MAP_WIDTH, MAP_HEIGHT, data_row_len, sigma=0.6, learning_rate=0.8)
        som.pca_weights_init(x)
        som.train_random(x, 100, verbose=False)

        som_weights = som.get_weights()
        soms.append(som_weights)

    for i in range(len(titles)):
        weight_labeled = weight_centric_labeling(soms[i], data_sets[i], class_sets[i])
        print_labeled_som(weight_labeled, MAP_WIDTH, MAP_HEIGHT, titles[i])

        # rule_tree = rule_extraction(weight_labeled)
        # plt.figure(figsize=(15.0, 15.0))
        # dot_data = tree.export_graphviz(rule_tree, class_names=labels[i], filled=True)
        # graph = graphviz.Source(dot_data)
        # graph.view()

    print("Done!")


def onehot_encode(data, excluded, label):

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


def min_max_normalisation(data, index, Rmin, Rmax):

    transposed = np.transpose(data)

    for i in range(len(transposed[index])):
        value = (transposed[index][i] - Rmin)/(Rmax - Rmin) * (1 - 0) + 0
        transposed[index][i] = value

    data = np.transpose(transposed)

    return data


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


def print_labeled_som(labeled_set, x_lim, y_lim, title):

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

    plt.title(title)
    plt.yticks(np.arange(0, cols, step=1))
    plt.xticks(np.arange(0, rows, step=1))
    ax.set_xlim(0, x_lim)
    ax.set_ylim(0, y_lim)

    plt.grid()
    plt.show()


def rule_extraction(labeled_set):

    x = []
    y = []

    c5 = tree.DecisionTreeClassifier()

    for i in range(len(labeled_set)):
        for j in range(len(labeled_set[i])):
            x.append(labeled_set[i][j]['neuron'])
            y.append(labeled_set[i][j]['label'])

    c5.fit(x, y)

    return c5


if __name__ == "__main__":
    main()
