from __future__ import absolute_import
import six
import copy
import numpy as np
from six.moves import zip
from keras import backend as K

from keras.optimizers import Optimizer
from keras.legacy import interfaces
# from . import backend as K
# from .utils.generic_utils import serialize_keras_object
# from .utils.generic_utils import deserialize_keras_object

import tensorflow as tf
# if K.backend() == 'tensorflow':


class SGD2(Optimizer):
    """Stochastic gradient descent using second-order information.
   Ye, C., Yang, Y., Fermuller, C., & Aloimonos, Y. (2017). 
   On the Importance of Consistency in Training Deep Neural Networks. arXiv pre
   arXiv:1708.00631.
    # Arguments
        lr: float >= 0. Learning rate.
        momentum: float >= 0. Parameter updates momentum.
        decay: float >= 0. Learning rate decay over each update.
        nesterov: boolean. Whether to apply Nesterov momentum.
    """

    def __init__(self, lr=0.01, momentum=0., decay=0., nesterov=False, **kwargs):
        super(SGD2, self).__init__(**kwargs)
        with K.name_scope(self.__class__.__name__):
            self.iterations = K.variable(0, dtype='int64', name='iterations')
            self.lr = K.variable(lr, name='lr')
            self.momentum = K.variable(momentum, name='momentum')
            self.decay = K.variable(decay, name='decay')
        self.initial_decay = decay
        self.layer_inputs = []

    @interfaces.legacy_get_updates_support
    def get_updates(self, loss, params):
        grads = self.get_gradients(loss, params)
        self.updates = [K.update_add(self.iterations, 1)]
        lr = self.lr
        if self.initial_decay > 0:
            lr *= (1. / (1. + self.decay * K.cast(self.iterations, K.dtype(self.decay))))
        layer_count = 0
        lambda_value = 0.01
        # momentum
        shapes = [K.int_shape(p) for p in params]
        moments = [K.zeros(shape) for shape in shapes]
        self.weights = [self.iterations] + moments

        for p, g, m in zip(params, grads, moments):
            # gradients correction by second order information
            if len(K.int_shape(g)) > 1:
                x = self.layer_inputs[layer_count]
                shape_g = K.int_shape(g)
                # First permute the x, then compute transpose of x
                layer_count = layer_count + 1
                # For 3 channel image
                if len(K.int_shape(x)) == 4:
                    x = tf.transpose(x, perm=[3, 0, 1, 2])
                    x = tf.reshape(x, [K.int_shape(x)[0], -1])
                    x = tf.matmul(x, tf.transpose(x))
                    g = tf.transpose(g, perm=[2, 0, 1, 3])
                    g = tf.reshape(g, [K.int_shape(g)[0], -1])

                elif len(K.int_shape(x)) == 2:
                    xt = tf.reshape(x, [K.int_shape(x)[1], -1])
                    x = tf.matmul(xt, x)
                    x = tf.reshape(x, [K.int_shape(x)[0], K.int_shape(x)[0]])

                lambda_eye = tf.eye(K.int_shape(x)[0])
                corr_term = tf.matrix_inverse(tf.add(x, tf.multiply(lambda_value, lambda_eye)))
                g = tf.matmul(corr_term, g)
                g = tf.reshape(g, shape_g)

            v = self.momentum * m - lr * g  # velocity
            self.updates.append(K.update(m, v))
            new_p = p + v
            self.updates.append(K.update(p, new_p))
        return self.updates

    def get_config(self):
        config = {'lr': float(K.get_value(self.lr)),
                  'momentum': float(K.get_value(self.momentum)),
                  'decay': float(K.get_value(self.decay))}
        base_config = super(SGD2, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))
