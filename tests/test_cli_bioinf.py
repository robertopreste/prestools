#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
from click.testing import CliRunner
from prestools import cli
from prestools.bioinf import nt_list, aa_list


# hamming-distance

def test_cli_hamming_distance_zero():
    runner = CliRunner()
    expect = "0"
    result = runner.invoke(cli.main, ["bioinf", "hamming-distance",
                                      "CAGATA", "CAGATA"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_hamming_distance_one():
    runner = CliRunner()
    expect = "1"
    result = runner.invoke(cli.main, ["bioinf", "hamming-distance",
                                      "CAGATA", "CACATA"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_hamming_distance_many():
    runner = CliRunner()
    expect = "6"
    result = runner.invoke(cli.main, ["bioinf", "hamming-distance",
                                      "CAGATA", "GTCTAT"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_hamming_distance_error():
    runner = CliRunner()
    expect = "Cannot calculate Hamming distance of sequences with different lengths."
    result = runner.invoke(cli.main, ["bioinf", "hamming-distance",
                                      "CAGATA", "CACACACA"])
    assert result.exit_code == 1
    assert result.exception.args[0] == expect


def test_cli_hamming_distance_different_case():
    runner = CliRunner()
    expect = "6"
    result = runner.invoke(cli.main, ["bioinf", "hamming-distance",
                                      "CAGATA", "cagata"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_hamming_distance_ignore_case_long():
    runner = CliRunner()
    expect = "0"
    result = runner.invoke(cli.main, ["bioinf", "hamming-distance",
                                      "CAGATA", "cagata", "--ignore_case"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_hamming_distance_ignore_case_short():
    runner = CliRunner()
    expect = "0"
    result = runner.invoke(cli.main, ["bioinf", "hamming-distance",
                                      "CAGATA", "cagata", "-i"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


# reverse-complement

def test_cli_reverse_complement():
    runner = CliRunner()
    expect = "CAGATA"
    result = runner.invoke(cli.main, ["bioinf", "reverse-complement",
                                      "TATCTG"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_reverse_complement_reverse_long():
    runner = CliRunner()
    expect = "CAGATA"
    result = runner.invoke(cli.main, ["bioinf", "reverse-complement",
                                      "ATAGAC", "--conversion", "reverse"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_reverse_complement_reverse_short():
    runner = CliRunner()
    expect = "CAGATA"
    result = runner.invoke(cli.main, ["bioinf", "reverse-complement",
                                      "ATAGAC", "-c", "reverse"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_reverse_complement_complement_long():
    runner = CliRunner()
    expect = "CAGATA"
    result = runner.invoke(cli.main, ["bioinf", "reverse-complement",
                                      "GTCTAT", "--conversion", "complement"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_reverse_complement_complement_short():
    runner = CliRunner()
    expect = "CAGATA"
    result = runner.invoke(cli.main, ["bioinf", "reverse-complement",
                                      "GTCTAT", "-c", "complement"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_reverse_complement_error():
    runner = CliRunner()
    expect = "Invalid conversion option."
    result = runner.invoke(cli.main, ["bioinf", "reverse-complement",
                                      "CAGATA", "-c", "invalid"])
    assert result.exit_code == 1
    assert result.exception.args[0] == expect


# shuffle-sequence

def test_cli_shuffle_sequence_nt(sample_nt_sequence):
    runner = CliRunner()
    expect = len(sample_nt_sequence)
    result = runner.invoke(cli.main, ["bioinf", "shuffle-sequence",
                                      sample_nt_sequence])
    assert result.exit_code == 0
    assert len(result.output.strip()) == expect


def test_cli_shuffle_sequence_aa(sample_aa_sequence):
    runner = CliRunner()
    expect = len(sample_aa_sequence)
    result = runner.invoke(cli.main, ["bioinf", "shuffle-sequence",
                                      sample_aa_sequence])
    assert result.exit_code == 0
    assert len(result.output.strip()) == expect


# random-sequence

def test_cli_random_sequence_nt():
    runner = CliRunner()
    expect = 200
    result = runner.invoke(cli.main, ["bioinf", "random-sequence",
                                      "200"])
    assert result.exit_code == 0
    assert len(result.output.strip()) == expect
    assert set(result.output.strip()) == set(nt_list)


def test_cli_random_sequence_aa_long():
    runner = CliRunner()
    expect = 200
    result = runner.invoke(cli.main, ["bioinf", "random-sequence",
                                      "200", "--alphabet", "aa"])
    assert result.exit_code == 0
    assert len(result.output.strip()) == expect
    assert set(result.output.strip()) == set(aa_list)


def test_cli_random_sequence_aa_short():
    runner = CliRunner()
    expect = 200
    result = runner.invoke(cli.main, ["bioinf", "random-sequence",
                                      "200", "-a", "aa"])
    assert result.exit_code == 0
    assert len(result.output.strip()) == expect
    assert set(result.output.strip()) == set(aa_list)


def test_cli_random_sequence_error():
    runner = CliRunner()
    expect = "Invalid alphabet option."
    result = runner.invoke(cli.main, ["bioinf", "random-sequence",
                                      "200", "-a", "invalid"])
    assert result.exit_code == 1
    assert result.exception.args[0] == expect
