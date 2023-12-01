from pathlib import Path

from src.day_1.day_1 import solve_day_1_part_1
from src.utils.parser import read_list_from_file_as_string_list


def day_1():
    input = read_list_from_file_as_string_list(Path('../../advent_of_code_2023/src/day_1/day_1_real_input.txt'))
    result = solve_day_1_part_1(input)
    print(result)


if __name__ == "__main__":
    day_1()
