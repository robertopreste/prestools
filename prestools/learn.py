#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import numpy as np
from typing import Union


def sigmoid(x: Union[int, np.ndarray]) -> Union[int, np.ndarray]:
    """Calculate the sigmoid of x.

    :param Union[int,np.ndarray] x: input scalar or numpy array

    :return: Union[int,np.ndarray]
    """
    s = 1 / (1 + np.exp(-x))

    return s


def sigmoid_gradient(x: Union[int, np.ndarray]) -> Union[int, np.ndarray]:
    """Calculate the gradient (aka slope or derivative) of the sigmoid
    function of x.

    :param Union[int,np.ndarray] x: input scalar or numpy array

    :return: Union[int,np.ndarray]
    """
    s = sigmoid(x)
    ds = s * (1 - s)

    return ds


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
