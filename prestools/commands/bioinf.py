#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import prestools.bioinf as pb


@click.group()
def bioinf():
    """
    Bioinformatics utilities
    """
    pass


@bioinf.command()
@click.argument("seq_1")
@click.argument("seq_2")
@click.option("--ignore_case", "-i", is_flag=True, default=False,
              help="""Ignore case when comparing sequences (default: False)""")
def hamming_distance(seq_1, seq_2, ignore_case):
    """Hamming distance between two sequences

    Calculate the Hamming distance between SEQ_1 and SEQ_2.
    """
    result = pb.hamming_distance(seq_1, seq_2, ignore_case=ignore_case)
    click.echo(result)


@bioinf.command()
@click.argument("seq_1")
@click.argument("seq_2")
def p_distance(seq_1, seq_2):
    """Pairwise distance between two sequences

    Return the uncorrected distance between SEQ_1 and SEQ_2.
    """
    result = pb.p_distance(seq_1, seq_2)
    click.echo(result)


@bioinf.command()
@click.argument("seq_1")
@click.argument("seq_2")
def jukes_cantor_distance(seq_1, seq_2):
    """Jukes-Cantor distance between two sequences

    Return the Jukes-Cantor distance between SEQ_1 and SEQ_2, calculated
    as distance = -b log(1 - p/b) where b = 3/4 and p = p_distance.
    """
    result = pb.jukes_cantor_distance(seq_1, seq_2)
    click.echo(result)


@bioinf.command()
@click.argument("seq_1")
@click.argument("seq_2")
def tajima_nei_distance(seq_1, seq_2):
    """Tajima-Nei distance between two sequences

    Return the Tajima-Nei distance between SEQ_1 and SEQ_2, calculated
    as distance = -b log(1 - p / b) where
    b = 0.5 * [1 - Sum i from A to T(Gi^2+p^2/h)]
    h = Sum i from A to G(Sum j from C to T (Xij^2/2*Gi*Gj))
    p = p-distance
    Xij = frequency of pair (i,j) in SEQ_1 and SEQ_2, with gaps removed
    Gi = frequency of base i over SEQ_1 and SEQ_2
    """
    result = pb.tajima_nei_distance(seq_1, seq_2)
    click.echo(result)


@bioinf.command()
@click.argument("seq_1")
@click.argument("seq_2")
def kimura_distance(seq_1, seq_2):
    """Kimura 2-Parameter distance between two sequences

    Return the Kimura 2-Parameter distance between SEQ_1 and SEQ_2,
    calculated as distance = -0.5 log((1 - 2p -q) * sqrt( 1 - 2q )) where
    p = transition frequency and q = transversion frequency.
    """
    result = pb.kimura_distance(seq_1, seq_2)
    click.echo(result)


@bioinf.command()
@click.argument("seq_1")
@click.argument("seq_2")
def tamura_distance(seq_1, seq_2):
    """Tamura distance between two sequences

    Return the Tamura distance between SEQ_1 and SEQ_2, calculated as
    distance = -C log(1 - P/C - Q) - 0.5(1 - C)log(1 - 2Q) where
    P = transition frequency
    Q = transversion frequency
    C = GC1 + GC2 - 2 * GC1 * GC2
    GC1 = GC-content of SEQ_1
    GC2 = GC-content of SEQ_2
    """
    result = pb.tamura_distance(seq_1, seq_2)
    click.echo(result)


@bioinf.command()
@click.argument("sequence")
@click.option("--conversion", "-c", default="reverse_complement",
              type=click.Choice(["reverse", "complement", "reverse_complement",
                                 "r", "c", "rc"]),
              help="""Type of conversion to perform ('r'|'reverse', 
              'c'|'complement', 'rc'|'reverse_complement') 
              (default: 'rc'|'reverse_complement')""")
def reverse_complement(sequence, conversion):
    """Convert a nucleotide sequence into its reverse complement

    Convert a nucleotide SEQUENCE into its reverse, complement or reverse
    complement.
    """
    result = pb.reverse_complement(sequence, conversion=conversion)
    click.echo(result)


@bioinf.command()
@click.argument("sequence")
def shuffle_sequence(sequence):
    """Shuffle the given sequence

    Randomly shuffle a SEQUENCE, maintaining the same nucleotide composition.
    """
    result = pb.shuffle_sequence(sequence)
    click.echo(result)


@bioinf.command()
@click.argument("length")
@click.option("--alphabet", "-a", default="nt", type=click.Choice(["nt", "aa"]),
              help="""Character alphabet to use to create the sequence ('nt', 
              'aa') (default: 'nt')""")
def random_sequence(length, alphabet):
    """Create a random sequence of the given length

    Create a random sequence of the given LENGTH using the specified ALPHABET
    (nucleotides or aminoacids).
    """
    result = pb.random_sequence(length, alphabet=alphabet)
    click.echo(result)
