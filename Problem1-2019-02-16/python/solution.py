#!/usr/bin/env python3
from typing import List

def result(target_number: int, number_list: List[int]):
    seen = set()
    for n in number_list:
        diff = target_number - n
        if diff in seen:
            return True
        seen.add(n)
    return False
