#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import numpy as np
from click.testing import CliRunner
from prestools import cli


# find_n_clusters_elbow
#
# def test_cli_find_n_clusters_elbow_empty_df(sample_empty_df):
#     runner = CliRunner()
#     expect = ""
#     result = runner.invoke(cli.main, ["clustering", "find_n_clusters_elbow", sample_empty_df])
