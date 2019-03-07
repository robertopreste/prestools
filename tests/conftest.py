#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import pandas as pd


@pytest.fixture
def sample_corr_df() -> pd.DataFrame:
    """
    Returns a sample dataframe with pairwise correlations of features.
    :return: pd.Dataframe
    """
    df = pd.DataFrame({
        "feat_a": [1.0, -0.20, -0.05, -0.10, 0.17],
        "feat_b": [-0.20, 1.0, -0.04, -0.08, -0.15],
        "feat_c": [-0.05, -0.04, 1.0, -0.11, -0.56],
        "feat_d": [-0.10, -0.08, -0.11, 1.0, -0.20],
        "feat_e": [0.17, -0.15, -0.56, -0.20, 1.0]
    }, index=["feat_a", "feat_b", "feat_c", "feat_d", "feat_e"])
    return df


@pytest.fixture
def sample_empty_df() -> pd.DataFrame:
    """
    Returns an empty dataframe (with shape (0, 0)).
    :return: pd.Dataframe
    """
    df = pd.DataFrame()
    return df


@pytest.fixture
def sample_one_entry_df() -> pd.DataFrame:
    """
    Returns a dataframe with a single value (with shape (1, 1)).
    :return: pd.Dataframe
    """
    df = pd.DataFrame({"feat_a": [1.0]}, index=["feat_a"])
    return df

