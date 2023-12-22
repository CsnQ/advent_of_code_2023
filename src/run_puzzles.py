from pathlib import Path

from src.day_1.day_1 import solve_day_1_part_1, solve_day_1_part_2
from src.day_2.day_2_solver import solve_day_2_part_1, solve_day_2_part_2
from src.day_4.part_1 import solve_day_4_part_1
from src.utils.parser import read_list_from_file_as_string_list, read_from_file_as_str


def day_1():
    input = read_list_from_file_as_string_list(Path('../../advent_of_code_2023/src/day_1/day_1_real_input.txt'))
    result_1 = solve_day_1_part_1(input)
    result_2 = solve_day_1_part_2(input)
    print(result_1)
    print(result_2)


def day_2():
    input = read_list_from_file_as_string_list(Path('../../advent_of_code_2023/src/day_2/input.txt'))
    result_1 = solve_day_2_part_1(input)
    result_2 = solve_day_2_part_2(input)
    print(result_1)
    print(result_2)

def day_4():
    input = read_list_from_file_as_string_list(Path('../../advent_of_code_2023/src/day_4/input.txt'))
    result_1 = solve_day_4_part_1(input)
    print(result_1)


if __name__ == "__main__":
    day_4()
