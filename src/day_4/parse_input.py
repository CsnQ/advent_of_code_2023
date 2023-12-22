from typing import List, Dict


def parse_input(scratch_cards: List[str]) -> list[Dict[str, list]]:
    card_number = 1
    parsed_scratch_cards = []
    for card in scratch_cards:
        card_modified = card.split('|')
        card_numbers = card_modified[0][6:].split(':')[1].strip().split()
        card_numbers = [int(num) for num in card_numbers]

        winning_number_list = card_modified[1].split()
        winning_number_list = [int(num) for num in winning_number_list]

        card_dict = {'card': card_numbers, 'winning_numbers': winning_number_list}
        parsed_scratch_cards.append(card_dict)

    return parsed_scratch_cards
