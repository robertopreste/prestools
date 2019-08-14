#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import prestools.clustering as pc


@click.group()
def clustering():
    """
    Data clustering utilities
    """
    pass


@clustering.command()
@click.argument("df")
@click.option("--method", "-m", default="ward",
              type=click.Choice(["ward", "single", "complete", "average",
                                 "weighted", "centroid", "median"]),
              help="""Method to be used to cluster the data ['ward', 
              'single', 'complete', 'average', 'weighted', 'centroid', 
              'median'] (default = 'ward')""")
def find_n_clusters_elbow(df, method):
    """Find the number of clusters using the elbow method

    Find the suggested number of clusters for the given dataframe of
    correlations, using the elbow method.
    """
    result = pc.find_n_clusters_elbow(df, method=method)
    click.echo(result)
