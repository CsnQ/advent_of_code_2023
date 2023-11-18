from pathlib import Path
from typing import List


def read_list_from_file_as_string_list(file_path: Path) -> List[str]:
    data_from_file = []
    with open(file_path) as file:
        for line in file:
            data_from_file.append(line.rstrip())

    return data_from_file


def read_from_file_as_str(file_path: Path) -> str:
    with open(file_path) as file:
        data = file.read()

    return data


def read_list_from_file_as_int(file_path: Path) -> List[int]:
    data_from_file = []
    with open(file_path) as file:
        for line in file:
            data_from_file.append(int(line.rstrip()))

    return data_from_file


def read_list_from_file_as_int_list(file_path: Path) -> List[List[int]]:
    int_list = []
    with open(file_path) as file:
        data = file.read()

    data_array = data.split("\n\n")
    for item in data_array:
        list = item.split("\n")

        int_list.append([int(x) for x in list])

    return int_list
