import pytest

from day05 import process_list, react


@pytest.mark.parametrize("input_, result", [("dabAcCaCBAcCcaDA", 10)])
def test_day5_process_list(input_, result):
    output = process_list(input_)
    assert len(output) == result


@pytest.mark.parametrize(
    "input_, result", [("AA", False), ("aa", False), ("Aa", True), ("aA", True)]
)
def test_day5_react(input_, result):
    assert react(input_) == result
