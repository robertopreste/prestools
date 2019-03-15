#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import prestools.clustering as pc
import numpy as np


# pc.hierarchical_clustering

def test_hierarchical_clustering_empty_df(sample_empty_df):
    expect = None
    result = pc.hierarchical_clustering(sample_empty_df)
    assert result == expect


def test_hierarchical_clustering_one_entry_df(sample_one_entry_df):
    expect = None
    result = pc.hierarchical_clustering(sample_one_entry_df)
    assert result == expect


def test_hierarchical_clustering_sample_df(sample_corr_df):
    expect_linkage = np.array([[0.0, 4.0, 1.28467895, 2.0],
                               [1.0, 3.0, 1.5330362, 2.0],
                               [2.0, 6.0, 1.58692575, 3.0],
                               [5.0, 7.0, 2.20363941, 5.0]])
    expect_pair_dist = np.array([1.72710741, 1.66240789, 1.60464949,
                                 1.28467895, 1.53450318, 1.5330362,
                                 1.75119959, 1.61180024, 2.22166604,
                                 1.77772326])
    expect_coph_dist = 0.7027486505845463
    expect_coph_matr = np.array([2.20363941, 2.20363941, 2.20363941,
                                 1.28467895, 1.58692575, 1.5330362,
                                 2.20363941, 1.58692575, 2.20363941,
                                 2.20363941])
    result = pc.hierarchical_clustering(sample_corr_df)
    assert np.allclose(result.linkage, expect_linkage)
    assert np.allclose(result.pair_dist, expect_pair_dist)
    assert np.allclose(result.coph_dist, expect_coph_dist)
    assert np.allclose(result.coph_matr, expect_coph_matr)


# pc.find_n_clusters_elbow

def test_find_n_clusters_elbow_empty_df(sample_empty_df):
    expect = None
    result = pc.find_n_clusters_elbow(sample_empty_df)
    assert result == expect


def test_find_n_clusters_elbow_one_entry_df(sample_one_entry_df):
    expect = None
    result = pc.find_n_clusters_elbow(sample_one_entry_df)
    assert result == expect


def test_find_n_clusters_elbow_sample_df(sample_corr_df):
    expect = 2
    result = pc.find_n_clusters_elbow(sample_corr_df)
    assert result == expect


