from typing import Any


# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
def parse_game(game: str) -> dict[str, Any]:
    id_and_handfuls = game.lower().split(':')
    full_game_id = id_and_handfuls[0]
    game_id = int(full_game_id.split(" ")[1])
    handfuls = id_and_handfuls[1].split(";")
    handfuls = [handful.strip() for handful in handfuls]

    handfuls_processed = []
    for handful in handfuls:
        handfuls_processed.append(process_handful(handful))
    return {'game_id': game_id, 'handfuls': handfuls_processed}


def process_handful(handful: str) -> dict[str, Any]:
    items = handful.split(',')
    items = [selection.strip() for selection in items]
    handful_dict = {}
    for item in items:
        pairing = item.split(" ")
        colour = pairing[1]
        frequency = int(pairing[0])
        handful_dict[colour] = frequency

    return handful_dict
