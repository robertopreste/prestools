#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import random
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch
from typing import Union, Optional
from string import ascii_letters


def plot_heatmap_dendrogram(df: pd.DataFrame,
                            cmap: str = "RdBu_r",
                            title: str = "Cluster Heatmap",
                            save: Union[bool, str] = False,
                            method: str = "ward") -> bool:
    """Plot a heatmap with hierarchical clustering of a dataframe.

    Create (and optionally save) a heatmap with hierarchical clustering
    created using Seaborn, starting from a given dataframe of
    correlations.

    :param pd.Dataframe df: input dataframe of correlations

    :param str cmap: colormap to be used (default = 'RdBu_r')

    :param str title: title for the resulting plot (default = 'Cluster
        Heatmap')

    :param Union[bool,str] save: if False, the plot will not be saved,
        just shown; otherwise it is possible to specify the path/filename
        where the file will be saved (default = False)

    :param str method: method to be used to cluster the data
        (default = 'ward')

    :return: bool
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

    :param Union[pd.Dataframe,np.ndarray] df: input dataframe of
        correlations

    :param Union[bool,float] cut_off: if not False, a vertical line will
        be added that can be used to better identify clusters
        (default = False)

    :param str title: title for the resulting plot
        (default = 'Dendrogram')

    :param Union[bool,str] save: if False, the plot will not be saved,
        just shown; otherwise it is possible to specify the path/filename
        where the file will be saved (default = False)

    :param str method: method to be used to cluster the data
        (default = 'ward')

    :return: bool
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


def random_image(save: Optional[str] = None) -> bool:
    """Retrieve a random image from the web.

    Retrieve and save a random image from the web, using the service
    provided by Picsum. The downloaded image can be opened using
    IPython.display.Image().

    :param Optional[str] save: if a path/filename is provided, the image
        will be saved to the given destination; otherwise, a random name will
        be created, taking care that no other files with the same name are
        present

    :return: bool
    """
    def random_suffix(length: int = 6) -> str:
        """Create a random string of the given length.

        Return a random string of the given length which will be used
        as suffix for the image filename.

        :param int length: desired length of the random string
            (default: 6)

        :return: str
        """
        return "".join([random.choice(ascii_letters) for _ in range(length)])

    rnd_art = requests.get("https://picsum.photos/500/500/?random")
    rnd_name = "random_img_{}.png".format(random_suffix())

    if save:
        # if given path is a directory
        if os.path.isdir(save):
            # if rnd_name already exists, will create a new rnd_name
            while os.path.isfile(os.path.join(save, rnd_name)):
                rnd_name = "random_img_{}.png".format(random_suffix())
            filename = os.path.join(save, rnd_name)
        elif os.path.isfile(save):  # provided filename already exists
            raise FileExistsError
        else:
            filename = save
    else:
        while os.path.isfile(rnd_name):
            rnd_name = "random_img_{}.png".format(random_suffix())
        filename = rnd_name

    with open(filename, "wb") as f:
        f.write(rnd_art.content)

    return True





