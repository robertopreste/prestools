#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from collections import Iterable


def flatten(iterable: Iterable, drop_null: bool = False) -> list:
    """
    Flatten a nested iterable, even with multiple nesting levels and different data types. It is
    also possible to drop null values (None) from the resulting list.
    :param iterable: nested iterable to flatten
    :param drop_null: filter out None from the flattened list (default = False)
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
