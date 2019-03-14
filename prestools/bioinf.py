#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import math
import random
from typing import Optional

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


def aa_one_to_three(sequence: str) -> str:
    """
    Convert one-letter aminoacid code to three-letter code.
    :param str sequence: sequence of aminoacids in single-letter code
    :return: str with aminoacid sequence in three-letter code
    """
    return "".join([aa_dict[aa.upper()][0] for aa in sequence])


def aa_three_to_one(sequence: str) -> str:
    """
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
    """
    Convert a nucleotide sequence into its reverse, complement or reverse
    complement.
    :param str sequence: nucleotide sequence to be converted
    :param str conversion: type of conversion to perform ('reverse',
    'complement', 'reverse_complement') (default: 'reverse_complement')
    :return: str
    """
    if conversion == "reverse":
        return sequence[::-1]
    elif conversion == "complement":
        return "".join([complem_dict[nt.upper()] for nt in sequence])
    else:
        return "".join([complem_dict[nt.upper()] for nt in sequence])[::-1]


def shuffle(sequence: str, random_state: Optional[int] = None) -> str:
    """
    Randomly shuffle a sequence, maintaining the same nucleotide composition.
    :param str sequence: input sequence to shuffle
    :param Optional[int] random_state: optional random state seed, can be used
    for reproducibility
    :return: str
    """
    tmp_seq: str = ""
    if random_state:
        random.seed(random_state)

    while len(sequence) > 0:
        max_num = len(sequence)
        rand_num = math.floor(random.random() * max_num)
        tmp_char = sequence[rand_num]
        tmp_seq += tmp_char
        tmp_str_1 = sequence[:rand_num]
        tmp_str_2 = sequence[rand_num + 1:]
        sequence = tmp_str_1 + tmp_str_2

    return tmp_seq


def random_sequence(length: int, alphabet: str = "nt") -> str:
    """
    Create a random sequence of the given length using the specified alphabet
    (nucleotides or aminoacids).
    :param int length: desired length of the random sequence
    :param str alphabet: character alphabet to use to create the sequence
    ('nt', 'aa') (default: 'nt')
    :return: str
    """
    sequence = ""

    if alphabet == "nt":
        elems = nt_list
    elif alphabet == "aa":
        elems = aa_list
    else:
        raise ValueError("alphabet not recognised!")

    for i in range(length):
        temp_num = random.randint(0, len(elems) - 1)
        temp_char = elems[temp_num]
        sequence += temp_char

    return sequence
