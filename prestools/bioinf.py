#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import random
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

    Calculate the Hamming distance between two sequences.

    :param str seq_1: first sequence to compare

    :param str seq_2: second sequence to compare

    :param bool ignore_case: ignore case when comparing sequences
        (default: False)

    :return: int
    """
    if len(seq_1) != len(seq_2):
        raise ValueError("Cannot calculate Hamming distance of "
                         "sequences with different lengths.")

    if ignore_case:
        seq_1 = seq_1.casefold()
        seq_2 = seq_2.casefold()

    return sum([1 for i in range(len(seq_1))
                if seq_1[i] != seq_2[i]
                and seq_1[i] != "-" and seq_2[i] != "-"])


def aa_one_to_three(sequence: str) -> str:
    """Convert one-letter aminoacid code to three-letter code.

    Convert one-letter aminoacid code to three-letter code.

    :param str sequence: sequence of aminoacids in single-letter code

    :return: str with aminoacid sequence in three-letter code
    """
    return "".join([_AA_DICT[aa.upper()][0] for aa in sequence])


def aa_three_to_one(sequence: str) -> str:
    """Convert three-letter aminoacid code to one-letter code.

    Convert three-letter aminoacid code to one-letter code.

    :param str sequence: sequence of aminoacids in three-letter code

    :return: str with aminoacid sequence in one-letter code
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

    :param str sequence: nucleotide sequence to be converted

    :param str conversion: type of conversion to perform ('reverse',
        'complement', 'reverse_complement') (default: 'reverse_complement')

    :return: str
    """
    if conversion not in ["reverse", "complement", "reverse_complement"]:
        raise ValueError("Invalid conversion option.")

    if conversion == "reverse":
        return sequence[::-1]
    elif conversion == "complement":
        return "".join([_COMPLEM_DICT[nt.upper()] for nt in sequence])

    return "".join([_COMPLEM_DICT[nt.upper()] for nt in sequence])[::-1]


def shuffle_sequence(sequence: str) -> str:
    """Shuffle the given sequence.

    Randomly shuffle a sequence, maintaining the same composition.

    :param str sequence: input sequence to shuffle

    :return: str
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
    (nucleotides or aminoacids).

    :param Union[int, str] length: desired length of the random sequence

    :param str alphabet: character alphabet to use to create the sequence
        ('nt', 'aa') (default: 'nt')

    :return: str
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

    :param str sequence: input sequence to mutate

    :param int mutations: number of mutations to introduce (default: 1)

    :param str alphabet: character alphabet to use to introduce mutations
        ('nt', 'aa') (default: 'nt')

    :return: str
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

    :param str sequence: input nucleotide sequence

    :return: Dict[str,float]
    """
    sequence = sequence.upper()
    length = len(sequence)

    return {nt: sequence.count(nt)/length
            for nt in _NT_LIST}


def p_distance(seq_1: str, seq_2: str) -> float:
    """Calculate the pairwise distance between two sequences.

    Return the uncorrected distance between seq_1 and seq_2.

    :param str seq_1: first sequence to compare

    :param str seq_2: second sequence to compare

    :return: float
    """
    return hamming_distance(seq_1, seq_2, ignore_case=True) / len(seq_1)


def jukes_cantor_distance(seq_1: str, seq_2: str) -> float:
    """Calculate the Jukes-Cantor distance between two sequences.

    Return the Jukes-Cantor distance between seq_1 and seq_2, calculated
    as distance = -b log(1 - p/b) where b = 3/4 and p = p_distance.

    :param str seq_1: first sequence to compare

    :param str seq_2: second sequence to compare

    :return: float
    """
    from math import log
    b = 0.75
    p = p_distance(seq_1, seq_2)
    try:
        d = -b * log(1 - p/b)
    except ValueError:
        raise ValueError("Cannot calculate log of a negative number.")

    return d


def tajima_nei_distance(seq_1: str, seq_2: str) -> float:
    """Calculate the Tajima-Nei distance between two sequences.

    Return the Tajima-Nei distance between seq_1 and seq_2, calculated
    as distance = -b log(1 - p / b) where
    b = 0.5 * [1 - Sum i from A to T(Gi^2+p^2/h)]
    h = Sum i from A to G(Sum j from C to T (Xij^2/2*Gi*Gj))
    p = p-distance
    Xij = frequency of pair (i,j) in seq1 and seq2, with gaps removed
    Gi = frequency of base i over seq1 and seq2

    :param str seq_1: first sequence to compare

    :param str seq_2: second sequence to compare

    :return: float
    """
    from math import log
    from itertools import combinations

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
        d = -b * log(1 - p/b)
    except ValueError:
        raise ValueError("Cannot calculate log of a negative number.")

    return d


def kimura_distance(seq_1: str, seq_2: str) -> float:
    """Calculate the Kimura 2-Parameter distance between two sequences.

    Return the Kimura 2-Parameter distance between seq_1 and seq_2,
    calculated as distance = -0.5 log((1 - 2p -q) * sqrt( 1 - 2q )) where
    p = transition frequency and q = transversion frequency.

    :param str seq_1: first sequence to compare

    :param str seq_2: second sequence to compare

    :return: float
    """
    from math import log, sqrt

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
        d = -0.5 * log((1 - 2 * p - q) * sqrt(1 - 2 * q))
    except ValueError:
        raise ValueError("Cannot calculate log of a negative number.")

    return d


def tamura_distance(seq_1: str, seq_2: str) -> float:
    """Calculate the Tamura distance between two sequences.

    Return the Tamura distance between seq_1 and seq_2, calculated as
    distance = -C log(1 - P/C - Q) - 0.5(1 - C)log(1 - 2Q) where
    P = transition frequency
    Q = transversion frequency
    C = GC1 + GC2 - 2 * GC1 * GC2
    GC1 = GC-content of sequence 1
    GC2 = GC-coontent of sequence 2

    :param str seq_1: first sequence to compare

    :param str seq_2: second sequence to compare

    :return: float
    """
    from math import log

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
        d = -c * log(1 - p/c - q) - 0.5 * (1 - c) * log(1 - 2*q)
    except ValueError:
        raise ValueError("Cannot calculate log of a negative number.")

    return d
