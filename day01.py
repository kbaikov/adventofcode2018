import os
from itertools import cycle
import logging as log

LOGLEVEL = os.environ.get("LOGLEVEL", "DEBUG").upper()
log.basicConfig(level=LOGLEVEL)


def part1(iterable):
    return sum(iterable)


def part2(iterable):
    s = 0
    seen = [0]
    for line in cycle(iterable):
        s += int(line)
        # log.debug(s)
        if s in seen:
            return s
        else:
            seen.append(s)


if __name__ == "__main__":

    assert part1([+1, -2, +3, +1]) == 3
    assert part1([+1, +1, +1]) == 3
    assert part1([+1, +1, -2]) == 0
    assert part1([-1, -2, -3]) == -6

    assert part2([+1, -1]) == 0
    assert part2([+3, +3, +4, -2, -4]) == 10
    assert part2([-6, +3, +8, +5, -6]) == 5
    assert part2([+7, +7, -2, -7, -4]) == 14

    with open("day01_input.txt") as file:
        list_of_ints = [int(x) for x in file.readlines()]
        print(part1(list_of_ints))  # 439
        print(part2(list_of_ints))  # 124645
