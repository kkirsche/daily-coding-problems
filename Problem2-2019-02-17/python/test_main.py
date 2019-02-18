from .main import product_of_list_except_at_index

def test_product_of_list_except_at_index_example1():
    list_in = [1, 2, 3, 4, 5]
    expected_out = [120, 60, 40, 30, 24]

    list_out = product_of_list_except_at_index(list_in)
    assert list_out == expected_out

def test_product_of_list_except_at_index_example2():
    list_in = [3, 2, 1]
    expected_out = [2, 3, 6]

    list_out = product_of_list_except_at_index(list_in)
    assert list_out == expected_out
