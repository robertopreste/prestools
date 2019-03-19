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
