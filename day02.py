import os
from collections import Counter
from itertools import combinations
import difflib
import logging as log

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
log.basicConfig(level=LOGLEVEL)

test_data = ["abcdef", "bababc", "abbcde", "abcccd" "aabcdd", "abcdee", "ababab"]
test_data2 = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]


def two_three(iterable):
    c = Counter(iterable)
    return 2 in c.values(), 3 in c.values()


def part1(iterable):
    twos = 0
    threes = 0
    for item in iterable:
        aa, aaa = two_three(item)
        twos += aa
        threes += aaa

    return twos * threes


def part2(iterable):
    l = len(iterable[0].strip())
    one_diff_ratio = 2 * (l - 1) / (l * 2)
    result = ""
    for x, y in combinations(iterable, 2):
        s = difflib.SequenceMatcher(None, x, y)
        if s.ratio() >= one_diff_ratio:
            for a, b, size in s.get_matching_blocks():
                result += x[a : b + size]
            return result


if __name__ == "__main__":

    assert part1(test_data) == 12
    assert part2(test_data2) == "fgij"

    with open("day02_input.txt") as file:
        list_of_lines = [line.strip() for line in file.readlines()]
        print(part1(list_of_lines))  # 6888
        print(
            part2(list_of_lines)
        )  # icxjvbrobtunlelzpdmfkahgs not icxjvbeoqtunlryzpdmfksagw cxjfbroltuneyzpdmqksahgw wcxjvbroqunleyzpdmfksahg
