#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as sch
import scipy.spatial.distance as ssd
from typing import Union


def hierarchical_clustering(df: Union[pd.DataFrame, np.ndarray], method: str = "ward") -> dict:
    """
    Returns clustering created using scipy from a given dataframe of correlations.
    :param Union[pd.Dataframe, np.ndarray] df: input dataframe of correlations
    :param str method: method to be used to cluster the data (default = 'ward')
    :return: dict
    """
    Z = sch.linkage(df, method=method)
    dists = ssd.pdist(df)
    c, coph_dists = sch.cophenet(Z, dists)
    res = {"Z": Z, "dists": dists, "c": c, "coph_dists": coph_dists}

    return res

