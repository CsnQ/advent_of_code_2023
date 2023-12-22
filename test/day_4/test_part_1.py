import pytest

from src.day_4.part_1 import calculate_winning_score_for_1_card, calculate_part_1


def test_calculate_winning_score_for_1_card():
    card_1 = {'card': [41, 48, 83, 86, 17], 'winning_numbers': [83, 86, 6, 31, 17, 9, 48, 53]}
    card_2 = {'card': [13, 32, 20, 16, 61], 'winning_numbers': [61, 30, 68, 82, 17, 32, 24, 19]}
    card_3 = {'card': [1, 21, 53, 59, 44], 'winning_numbers': [69, 82, 63, 72, 16, 21, 14, 1]}
    card_4 = {'card': [41, 92, 73, 84, 69], 'winning_numbers': [59, 84, 76, 51, 58, 5, 54, 83]}
    card_5 = {'card': [87, 83, 26, 28, 32], 'winning_numbers': [88, 30, 70, 12, 93, 22, 82, 36]}
    card_6 = {'card': [31, 18, 13, 56, 72], 'winning_numbers': [74, 77, 10, 23, 35, 67, 36, 11]}

    assert calculate_winning_score_for_1_card(card_1) == 8
    assert calculate_winning_score_for_1_card(card_2) == 2
    assert calculate_winning_score_for_1_card(card_3) == 2
    assert calculate_winning_score_for_1_card(card_4) == 1
    assert calculate_winning_score_for_1_card(card_5) == 0
    assert calculate_winning_score_for_1_card(card_6) == 0


def test_calculate_part_1():
    card_batch = [{'card': [41, 48, 83, 86, 17], 'winning_numbers': [83, 86, 6, 31, 17, 9, 48, 53]},
                  {'card': [13, 32, 20, 16, 61], 'winning_numbers': [61, 30, 68, 82, 17, 32, 24, 19]},
                  {'card': [1, 21, 53, 59, 44], 'winning_numbers': [69, 82, 63, 72, 16, 21, 14, 1]},
                  {'card': [41, 92, 73, 84, 69], 'winning_numbers': [59, 84, 76, 51, 58, 5, 54, 83]},
                  {'card': [87, 83, 26, 28, 32], 'winning_numbers': [88, 30, 70, 12, 93, 22, 82, 36]},
                  {'card': [31, 18, 13, 56, 72], 'winning_numbers': [74, 77, 10, 23, 35, 67, 36, 11]}]
    expected_score = 13
    actual_score = calculate_part_1(card_batch)
    assert expected_score == actual_score
