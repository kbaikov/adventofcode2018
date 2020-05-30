import os
from itertools import zip_longest, tee, filterfalse
import logging as log
from pathlib import Path

import pytest

LOGLEVEL = os.environ.get("LOGLEVEL", "DEBUG").upper()
log.basicConfig(level=LOGLEVEL)

test_pattern = "dabAcCaCBAcCcaDA"


def react(pair):
    x, y = pair
    if x == y:
        return False
    if x == y.upper() or y == x.upper():
        return True
    return False


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def can_react(i):
    for pair in pairwise(i):
        if react(pair):
            return True
    return False


def process_list(test_pattern):
    paired_list = list(pairwise(test_pattern))
    result_string = test_pattern

    while can_react(result_string):
        for pair in pairwise(result_string):
            if react(pair):
                reacted_string = "".join(pair)
                half1, _, half2 = result_string.partition(reacted_string)
                result_string = f"{half1}{half2}"
                break
    return result_string


if __name__ == "__main__":
    pattern = Path("day05_input.txt").read_text().strip()
    result = process_list(pattern)
    print(result, len(result))  # 11590
