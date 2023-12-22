from src.day_4.parse_input import parse_input


def calculate_winning_score_for_1_card(card_dict: dict[str, list]) -> int:
    score = 0
    for number in card_dict['card']:
        if (number in card_dict['winning_numbers']) and (score == 0):
            score = 1
        elif number in card_dict['winning_numbers']:
            score = score * 2

    return score


def calculate_part_1(card_batch: list[dict[str, list]]) -> int:
    total_score = 0
    for card in card_batch:
        total_score = total_score + calculate_winning_score_for_1_card(card)
    return total_score


def solve_day_4_part_1(input: list[str]):
    parsed_cards = parse_input(input)
    result = calculate_part_1(parsed_cards)
    return result
