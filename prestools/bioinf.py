#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import random
import numpy as np
from scipy import stats
from math import log, sqrt
from itertools import combinations
from typing import Union, Dict

_NT_LIST = ["A", "C", "G", "T"]

_AA_LIST = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P",
            "Q", "R", "S", "T", "V", "W", "Y"]

_TRANSITIONS = ["AG", "GA", "CT", "TC"]

_TRANSVERSIONS = ["AC", "CA", "AT", "TA", "GC", "CG", "GT", "TG"]


_NT_DICT = {"A": "Adenine", "C": "Cytosine", "G": "Guanine", "T": "Thymine",
            "U": "Uracil", "R": "A/G", "Y": "C/T", "S": "G/C", "W": "A/T",
            "K": "G/T", "M": "A/C", "B": "C/G/T", "D": "A/G/T", "H": "A/C/T",
            "V": "A/C/G", "N": "A/C/G/T", "./-": "gap"}

_AA_DICT = {"A": ("Ala", "Alanine"), "B": ("Asx", "Aspartic Acid/Asparagine"),
            "C": ("Cys", "Cysteine"), "D": ("Asp", "Aspartic Acid"),
            "E": ("Glu", "Glutamic Acid"), "F": ("Phe", "Phenylalanine"),
            "G": ("Gly", "Glycine"), "H": ("His", "Histidine"),
            "I": ("Ile", "Isoleucine"), "K": ("Lys", "Lysine"),
            "L": ("Leu", "Leucine"), "M": ("Met", "Methionine"),
            "N": ("Asn", "Asparagine"), "P": ("Pro", "Proline"),
            "Q": ("Gln", "Glutamine"), "R": ("Arg", "Arginine"),
            "S": ("Ser", "Serine"), "T": ("Thr", "Threonine"),
            "V": ("Val", "Valine"), "W": ("Trp", "Tryptophan"),
            "X": ("Xaa", "Any"), "Y": ("Tyr", "Tyrosine"),
            "Z": ("Glx", "Glutamine/Glutamic Acid"), "*": ("***", "Stop")}

_COMPLEM_DICT = {"A": "T", "C": "G", "G": "C", "T": "A", "U": "A", "R": "Y",
                 "Y": "R", "S": "W", "W": "S", "K": "M", "M": "K", "B": "A",
                 "D": "C", "H": "G", "V": "T"}


def hamming_distance(seq_1: str, seq_2: str,
                     ignore_case: bool = False) -> int:
    """Calculate the Hamming distance between two sequences.

    Args:
        seq_1: first sequence to compare
        seq_2: second sequence to compare
        ignore_case: ignore case when comparing sequences (default: False)

    Returns:
        distance: Hamming distance
    """
    if len(seq_1) != len(seq_2):
        raise ValueError("Cannot calculate Hamming distance of "
                         "sequences with different lengths.")

    if ignore_case:
        seq_1 = seq_1.casefold()
        seq_2 = seq_2.casefold()

    distance = sum([1 for i in range(len(seq_1))
                    if seq_1[i] != seq_2[i]
                    and seq_1[i] != "-" and seq_2[i] != "-"])

    return distance


def aa_one_to_three(sequence: str) -> str:
    """Convert one-letter amino acid code to three-letter code.

    Args:
        sequence: sequence of amino acids in one-letter code

    Returns:
        new_seq: sequence converted to three-letter code
    """
    new_seq = "".join([_AA_DICT[aa.upper()][0] for aa in sequence])

    return new_seq


def aa_three_to_one(sequence: str) -> str:
    """Convert three-letter amino acid code to one-letter code.

    Args:
        sequence: sequence of amino acids in three-letter code

    Returns:
        new_seq: sequence converted to one-letter code
    """
    # TODO: this is very ugly, will have to refactor it
    new_seq = ""

    for n in range(0, len(sequence), 3):
        aa = sequence[n: n + 3].capitalize()
        for cod in _AA_DICT:
            if _AA_DICT[cod][0] == aa:
                new_seq += cod
                break

    return new_seq


def reverse_complement(sequence: str,
                       conversion: str = "reverse_complement") -> str:
    """Convert a nucleotide sequence into its reverse complement.

    Convert a nucleotide sequence into its reverse, complement or reverse
    complement.

    Args:
        sequence: nucleotide sequence to be converted
        conversion: type of conversion to perform ('r'|'reverse',
            'c'|'complement', 'rc'|'reverse_complement')
            (default: 'rc'|'reverse_complement')

    Returns:
        converted sequence
    """
    if conversion not in ["r", "c", "rc",
                          "reverse", "complement", "reverse_complement"]:
        raise ValueError("Invalid conversion option.")

    if conversion in ["r", "reverse"]:
        return sequence[::-1]
    elif conversion in ["c", "complement"]:
        return "".join([_COMPLEM_DICT[nt.upper()] for nt in sequence])

    return "".join([_COMPLEM_DICT[nt.upper()] for nt in sequence])[::-1]


