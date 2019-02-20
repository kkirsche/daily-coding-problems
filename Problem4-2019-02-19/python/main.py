#!/usr/bin/env python3

from typing import List


def first_positive_missing_integer(list_in: List[int]) -> int:
    missing_value = 0
    largest_number = 0
    seen = set()
    for n in list_in:
        if n > 0:
            # we only care about positive integers
            seen.add(n)
            next_number = n + 1
            if n > largest_number:
                largest_number = n
            if missing_value == 0:
                missing_value = next_number
            if next_number not in seen and missing_value > next_number:
                missing_value = next_number
    if largest_number == missing_value:
        missing_value = missing_value + 1
    return missing_value
