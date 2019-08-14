#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import re
import time
import numpy as np
import pandas as pd
from multiprocessing import Pool
from typing import List, Any, Type, Union, Callable, Tuple, Iterable


def flatten(iterable: Iterable, drop_null: bool = False) -> List[Any]:
    """Flatten out a nested iterable.

    Flatten a nested iterable, even with multiple nesting levels and
    different data types. It is also possible to drop null values (None)
    from the resulting list.

    Args:
        iterable: nested iterable to flatten
        drop_null: filter out None from the flattened list (default: False)

    Returns:
        flat list
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

    Args:
        input_dict: original dictionary to be inverted
        sort_keys: sort the keys in the inverted dictionary in
            alphabetical order (default: False)

    Returns:
        new_dict: inverted dictionary
    """
    new_dict = {el: x for x in input_dict for el in input_dict[x]}
    if sort_keys:
        return {el: new_dict[el] for el in sorted(new_dict)}

    return new_dict


def prime_factors(number: int) -> List[int]:
    """Calculate the prime factors of a number.

    Calculate the prime factors of a given natural number. Note that 1 is
    not a prime number, so it will not be included.

    Args:
        number: input natural number

    Returns:
        factors: list of prime factors
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

    Args:
        input_list: input list to filter
        target_type: desired type to keep

    Returns:
        filtered: filtered list
    """
    filtered = [el for el in input_list if type(el) == target_type]

    return filtered


def wordcount(sentence: str,
              word: Union[bool, str] = False,
              ignore_case: bool = False) -> Union[dict, int]:
    """Count occurrences of words in a sentence.

    Return the number of occurrences of each word in the given sentence,
    in the form of a dictionary; it is also possible to directly return
    the number of occurrences of a specific word.

    Args:
        sentence: input sentence to count words from
        word: target word to count occurrences of
        ignore_case: ignore case in the given sentence (default: False)

    Returns:
        word_dict: dictionary of word counts
    """
    if ignore_case:
        sentence = sentence.casefold()
    words = re.sub(r"\W", " ", sentence).split()
    wordset = set(words)
    word_dict = {el: words.count(el) for el in wordset}
    if word:
        return word_dict.get(word, 0)

    return word_dict


def equal_files(file1: str, file2: str) -> bool:
    """Check whether two files are identical.

    First check whether the files have the same size, if so read them and
    check their content for equality.

    Args:
        file1: first file to compare
        file2: second file to compare
    """
    if os.path.getsize(file1) == os.path.getsize(file2):
        with open(file1) as f1, open(file2) as f2:
            if f1.read() == f2.read():
                return True

    return False


def benchmark(function: Callable) -> Callable:
    """Benchmark a given function.

    Decorator to run the given function and return the function name and
    the amount of time spent in executing it.

    Args:
        function: function to benchmark
    """
    def wrapper(*args, **kwargs) -> Tuple[str, float, Any]:
        """Return time spent to call a function.

        Benchmark the input function and return function name time needed
        to call it and values returned by the function.

        :param args: positional arguments for the input function

        :param kwargs: keywork arguments for the input function

        :return: Tuple[str,float,Any]
        """
        f_name = function.__name__
        start = time.time()
        f_val = function(*args, **kwargs)
        end = time.time()
        f_time = end - start

        return f_name, f_time, f_val

    return wrapper


def apply_parallel(df: pd.DataFrame,
                   function: Callable,
                   cores: int = 4) -> pd.DataFrame:
    """Apply a function to a dataframe in parallel.

    Apply the given function to the dataframe, using the given number of
    cores for computation. The dataframe will be split in `cores` part,
    and the function will be applied to each separately; finally, the
    dataframe is reconstructed and returned.

    Args:
        df: input dataframe
        function: function to apply
        cores: number of cores to use (default: 4)

    Returns:
        df: resulting dataframe
    """
    df_split = np.array_split(df, cores)
    pool = Pool(cores)
    df = pd.concat(pool.map(function, df_split))
    pool.close()
    pool.join()

    return df