def shuffle_sequence(sequence: str) -> str:
    """Shuffle the given sequence.

    Randomly shuffle a sequence, maintaining the same composition.

    Args:
        sequence: input sequence to shuffle

    Returns:
        tmp_seq: shuffled sequence
    """
    tmp_seq: str = ""

    while len(sequence) > 0:
        max_num = len(sequence)
        rand_num = random.randrange(max_num)
        tmp_char = sequence[rand_num]
        tmp_seq += tmp_char
        tmp_str_1 = sequence[:rand_num]
        tmp_str_2 = sequence[rand_num + 1:]
        sequence = tmp_str_1 + tmp_str_2

    return tmp_seq


def random_sequence(length: Union[int, str],
                    alphabet: str = "nt") -> str:
    """Create a random sequence of the given length.

    Create a random sequence of the given length using the specified alphabet
    (nucleotides or amino acids).

    Args:
        length: desired length of the random sequence
        alphabet: character alphabet to use ('nt', 'aa') (default: 'nt')

    Returns:
        sequence: new random sequence
    """
    if alphabet not in ["nt", "aa"]:
        raise ValueError("Invalid alphabet option.")

    sequence = ""
    elems = _NT_LIST if alphabet == "nt" else _AA_LIST

    for i in range(int(length)):
        temp_char = random.choice(elems)
        sequence += temp_char

    return sequence


def mutate_sequence(sequence: str,
                    mutations: int = 1,
                    alphabet: str = "nt") -> str:
    """Mutate a sequence introducing a given number of mutations.

    Introduce a specific number of mutations into the given sequence.

    Args:
        sequence: input sequence to mutate
        mutations: number of mutations to introduce (default: 1)
        alphabet: character alphabet to use ('nt', 'aa') (default: 'nt')

    Returns:
        sequence: mutated sequence
    """
    if alphabet not in ["nt", "aa"]:
        raise ValueError("Invalid alphabet option.")

    elems = _NT_LIST if alphabet == "nt" else _AA_LIST

    for n in range(mutations):
        max_num = len(sequence)
        rand_num = random.randrange(max_num)
        curr_char = sequence[rand_num]
        mut_char = random.choice(elems)
        while mut_char == curr_char:
            mut_char = random.choice(elems)

        sequence = sequence[0: rand_num] + mut_char + sequence[rand_num + 1:]

    return sequence


def nt_frequency(sequence: str) -> Dict[str, float]:
    """Calculate nucleotide frequencies.

    Return a dictionary with nucleotide frequencies from the given
    sequence.

    Args:
        sequence: input nucleotide sequence

    Returns:
        freqs: dictionary of nucleotide frequencies
    """
    sequence = sequence.upper()
    length = len(sequence)

    freqs = {nt: sequence.count(nt)/length for nt in _NT_LIST}

    return freqs


def p_distance(seq_1: str, seq_2: str) -> float:
    """Calculate the pairwise distance between two sequences.

    Return the uncorrected distance between seq_1 and seq_2.

    Args:
        seq_1: first sequence to compare
        seq_2: second sequence to compare

    Returns:
        distance: pairwise distance
    """
    distance = hamming_distance(seq_1, seq_2, ignore_case=True) / len(seq_1)

    return distance


def jukes_cantor_distance(seq_1: str, seq_2: str) -> float:
    """Calculate the Jukes-Cantor distance between two sequences.

    Return the Jukes-Cantor distance between seq_1 and seq_2, calculated
    as distance = -b log(1 - p/b) where b = 3/4 and p = p_distance.

    Args:
        seq_1: first sequence to compare
        seq_2: second sequence to compare

    Returns:
        distance: Jukes-Cantor distance
    """
    b = 0.75
    p = p_distance(seq_1, seq_2)
    try:
        distance = -b * log(1 - p/b)
    except ValueError:
        raise ValueError("Cannot calculate log of a negative number.")

    return distance


def tajima_nei_distance(seq_1: str, seq_2: str) -> float:
    """Calculate the Tajima-Nei distance between two sequences.

    Return the Tajima-Nei distance between seq_1 and seq_2, calculated
    as distance = -b log(1 - p / b) where
    b = 0.5 * [1 - Sum i from A to T(Gi^2+p^2/h)]
    h = Sum i from A to G(Sum j from C to T (Xij^2/2*Gi*Gj))
    p = p-distance
    Xij = frequency of pair (i,j) in seq1 and seq2, with gaps removed
    Gi = frequency of base i over seq1 and seq2

    Args:
        seq_1: first sequence to compare
        seq_2: second sequence to compare

    Returns:
        distance: Tajima-Nei distance
    """
    G = nt_frequency(seq_1 + seq_2)
    p = p_distance(seq_1, seq_2)
    h = 0.0
    pairs = [el for el in zip(seq_1, seq_2) if "-" not in el]
    nt_pairs = combinations(_NT_LIST, 2)
    length = len(pairs)

    for el in nt_pairs:
        paircount = pairs.count(el) + pairs.count(el[::-1])
        x_ij_sq = (paircount / length) ** 2
        gi_gj = G[el[0]] * G[el[1]]
        h += 0.5 * x_ij_sq / gi_gj

    b = 0.5 * (1 - sum([G[nt] ** 2 for nt in G]) + p ** 2 / h)

    try:
        distance = -b * log(1 - p/b)
    except ValueError:
        raise ValueError("Cannot calculate log of a negative number.")

    return distance


