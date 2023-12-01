from typing import List


def get_digits(calibration_code: str) -> List[str]:
    num_array = []
    for param in calibration_code:
        if param.isnumeric():
            num_array.append(param)

    return num_array


def combine_digits(num_list: List[str]) -> int:
    last_item = len(num_list) - 1
    return int(num_list[0]+num_list[last_item])


def solve_day_1_part_1(calibration_array: List[str]) -> int:
    total = 0
    for calibration_code in calibration_array:
        num_list = get_digits(calibration_code)
        running_total = combine_digits(num_list)
        total = total + running_total

    return total
