#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import numpy as np
from typing import Union


def sigmoid(z: Union[int, np.ndarray]) -> Union[int, np.ndarray]:
    """Calculate the sigmoid function of z.

    :param Union[int,np.ndarray] z: input scalar or numpy array

    :return: Union[int,np.ndarray]
    """
    a = 1 / (1 + np.exp(-z))

    return a


def sigmoid_gradient(z: Union[int, np.ndarray]) -> Union[int, np.ndarray]:
    """Calculate the gradient of the sigmoid function of z.

    :param Union[int,np.ndarray] z: input scalar or numpy array

    :return: Union[int,np.ndarray]
    """
    a = sigmoid(z)
    da = a * (1 - a)

    return da


def flatten_image(img: np.ndarray, scale: bool = False) -> np.ndarray:
    """Convert an image array to a single-dimension vector.

    :param np.ndarray img: input image array of shape (l, h, d = 3)

    :param bool scale: scale resulting vector dividing its values by 255
        (default: False)

    :return: np.ndarray of shape (l * h * d, 1)
    """
    v = img.reshape(img.shape[0] * img.shape[1] * img.shape[2], 1)
    if scale:
        return v / 255

    return v


def softmax(x: np.ndarray) -> np.ndarray:
    """Calculate the softmax function for each row of x.

    :param np.ndarray x: input numpy array

    :return: np.ndarray
    """
    x_exp = np.exp(x)
    try:
        s = x_exp / np.sum(x_exp, axis=1, keepdims=True)
    except np.AxisError:  # x.ndim == 1
        s = x_exp / np.sum(x_exp, keepdims=True)

    return s


def loss_L1(yhat: np.ndarray, y: np.ndarray) -> np.float64:
    """Calculate the L1 loss function of the given predictions vs true
    values.

    :param np.ndarray yhat: input array with predictions

    :param np.ndarray y: input array with true values

    :return: np.float64
    """
    loss = np.sum(np.abs(y - yhat))

    return loss


def loss_L2(yhat: np.ndarray, y: np.ndarray) -> np.float64:
    """Calculate the L2 loss function of the given predictions vs true
    values.

    :param np.ndarray yhat: input array with predictions

    :param np.ndarray y: input array with true values

    :return: np.float64
    """
    loss = np.sum(np.dot((y - yhat), (y - yhat)))

    return loss


def relu(z):
    """Calculate the ReLU activation function of z.

    :param z: input numpy array

    :return:
    """
    a = np.maximum(0, z)

    return a


def relu_gradient(z: Union[int, np.ndarray]) -> Union[int, np.ndarray]:
    """Calculate the gradient of the ReLU function of z.

    :param Union[int,np.ndarray] z: input scalar or numpy array

    :return: Union[int,np.ndarray]
    """
    a = relu(z)
    da = np.zeros_like(a)
    da[z > 0] = 1.0
    # TODO: or also
    # da = np.heaviside(z, 0)

    return da
