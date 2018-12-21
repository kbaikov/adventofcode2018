import os
from collections import Counter
from itertools import combinations, permutations
import difflib
import datetime
import logging as log

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
log.basicConfig(level=LOGLEVEL)

test_data = [
    "[1518-11-01 00:00] Guard #10 begins shift",
    "[1518-11-01 00:05] falls asleep",
    "[1518-11-01 00:25] wakes up",
    "[1518-11-01 00:30] falls asleep",
    "[1518-11-01 00:55] wakes up",
    "[1518-11-01 23:58] Guard #99 begins shift",
    "[1518-11-02 00:40] falls asleep",
    "[1518-11-02 00:50] wakes up",
    "[1518-11-03 00:05] Guard #10 begins shift",
    "[1518-11-03 00:24] falls asleep",
    "[1518-11-03 00:29] wakes up",
    "[1518-11-04 00:02] Guard #99 begins shift",
    "[1518-11-04 00:36] falls asleep",
    "[1518-11-04 00:46] wakes up",
    "[1518-11-05 00:03] Guard #99 begins shift",
    "[1518-11-05 00:45] falls asleep",
    "[1518-11-05 00:55] wakes up",
]


def parse_date_time(string):
    """Return a datetime object and the rest of the string"""
    date, time, *rest = string.split()
    date_time_string = f'{date.replace("[", "")} {time.replace("]", "")}'
    return datetime.datetime.strptime(date_time_string, "%Y-%m-%d %H:%M"), rest


def part1(iterable):
    pass


def part2(iterable):
    pass


if __name__ == "__main__":
    a = dict()
    for s in test_data:
        k, v = parse_date_time(s)
        a[k] = v
        print(a)

    with open("day04_input.txt") as file:
        list_of_lines = [line.strip() for line in file.readlines()]
        # print(part1(list_of_lines))  #
        # print(part2(list_of_lines))  #
