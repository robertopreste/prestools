#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import prestools.bioinf as pb


@click.group()
def bioinf():
    """
    Bioinformatics utilities.
    """
    pass


@bioinf.command()
@click.argument("seq_1")
@click.argument("seq_2")
@click.option("--ignore_case", "-i", is_flag=True, default=False,
              help="""Ignore case when comparing sequences (default: False)""")
def hamming_distance(seq_1, seq_2, ignore_case):
    """
    Calculate the Hamming distance between two sequences.
    """
    result = pb.hamming_distance(seq_1, seq_2, ignore_case=ignore_case)
    click.echo(result)


@bioinf.command()
@click.argument("sequence")
@click.option("--conversion", "-c", default="reverse_complement",
              help="""Type of conversion to perform ('reverse', 'complement', 
              'reverse_complement') (default: 'reverse_complement')""")
def reverse_complement(sequence, conversion):
    """
    Convert a nucleotide sequence into its reverse, complement or reverse
    complement.
    """
    result = pb.reverse_complement(sequence, conversion=conversion)
    click.echo(result)


@bioinf.command()
@click.argument("sequence")
def shuffle_sequence(sequence):
    """
    Randomly shuffle a sequence, maintaining the same nucleotide composition.
    """
    result = pb.shuffle_sequence(sequence)
    click.echo(result)


@bioinf.command()
@click.argument("length")
@click.option("--alphabet", "-a", default="nt",
              help="""Character alphabet to use to create the sequence ('nt', 
              'aa') (default: 'nt')""")
def random_sequence(length, alphabet):
    """
    Create a random sequence of the given length using the specified alphabet
    (nucleotides or aminoacids).
    """
    result = pb.random_sequence(length, alphabet=alphabet)
    click.echo(result)
