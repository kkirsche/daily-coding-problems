from .main import first_positive_missing_integer


def test_first_positive_missing_integer_example_one():
    list_in = [3, 4, -1, 1]
    expected_output = 2

    actual_output = first_positive_missing_integer(list_in)
    assert actual_output == expected_output


def test_first_positive_missing_integer_example_two():
    list_in = [1, 2, 0]
    expected_output = 3

    actual_output = first_positive_missing_integer(list_in)
    assert actual_output == expected_output


def test_first_positive_missing_integer_example_three():
    list_in = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, -1, 1]
    expected_output = 14

    actual_output = first_positive_missing_integer(list_in)
    assert actual_output == expected_output
