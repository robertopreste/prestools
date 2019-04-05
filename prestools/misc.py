#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import re 
from collections import Iterable
from typing import List, Any, Type, Union


def flatten(iterable: Iterable, drop_null: bool = False) -> list:
    """Flatten out a nested iterable.

    Flatten a nested iterable, even with multiple nesting levels and
    different data types. It is also possible to drop null values (None)
    from the resulting list.
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
    """Create a new dictionary swapping keys and values.

    Invert a given dictionary, creating a new dictionary where each key is
    created from a value of the original dictionary, and its value is the
    key that it was associated to in the original dictionary
    (e.g. invert_dict({1: ["A", "E"], 2: ["D", "G"]}) =
    {"A": 1, "E": 1, "D": 2, "G": 2}).
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
    """Calculate the prime factors of a number.

    Calculate the prime factors of a given natural number. Note that 1 is
    not a prime number, so it will not be included.
    :param int number: input natural number
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


def filter_type(input_list: List[Any], target_type: Type) -> List[Any]:
    """Only keep elements of a given type from a list of elements.

    Traverse a list and return a new list with only elements of the original
    list belonging to a given type.
    :param List[Any] input_list: input list to filter
    :param Type target_type:
    :return: List[Any]
    """
    return [el for el in input_list if type(el) == target_type]


def wordcount(sentence: str,
              word: Union[bool, str] = False,
              ignore_case: bool = False) -> Union[dict, int]:
    """Count occurrences of words in a sentence.

    Return the number of occurrences of each word in the given sentence,
    in the form of a dictionary; it is also possible to directly return
    the number of occurrences of a specific word.
    :param str sentence: input sentence to count words from 
    :param Union[bool, str] word: target word to count occurrences of
    :param bool ignore_case: ignore case in the given sentence
    (default: False)
    :return: Union[dict, int]
    """
    if ignore_case:
        sentence = sentence.casefold()
    words = re.sub(r"\W", " ", sentence).split()
    wordset = set(words)
    wordict = {el: words.count(el) for el in wordset}
    if word: 
        return wordict.get(word, 0)
    return wordict


def equal_files(file1: str, file2: str) -> bool:
    """Check whether two files are identical.

    First check whether the files have the same size, if so read them and
    check their content for equality.
    :param str file1: first file to compare
    :param str file2: second file to compare
    :return: bool
    """
    if os.path.getsize(file1) == os.path.getsize(file2):
        with open(file1) as f1, open(file2) as f2:
            if f1.read() == f2.read():
                return True
    return False

