#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import numpy as np
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


def test_reverse_complement_short():
    expect = "CAGATA"
    result = pb.reverse_complement("TATCTG", conversion="rc")
    assert result == expect


def test_reverse_complement_reverse():
    expect = "CAGATA"
    result = pb.reverse_complement("ATAGAC", conversion="reverse")
    assert result == expect


def test_reverse_complement_reverse_short():
    expect = "CAGATA"
    result = pb.reverse_complement("ATAGAC", conversion="r")
    assert result == expect


def test_reverse_complement_complement():
    expect = "CAGATA"
    result = pb.reverse_complement("GTCTAT", conversion="complement")
    assert result == expect


def test_reverse_complement_complement_short():
    expect = "CAGATA"
    result = pb.reverse_complement("GTCTAT", conversion="c")
    assert result == expect


def test_reverse_complement_error():
    with pytest.raises(ValueError):
        pb.reverse_complement("CAGATA", conversion="invalid")


# pb.shuffle_sequence()

def test_shuffle_sequence_nt(sample_nt_sequence):
    expect = {nt: sample_nt_sequence.count(nt) for nt in pb._NT_LIST}
    res = pb.shuffle_sequence(sample_nt_sequence)
    result = {nt: res.count(nt) for nt in pb._NT_LIST}
    assert len(res) == len(sample_nt_sequence)
    assert result == expect


def test_shuffle_sequence_aa(sample_aa_sequence):
    expect = {aa: sample_aa_sequence.count(aa) for aa in pb._AA_LIST}
    res = pb.shuffle_sequence(sample_aa_sequence)
    result = {aa: res.count(aa) for aa in pb._AA_LIST}
    assert len(res) == len(sample_aa_sequence)
    assert result == expect


# pb.random_sequence()

def test_random_sequence_nt():
    result = pb.random_sequence(200, alphabet="nt")
    assert len(result) == 200
    assert set(result) == set(pb._NT_LIST)


def test_random_sequence_aa():
    result = pb.random_sequence(200, alphabet="aa")
    assert len(result) == 200
    assert set(result) == set(pb._AA_LIST)


def test_random_sequence_error():
    with pytest.raises(ValueError):
        pb.random_sequence(200, alphabet="invalid")


# pb.mutate_sequence()

def test_mutate_sequence_nt_one(sample_nt_sequence):
    result = pb.mutate_sequence(sample_nt_sequence)
    assert len(result) == len(sample_nt_sequence)
    assert set(result) == set(pb._NT_LIST)
    assert pb.hamming_distance(sample_nt_sequence, result) == 1


def test_mutate_sequence_aa_one(sample_aa_sequence):
    result = pb.mutate_sequence(sample_aa_sequence, alphabet="aa")
    assert len(result) == len(sample_aa_sequence)
    assert set(result) == set(pb._AA_LIST)
    assert pb.hamming_distance(sample_aa_sequence, result) == 1


def test_mutate_sequence_nt_many(sample_nt_sequence):
    result = pb.mutate_sequence(sample_nt_sequence, mutations=10)
    assert len(result) == len(sample_nt_sequence)
    assert set(result) == set(pb._NT_LIST)
    assert pb.hamming_distance(sample_nt_sequence, result) <= 10


def test_mutate_sequence_aa_many(sample_aa_sequence):
    result = pb.mutate_sequence(sample_aa_sequence, mutations=10,
                                alphabet="aa")
    assert len(result) == len(sample_aa_sequence)
    assert set(result) == set(pb._AA_LIST)
    assert pb.hamming_distance(sample_aa_sequence, result) <= 10


def test_mutate_sequence_error():
    with pytest.raises(ValueError):
        pb.mutate_sequence("CAGATA", alphabet="invalid")


# pb.p_distance

def test_p_distance(sample_nt_long_1, sample_nt_long_2):
    expect = 0.7266
    result = pb.p_distance(sample_nt_long_1, sample_nt_long_2)
    assert result == expect


# pb.jukes_cantor_distance

def test_jukes_cantor_distance(sample_nt_long_1, sample_nt_long_2):
    expect = 2.600502888125025
    result = pb.jukes_cantor_distance(sample_nt_long_1, sample_nt_long_2)
    assert result == expect


# pb.tajima_nei_distance

def test_tajima_nei_distance(sample_nt_long_1, sample_nt_long_2):
    expect = 2.612489480361321
    result = pb.tajima_nei_distance(sample_nt_long_1, sample_nt_long_2)
    assert result == expect


# pb.kimura_distance

def test_kimura_distance(sample_nt_long_1, sample_nt_long_2):
    expect = 2.6031087353225875
    result = pb.kimura_distance(sample_nt_long_1, sample_nt_long_2)
    assert result == expect


# pb.tamura_distance

def test_tamura_distance(sample_nt_long_1, sample_nt_long_2):
    expect = 2.603755899559136
    result = pb.tamura_distance(sample_nt_long_1, sample_nt_long_2)
    assert result == expect


# pb.rpkm

def test_rpkm(sample_gene_counts, sample_gene_lengths):
    expect = np.array([
        [225335.50543533, 114525.36331398, 149823.72302588, 179779.64409024],
        [0., 0., 0., 733.40990133],
        [0., 0., 0., 0.],
        [40426.94801193, 194619.75108416, 145501.92735762, 103192.72022265]
    ])
    result = pb.rpkm(sample_gene_counts, sample_gene_lengths)
    np.testing.assert_array_almost_equal(result, expect)


# pb.quantile_norm

def test_quantile_norm_raw(sample_gene_counts):
    expect = np.array([
        [6.280e+02, 2.455e+02, 6.280e+02, 6.280e+02],
        [0.000e+00, 0.000e+00, 0.000e+00, 2.500e-01],
        [0.000e+00, 0.000e+00, 0.000e+00, 0.000e+00],
        [2.455e+02, 6.280e+02, 2.455e+02, 2.455e+02]
    ])
    result = pb.quantile_norm(sample_gene_counts)
    np.testing.assert_array_almost_equal(result, expect)


def test_quantile_norm_log(sample_gene_counts):
    expect = np.array([
        [6.28121943, 5.41052327, 6.28121943, 6.28121943],
        [0., 0., 0., 0.1732868],
        [0., 0., 0., 0.],
        [5.41052327, 6.28121943, 5.41052327, 5.41052327]
    ])
    result = pb.quantile_norm(sample_gene_counts, to_log=True)
    np.testing.assert_array_almost_equal(result, expect)