def kimura_distance(seq_1: str, seq_2: str) -> float:
    """Calculate the Kimura 2-Parameter distance between two sequences.

    Return the Kimura 2-Parameter distance between seq_1 and seq_2,
    calculated as distance = -0.5 log((1 - 2p -q) * sqrt( 1 - 2q )) where
    p = transition frequency and q = transversion frequency.

    Args:
        seq_1: first sequence to compare
        seq_2: second sequence to compare

    Returns:
        distance: Kimura distance
    """
    pairs = [el for el in zip(seq_1, seq_2) if "-" not in el]
    ts = 0
    tv = 0
    length = len(pairs)

    for pair in pairs:
        if pair[0] + pair[1] in _TRANSITIONS:
            ts += 1
        elif pair[0] + pair[1] in _TRANSVERSIONS:
            tv += 1

    p = ts / length
    q = tv / length

    try:
        distance = -0.5 * log((1 - 2 * p - q) * sqrt(1 - 2 * q))
    except ValueError:
        raise ValueError("Cannot calculate log of a negative number.")

    return distance


def tamura_distance(seq_1: str, seq_2: str) -> float:
    """Calculate the Tamura distance between two sequences.

    Return the Tamura distance between seq_1 and seq_2, calculated as
    distance = -C log(1 - P/C - Q) - 0.5(1 - C)log(1 - 2Q) where
    P = transition frequency
    Q = transversion frequency
    C = GC1 + GC2 - 2 * GC1 * GC2
    GC1 = GC-content of seq_1
    GC2 = GC-content of seq_2

    Args:
        seq_1: first sequence to compare
        seq_2: second sequence to compare

    Returns:
        distance: Tamura distance
    """
    pairs = [el for el in zip(seq_1, seq_2) if "-" not in el]
    ts = 0
    tv = 0
    length = len(pairs)

    for pair in pairs:
        if pair[0] + pair[1] in _TRANSITIONS:
            ts += 1
        elif pair[0] + pair[1] in _TRANSVERSIONS:
            tv += 1

    p = ts / length
    q = tv / length
    fr1 = nt_frequency(seq_1)
    fr2 = nt_frequency(seq_2)
    gc1 = fr1["C"] + fr1["G"]
    gc2 = fr2["C"] + fr2["G"]
    c = gc1 + gc2 - 2 * gc1 * gc2

    try:
        distance = -c * log(1 - p/c - q) - 0.5 * (1 - c) * log(1 - 2*q)
    except ValueError:
        raise ValueError("Cannot calculate log of a negative number.")

    return distance


def rpkm(counts: np.ndarray, lengths: np.ndarray) -> np.ndarray:
    """Calculate reads per kilobase transcript per million reads.

    RPKM = (10^9 * C) / (N * L)

    Where:
    C = Number of reads mapped to a gene
    N = Total mapped reads in the experiment
    L = Exon length in base pairs for a gene

    Args:
        counts: count data where columns are individual samples
            and rows are genes, of shape (N_genes, N_samples)
        lengths: gene lengths in base pairs in the same order
            as the rows in counts, of shape (N_genes, )

    Returns:
        normed: RPKM normalized counts matrix, of
            shape (N_genes, N_samples)
    """
    c = counts.astype(float)
    n = np.sum(c, axis=0)
    n = n.reshape((1, n.shape[0]))
    l = lengths.reshape((lengths.shape[0], 1))
    normed = 1e9 * c / (n * l)

    return normed


def quantile_norm(x: np.ndarray, to_log: bool = False) -> np.ndarray:
    """Normalize the columns of X to each have the same distribution.

    Given an expression matrix (microarray data, read counts, etc) of M genes
    by N samples, quantile normalization ensures all samples have the same
    spread of data (by construction).

    The data across each row are averaged to obtain an average column. Each
    column quantile is replaced with the corresponding quantile of the average
    column.

    Args:
        x: array of input data, of shape (N_genes, N_samples)
        to_log: log-transform the data before normalising (default: False)

    Returns:
        xn: array of normalised data, of shape (N_genes, N_samples)
    """
    if to_log:
        x = np.log(x + 1)
    quantiles = np.mean(np.sort(x, axis=0), axis=1)

    ranks = np.apply_along_axis(stats.rankdata, 0, x)
    rank_indices = ranks.astype(int) - 1

    xn = quantiles[rank_indices]

    return xn
