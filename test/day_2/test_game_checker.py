import pytest

from src.day_2.game_checker import handful_valid_agaisnt_params, game_is_valid, get_power_for_a_game


def test_handful_valid_agaisnt_params_returns_true():
    input = {'blue': 3, 'red': 4}
    expected = True
    actual = handful_valid_agaisnt_params(input)
    assert actual == expected


def test_handful_valid_agaisnt_params_returns_false():
    input = {'blue': 33, 'red': 4}
    expected = False
    actual = handful_valid_agaisnt_params(input)
    assert actual == expected


def test_handful_valid_agaisnt_params_returns_false_for_later_val():
    input = {'blue': 3, 'red': 54}
    expected = False
    actual = handful_valid_agaisnt_params(input)
    assert actual == expected


def test_check_game_is_valid_returns_game_id_for_valid_game():
    game = [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]
    id = 1
    expected = id
    actual = game_is_valid(id, game)
    assert actual == expected


def test_check_game_is_valid_returns_game_id_for_invalid_game():
    game = [{'green': 8, 'blue': 6, 'red': 20}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]
    id = 1
    expected = 0
    actual = game_is_valid(id, game)
    assert actual == expected


# In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes.
# If any color had even one fewer cube, the game would have been impossible.
# 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
def test_get_minimum_num_colours_for_a_game_returns_expected_for_game():
    game = [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]
    expected = 48
    actual = get_power_for_a_game(game)
    assert actual == expected
