import pytest

from src.day_2.game_parser import parse_game, process_handful


@pytest.fixture
def single_digit_game() -> str:
    return 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'


@pytest.fixture
def double_digit_game() -> str:
    return 'Game 33: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'


def test_parse_game_returns_dict(single_digit_game):
    expected = {'game_id': 1, 'handfuls': [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]}
    actual = parse_game(single_digit_game)
    print(actual)
    assert expected == actual


def test_get_game_id_returns_game_id_for_double_int(double_digit_game):
    expected = {'game_id': 33, 'handfuls': [{'blue': 6, 'green': 8, 'red': 20}, {'blue': 5, 'green': 13, 'red': 4},
                                            {'green': 5, 'red': 1}]}
    actual = parse_game(double_digit_game)
    assert expected == actual


def test_process_handfuls_resturns_dict_single_figures():
    handful = '3 blue, 4 red'
    expected = {'blue': 3, 'red': 4}
    actual = process_handful(handful)
    assert expected == actual


def test_process_handfuls_resturns_dict_double_figures():
    handful = '3 blue, 45 red'
    expected = {'blue': 3, 'red': 45}
    actual = process_handful(handful)
    assert expected == actual
