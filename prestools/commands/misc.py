#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import prestools.misc as pm


@click.group()
def misc():
    """
    Miscellaneous utilities.
    """
    pass


@misc.command()
@click.argument("number")
def prime_factors(number):
    """
    Calculate the prime factors of a given natural number. Note that 1 is not a
    prime number, so it will not be included.
    """
    result = pm.prime_factors(int(number))
    click.echo(result)


@misc.command()
@click.argument("sentence")
@click.option("--word", "-w", default=False,
              help="""Target word to count occurrences of""")
@click.option("--ignore_case", "-i", is_flag=True, default=False,
              help="""Ignore case in the given sentence (default: False)""")
def wordcount(sentence, word, ignore_case):
    """
    Return the number of occurrences of each word in the given sentence, in
    the form of a dictionary; it is also possible to directly return the
    number of occurrences of a specific word.
    """
    result = pm.wordcount(sentence, word, ignore_case)
    click.echo(result)
