from typing import List

params_for_checking = {
    'red': 12,
    'green': 13,
    'blue': 14
}


# {'game_id': 1, 'handfuls': [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]}
def handful_valid_agaisnt_params(handful: dict) -> bool:
    for key in handful:
        if params_for_checking[key] < handful[key]:
            return False

    return True


def game_is_valid(game_id: int, handfuls: List[dict]) -> int:
    for handful in handfuls:
        if handful_valid_agaisnt_params(handful) is False:
            return 0

    return game_id


def get_total_for_valid_games(parsed_games: List[dict]) -> int:
    total = 0
    for game in parsed_games:
        total = total + game_is_valid(game['game_id'], game['handfuls'])

    return total


def get_power_for_a_game(handfuls: List[dict]) -> int:
    min_number_dict = {'red': 0,
                       'green': 0,
                       'blue': 0}

    for handful in handfuls:
        for key in handful:
            if handful[key] > min_number_dict[key]:
                min_number_dict[key] = handful[key]

    return min_number_dict['red']*min_number_dict['green']*min_number_dict['blue']

