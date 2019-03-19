#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
from click.testing import CliRunner
from prestools import cli


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

