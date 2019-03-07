#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import prestools.clustering as pc


def test_hierarchical_clustering_empty_df(sample_empty_df):
    expect = None
    result = pc.hierarchical_clustering(sample_empty_df)
    assert result == expect

