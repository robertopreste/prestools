#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import prestools.bioinf as pb


# pb.hamming_distance

def test_hamming_distance_zero():
    expect = 0
    result = pb.hamming_distance("CAGATA", "CAGATA")
    assert result == expect


def test_hamming_distance_one():
    expect = 1
    result = pb.hamming_distance("CAGATA", "CACATA")
    assert result == expect


def test_hamming_distance_many():
    expect = 6
    result = pb.hamming_distance("CAGATA", "GTCTAT")
    assert result == expect


def test_hamming_distance_error():
    with pytest.raises(ValueError):
        pb.hamming_distance("CAGATA", "CACACACA")


def test_hamming_distance_different_case():
    expect = 6
    result = pb.hamming_distance("CAGATA", "cagata", ignore_case=False)
    assert result == expect


def test_hamming_distance_ignore_case():
    expect = 0
    result = pb.hamming_distance("CAGATA", "cagata", ignore_case=True)
    assert result == expect


# pb.aa_one_to_three()

def test_aa_one_to_three():
    expect = "CysAlaAsnAsnGlu"
    result = pb.aa_one_to_three("CANNE")
    assert result == expect


def test_aa_one_to_three_lowercase():
    expect = "CysAlaAsnAsnGlu"
    result = pb.aa_one_to_three("canne")
    assert result == expect


# pb.aa_three_to_one()

def test_aa_three_to_one():
    expect = "CANNE"
    result = pb.aa_three_to_one("CysAlaAsnAsnGlu")
    assert result == expect


def test_aa_three_to_one_lowercase():
    expect = "CANNE"
    result = pb.aa_three_to_one("cysalaasnasnglu")
    assert result == expect


# pb.reverse_complement()

def test_reverse_complement():
    expect = "CAGATA"
    result = pb.reverse_complement("TATCTG", conversion="reverse_complement")
    assert result == expect


def test_reverse_complement_reverse():
    expect = "CAGATA"
    result = pb.reverse_complement("ATAGAC", conversion="reverse")
    assert result == expect


def test_reverse_complement_complement():
    expect = "CAGATA"
    result = pb.reverse_complement("GTCTAT", conversion="complement")
    assert result == expect


def test_reverse_complement_error():
    with pytest.raises(ValueError):
        pb.reverse_complement("CAGATA", conversion="invalid")


# pb.shuffle_sequence()

def test_shuffle_sequence_nt(sample_nt_sequence):
    expect = {nt: sample_nt_sequence.count(nt) for nt in pb.nt_list}
    res = pb.shuffle_sequence(sample_nt_sequence)
    result = {nt: res.count(nt) for nt in pb.nt_list}
    assert len(res) == len(sample_nt_sequence)
    assert result == expect


def test_shuffle_sequence_aa(sample_aa_sequence):
    expect = {aa: sample_aa_sequence.count(aa) for aa in pb.aa_list}
    res = pb.shuffle_sequence(sample_aa_sequence)
    result = {aa: res.count(aa) for aa in pb.aa_list}
    assert len(res) == len(sample_aa_sequence)
    assert result == expect


# pb.random_sequence()

def test_random_sequence_nt():
    result = pb.random_sequence(200, alphabet="nt")
    assert len(result) == 200
    assert set(result) == set(pb.nt_list)


def test_random_sequence_aa():
    result = pb.random_sequence(200, alphabet="aa")
    assert len(result) == 200
    assert set(result) == set(pb.aa_list)


def test_random_sequence_error():
    with pytest.raises(ValueError):
        pb.random_sequence(200, alphabet="invalid")


# pb.mutate_sequence()

def test_mutate_sequence_nt_one(sample_nt_sequence):
    result = pb.mutate_sequence(sample_nt_sequence)
    assert len(result) == len(sample_nt_sequence)
    assert set(result) == set(pb.nt_list)
    assert pb.hamming_distance(sample_nt_sequence, result) == 1


def test_mutate_sequence_aa_one(sample_aa_sequence):
    result = pb.mutate_sequence(sample_aa_sequence, alphabet="aa")
    assert len(result) == len(sample_aa_sequence)
    assert set(result) == set(pb.aa_list)
    assert pb.hamming_distance(sample_aa_sequence, result) == 1


def test_mutate_sequence_nt_many(sample_nt_sequence):
    result = pb.mutate_sequence(sample_nt_sequence, mutations=10)
    assert len(result) == len(sample_nt_sequence)
    assert set(result) == set(pb.nt_list)
    assert pb.hamming_distance(sample_nt_sequence, result) == 10


def test_mutate_sequence_aa_many(sample_aa_sequence):
    result = pb.mutate_sequence(sample_aa_sequence, mutations=10,
                                alphabet="aa")
    assert len(result) == len(sample_aa_sequence)
    assert set(result) == set(pb.aa_list)
    assert pb.hamming_distance(sample_aa_sequence, result) == 10


def test_mutate_sequence_error():
    with pytest.raises(ValueError):
        pb.mutate_sequence("CAGATA", alphabet="invalid")
