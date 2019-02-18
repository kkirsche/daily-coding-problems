from typing import List
from functools import reduce

def product(x: int, y: int) -> int:
    return x * y

def product_of_list_except_at_index(list_in: List[int]) -> List[int]:
    # create a list to store our results
    list_out = []
    # we want to calculate a new array for each item in the list
    # to get the index we want to exclude for each iteration, we
    # loop over the range using the list's length as the stopping value
    for index in range(len(list_in)):
        # create a new list which gathers all numbers EXCEPT the one at the
        # index
        list_in_except_index = list_in[:index] + list_in[(index + 1):]
        # generate the product of all remaining items in the list
        list_product = reduce(product, list_in_except_index)
        list_out.append(list_product)
    return list_out
