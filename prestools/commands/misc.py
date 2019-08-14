#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import prestools.misc as pm


@click.group()
def misc():
    """
    Miscellaneous utilities
    """
    pass


@misc.command()
@click.argument("number")
def prime_factors(number):
    """Calculate the prime factors of a number

    Calculate the prime factors of a given natural NUMBER. Note that 1 is
    not a prime number, so it will not be included.
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
    """Count occurrences of words in a sentence

    Return the number of occurrences of each word in the given SENTENCE,
    in the form of a dictionary; it is also possible to directly return
    the number of occurrences of a specific WORD.
    """
    result = pm.wordcount(sentence, word, ignore_case)
    click.echo(result)


@misc.command()
@click.argument("file1")
@click.argument("file2")
def equal_files(file1, file2):
    """Check whether two files are identical

    First check whether FILE1 and FILE2 have the same size, if so read
    them and check their content for equality.
    """
    result = pm.equal_files(file1, file2)
    click.echo(result)
