#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import pytest
from click.testing import CliRunner
from prestools import cli

DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
SAME1 = os.path.join(DATADIR, "same1.txt")
SAME2 = os.path.join(DATADIR, "same2.txt")
SAMENOT = os.path.join(DATADIR, "samenot.txt")
SIZENOT = os.path.join(DATADIR, "sizenot.txt")


# prime_factors

def test_cli_prime_factors_one():
    runner = CliRunner()
    expect = "[]"
    result = runner.invoke(cli.main, ["misc", "prime-factors", "1"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_prime_factors_square():
    runner = CliRunner()
    expect = "[3, 3]"
    result = runner.invoke(cli.main, ["misc", "prime-factors", "9"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_prime_factors_cube():
    runner = CliRunner()
    expect = "[3, 3, 3]"
    result = runner.invoke(cli.main, ["misc", "prime-factors", "27"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_prime_factors_mixed():
    runner = CliRunner()
    expect = "[5, 17, 23, 461]"
    result = runner.invoke(cli.main, ["misc", "prime-factors", "901255"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_prime_factors_large():
    runner = CliRunner()
    expect = "[11, 9539, 894119]"
    result = runner.invoke(cli.main, ["misc", "prime-factors", "93819012551"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


# pm.wordcount

def test_cli_wordcount():
    runner = CliRunner()
    expect = {"word": 2, "test": 1, "wordcount": 1}
    result = runner.invoke(cli.main, ["misc", "wordcount",
                                      "word test wordcount word"])
    assert result.exit_code == 0
    assert eval(result.output.strip()) == expect


def test_cli_wordcount_specific_word():
    runner = CliRunner()
    expect = "2"
    result = runner.invoke(cli.main, ["misc", "wordcount",
                                      "word test wordcount word",
                                      "--word", "word"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_wordcount_specific_word_not_present():
    runner = CliRunner()
    expect = "0"
    result = runner.invoke(cli.main, ["misc", "wordcount",
                                      "word test wordcount word",
                                      "--word", "prova"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_wordcount_ignore_case_true():
    runner = CliRunner()
    expect = {"word": 2, "test": 1, "wordcount": 1}
    result = runner.invoke(cli.main, ["misc", "wordcount",
                                      "word test wordcount WORD",
                                      "--ignore_case"])
    assert result.exit_code == 0
    assert eval(result.output.strip()) == expect


def test_cli_wordcount_ignore_case_false():
    runner = CliRunner()
    expect = {"word": 1, "test": 1, "wordcount": 1, "WORD": 1}
    result = runner.invoke(cli.main, ["misc", "wordcount",
                                      "word test wordcount WORD"])
    assert result.exit_code == 0
    assert eval(result.output.strip()) == expect


def test_cli_wordcount_specific_word_ignore_case_true():
    runner = CliRunner()
    expect = "2"
    result = runner.invoke(cli.main, ["misc", "wordcount",
                                      "word test wordcount WORD",
                                      "--word", "word", "--ignore_case"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_wordcount_specific_word_ignore_case_false():
    runner = CliRunner()
    expect = "1"
    result = runner.invoke(cli.main, ["misc", "wordcount",
                                      "word test wordcount WORD",
                                      "--word", "word"])
    assert result.exit_code == 0
    assert result.output.strip() == expect


# pm.equal_files

def test_cli_equal_files():
    runner = CliRunner()
    expect = "True"
    result = runner.invoke(cli.main, ["misc", "equal-files", SAME1, SAME2])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_equal_files_false():
    runner = CliRunner()
    expect = "False"
    result = runner.invoke(cli.main, ["misc", "equal-files", SAME1, SAMENOT])
    assert result.exit_code == 0
    assert result.output.strip() == expect


def test_cli_equal_files_false_size():
    runner = CliRunner()
    expect = "False"
    result = runner.invoke(cli.main, ["misc", "equal-files", SAME1, SAMENOT])
    assert result.exit_code == 0
    assert result.output.strip() == expect
