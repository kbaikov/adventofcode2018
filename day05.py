import os
from itertools import tee
import logging as log
from pathlib import Path
from collections import Counter, deque
import string

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


def process_list2(test_pattern):
    c = Counter()
    paired_list = list(pairwise(test_pattern))
    result_string = test_pattern

    while can_react(result_string):
        for pair in pairwise(result_string):
            if react(pair):
                reacted_string = "".join(pair)
                c[reacted_string.lower()] += 1
                half1, _, half2 = result_string.partition(reacted_string)
                result_string = f"{half1}{half2}"
                break
    return result_string, c


def potential_pairs(pattern):
    c = 0
    for pair in pairwise(pattern):
        if react(pair):
            c += 1
    return c


def process_stack(pattern):
    """Pop if reacts, add if not.

    idea taken from: https://steadbytes.com/blog/advent-of-code-2018/05/"""
    stack = deque()

    for char in pattern:
        if stack and react((char, stack[-1])):
            stack.pop()
        else:
            stack.append(char)
    return len(stack)


def process_stack2(pattern):
    """idea taken from: https://steadbytes.com/blog/advent-of-code-2018/05/"""
    best = len(pattern)

    for char in string.ascii_lowercase:
        modified = pattern.replace(char, "")
        modified = modified.replace(char.upper(), "")
        modified_reacted_len = process_stack(modified)
        best = min(best, modified_reacted_len)
    return best


if __name__ == "__main__":
    # part 1: 11590
    # part 2: 4504
    pattern = Path("day05_input.txt").read_text().strip()
    result1 = process_stack(pattern)
    result2 = process_stack2(pattern)

    print(result1, result2)
