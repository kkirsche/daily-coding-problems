from .main import first_positive_missing_integer
from typing import List


def test_first_positive_missing_integer_example_one():
    list_in: List[int] = [3, 4, -1, 1]
    expected_output: int = 2

    actual_output: List[int] = first_positive_missing_integer(list_in)
    assert actual_output == expected_output


def test_first_positive_missing_integer_example_two():
    list_in: List[int] = [1, 2, 0]
    expected_output: int = 3

    actual_output: List[int] = first_positive_missing_integer(list_in)
    assert actual_output == expected_output


def test_first_positive_missing_integer_example_three():
    list_in: List[int] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, -1, 1]
    expected_output: int = 14

    actual_output: List[int] = first_positive_missing_integer(list_in)
    assert actual_output == expected_output
