#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import prestools.bioinf as pb


def test_aa_one_to_three():
    expect = "CysAlaAsnAsnGlu"
    result = pb.aa_one_to_three("CANNE")
    assert result == expect


def test_aa_one_to_three_lowercase():
    expect = "CysAlaAsnAsnGlu"
    result = pb.aa_one_to_three("canne")
    assert result == expect


def test_aa_three_to_one():
    expect = "CANNE"
    result = pb.aa_three_to_one("CysAlaAsnAsnGlu")
    assert result == expect


def test_aa_three_to_one_lowercase():
    expect = "CANNE"
    result = pb.aa_three_to_one("cysalaasnasnglu")
    assert result == expect


def test_reverse_complement():
    expect = "CAGATA"
    result = pb.reverse_complement("TATCTG")
    assert result == expect


def test_reverse_complement_reverse():
    expect = "CAGATA"
    result = pb.reverse_complement("ATAGAC", conversion="reverse")
    assert result == expect


def test_reverse_complement_complement():
    expect = "CAGATA"
    result = pb.reverse_complement("GTCTAT", conversion="complement")
    assert result == expect


def test_shuffle():
    s = "ACGATCGTAGCTACATAATCGATCAGATGATGCAGCATG"
    expect = {nt: s.count(nt) for nt in ["A", "C", "G", "T"]}
    res = pb.shuffle(s)
    result = {nt: res.count(nt) for nt in ["A", "C", "G", "T"]}
    assert result == expect


def test_shuffle_random_state():
    expect = "CTTTAGAAGGGTTCAACGGAAATATACCTGGCGACTAAC"
    result = pb.shuffle("ACGATCGTAGCTACATAATCGATCAGATGATGCAGCATG", random_state=420)
    assert result == expect


def test_random_sequence_nt():
    result = pb.random_sequence(100, "nt")
    assert len(result) == 100
    assert set(result) == set(pb.nt_list)


def test_random_sequence_aa():
    result = pb.random_sequence(100, "aa")
    assert len(result) == 100
    assert set(result) == set(pb.aa_list)


