#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from collections import Iterable
from typing import List


def flatten(iterable: Iterable, drop_null: bool = False) -> list:
    """
    Flatten a nested iterable, even with multiple nesting levels and different
    data types. It is also possible to drop null values (None) from the
    resulting list.
    :param Iterable iterable: nested iterable to flatten
    :param bool drop_null: filter out None from the flattened list
    (default = False)
    :return: list
    """
    def flattenator(element):
        for el in element:
            if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
                yield from flattenator(el)
            else:
                yield el

    if drop_null:
        return list(filter(None.__ne__, list(flattenator(iterable))))
    return list(flattenator(iterable))


def invert_dict(input_dict: dict, sort_keys: bool = False) -> dict:
    """
    Invert a given dictionary, creating a new dictionary where each key is
    created from a value of the original dictionary, and its value is the key
    that it was associated to in the original dictionary (e.g. invert_dict({1:
    ["A", "E"], 2: ["D", "G"]}) = {"A": 1, "E": 1, "D": 2, "G": 2}).
    It is also possible to return an inverted dictionary with keys in
    alphabetical order, although this makes little sense for intrinsically
    unordered data structures like dictionaries, but it may be useful when
    printing the results.
    :param dict input_dict: original dictionary to be inverted
    :param bool sort_keys: sort the keys in the inverted dictionary in
    alphabetical order (default = False)
    :return: dict
    """
    new_dict = {el: x for x in input_dict for el in input_dict[x]}
    if sort_keys:
        return {el: new_dict[el] for el in sorted(new_dict)}
    return new_dict


def prime_factors(number: int) -> List[int]:
    """
    Calculate the prime factors of a given natural number. Note that 1 is not a
    prime number, so it will not be included.
    :param number: input natural number
    :return: List[int]
    """
    factors = []
    i = 2
    while number > 1:
        if number % i == 0:
            number = number // i
            factors.append(i)
            continue
        i += 1
    return factors
