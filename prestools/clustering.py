#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as sch
import scipy.spatial.distance as ssd
from typing import Union
from .classes import HierCluster


def hierarchical_clustering(df: Union[pd.DataFrame, np.ndarray],
                            method: str = "ward") -> Union[HierCluster, None]:
    """
    Returns clustering created using scipy from a given dataframe of correlations. Uses the
    HierCluster class available in prestools.classes
    :param Union[pd.Dataframe, np.ndarray] df: input dataframe of correlations
    :param str method: method to be used to cluster the data (default = 'ward')
    :return: HierCluster
    """
    if df.shape == (0, 0) or df.shape == (1, 1):
        return
    cl = HierCluster()
    cl.linkage = sch.linkage(df, method=method)
    cl.pair_dist = ssd.pdist(df)
    cl.coph_dist, cl.coph_matr = sch.cophenet(cl.linkage, cl.pair_dist)

    return cl

