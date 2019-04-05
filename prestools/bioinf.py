#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import random
from typing import Union

nt_list = ["A", "C", "G", "T"]

aa_list = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P",
           "Q", "R", "S", "T", "V", "W", "Y"]


nt_dict = {"A": "Adenine", "C": "Cytosine", "G": "Guanine", "T": "Thymine",
           "U": "Uracil", "R": "A/G", "Y": "C/T", "S": "G/C", "W": "A/T",
           "K": "G/T", "M": "A/C", "B": "C/G/T", "D": "A/G/T", "H": "A/C/T",
           "V": "A/C/G", "N": "A/C/G/T", "./-": "gap"}

aa_dict = {"A": ("Ala", "Alanine"), "B": ("Asx", "Aspartic Acid/Asparagine"),
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

complem_dict = {"A": "T", "C": "G", "G": "C", "T": "A", "U": "A", "R": "Y",
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

    return sum([1 for i in range(len(seq_1)) if seq_1[i] != seq_2[i]])


def aa_one_to_three(sequence: str) -> str:
    """Convert one-letter aminoacid code to three-letter code.

    Convert one-letter aminoacid code to three-letter code.
    :param str sequence: sequence of aminoacids in single-letter code
    :return: str with aminoacid sequence in three-letter code
    """
    return "".join([aa_dict[aa.upper()][0] for aa in sequence])


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
        for cod in aa_dict:
            if aa_dict[cod][0] == aa:
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
        return "".join([complem_dict[nt.upper()] for nt in sequence])

    return "".join([complem_dict[nt.upper()] for nt in sequence])[::-1]


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
    elems = nt_list if alphabet == "nt" else aa_list

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

    elems = nt_list if alphabet == "nt" else aa_list

    for n in range(mutations):
        max_num = len(sequence)
        rand_num = random.randrange(max_num)
        curr_char = sequence[rand_num]
        mut_char = random.choice(elems)
        while mut_char == curr_char:
            mut_char = random.choice(elems)

        sequence = sequence[0: rand_num] + mut_char + sequence[rand_num + 1:]

    return sequence
