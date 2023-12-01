from typing import List

number_words = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']


def get_digits(calibration_code: str) -> List[str]:
    num_array = []
    for param in calibration_code:
        if param.isnumeric():
            num_array.append(param)

    return num_array


def combine_digits(num_list: List[str]) -> int:
    last_item = len(num_list) - 1
    return int(num_list[0] + num_list[last_item])


def get_digits_from_string(calibration_code: str) -> List[str]:
    formatted_code = calibration_code.upper()
    int_list = []

    for i in range(len(formatted_code)):
        calibration_code_substr = formatted_code[i:]
        if calibration_code_substr[0].isnumeric():
            int_list.append(str(calibration_code_substr[0]))
            continue
        for num_str in number_words:
            if calibration_code_substr.startswith(num_str):
                int_list.append(str(number_words.index(num_str)))

    return int_list


def solve_day_1_part_1(calibration_array: List[str]) -> int:
    total = 0
    for calibration_code in calibration_array:
        num_list = get_digits(calibration_code)
        running_total = combine_digits(num_list)
        total = total + running_total

    return total


def solve_day_1_part_2(calibration_array: List[str]) -> int:
    total = 0
    for calibration_code in calibration_array:
        num_list = get_digits_from_string(calibration_code)
        running_total = combine_digits(num_list)
        total = total + running_total

    return total
