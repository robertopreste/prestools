#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest
import prestools.misc as pm

DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
SAME1 = os.path.join(DATADIR, "same1.txt")
SAME2 = os.path.join(DATADIR, "same2.txt")
SAMENOT = os.path.join(DATADIR, "samenot.txt")
SIZENOT = os.path.join(DATADIR, "sizenot.txt")


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


# pm.filter_type

def test_filter_type_int():
    expect = [1, 2, 3]
    result = pm.filter_type([1, [3, "a"], 2, "ab", 3],
                            int)
    assert result == expect


def test_filter_type_str():
    expect = ["a", "b", "c"]
    result = pm.filter_type(["a", [3, "bc"], "b", 2, "c"],
                            str)
    assert result == expect


def test_filter_type_list():
    expect = [[1, "a"], ["2", 3]]
    result = pm.filter_type(["a", [1, "a"], 2, "b", ["2", 3]],
                            list)
    assert result == expect


# pm.wordcount

def test_wordcount():
    expect = {"word": 2, "test": 1, "wordcount": 1}
    result = pm.wordcount("word test wordcount word")
    assert result == expect


def test_wordcount_specific_word():
    expect = 2
    result = pm.wordcount("word test wordcount word",
                          "word")
    assert result == expect


def test_wordcount_specific_word_not_present():
    expect = 0
    result = pm.wordcount("word test wordcount word",
                          "prova")
    assert result == expect


def test_wordcount_ignore_case_true():
    expect = {"word": 2, "test": 1, "wordcount": 1}
    result = pm.wordcount("word test wordcount WORD",
                          ignore_case=True)
    assert result == expect


def test_wordcount_ignore_case_false():
    expect = {"word": 1, "test": 1, "wordcount": 1, "WORD": 1}
    result = pm.wordcount("word test wordcount WORD",
                          ignore_case=False)
    assert result == expect


def test_wordcount_specific_word_ignore_case_true():
    expect = 2
    result = pm.wordcount("word test wordcount WORD",
                          "word",
                          ignore_case=True)
    assert result == expect


def test_wordcount_specific_word_ignore_case_false():
    expect = 1
    result = pm.wordcount("word test wordcount WORD",
                          "word",
                          ignore_case=False)
    assert result == expect


# pm.equal_files

def test_equal_files():
    expect = True
    result = pm.equal_files(SAME1, SAME2)
    assert result == expect


def test_equal_files_false():
    expect = False
    result = pm.equal_files(SAME1, SAMENOT)
    assert result == expect


def test_equal_files_false_size():
    expect = False
    result = pm.equal_files(SAME1, SIZENOT)
    assert result == expect


# pm.benchmark

def test_benchmark():
    @pm.benchmark
    def t_sum():
        return sum([1, 2, 3])

    result = t_sum()

    assert isinstance(result, tuple)
    assert result[0] == "t_sum"
    assert isinstance(result[1], float)
    assert result[2] == 6
