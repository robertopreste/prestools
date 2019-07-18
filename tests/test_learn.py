#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import prestools.learn as pl
import numpy as np
from numpy.testing import assert_array_almost_equal, assert_array_equal


# pl.sigmoid()

def test_sigmoid_scalar():
    expect = 0.9525741268224334
    result = pl.sigmoid(3)
    assert result == expect


def test_sigmoid_vector():
    expect = np.array([0.73105858, 0.88079708, 0.95257413])
    result = pl.sigmoid(np.array([1, 2, 3]))
    assert_array_almost_equal(result, expect)


# pl.sigmoid_gradient()

def test_sigmoid_gradient_scalar():
    expect = 0.045176659730912
    result = pl.sigmoid_gradient(3)
    assert result == expect


def test_sigmoid_gradient_vector():
    expect = np.array([0.19661193, 0.10499359, 0.04517666])
    result = pl.sigmoid_gradient(np.array([1, 2, 3]))
    assert_array_almost_equal(result, expect)


# pl.flatten_image

def test_flatten_image(sample_image_array):
    expect = np.array([[0.67826139], [0.29380381], [0.90714982],
                       [0.52835647], [0.4215251], [0.45017551],
                       [0.92814219], [0.96677647], [0.85304703],
                       [0.52351845], [0.19981397], [0.27417313],
                       [0.60659855], [0.00533165], [0.10820313],
                       [0.49978937], [0.34144279], [0.94630077]])
    result = pl.flatten_image(sample_image_array)
    assert_array_equal(result, expect)


def test_flatten_image_scale(sample_image_array):
    expect = np.array([[2.65984859e-03], [1.15217180e-03], [3.55745027e-03],
                       [2.07198616e-03], [1.65303961e-03], [1.76539416e-03],
                       [3.63977329e-03], [3.79128027e-03], [3.34528247e-03],
                       [2.05301353e-03], [7.83584196e-04], [1.07518875e-03],
                       [2.37881784e-03], [2.09084314e-05], [4.24326000e-04],
                       [1.95995831e-03], [1.33899133e-03], [3.71098341e-03]])
    result = pl.flatten_image(sample_image_array, scale=True)
    assert_array_almost_equal(result, expect)


# pl.softmax()

def test_softmax():
    expect = np.array([[9.81135202e-01, 8.94679497e-04, 1.79701181e-02],
                       [8.80090205e-01, 1.19107257e-01, 8.02538386e-04]])
    result = pl.softmax(np.array([[9, 2, 5], [7, 5, 0]]))
    assert_array_almost_equal(result, expect)


def test_softmax_ndim_1():
    expect = np.array([0.0320586, 0.08714432, 0.23688282, 0.64391426])
    result = pl.softmax(np.array([1, 2, 3, 4]))
    assert_array_almost_equal(result, expect)


# pl.loss_L1()

def test_loss_L1():
    expect = 1.1
    result = pl.loss_L1(np.array([0.9, 0.2, 0.1, 0.4, 0.9]),
                        np.array([1, 0, 0, 1, 1]))
    assert result == expect


# pl.loss_L2()

def test_loss_L2():
    expect = 0.43
    result = pl.loss_L2(np.array([0.9, 0.2, 0.1, 0.4, 0.9]),
                        np.array([1, 0, 0, 1, 1]))
    assert result == expect
