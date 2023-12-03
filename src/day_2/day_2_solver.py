from typing import List, Any

from src.day_2.game_checker import get_total_for_valid_games, get_power_for_a_game
from src.day_2.game_parser import parse_game


def solve_day_2_part_1(day_2_input: List[str]) -> int:
    parsed_games = get_list_of_parsed_games(day_2_input)
    total = get_total_for_valid_games(parsed_games)
    return total


def solve_day_2_part_2(day_2_input: List[str]) -> int:
    total_power = 0
    parsed_games = get_list_of_parsed_games(day_2_input)
    for game in parsed_games:
        total_power = total_power + get_power_for_a_game(game['handfuls'])

    return total_power


def get_list_of_parsed_games(day_2_input: List[str]) -> List[dict[str, Any]]:
    parsed_games = []
    for game in day_2_input:
        parsed_games.append(parse_game(game))
    return parsed_games
