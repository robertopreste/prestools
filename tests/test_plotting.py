#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import prestools.plotting as pp


def test_plot_heatmap_dendrogram_empty_df(sample_empty_df):
    expect = None
    result = pp.plot_heatmap_dendrogram(sample_empty_df)
    assert result == expect


def test_plot_heatmap_dendrogram_one_entry_df(sample_one_entry_df):
    expect = None
    result = pp.plot_heatmap_dendrogram(sample_one_entry_df)
    assert result == expect

