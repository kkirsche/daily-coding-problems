#!/usr/bin/env python3
from typing import List, Set


def result(target_number: int, number_list: List[int]) -> bool:
    seen: Set[int] = set()
    for n in number_list:
        diff: int = target_number - n
        if diff in seen:
            return True
        seen.add(n)
    return False
