#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import prestools.misc as pm


def test_flatten_no_nesting():
    expect = [0, 1, 2]
    result = pm.flatten([0, 1, 2])
    assert result == expect


def test_flatten_no_nesting_drop_null():
    expect = [0, 1, 2]
    result = pm.flatten([0, 1, 2], drop_null=True)
    assert result == expect


def test_flatten_nested():
    expect = [0, 2, 2, 3, None, 8, 100, 4, 50, None, -2]
    result = pm.flatten([0, 2, [[2, 3], None, 8, 100, 4, [[[50, None]]]], -2])
    assert result == expect


def test_flatten_nested_drop_null():
    expect = [0, 2, 2, 3, 8, 100, 4, 50, -2]
    result = pm.flatten([0, 2, [[2, 3], None, 8, 100, 4, [[[50, None]]]], -2], drop_null=True)
    assert result == expect


def test_flatten_multiple_types():
    expect = [0, 2, 2, 3, None, 8, "0", "1", "2", 100, 4, 50, None, -2]
    result = pm.flatten([0, 2, [(2, 3), None, 8, ["0", ["1", "2"]], 100, 4, [[[50, None]]]], -2])
    assert result == expect


def test_flatten_multiple_types_drop_null():
    expect = [0, 2, 2, 3, 8, "0", "1", "2", 100, 4, 50, -2]
    result = pm.flatten([0, 2, [(2, 3), None, 8, ["0", ["1", "2"]], 100, 4, [[[50, None]]]], -2],
                        drop_null=True)
    assert result == expect



