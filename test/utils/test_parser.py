from pathlib import Path

from src.utils.parser import read_list_from_file_as_string_list, read_from_file_as_str, read_list_from_file_as_int, \
    read_list_from_file_as_int_list


def test_read_list_from_file_as_string_list():
    expected_result = ['a', 'ab', 'abc', 'abcd', 'abcde']
    result = read_list_from_file_as_string_list(Path('./resources/string_list_file.txt'))
    assert result == expected_result


def test_read_from_file_as_string():
    expected_result = 'abcdefghijklmnopqrstuvwxyz1234567890'
    result = read_from_file_as_str(Path('./resources/test_string.txt'))
    assert result == expected_result


def test_read_list_from_file_as_int():
    expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = read_list_from_file_as_int(Path('./resources/test_int.txt'))
    assert result == expected_result


def test_read_list_from_file_as_int_list():
    expected_result = [[1, 2], [3, 4, 5]]
    result = read_list_from_file_as_int_list(Path('./resources/test_int_list.txt'))
    assert result == expected_result
