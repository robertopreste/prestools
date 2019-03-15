#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import prestools.misc as pm


# pm.flatten()

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
    result = pm.flatten([0, 2, [[2, 3], None, 8, 100, 4, [[[50, None]]]], -2],
                        drop_null=True)
    assert result == expect


def test_flatten_multiple_types():
    expect = [0, 2, 2, 3, None, 8, "0", "1", "2", 100, 4, 50, None, -2]
    result = pm.flatten([0, 2, [(2, 3), None, 8, ["0", ["1", "2"]], 100, 4,
                                [[[50, None]]]], -2])
    assert result == expect


def test_flatten_multiple_types_drop_null():
    expect = [0, 2, 2, 3, 8, "0", "1", "2", 100, 4, 50, -2]
    result = pm.flatten([0, 2, [(2, 3), None, 8, ["0", ["1", "2"]], 100, 4,
                                [[[50, None]]]], -2],
                        drop_null=True)
    assert result == expect


# pm.invert_dict()

def test_invert_dict_single_key_single_val():
    expect = {"A": 1}
    result = pm.invert_dict({1: ["A"]})
    assert result == expect


def test_invert_dict_single_key_multiple_val():
    expect = {"A": 1, "I": 1, "E": 1, "U": 1, "O": 1}
    result = pm.invert_dict({1: ["A", "I", "E", "U", "O"]})
    assert result == expect


def test_invert_dict_single_key_multiple_val_sort_keys():
    expect = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1}
    result = pm.invert_dict({1: ["A", "I", "E", "U", "O"]}, sort_keys=True)
    assert result == expect


def test_invert_dict_multiple_key_multiple_val():
    expect = {"A": 1, "E": 1, "D": 2, "G": 2}
    result = pm.invert_dict({1: ["A", "E"], 2: ["D", "G"]})
    assert result == expect


def test_invert_dict_multiple_key_multiple_val_sort_keys():
    expect = {"A": 1, "D": 2, "E": 1, "G": 2}
    result = pm.invert_dict({1: ["A", "E"], 2: ["D", "G"]}, sort_keys=True)
    assert result == expect


# pm.prime_factors()

def test_prime_factors_one():
    expect = []
    result = pm.prime_factors(1)
    assert result == expect


def test_prime_factors_square():
    expect = [3, 3]
    result = pm.prime_factors(9)
    assert result == expect


def test_prime_factors_cube():
    expect = [3, 3, 3]
    result = pm.prime_factors(27)
    assert result == expect


def test_prime_factors_mixed():
    expect = [5, 17, 23, 461]
    result = pm.prime_factors(901255)
    assert result == expect


def test_prime_factors_large():
    expect = [11, 9539, 894119]
    result = pm.prime_factors(93819012551)
    assert result == expect
