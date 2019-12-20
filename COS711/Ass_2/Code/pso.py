import matplotlib.pyplot as plt
import numpy as np
import pyswarms as ps
from numpy import loadtxt

import nn


def pso():
    def forward_prop(parameters):

        input_to_hidden = n_inputs * n_hidden
        input_to_hidden_bias = (n_inputs * n_hidden) + n_hidden

        hidden_to_output = (n_hidden * n_outputs) + input_to_hidden_bias
        hidden_to_output_bias = (n_hidden * n_outputs) + hidden_to_output

        W1 = parameters[0:input_to_hidden].reshape((n_inputs, n_hidden))
        B1 = parameters[input_to_hidden:input_to_hidden_bias].reshape((n_hidden, ))
        W2 = parameters[input_to_hidden_bias:hidden_to_output].reshape((n_hidden, n_outputs))
        B2 = parameters[hidden_to_output:hidden_to_output_bias].reshape((n_outputs, ))

        weights = [W1, B1, W2, B2]

        model.set_weights(weights)

        loss, acc = model.evaluate(x, y)

        return loss

    def propagate_swarm(x):
        n_particles = x.shape[0]
        j = [forward_prop(x[i]) for i in range(n_particles)]

        return np.array(j)

    model = nn.generate_nn()
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
    n_inputs = 8
    n_hidden = model.layers[0].output_shape[1]
    n_outputs = model.layers[1].output_shape[1]

    dataset = loadtxt('Data/training.csv', delimiter=',')
    x = dataset[:, 0:8]
    y = dataset[:, 8]

    dimensions = (n_inputs * n_hidden) + (n_hidden * n_outputs) + n_hidden + n_outputs

    optimizer = ps.single.GlobalBestPSO(n_particles=100, dimensions=dimensions, options=options)

    cost, pos = optimizer.optimize(propagate_swarm, iters=10)
    return pos
    # print(cost)
    # print(pos)


def test(parameters):
    n_inputs = 8
    n_hidden = 10
    n_outputs = 1
    model = nn.generate_nn()
    dataset = loadtxt('Data/test_shuf.csv', delimiter=',')
    x = dataset[:, 0:8]
    y = dataset[:, 8]

    input_to_hidden = n_inputs * n_hidden
    input_to_hidden_bias = (n_inputs * n_hidden) + n_hidden

    hidden_to_output = (n_hidden * n_outputs) + input_to_hidden_bias
    hidden_to_output_bias = (n_hidden * n_outputs) + hidden_to_output

    W1 = parameters[0:input_to_hidden].reshape((n_inputs, n_hidden))
    B1 = parameters[input_to_hidden:input_to_hidden_bias].reshape((n_hidden, ))
    W2 = parameters[input_to_hidden_bias:hidden_to_output].reshape((n_hidden, n_outputs))
    B2 = parameters[hidden_to_output:hidden_to_output_bias].reshape((n_outputs, ))

    weights = [W1, B1, W2, B2]

    model.set_weights(weights)

    loss, acc = model.evaluate(x, y)

    return loss, acc


test(pso())
