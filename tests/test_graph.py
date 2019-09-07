#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import numpy as np
from numpy.testing import assert_array_almost_equal
import prestools.graph as pg


# pg.plot_heatmap_dendrogram

def test_plot_heatmap_dendrogram_empty_df(sample_empty_df):
    expect = False
    result = pg.plot_heatmap_dendrogram(sample_empty_df)
    assert result == expect


def test_plot_heatmap_dendrogram_one_entry_df(sample_one_entry_df):
    expect = False
    result = pg.plot_heatmap_dendrogram(sample_one_entry_df)
    assert result == expect


# pg.flatten_image

def test_flatten_image(sample_image_array):
    expect = np.array([[0.67826139], [0.29380381], [0.90714982],
                       [0.52835647], [0.4215251], [0.45017551],
                       [0.92814219], [0.96677647], [0.85304703],
                       [0.52351845], [0.19981397], [0.27417313],
                       [0.60659855], [0.00533165], [0.10820313],
                       [0.49978937], [0.34144279], [0.94630077]])
    result = pg.flatten_image(sample_image_array)
    assert_array_almost_equal(result, expect)


def test_flatten_image_scale(sample_image_array):
    expect = np.array([[2.65984859e-03], [1.15217180e-03], [3.55745027e-03],
                       [2.07198616e-03], [1.65303961e-03], [1.76539416e-03],
                       [3.63977329e-03], [3.79128027e-03], [3.34528247e-03],
                       [2.05301353e-03], [7.83584196e-04], [1.07518875e-03],
                       [2.37881784e-03], [2.09084314e-05], [4.24326000e-04],
                       [1.95995831e-03], [1.33899133e-03], [3.71098341e-03]])
    result = pg.flatten_image(sample_image_array, scale=True)
    assert_array_almost_equal(result, expect)


# pg.plot_confusion_matrix

def test_plot_confusion_matrix_empty_cm():
    cm = np.array([[0, 0], [0, 0]])
    expect = False
    result = pg.plot_confusion_matrix(cm, ["0", "1"])
    assert result == expect
