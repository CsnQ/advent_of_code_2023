import pytest

from src.day_4.parse_input import parse_input


def test_parse_input_returns_card_and_numbers():
    input = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53', 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19', ]

    expected_result = [{'card': [41, 48, 83, 86, 17], 'winning_numbers': [83, 86, 6, 31, 17, 9, 48, 53]},
                       {'card': [13, 32, 20, 16, 61], 'winning_numbers': [61, 30, 68, 82, 17, 32, 24, 19]}]
    actual_result = parse_input(input)
    assert expected_result == actual_result
