from typing import List

import pytest

from src.day_1.day_1 import get_digits, combine_digits, solve_day_1_part_1, \
    get_digits_from_string, solve_day_1_part_2


@pytest.fixture
def test_line_1() -> str:
    return '1abc2'


@pytest.fixture
def test_line_2() -> str:
    return 'a1b2c3d4e5f'


@pytest.fixture
def day_1_test_input() -> List[str]:
    return ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']


@pytest.fixture
def day_1_part_2_test_input() -> List[str]:
    return ['two1nine',
            'eightwothree',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'zoneight234',
            '7pqrstsixteen']


def test_get_digits_returns_expected_val_for_test_line_1(test_line_1) -> None:
    expected_result = ['1', '2']
    actual_result = get_digits(test_line_1)
    assert actual_result == expected_result


def test_get_digits_returns_expected_val_for_test_line_2(test_line_2) -> None:
    expected_result = ['1', '2', '3', '4', '5']
    actual_result = get_digits(test_line_2)
    assert actual_result == expected_result


def test_combine_digits_for_array_of_two_numbers() -> None:
    expected_result = 12
    actual_result = combine_digits(['1', '2'])
    assert actual_result == expected_result


def test_combine_digits_for_array_of_more_than_two_numbers() -> None:
    expected_result = 15
    actual_result = combine_digits(['1', '2', '3', '4', '5'])
    assert actual_result == expected_result


def test_solve_day_1_part_1(day_1_test_input) -> None:
    expected = 142
    actual = solve_day_1_part_1(day_1_test_input)
    assert actual == expected


def test_get_all_digits_from_string_returns_all_digits_from_input() -> None:
    input_val_1 = 'two1two'
    expected_1 = ['2', '1', '2']
    actual_1 = get_digits_from_string(input_val_1)
    assert actual_1 == expected_1


def test_solve_day_1_part_2(day_1_part_2_test_input) -> None:
    expected = 281
    actual = solve_day_1_part_2(day_1_part_2_test_input)
    assert actual == expected
