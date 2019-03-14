#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as sch
import scipy.spatial.distance as ssd
import matplotlib.pyplot as plt
from typing import Union
from .classes import HierCluster


def hierarchical_clustering(df: Union[pd.DataFrame, np.ndarray],
                            method: str = "ward") -> Union[HierCluster, None, ValueError]:
    """
    Returns clustering created using scipy from a given dataframe of correlations. Uses the
    HierCluster class available in prestools.classes
    :param Union[pd.Dataframe, np.ndarray] df: input dataframe of correlations
    :param str method: method to be used to cluster the data ['ward', 'single', 'complete',
    'average', 'weighted', 'centroid', 'median'] (default = 'ward')
    :return: Union[HierCluster, None, ValueError]
    """
    if method not in ["ward", "single", "complete", "average", "weighted", "centroid", "median"]:
        return ValueError("Method not valid!")
    if df.shape == (0, 0) or df.shape == (1, 1):
        return
    cl = HierCluster()
    cl.linkage = sch.linkage(df, method=method)
    cl.pair_dist = ssd.pdist(df)
    cl.coph_dist, cl.coph_matr = sch.cophenet(cl.linkage, cl.pair_dist)

    return cl


def find_n_clusters_elbow(df: Union[pd.DataFrame, np.ndarray],
                          plot: bool = False,
                          method: str = "ward") -> Union[int, None, ValueError]:
    """
    Find the suggested number of clusters for the given dataframe of correlations, using the elbow
    method.
    :param Union[pd.Dataframe, np.ndarray] df: input dataframe of correlations
    :param bool plot: plot the resulting elbow plot (default: False)
    :param str method: method to be used to cluster the data ['ward', 'single', 'complete',
    'average', 'weighted', 'centroid', 'median'] (default = 'ward')
    :return:
    """
    if method not in ["ward", "single", "complete", "average", "weighted", "centroid", "median"]:
        return ValueError("Method not valid!")
    if df.shape == (0, 0) or df.shape == (1, 1):
        return
    cl = hierarchical_clustering(df, method=method)
    Z = cl.linkage[:, 2]
    acceleration = np.diff(Z, 2)
    acceleration_rev = acceleration[::-1]
    if len(acceleration_rev) == 0:
        return
    n_clusters = acceleration_rev.argmax() + 2

    if plot:
        Z_rev = Z[::-1]
        idxs = np.arange(1, len(Z) + 1)
        plt.plot(idxs, Z_rev)
        plt.plot(idxs[:-2] + 1, acceleration_rev)
        plt.axvline(n_clusters, color="red", linestyle="--")
        plt.xlabel("num of clusters", fontsize=14)
        plt.ylabel("acceleration of distance growth", fontsize=14)
        plt.title("Suggested number of clusters: {}".format(n_clusters), fontsize=22)
        plt.show()

    return n_clusters


