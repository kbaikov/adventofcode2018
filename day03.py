import os
from collections import Counter
from itertools import combinations, permutations
import difflib
import logging as log

import pygame

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
log.basicConfig(level=LOGLEVEL)

test_data = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]


def rectangle(string):
    """Returns a pygame rect object based on a passed string"""
    string_list = string.split()
    left, _, top = string_list[2].partition(",")
    top = top[:-1]
    width, _, height = string_list[3].partition("x")
    log.debug(f"Created a rectangle {left}, {top}, {width}, {height}")
    return pygame.Rect(int(left), int(top), int(width), int(height))


def part1(iterable):
    shared_points = Counter()
    all_rect = [rectangle(s) for s in iterable]
    for x in range(1000):
        for y in range(1000):
            for rect in all_rect:
                if rect.collidepoint(x, y):
                    shared_points[(x, y)] += 1
                    log.debug(f"Added point {x}, {y}")
    log.debug(f"{shared_points}")
    return len([key for key in shared_points if shared_points[key] >= 2])


def part2(iterable):
    # all_rect_dict = {s.split()[0]: rectangle(s) for s in iterable}
    all_rect_list = [rectangle(s) for s in iterable]
    for rect in all_rect_list:
        rcopy = all_rect_list[:]
        rcopy = rcopy.remove(rect)
        if rect.collidelist(rcopy) == -1:
            return rect


if __name__ == "__main__":
    assert part1(test_data) == 4
    # assert part2(test_data) == 3
    print(part2(test_data))

    with open("day03_input.txt") as file:
        list_of_lines = [line.strip() for line in file.readlines()]
        # print(part1(list_of_lines))  # 115242 not 47814390
        # print(part2(list_of_lines))
