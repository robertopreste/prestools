#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch
from typing import Union


def flatten_image(img: np.ndarray, scale: bool = False) -> np.ndarray:
    """Convert an image array to a single-dimension vector.

    Args:
        img: input image array of shape (l, h, d = 3)
        scale: scale resulting vector dividing its values by 255
            (default: False)

    Returns:
        v: reshaped vector of shape (l * h * d, 1)
    """
    v = img.reshape(img.shape[0] * img.shape[1] * img.shape[2], 1)
    if scale:
        return v / 255

    return v


def plot_heatmap_dendrogram(df: pd.DataFrame,
                            cmap: str = "RdBu_r",
                            title: str = "Cluster Heatmap",
                            save: Union[bool, str] = False,
                            method: str = "ward") -> bool:
    """Plot a heatmap with hierarchical clustering of a dataframe.

    Create (and optionally save) a heatmap with hierarchical clustering
    created using Seaborn, starting from a given dataframe of
    correlations.

    See Also:
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html

    Args:
        df: input dataframe of correlations
        cmap: colormap to use (default: 'RdBu_r')
        title: title for resulting plot (default: 'Cluster Heatmap')
        save: if False, the plot will not be saved, just shown; otherwise
            it is possible to specify the path/filename where the file
            will be saved (default: False)
        method: method to use to cluster the data (default: 'ward')
    """
    if df.shape == (0, 0) or df.shape == (1, 1):
        return False
    cm = sns.clustermap(df, method=method, figsize=(20, 16), vmin=-1, vmax=1,
                        annot=True, cmap=cmap)
    plt.suptitle(title, fontsize=22)
    if save:
        cm.savefig(save)
    plt.show()

    return True


def plot_dendrogram(df: Union[pd.DataFrame, np.ndarray],
                    cut_off: Union[bool, float] = False,
                    title: str = "Dendrogram",
                    save: Union[bool, str] = False,
                    method: str = "ward") -> bool:
    """Plot a dendrogram plot from a dataframe.

    Create (and optionally save) a dendrogram plot starting from a given
    dataframe of correlations. It is also possible to add a cut-off line
    given a distance to use for separating clusters.

    See Also:
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html

    Args:
        df: input dataframe of correlations
        cut_off: if not False, a vertical line will be added to better
            identify clusters (default: False)
        title: title for resulting plot (default: 'Dendrogram')
        save: if False, the plot will not be saved, just shown; otherwise
            it is possible to specify the path/filename where the file
            will be saved (default: False)
        method: method to use to cluster the data (default: 'ward')
    """
    if df.shape == (0, 0) or df.shape == (1, 1):
        return False
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

    return True


def reduce_xaxis_ticks(ax: plt.Axes, step: int):
    """Show every ith x axis tick.

    Args:
        ax: axis to be adjusted
        step: factor to reduce the number of x axis ticks by

    Examples:
        >>> fig, ax = plt.subplots()
        >>> reduce_xaxis_ticks(ax, 5)
    """
    plt.setp(ax.xaxis.get_ticklabels(), visible=False)
    for label in ax.xaxis.get_ticklabels()[step-1::step]:
        label.set_visible(True)

    return


def reduce_yaxis_ticks(ax: plt.Axes, step: int):
    """Show every ith y axis tick.

    Args:
        ax: axis to be adjusted
        step: factor to reduce the number of y axis ticks by

    Examples:
        >>> fig, ax = plt.subplots()
        >>> reduce_yaxis_ticks(ax, 5)
    """
    plt.setp(ax.yaxis.get_ticklabels(), visible=False)
    for label in ax.yaxis.get_ticklabels()[step - 1::step]:
        label.set_visible(True)

    return
