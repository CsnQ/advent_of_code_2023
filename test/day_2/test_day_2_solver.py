from typing import List

import pytest

from src.day_2.day_2_solver import solve_day_2_part_1, solve_day_2_part_2


@pytest.fixture
def input_for_test() -> list[str]:
    return ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']


def test_day_1_solver_returns_expected(input_for_test):
    expected = 8
    actual = solve_day_2_part_1(input_for_test)
    assert actual == expected

def test_day_2_solver_returns_expected(input_for_test):
    expected = 2286
    actual = solve_day_2_part_2(input_for_test)
    assert actual == expected
