# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras import backend as K
from keras.constraints import maxnorm
from keras.optimizers import SGD, adadelta, Adam
from keras.regularizers import l2

def generate_nn():
    model = Sequential()
    model.add(Dense(10, input_dim=8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer="Adam", metrics=['acc'])
    return model


def generate_nn_fo(p1, p2, p3):
    model = Sequential()
    model.add(Dense(10, input_dim=8, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation='sigmoid'))

    first_opt = Adam(lr=p1, beta_1=p2, beta_2=p3)
    model.compile(loss='binary_crossentropy', optimizer=first_opt, metrics=['acc'])
    return model



def generate_nn_so(p1, p2):
    model = Sequential()
    model.add(Dense(10, input_dim=8, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation='sigmoid'))

    second_opt = adadelta(lr=p1, rho=p2)
    model.compile(loss='binary_crossentropy', optimizer=second_opt, metrics=['acc'])
    return model


# # load the dataset
# # dataset = loadtxt('pima-indians-diabetes.data.csv', delimiter=',')
# dataset = loadtxt('Data/training.csv', delimiter=',')
# # split into input (X) and output (y) variables
# X = dataset[:, 0:8]
# y = dataset[:, 8]
# test_dataset = loadtxt('pulsar_stars.csv', delimiter=',')
# # split into input (X) and output (y) variables
# test_X = test_dataset[:, 0:8]
# test_y = test_dataset[:, 8]
# # define the keras model
# model = generate_nn()
# # fit the keras model on the dataset
# model.fit(X, y, epochs=50, batch_size=10)
# # evaluate the keras model
# _, accuracy = model.evaluate(test_X, test_y)
# print('Accuracy: %.2f' % (accuracy * 100))
