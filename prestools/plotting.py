#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch
from typing import Union


def plot_heatmap_dendrogram(df: pd.DataFrame, cmap: str = "RdBu_r",
                            title: str = "Cluster Heatmap",
                            save: Union[bool, str] = False,
                            method: str = "ward"):
    """Plot a heatmap with hierarchical clustering of a dataframe.

    Create (and optionally save) a heatmap with hierarchical clustering
    created using Seaborn, starting from a given dataframe of
    correlations.
    :param pd.Dataframe df: input dataframe of correlations
    :param str cmap: colormap to be used (default = 'RdBu_r')
    :param str title: title for the resulting plot (default = 'Cluster
    Heatmap')
    :param Union[bool, str] save: if False, the plot will not be saved,
    just shown; otherwise it is possible to specify the path/filename
    where the file will be saved (default = False)
    :param str method: method to be used to cluster the data
    (default = 'ward')
    :return:
    """
    if df.shape == (0, 0) or df.shape == (1, 1):
        return
    cm = sns.clustermap(df, method=method, figsize=(20, 16), vmin=-1, vmax=1,
                        annot=True, cmap=cmap)
    plt.suptitle(title, fontsize=22)
    if save:
        cm.savefig(save)
    plt.show()


def plot_dendrogram(df: Union[pd.DataFrame, np.ndarray],
                    cut_off: Union[bool, float] = False,
                    title: str = "Dendrogram",
                    save: Union[bool, str] = False,
                    method: str = "ward"):
    """Plot a dendrogram plot from a dataframe.

    Create (and optionally save) a dendrogram plot starting from a given
    dataframe of correlations. It is also possible to add a cut-off line
    given a distance to use for separating clusters.
    :param Union[pd.Dataframe, np.ndarray] df: input dataframe of
    correlations
    :param Union[bool, float] cut_off: if not False, a vertical line will
    be added that can be used to better identify clusters
    (default = False)
    :param str title: title for the resulting plot
    (default = 'Dendrogram')
    :param Union[bool, str] save: if False, the plot will not be saved,
    just shown; otherwise it is possible to specify the path/filename
    where the fill will be saved (default = False)
    :param str method: method to be used to cluster the data
    (default = 'ward')
    :return:
    """
    if df.shape == (0, 0) or df.shape == (1, 1):
        return
    Z = sch.linkage(df, method=method)
    # dists = ssd.pdist(df)
    # c, coph_dists = sch.cophenet(Z, dists)
    plt.figure(figsize=(20, 16))
    sch.dendrogram(Z, leaf_font_size=16, labels=df.columns, orientation="left")
    if cut_off:
        plt.axvline(x=cut_off, linewidth=4.0, linestyle="--")
    plt.title(title, fontsize=22)
    plt.xlabel("distance", fontsize=14)
    plt.ylabel("feature", fontsize=14)
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14)
    if save:
        plt.savefig(save)
    plt.show()
